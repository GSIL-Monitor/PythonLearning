def url_reset(url):
    """
    :param url: 微信提供的头像链接
    :return url: 替换结尾的图片尺寸参数,使用/132为标准尺寸
    """
    import re
    replace_reg = re.compile(r'/\d+$')
    url = replace_reg.sub('/132', url)
    return url


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


if __name__ == '__main__':
    mkdir('/Users/admin/test')