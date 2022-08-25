# Machine Learning

## Introduction

"Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed."

Machine learning focuses on the development of computer programs that can access data and use it to learn for themselves.

The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in data and make better decisions in the future based on the examples provided.

### Applications of Machine Learning

Some most common applications where Machine Learning is used are depicted in this figure: 

![QR](Applications_Machine_Learning.png)

### Types of Machine Learning

There are four types of Machine Learning, which are briefly discussed below:

1. Supervised
   - Works under supervision
   - Teacher teaches
   - Prediction
   - Outcome

2. Unsupervised/Clustering
   - No supervision
   - No teacher
   - Self learning
   - No labeling of data
   - Finds pattern by itself

3. Semisupervised
   - Mixture of supervised and unsupervised learnings
   - Some of the data is labeled and most is not labeled
     
4. Reinforcement
   - Hit and Trail learning
   - Learn from mistakes
   - Reward and punishment rule
   - Prediction based on reward and punishment
   - Depends on feedback

### Supervised Machine Learning
This machine learning type takes in raw and labeled data to train the model, and then it is abled to predict any input value based on the training dataset. How a supervised machine learning algorithm works:

![QR](supervised.png)

There are two broad categories of Supervised Machine Learning:

a) Classification
   - For categories

![QR](classification.png)

b) Regression  
- For numerical/continuous data

![QR](regression.png)

#### Supervised Machine Learning Algorithms:

- Linear Regression
- Logistic Regression
- K-Nearest Neighbors (K-NN)
- Support Vector Machines (SVM)
- Kernel SVM
- Naive Bayes
- Decision Tree Classification
- Random Forest Classification

### Unsupervised Machine Learning

In unsupervised machine learning, the output is unknown, only the input data is available. The algorithm learns by itself and discovers patterns in the data.

![QR](unsupervised.png)

#### Unsupervised Machine Learning Algorithms:

Following are the well known unsupervised machine learning algorithms:

- K-Means Clustering
- Hierarchical Clustering
- Probabalistic Clustering

### Semisupervised Machine Learning
Some labelled data and some unlabelled data. The first step is to cluster similar data with the help of an unsupervised machine learning algorithm. Next, unlabelled data is labelled using the characteristics of the limited labelled data available. After labelling the complete data, one can use supervised learning algorithms to solve the problem.

![QR](semisupervised.png)

<div style="page-break-after: always;"></div>

### Reinforcement Learning

In this type of machine learning, models are trained to make a series of decisions based on the rewards and feedback they receive for their actions. 

The machine learns to achieve a goal in complex and uncertain situations and is rewarded each time it achieves it during the learning period.

The machine learns from its own experiences when there is no training data set present.

![QR](reinforcement.png)

#### Reinforcement Learning Algorithms:

- Model Free Reinforcement Learning
  - Policy Optimization
  - Q-Learning 

- Model Based Reinforcement Learning
  - Learn the Model
  - Given the Model

<div style="page-break-after: always;"></div>

## Scikit-Learn Library

Open-source ML library for Python. Built on NumPy, SciPy, and Matplotlib.

In the real world, however, we don’t want to recreate a complex algorithm every time we want to use it. Writing an algorithm from scratch is a great way to understand the fundamental principles of why it works, but we may not get the efficiency or reliability we need. Therefore, we bring in use already written codes by experts which are known as libraries. Although, there are many libraries for applying machine learning such as Keras, PyTorch, and TensorFlow, however, for basic understanding we are going to learn and apply machine learning with Scikit-Learn library.

Scikit-learn is a library in Python that provides many unsupervised and supervised learning algorithms. It’s built upon some of the technology you might already be familiar with, like NumPy, pandas, and Matplotlib!

The functionality that scikit-learn provides include:

- Regression, including Linear and Logistic Regression
- Classification, including K-Nearest Neighbors
- Clustering, including K-Means and K-Means++
- Model selection
- Preprocessing, including Min-Max Normalization

### How to install scikit-learn library in VSCode IDE or Jupyter Notebook

Open Terminal in VSCode (Ctrl + Shift + ~) and run the below command:

```python
pip install -U scikit-learn
```

Reference:
<https://www.codecademy.com/article/scikit-learn>
