## Support Vector Machine

"SVM is mainly a classification algorithm, however, it can also be used for regression. For classification problem, it creates binary or multiple classes based on the features."

For example, classifying the data into Men and Women, or Upper Class, Middle Income, and Lower Income.

SVM is a supervised learning algorithm, so it needs training data. The goal of a support vector machine is to find the optimal separating hyperplane which maximizes the margin of the training data.

### What is a Hyper-Plane?

"A hyperplane is a decision boundary that separates the data points and attributes them into classes."

The dimension of a hyperplane depends on the number of input features in the dataset. If there are 2 input features, the hyper-plane will be a line in 2D space. However, if the number of features is 3, hyper-plane will classify the data in a 3D space and it will be a plane.

### Support-Vectors

Support vectors are the points, which lie nearest to the hyper-plane. 

They guide the position and the orientation of a hyper-plane. 

A hyperplane is adjusted, where the distance between support vectors and the hyper-plane is maximum. That maximum distance is called "Margin".

![QR](SV.png)

### What is the goal of Support Vector Machine?

It determines the optimal separating hyperplane which maximizes the margin of the training data. Let's understand the function of SVM and the hyperplane with the help of following example and visuals.\
For example, weight of population is plotted against their heights in the following scatter plot. The blue colored plus signs show the class of men, whereas the red dots represent weights of women based on their heights.\
![QR](SVM.png)\
From the above plot, it is easier to identify that if someone has height 175 cm and weighs 80 kgs, is it a man or a woman?

Just by looking at the plot, we can see that it is possible to separate the data.  For instance, we could trace a line and then all the data points representing men will be above the line, and all the data points representing women will be below the line.

Such a line is called a separating hyperplane and is depicted below:

![QR](hyper.png)

### What is the optimal separating hyperplane?

A separating line or hyperplane does not mean that it's the best classifier. In the following visual, there are many separating lines that rightfully divides the data into classes such as in the following visual:

![QR](SL.png)

Suppose that we consider the green line to classify the data.\
![QR](green.png)\
It can be seen from the above figure that the green line separates the classes in such a away that some of the women land in the portion of men. Hence, the green line is not optimal because it is at a position, where data points from the women portion are nearer. Therefore, while separating the data, it is must that the line is farthest from the data points of both classes. Therefore, line in the following figure perfectly classifies the data points because it is at a maximum distance from both classes.\
![QR](fit.png)

The objective of SVM model is to find the optimal separating hyperplane i.e. to correctly classify the training data
and because it is the one which will generalize better with out-of-sample data.

### How does the margin help choose optimal hyperplane?

Margin is the empty space between the data points and the hyperplane. No points land in this area. Margins are depicted in the following two visuals, where one has more space than the other.

![QR](margin1.png)

Margin A is maximum since the hyperplane is farther from the data points.

![QR](margin2.png)

Here, the data points are closer to the hyperplane, hence, area of Margin B is smaller.

It is obvious from the above discussion that the optimal hyperplane is the one which has the highest margin.
