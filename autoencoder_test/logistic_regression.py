'''
A logistic regression learning algorithm example using TensorFlow library.
This example is using the MNIST database of handwritten digits
(http://yann.lecun.com/exdb/mnist/)

Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

from __future__ import print_function

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Import get_data
import get_data
review_data = get_data.load_review_data("./data/make_data.csv")

# Parameters
learning_rate = 0.01
training_epochs = 25
batch_size = 100
display_step = 1

# Training Data
train_X = review_data.data
train_Y = review_data.target
n_samples = train_X.shape[0]

# tf Graph Input
x = tf.placeholder(tf.float32, shape=[None,2]) # mnist data image of shape 28*28=784
print(x)
y = tf.placeholder(tf.float32, shape=[None]) # 0-9 digits recognition => 10 classes
print(y)
# Set model weights
W = tf.Variable(tf.ones([2, 245]))
print(tf.shape(W))
b = tf.Variable(tf.ones([245, 245]))

# Construct model
pred = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax
# Minimize error using cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
# Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(review_data.num_examples/batch_size)
        # Run optimization op (backprop) and cost op (to get loss value)
        _, c = sess.run([optimizer, cost], feed_dict={x: train_X, y: train_Y})
        # Compute average loss
        avg_cost += c / total_batch
        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))

    print("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy:", accuracy.eval({x: train_X, y: train_Y}))