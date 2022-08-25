# Brief Discussion of Most Common Machine Learning Algorithms

## 1. Supervised Machine Learning Algorithms


### Simple Linear Regression

It depicts a relationship that is established between an independent variable and a dependent variable by fitting them to a line. This line is known as the regression line and represented by a linear equation: 
                
                        Y = AX + B

### Multiple Linear Regression

Multiple Linear Regression is one of the important regression algorithms which models the linear relationship between a single dependent continuous variable and more than one independent variable.

### Logistic Regression

It is used to estimate discrete values (usually binary values like 0/1) from a set of independent variables. It helps predict the probability of an event by fitting data to a logit function. It is also called logit regression.

### Decision Tree

This is a supervised learning algorithm that is used for classification. It works well classifying for both categorical and continuous dependent variables.


### Random Forest Algorithm

It is used widely in Classification and Regression problems. It builds decision trees on different samples and takes their majority vote for classification and average in case of regression. It performs better results for classification problems.

### KNN (K- Nearest Neighbors)

K-NN algorithm stores all the available data and classifies a new data point based on the similarity. This means when new data appears then it can be easily classified into a well suited category by using K-NN algorithm.

K-NN algorithm can be used for Regression as well as for Classification but mostly it is used for the Classification problems.

### Naive Bayes

Naïve Bayes algorithm is a supervised learning method, which is based on Bayes theorem and used for solving classification problems.

<div style="page-break-after: always;"></div>

It is mainly used in text classification that includes a high-dimensional training dataset.

Naïve Bayes Classifier is one of the simple and most effective Classification algorithms which helps in building the fast machine learning models that can make quick predictions.

It is a probabilistic classifier, which means it predicts on the basis of the probability of an object.

Some popular applications of Naïve Bayes Algorithm are spam filtration, Sentimental analysis, and classifying articles.


### SVM (Support Vector Machines) Algorithm

SVM algorithm is a method of classification algorithm in which you plot raw data as points in an n-dimensional space (where n is the number of features you have).

The goal of the SVM algorithm is to create the best line or decision boundary that can segregate n-dimensional space into classes so that we can easily put the new data point in the correct category in the future. This best decision boundary is called a hyperplane.

## 2. UnSupervised Machine Learning Algorithms

### K-Means Clustering

K-Means Clustering is an Unsupervised Learning algorithm, which groups the unlabeled dataset into different clusters. Here K defines the number of pre-defined clusters that need to be created in the process, as if K=2, there will be two clusters, and for K=3, there will be three clusters, and so on.

### Hierarchical Clustering 

It is another unsupervised machine learning algorithm, which is used to group the unlabeled datasets into a cluster and also known as hierarchical cluster analysis or HCA.

In this algorithm, we develop the hierarchy of clusters in the form of a tree, and this tree-shaped structure is known as the dendrogram.

Sometimes the results of K-means clustering and hierarchical clustering may look similar, but they both differ depending on how they work.

The hierarchical clustering technique has two approaches:

1) Agglomerative: Agglomerative is a bottom-up approach, in which the algorithm starts with taking all data points as single clusters and merging them until one cluster is left.

2) Divisive: Divisive algorithm is the reverse of the agglomerative algorithm as it is a top-down approach.

Reference:

<https://www.javatpoint.com/machine-learning>
