# Problem Statement
```
You may use the MNIST dataset or any dataset for Face Images or Flower Images for this assignment. 
1) Implement k-means clustering. Analyse the clusters formed for various values of k. Display the centroids of the clusters. DO NOT USE IN_BUILT ROUTINE for k-means clustering. 
2) Implement Dimensionality reduction using PCA. Analyse the reconstruction error for various values of k. Display the Eigen Vectors. DO NOT USE IN_BUILT ROUTINE for implementing PCA. However you can use in-built routines for computing Eigen vectors and Eigen values. 

Note that when you apply PCA on images, you are dealing with data with a very high dimensionality, i.e. d>m, where m is the number of images in the training dataset. Therefore you need to apply the technique given in Section 23.1.1. of the Textbook. 

Further, for images, you have the red, green and blue components for the color at every pixel location. You can simply consider the average of the three color components. This average is the intensity value at the pixel. The feature vector is constructed using the intensity values of the all the pixels in the image. 

Prepare a report with all the results and steps of implementation. 
```


# Folder contains
- notebook for K-mean
- notebook for PCA
- Assignment report
