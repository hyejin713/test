import tensorflow as tf

filename = "./data/make_data.csv"

# features = tf.placeholder(tf.int32, shape=[3], name='features')
# country = tf.placeholder(tf.string, name='country')
# total = tf.reduce_sum(features, name='total')

# reviewerId, price,helpful,overall
reviewerID = tf.placeholder(tf.string, name='reviewerID')
features = tf.placeholder(tf.float32, shape=[3], name='features')
total = tf.reduce_sum(features, name='total')


with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    with open(filename) as inf:
        # Skip header
        next(inf)
        for line in inf:
            # Read data, using python, into our features
            reviewer_ID, price, helpful, overall = line.strip().split(",")
            price = float(price)
            helpful = float(helpful)
            overall = float(overall)
            printerop = tf.Print(total, [price, helpful, overall], name='printer')

            # Run the Print ob
            total = sess.run(printerop, feed_dict={features:[price, helpful, overall], reviewerID:reviewer_ID})
            print(reviewer_ID, total)