# Important Metrices for Measuring the Classification Model Accuracy

Following are some of the most commonly used performace metrices of classfication models:

## 1- Classification Accuracy
#

It is mostly used metrix for measuring the accuracy of a classification model. However, alone this accuracy metrix is not sufficient. Most importantly, it is not suitable for a training set that is dominant by one class from the responce variable.

For example, if a training set contains two classes, such as A and B, where class A represents 90% of the training set data. This will make the training model biased. Hence, it will usually render incorrect predictions.

Even though the accuracy score is 90%, but that is based on the biased model. This may cause costly consequences, for example, when a patient undergoes a very rare disease, but that was missclassified because of the dominant class. However, this metrix works best where the classes in the training dataset are in relative proportions i.e. in the range of 40/60 and 50/50.

Application accuracy measure in code:
```python
from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_pred)
```

## 2- Logarithmic Loss (log-loss)
#
Works well for multi class training dataset. It measures the accuracy of classfication model by returning output in the range of 0 to infinity.
Closer to 0 means that the model is highly accurate, whereas going away from zero shows that the model is less accurate.

Example code:

```python
from sklearn.metrics import log_loss
score = log_loss(y_test, clf_probs)
cal_score = log_loss(y_test, cal_clf_probs)
```

## 3- Jaccard Index
#
Also known as Jaccard similarity coefficient is a metrix to identify the similarity of the two sets. It is defined as the size of intersection (common) of the two sets divided by the size of the union of the same two sets and multiplied by 100. This metrix is used to compare set of predicted values for a sample to the corresponding set of true values.

Example code:

```Python
from sklearn.metrics import jaccard_score
jaccard_score(y_true, y_pred)
```

## 4- Confusion Metrix
#
It returns a matrix in the output, which describes the performance of the model.

There are four important terms in this metrix:

1. True Positive: The case in which both the prediction and the actual output are true.

2. True Negative: Both the predicted output and the actual output are false.

3. False Positive: Here the predicted values are true, but the actual outputs are false.

4. False Negative : Predicted values are false, but the actual output values are true.

True positive and true negative both lie on the main diagonal, however, False Positive and False Negative lie across the anti-diagonal of the metrix.

For example, a set of gender as responce variable consists of two classes i.e. Male and Female. The males are represented by 1, and the females are represented by 0. So, for binary output, the output confusion metrix would look like this:

![QR](capture.png)

Numbers across the main diagonal represent correct predictions and thus they are added to know the total number of right predictions by the model, and the sum of output values on the anti-diagonal are those which were predicted wrongly. In our example case:

Correct predictions: 50 + 50 = 100
Incorrect predictions: 5 + 10 = 15.

Python code for measuring confusion metrix accuracy:
```python
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_true)
```

## 5- Area Under the Receiver Operating Characteristic Curve (ROC AUC)
#

This is the curve for performance measurement of a classification model, and is most widely used for measuring accuracy. It can be used with binary, multiclass and multilabel classifications.


Code implementation:

```
from sklearn import metrics

```

## 6- Recall Score
#

The recall is the ratio TP / (TP + FN) where TP is the number of true positives and fn the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples.

The best value is 1 and the worst value is 0.

Code to implement this metrix for binary class training set:
```python
from sklearn.metrics import recall_score
recall_score(y_true, y_pred)
```

## 7- Precision Score
#

The precision is the ratio TP / (TP + FP) where TP is the number of true positives and FP IS the number of false positives. The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.

The best value is 1 and the worst value is 0.

Code for Precision Score:
```python
from sklearn.metrics import precision_score
precision_score(y_true, y_pred)
```

## 8- F1 Score
#

The F1 score can be interpreted as a harmonic mean of the precision and recall, where an F1 score reaches its best value at 1 and worst score at 0. The relative contribution of precision and recall to the F1 score are equal. The formula for the F1 score is:

F1 = 2 * (precision * recall) / (precision + recall)

In the multi-class and multi-label case, this is the average of the F1 score of each class with weighting depending on the average parameter.

How to apply F1 performance metrix:

```python
from sklearn.metrics import f1_score
f1_score(y_true, y_pred)
```

## 9- Mean Absolute Error
#

MAE is an accuracy metrix, which is the average of the absolute differences between the true values of responce variable and the predicted outcomes. It determines how far the predicted points are placed from the actual/true plot.

The best value for MAE is 0. The higher the value of MAE shows that the predictions are away from the actual, and hence the model is less accurate.

Code Implementation:

```python
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_true, y_pred)
```

## 10- Mean Squared Error:
#

This metrix is mean of the squared differences between the true values of responce variable and the predicted outcomes.

Code:
```python
from sklearn.metrics import mean_squared_error
mean_absolute_error(y_true, y_pred)
```

## Refrences:

1. https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
2. https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234
3. https://therised.medium.com/evaluation-metrics-for-classification-models-f27dfc276b87
