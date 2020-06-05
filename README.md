# Fake News Classifier

Exploratory project to predict fake news based on his text.

The models could be found on this repository as well as its implementation

The used dataset is a compiled real-world news, in which the truthful news were collected from Reuters.com and the fake news from multiple sources [[1]](#1)[[2]](#2).

The dataset could be found on: https://www.uvic.ca/engineering/ece/isot/datasets/index.php

## [The Classifier](https://github.com/Victoraq/FakeNewsClassification/blob/master/FakeNewsClassification.ipynb)

Multiple models were evaluated to find the best classificator for fake news. During the tests, the following classifiers obtained the best performance: Support Vector Machine, Decision Tree, and the Gradient Boost. Therefore, they were ensembled into a voting classifier to improve their performance which obtained 99.72% of accuracy over the test set.

## [The Server](https://github.com/Victoraq/FakeNewsClassification/tree/master/server)

A basic flask server was implemented to use as a fake news classifier. Where it uses the model to classify news by the provided URL.

## Improvements

 * Bias: The classifier shows a strong bias when predicting news from another sources besides the Reuters. After tests using the server, the model does not classify trustful news websites as truthful provider, like New York Times or BBC.
 * More Features: Apply an automatic feature extractor on the dataset. This approach could improve the bias issue and the models' performance.
 * More data: The main cause of the Bias issue is the unique provider of true news. Add more fake and true news could improve the models' performance in real-world prediction.

## References
<a id="1">[1]</a> Ahmed H, Traore I, Saad S. “Detecting opinion spams and fake news using text
classification”, Journal of Security and Privacy, Volume 1, Issue 1, Wiley,
January/February 2018.

<a id="2">[2]</a> Ahmed H, Traore I, Saad S. (2017) “Detection of Online Fake News Using N-Gram
Analysis and Machine Learning Techniques. In: Traore I., Woungang I., Awad A. (eds)
Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments.
ISDDC 2017. Lecture Notes in Computer Science, vol 10618. Springer, Cham (pp. 127-
138).
