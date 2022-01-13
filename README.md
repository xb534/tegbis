## TEGBIS (Texture extractor based on Efficient Graph-Based Image Segmentation)
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
- original image:
  
  parameters: (Sigma=0.5, K=300, Min=50)
  
  ![original image](http://github.com/xb534/tegbis/tree/master/data/images/blotchy/blotchy_0003.jpg)


- textures image extracted from original image.

  | | | | | |
  |:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
  |<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_0.png" width="100"/> |  <img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_1.png" width="100"/>|<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_2.png" width="100"/>|<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_3.png" width="100"/>|<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_4.png" width="100"/>|
  |<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_5.png" width="100"/> |  <img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_6.png" width="100"/>|<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_7.png" width="100"/>|<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_8.png" width="100"/>|<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_9.png" width="100"/>|
  |<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_10.png" width="100"/> |  <img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_11.png" width="100"/>|<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_12.png" width="100"/>|<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_13.png" width="100"/>|<img src="https://github.com/xb534/tegbis/tree/master/data/images_textures/blotchy/blotchy_0003_14.png" width="100"/>|

### Requirements
Python 3.5<br>

### Libraries used: 
scipy<br>
matplotlib<br>
glob<br>

