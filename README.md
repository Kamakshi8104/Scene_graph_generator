# SCENE GRAPH GENERATOR

## Table of Contents


-[Project](Scene Graph Generator)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
  - [Implementation details](#implementation-details-of-Scene-Graph-Generator)
  - [Research papers](#Research-papers)
  - [Domains Explored](#Domains-Explored)
  - [Project Workflow](#Project-Workflow)
  - [Future Work](#future-work)
  - [Courses Referred](#Courses-Referred)
  - [Contributors](#contributors)
  - [Acknowledgements and Resources](#acknowledgements-and-references)


----------

## About
Detecting objects and their relations in images in the form of a graph data structure and generating graphs to represent relations between objects in a given image.


<img src="/images/images/img2.png"/>

----------
## Implementation details of Scene Graph Generator


<img src="/images/images/img1.png"/>

---
## YOLO to detect object
Using YOLO to output the class of the objects and their bounding box coordinates to get their location in the image.

## Relationship Proposal network
- Creating a 2D array of all the objects detected which contains the word2vec embeddings of the class plus the four bounding box coordinates.
- Passing the input array through two identical neural networks to obtain the key and query matrix
- Multiplying the key and query matrices to generate an attention matrix
- All elements of the attention matrix having value 1, their respective row and column number is assigned the object name and hence we can obtain which all objects have relations between them.
- We then apply non-maximal suppres- sion (NMS) to filter out object pairs that have significant overlap with others. Each relationship has a pair of bounding boxes, and the combination order mat- ters. We compute the overlap between two object pairs {u,v} and {p,q} where operator I computes the intersection area between two boxes and U the union area. The remaining m object pairs are considered as candidates having meaningful relationships E. With E, we obtain a graph G = (V,E), which is much sparser than the original fully connected graph. Along with the edges proposed for the graph, we get the visual representations Xr = {xr1, ..., xrm} for all m relationships by extracting features from the union box of each object pair.






## Research papers:
- [Paper on Scene Graph Generator](https://openaccess.thecvf.com/content_ECCV_2018/papers/Jianwei_Yang_Graph_R-CNN_for_ECCV_2018_paper.pdf)
- [Paper on REPN](https://openaccess.thecvf.com/content_cvpr_2017/papers/Zhang_Relationship_Proposal_Networks_CVPR_2017_paper.pdf)

----------
  

## Domains Explored
Artificial intelligence,Deep Learning , Neural networks , Python , Libraries such as Pytorch,TensorFlow , Numpy, Pandas

----------
  
## Project Workflow
- Learning the basics of deep learning.
- Learning about convolutional Neural Networks and object detection algorithms.
- Learning about YOLO ( you only look once ) and implementing it.
- Learning about RNNs and Attention models
- Researching on REPN (Relationship Proposal Network)
- Implenting REPN from scratch using Pytorch 
- Training the RePN on visual genome
- connecting the RePN to the yolo object detection framework to obtain information about the detected objects.

-----------

## Future Work

- [ ] Implementing an Attention Graph Convolutional Neural Network to display image descriptions as proper sentences.
- [ ] Add a better YOLO version (v7 or v8) to improve the model.
- [ ] Achive higher accuracy of the model.

------------

## Courses Referred:
- [Neural Networks and Deep Learning](https://www.coursera.org/programs/vjti-cse-learning-program-batch-2022-2026-br5qt/learn/neural-networks-deep-learning?source=search)
- [Convolutional Neural Networks](https://www.coursera.org/learn/convolutional-neural-networks)
    
------------
  
  


## Contributors

* [Kamakshi Ramamurthy](https://github.com/Kamakshi8104)
* [Sarvesh Badjugar](https://github.com/LittleSani)
--------------


## Acknowledgements and References
* [SRA VJTI][https://sravjti.in/] Eklavya 2023
* Special thanks to our mentors [Prit Kanadiya](https://github.com/PritK99) and [Raghav Agarwal](https://github.com/Raghav323)
* [Darknet for yolo object detection](https://pjreddie.com/darknet/yolo/)



  






