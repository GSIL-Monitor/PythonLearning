import datetime
import hashlib
import os
from time import sleep
from urllib import request
import random
import cv2, json
import numpy as np
from .mailUtils import mail_send


def image_features(url, path):
    """
    :param url:  下载url来源
    :param path: 下载目标文件
    :return:
    """
    try:
        if download_image_succ(url, path):
            md5 = get_image_md5(path)
            p_hash, a_hash = get_hash_feature(path)
        else:
            md5 = a_hash = p_hash = None
    except BaseException as e:
        json_data = {'type': 'error', 'event': 'on get image_features',
                     'data': {'url': url, 'path': path, 'BaseException': e}}
        post_data = json.dumps(json_data)
        print(post_data)
        mail_send(mail_body=post_data)
        md5 = a_hash = p_hash = None
    return md5, p_hash, a_hash


def url_reset(url):
    """
    :param url: 微信提供的头像链接
    :return url: 替换结尾的图片尺寸参数,使用/132为计算用的尺寸
    """
    import re
    replace_reg = re.compile(r'/\d+$')
    url = replace_reg.sub('/132', url)
    return url


def download_image_succ(url, file_path):
    """
    :param url: 头像地址
    :param file_path: 头像下载后保存路径
    :return: 先url是否存在,再看文件是否存在就,有url的就重新下载头像,没有url先看有没有头像文件,有的话直接用,没有的话就返回没有文件
    """
    # 设置下载超时30s
    import socket
    socket.setdefaulttimeout(30)

    if url is None or len(url.strip()) == 0:
        if os.path.exists(file_path):
            return True
        else:
            print('{path} :this path\'s url is empty.'.format(path=file_path))
            return False
    else:
        if not os.path.exists(file_path):
            url = url_reset(url)
            print(url, file_path)
            request.urlretrieve(url, file_path)
            sleep(random.random() / 1000)
        return True


def get_image_md5(file_path):
    """
    :param file_name: 文件名
    :param url: 头像地址
    :param file_path: 头像下载后保存路径
    :return:如果要保存的目标文件已经有,就不下载了直接用该文件生成md5,
    """
    if os.path.exists(file_path):
        fd = open(file_path, "rb")
        fcont = fd.read()
        fmd5 = hashlib.md5(fcont).hexdigest()
        fd.close()
        return fmd5
    else:
        return None


def get_hash(image):
    average = np.mean(image)
    hash_list = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] > average:
                hash_list.append(1)
            else:
                hash_list.append(0)
    return ''.join(map(str, hash_list))


def transformgif2png(file_path):
    from PIL import Image
    im = Image.open(file_path)
    im.putpalette(im.getpalette())
    new_im = Image.new("RGBA", im.size)
    new_im.paste(im)
    new_file = file_path.replace('.jpeg', '.png')  # todo 待优化,用正则替换会更安全,目前瞒住需求
    new_im.save(new_file)
    print('transform gif to jpeg:{file}'.format(file=file_path))
    return new_file
    pass


# 对一个图片计算hash特征值
def get_hash_feature(file_path):
    """
    :param file_path: 传入图片文件路径
    :return:(p_hash, a_hash)
    # 取左上角的8*8，这些代表图片的最低频率
    # 这个操作等价于c++中利用opencv实现的掩码操作
    # 在python中进行掩码操作，可以直接这样取出图像矩阵的某一部分
    """
    cv_imread = cv2.imread(file_path)
    if cv_imread is None:
        file_path = transformgif2png(file_path)
        cv_imread = cv2.imread(file_path)
        pass
    # p_hash
    image = cv2.resize(cv_imread, (32, 32))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dct = cv2.dct(np.float32(gray))
    dct_roi = dct[0:8, 0:8]
    p_hash = get_hash(dct_roi)
    # a_hash
    image1 = cv2.resize(cv_imread, (8, 8))
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    a_hash = get_hash(gray1)

    return p_hash, a_hash


if __name__ == '__main__':
    mail_send()

    pass
