# TEGBIS (Texture extractor based on Efficient Graph-Based Image Segmentation)
- The End to End Python implementation of "Efficient Graph-Based Image Segmentation" paper.
- The source code is mainly based on [pegbis](https://github.com/salaee/pegbis).

### User Guide
- If you execute the `main.py`,it will process images from `data/images/`,export to
`data/image_textures/`.
- The file structure you should provide is as follows(DTD dataset as an example):
```angular2html
    /data/images/banded
    /data/images/blotchy
    /data/images/braided
    ...
```
- I've provided comments as detailed as possible so that you can modify the code to 
  suit your actual needs.
- Welcome to report bugs to me.

### Results
#### original image:
parameters: (Sigma=0.5, K=300, Min=50) 
<br>
![original image](https://github.com/xb534/tegbis/blob/master/results/blotchy_0003.jpg)
<br>
#### textures image extracted from original image.
![original image](https://github.com/xb534/tegbis/blob/master/results/blotchy_0003.jpg)
![original image](https://github.com/xb534/tegbis/blob/master/results/blotchy_0003.jpg)
![original image](https://github.com/xb534/tegbis/blob/master/results/blotchy_0003.jpg)
![original image](https://github.com/xb534/tegbis/blob/master/results/blotchy_0003.jpg)
![original image](https://github.com/xb534/tegbis/blob/master/results/blotchy_0003.jpg)


### Requirements
Python 3.5<br>

##### Libraries used: 
scipy、matplotlib

