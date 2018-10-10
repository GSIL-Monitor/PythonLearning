import os
import random
from asyncio import sleep
from datetime import datetime
from urllib import request

from utils.strUtils import url_reset


def download_image_succ(url, file_path):
    """
    :param url: 头像地址
    :param file_path: 头像下载后保存路径
    :return: 先url是否存在,再看文件是否存在就,有url的就重新下载头像,没有url先看有没有头像文件,有的话直接用,没有的话就返回没有文件
    """
    if url is None or len(url.strip()) == 0:
        if os.path.exists(file_path):
            return True
        else:
            print('{path} :this path\'s url is empty.'.format(path=file_path))
            return False
    else:
        if os.path.exists(file_path) :
            mtime = datetime.fromtimestamp(os.stat(file_path).st_mtime)
            mtime_str = mtime.strftime('%Y%m%d')
            download_day_str = datetime.now().strftime('%Y%m%d')
            if mtime_str != download_day_str:
                request.urlretrieve(url_reset(url), file_path)
                sleep(random.random() / 100)
                # print('download 更新')
        else:
            request.urlretrieve(url_reset(url), file_path)
            sleep(random.random() / 100)
            # print('download 新文件')
        return True



if __name__ == '__main__':
    url='http://wx.qlogo.cn/mmhead/ver_1/qJ3iazsFHXVniagJOSRYPRVoqRmU8eulfxHQ86xfPbITqrtiaFmaCxs5UXqlsXc4gxlapicv3Jdl5aZTAjsKbibcmQaHFCHlw3quN7kLlykQBqiaM/96'
    file_path='/Users/admin/PycharmProjects/learn-python/demo/pic2.jpge'
    # print(os.stat(file_path))
    is_succ=download_image_succ(url, file_path)
    print(is_succ)

    pass