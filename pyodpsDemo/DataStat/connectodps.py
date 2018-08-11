from odps import ODPS

o = ODPS('LTAIGcHUtiuARZin',
         'pxx57vjysvBurt76Jhd93X9goMMGdc',
         project='babyfs_data',
         endpoint='http://service.odps.aliyun.com/api')

print(type(o))
