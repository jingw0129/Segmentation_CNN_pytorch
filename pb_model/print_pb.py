from tensorflow.python.framework import tensor_util
from google.protobuf import text_format
import tensorflow as tf
from tensorflow.python.platform import gfile
from tensorflow.python.framework import tensor_util

pb_path = './model.pb'

with tf.Session() as sess:
    with gfile.FastGFile(pb_path, 'rb') as f:
        graph_def = tf.GraphDef()

        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')
        for i, n in enumerate(graph_def.node):
            print("Name of the node -%s" % n.name)