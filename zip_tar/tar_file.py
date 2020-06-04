import tarfile

def un_tar(file_name,  # 压缩包路径,为XXX.tar.gz文件
           save_path):  # 解压后文件保存文件夹路径
    '''对XXX.tar.gz压缩包文件解压'''

    tar = tarfile.open(file_name)

    # 获取压缩包中的所有文件及文件夹(包括子文件夹中文件)
    names = tar.getnames()
    # 判断保存文件的文件夹路径是否存在
    if os.path.isdir(save_path):
        pass
    else:
        os.mkdir(save_path)

    # 将压缩中的文件解压到指定文件夹下
    for name in names:
        tar.extract(name, save_path)
    tar.close()


file_name = os.path.join(WORK_DIRECTORY, filename)
save_path = os.path.join(WORK_DIRECTORY, "tar_data")
un_tar(file_name, save_path)

import numpy as np
import gzip


def get_data(data_path, num_images):
    """从压缩包中读取数据"""

    with gzip.open(data_path) as bytestream:
        bytestream.read(16)
        buf = bytestream.read(IMAGE_SIZE * IMAGE_SIZE * num_images * NUM_CHANNEL)
        data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
        return data