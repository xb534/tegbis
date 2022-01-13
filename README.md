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
parameters: (Sigma=0.5, K=300, Min=50) <br>
![alt text](https://github.com/salaee/egbis/blob/master/results/results_1.png)
<br>
parameters: (Sigma=0.5, K=300, Min=50) <br>
![alt text](https://github.com/salaee/egbis/blob/master/results/results_2.png)
<br>
parameters: (Sigma=0.5, K=1000, Min=50) <br>
![alt text](https://github.com/salaee/egbis/blob/master/results/results_3.png)
<br>
parameters: (Sigma=0.8, K=500, Min=10) <br>
![alt text](https://github.com/salaee/egbis/blob/master/results/results_4.png)
<br>
parameters: (Sigma=0.5, K=500, Min=50) <br>
![alt text](https://github.com/salaee/egbis/blob/master/results/results_5.png)
<br>
<br>
### Requirements
Python 3.5<br>

##### Libraries used: 
scipy、matplotlib

