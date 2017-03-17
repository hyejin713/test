import numpy as np
import tensorflow as tf

x = tf.constant([[1.0, 2.0]])
w = tf.constant([[2.0], [2.1]])
y = tf.matmul(w,x)
print(x.get_shape())
print(w.get_shape())
print(y)
print(y.get_shape())

# print(np.random.randn(100,2))