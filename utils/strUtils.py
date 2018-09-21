def url_reset(url):
    """
    :param url: 微信提供的头像链接
    :return url: 替换结尾的图片尺寸参数,使用/132为标准尺寸
    """
    import re
    replace_reg = re.compile(r'/\d+$')
    url = replace_reg.sub('/132', url)
    return url
