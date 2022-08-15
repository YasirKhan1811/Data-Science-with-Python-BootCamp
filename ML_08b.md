# Activation Functions

Activation functions are crucial for image classification, language transformation, disease detection, and object detection.

Activation functions define the output of input or set of inputs or in other terms defines node of the output of node that is given as input.

They basically activate or deactivate neurons to get the desired output. They also perform a nonlinear transformation on the input to get better results on a complex neural network.

Activation functions also help to normalize the output of any input in the range between 1 and -1. 

Activation functions must be efficient, and they should reduce the computation time because the neural network is sometimes trained on millions of data points.

**Types of Activation Functions**

There are 7 Activation Functions for Neural Network, which are detailed based on the following 3 major classes:

A. Binary step function

B. Linear function

C. Non-linear activation function

**A. Binary Step Neural Network Activation Function**

**1. Binary Step Function**

It is basically a threshold base classifier, wherein it defines some threshold value to decide output that neuron should be activated or deactivated.
```
f(x) = 1 if x > 0 else 0 if x < 0
```
![QR](1.png)

**B. Linear Neural Network Activation Function**
 
**2. Linear Function**

It is a simple straight line activation function, where the function is directly proportional to the weighted sum of neurons or input.

Linear activation functions are better in giving a wide range of activations and a line of a positive slope may increase the firing rate as the input rate increases.

> Y = mZ

Here derivative with respect to Z is constant m.

**C. Non Linear Neural Network Activation Function**
 
**3. ReLU( Rectified Linear unit) Activation function**
 
Rectified linear unit or ReLU is most widely used activation function right now which ranges from 0 to infinity. All the negative values are converted into zeros, and this conversion rate is so fast that neither it can map nor fit into data properly which creates a problem.

![QR](2.png)

To solve that problem, We use Leaky ReLU function instead of ReLU. In Leaky ReLU, range is expanded which enhances the performance.

**4. Leaky ReLU Activation Function**

Leky ReLU turns all the negative input values into zero.

![QR](3.png)

**5. Sigmoid Activation Function**

Sigmoid function is a probabilistic approach towards decision making and ranges in between 0 to 1. Since its output range is minimum, the prediction of sigmoid fucntion is more accurate.

![QR](4.png)

The equation for the sigmoid function is 

> f(x) = 1/(1+e(-x) )

The sigmoid function causes a problem, which occurs when we convert large input data in-between the range of 0 to 1, hence their derivatives become even more smaller, which do not give satisfactory output. 

To solve this problem another activation function such as ReLU is used where we do not have a small derivative problem.


**6. Hyperbolic Tangent Activation Function**

This activation function is slightly better than the sigmoid function. Similar to sigmoid function, it also classifies the input data in two classes, however, it maps the negative input as negative quantity only and ranges in between -1 to 1.

![QR](5.png)

**7. Softmax Activation Function**

Softmax is used mainly at the last layer i.e output layer for decision making, the softmax basically gives value to the input variable according to their weight, and the sum of these weights is eventually one.

![QR](6.png)

For Binary classification, both sigmoid and softmax are equally approachable, but in case of multi-class classification problem, we generally use softmax and cross-entropy along with it.