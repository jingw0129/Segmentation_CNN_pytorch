checkpoint是检查点的文件，文件保存了一个目录下所有的模型文件列表

model.ckpt.meta文件保存了Tensorflow计算图的结果，可以理解为神经网络的网络结构，该文件可以被tf.train.import_meta_graph加载到当前默认的图来使用

ckpt.data是保存模型中每个变量的取值

.index文件保存的是.data文件中数据和 .meta文件中结构图之间的对应关系

ckpt转换pb格式过程如下：

1，通过传入ckpt模型的路径得到模型的图和变量数据

2，通过import_meta_graph导入模型中的图

3，通过saver.restore从模型中恢复图中各个变量的数据

4，通过graph_util.convert_variables_to_constants将模型持久化

gen_pb_2
freeze_graph

总共有11个参数，一个个介绍下(必选： 表示必须有值；可选： 表示可以为空)：

1、input_graph：（必选）模型文件，可以是二进制的pb文件，或文本的meta文件，用input_binary来指定区分（见下面说明）

2、input_saver：（可选）Saver解析器。保存模型和权限时，Saver也可以自身序列化保存，以便在加载时应用合适的版本。主要用于版本不兼容时使用。可以为空，为空时用当前版本的Saver。

3、input_binary：（可选）配合input_graph用，为true时，input_graph为二进制，为false时，input_graph为文件。默认False

4、input_checkpoint：（必选）检查点数据文件。训练时，给Saver用于保存权重、偏置等变量值。这时用于模型恢复变量值。

5、output_node_names：（必选）输出节点的名字，有多个时用逗号分开。用于指定输出节点，将没有在输出线上的其它节点剔除。

6、restore_op_name：（可选）从模型恢复节点的名字。升级版中已弃用。默认：save/restore_all

7、filename_tensor_name：（可选）已弃用。默认：save/Const:0

8、output_graph：（必选）用来保存整合后的模型输出文件。

9、clear_devices：（可选），默认True。指定是否清除训练时节点指定的运算设备（如cpu、gpu、tpu。cpu是默认）

10、initializer_nodes：（可选）默认空。权限加载后，可通过此参数来指定需要初始化的节点，用逗号分隔多个节点名字。

11、variable_names_blacklist：（可先）默认空。变量黑名单，用于指定不用恢复值的变量，用逗号分隔多个变量名字。