import os.path

from filter import *
from segment_graph import *
import time
import imageio
import collections
from PIL import Image
import glob


def get_begin_and_end(input):
    """
        Get the first and last non-zero element of the input array.
        This function is used to assist in obtaining the position of the extracted texture in the input image.
        It didn't get an exception when I extracted the DTD dataset texture, and I didn't do a full test.
    """
    begin,end = 0,0
    for i, item in enumerate(input):
        if item != 0 and begin == 0:
            begin = i + 1
        elif (item == 0 and i != 0 and begin != 0) or i == (len(input) - 1):
            end = i
            break
    return begin,end


def get_texture(in_image,mask,path,thre=3,max_rate=0.1):
    """
    This function extracts textures from the in_image based on the given mask.
    The same values in the mask represent the same texture extracted.
    """
    height, width, _ = in_image.shape
    mask_ = mask.flatten().tolist()
    mask_count = collections.Counter(mask_)         # Statistics the area distribution of different textures.
    total_pixel = height * width
    i = 0
    for key, value in mask_count.items():
        if value / total_pixel < max_rate:          # This is a hyperarameter that needs to be set as you see fit.
                                                    # Most textures in real world are relatively small, so this parameter
                                                    # can be used to screen out impurities.
            # Get a mask for a texture
            mask_c = (mask == int(key)) + 0
            # Based on the continuity of the extracted texture itself,
            # I determine the length and width of the texture itself using the maximum pixel value of a row or column.
            # At the same time, we also get the range of rows and columns where the texture actually exists.
            sum_col = mask_c.sum(axis=0).flatten()
            sum_row = mask_c.sum(axis=1).flatten()
            begin_col, end_col = get_begin_and_end(sum_col)
            begin_row, end_row = get_begin_and_end(sum_row)
            # This is a hyperparameter(thre) that allows us to ignore textures with shortest edges of only a few pixels.
            if end_col-begin_col<thre or end_row-begin_row<thre:
                continue
            texture_img = (in_image * mask_c)[begin_row - 1:end_row - 1, begin_col - 1:end_col - 1, :]
            im = Image.fromarray(np.uint8(texture_img))
            im.save(path+'_'+str(i)+'.png')
            i += 1


def segment(in_image, sigma, k, min_size):
    height, width, band = in_image.shape
    smooth_red_band = smooth(in_image[:, :, 0], sigma)
    smooth_green_band = smooth(in_image[:, :, 1], sigma)
    smooth_blue_band = smooth(in_image[:, :, 2], sigma)

    # build graph
    edges_size = width * height * 4
    edges = np.zeros(shape=(edges_size, 3), dtype=object)
    num = 0
    for y in range(height):
        for x in range(width):
            if x < width - 1:
                edges[num, 0] = int(y * width + x)
                edges[num, 1] = int(y * width + (x + 1))
                edges[num, 2] = diff(smooth_red_band, smooth_green_band, smooth_blue_band, x, y, x + 1, y)
                num += 1
            if y < height - 1:
                edges[num, 0] = int(y * width + x)
                edges[num, 1] = int((y + 1) * width + x)
                edges[num, 2] = diff(smooth_red_band, smooth_green_band, smooth_blue_band, x, y, x, y + 1)
                num += 1

            if (x < width - 1) and (y < height - 2):
                edges[num, 0] = int(y * width + x)
                edges[num, 1] = int((y + 1) * width + (x + 1))
                edges[num, 2] = diff(smooth_red_band, smooth_green_band, smooth_blue_band, x, y, x + 1, y + 1)
                num += 1

            if (x < width - 1) and (y > 0):
                edges[num, 0] = int(y * width + x)
                edges[num, 1] = int((y - 1) * width + (x + 1))
                edges[num, 2] = diff(smooth_red_band, smooth_green_band, smooth_blue_band, x, y, x + 1, y - 1)
                num += 1
    # Segment
    u = segment_graph(width * height, num, edges, k)

    # post process small components
    for i in range(num):
        a = u.find(edges[i, 0])
        b = u.find(edges[i, 1])
        if (a != b) and ((u.size(a) < min_size) or (u.size(b) < min_size)):
            u.join(a, b)

    num_cc = u.num_sets()
    output = np.zeros(shape=(height, width, 3),dtype='int')
    mask = np.zeros(shape=(height,width,1),dtype='int')                             # add

    # pick random colors for each component
    colors = np.zeros(shape=(height * width, 3),dtype='int')
    for i in range(height * width):
        colors[i, :] = random_rgb()
    for y in range(height):
        for x in range(width):
            comp = u.find(y * width + x)
            output[y, x, :] = colors[comp, :]
            mask[y, x, :] = comp                                                      # add
    return in_image,mask



# --------------------------------------------------------------------------------
# Segment an image:
#
# Inputs:
#           sigma: to smooth the image.
#           k: constant for threshold function.
#           min_size: minimum component size (enforced by post-processing stage).
#           thre: the shortest edge of the texture that can be obtained.
#           max_rate: maximum area of texture (compared to input image)
# --------------------------------------------------------------------------------

if __name__ == "__main__":
    sigma = 0.5
    k = 500
    min = 50
    thre = 3
    max_rate = 0.1
    path_base = "data\images"
    out_path  = "data\images_textures"
    path_class = glob.glob(os.path.join(path_base,'*'))
    all_img_paths = []
    all_tex_paths = []
    for path in path_class:
        # 确保输出路径存在
        tmp = path.split('\\')
        tmp[1] = 'images_textures'
        tmp = os.path.join(tmp[0],tmp[1],tmp[2])
        if not os.path.exists(tmp):
            os.makedirs(tmp)
        path = os.path.join(path,'*')
        all_img_paths.extend(glob.glob(path))
    # 生成纹理输出所需路径，一一对应
    for path in all_img_paths:
        tmp = path.split('\\')
        tmp[1] = 'images_textures'
        tmp[-1] = tmp[-1].split('.')[0]
        all_tex_paths.append(os.path.join(tmp[0],tmp[1],tmp[2],tmp[3]))
    i =0
    data_len = len(all_img_paths)
    for img_path,tex_path in zip(all_img_paths,all_tex_paths):
        print('percent: {:.2%}'.format(i / data_len))
        i += 1
        input_image = imageio.imread(img_path)
        in_image, mask = segment(input_image, sigma, k, min)
        get_texture(in_image, mask, tex_path)