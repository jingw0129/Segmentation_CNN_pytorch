import tensorflow as tf


def model(input):
    net = tf.layers.conv2d(input, filters=32, kernel_size=3)
    net = tf.layers.batch_normalization(net, fused=False)
    net = tf.layers.separable_conv2d(net, 32, 3)
    net = tf.layers.conv2d(net, filters=32, kernel_size=3, name='output')

    return net


input_node = tf.placeholder(tf.float32, [1, 480, 480, 3], name='image')
output_node_names = 'head_neck_count/BiasAdd'
ckpt = ckpt_path
pb = pb_path

with tf.Session() as sess:
    model1 = model(input_node)
    sess.run(tf.global_variables_initializer())
    output_node_names = 'output/BiasAdd'

    input_graph_def = tf.get_default_graph().as_graph_def()
    output_graph_def = tf.graph_util.convert_variables_to_constants(sess, input_graph_def, output_node_names.split(','))

with tf.gfile.GFile(pb, 'wb') as f:
    f.write(output_graph_def.SerializeToString())