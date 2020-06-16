# Fake News Classifier

Exploratory project to predict fake news based on his text.

The models could be generated with its implementation [here](https://github.com/Victoraq/FakeNewsClassification/blob/master/FakeNewsClassification.ipynb).

The used dataset is a compiled real-world news, in which the truthful news were collected from Reuters.com and the fake news from multiple sources [[1]](#1)[[2]](#2).

The dataset could be found on: https://www.uvic.ca/engineering/ece/isot/datasets/index.php

## The Classifier

Multiple models were evaluated to find the best classificator for fake news. During the tests, the following classifiers obtained the best performance: Support Vector Machine, Random Forest, and the Stochastic Gradient Descent. Therefore, they were ensembled into a voting classifier to improve their performance which obtained 99.27% of accuracy over the test set.

## The Server

A basic flask server was implemented to use as a fake news classifier. Where it uses the model to classify news by the provided URL.

## Improvements

 * More Features: Apply an automatic feature extractor on the dataset. This approach could improve the models' generalization performance.
 * More data: The used dataset has few categories of news and only one truthful provider, include more data could improve significantly the performance.

## References
<a id="1">[1]</a> Ahmed H, Traore I, Saad S. “Detecting opinion spams and fake news using text
classification”, Journal of Security and Privacy, Volume 1, Issue 1, Wiley,
January/February 2018.

<a id="2">[2]</a> Ahmed H, Traore I, Saad S. (2017) “Detection of Online Fake News Using N-Gram
Analysis and Machine Learning Techniques. In: Traore I., Woungang I., Awad A. (eds)
Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments.
ISDDC 2017. Lecture Notes in Computer Science, vol 10618. Springer, Cham (pp. 127-
138).
