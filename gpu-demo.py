import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 不显示等级2以下的提示信息

print('GPU', tf.config.list_physical_devices('GPU'))

a = tf.constant(2.0)
b = tf.constant(4.0)
print(a + b)
