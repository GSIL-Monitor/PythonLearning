from functools import reduce

import cv2

liat = [1,0,1,1,1,0,0]
print(liat)

print(''.join(map(str,liat)))

a1=[1,23,43]
a2=[32,33,41]

print(a1,a2,a1+a2)

a = [[1,2,3], [4,6], [7,8,9,8]]
print(a)
print( reduce(lambda x, y: x+y, a) )

path='/Users/admin/PycharmProjects/TestPro/imageFeatureExtraction/fromList/'
jpg1 = '483840_1341085.jpeg'
image_file=path+jpg1
ori_image = cv2.imread(image_file)
image = cv2.resize(ori_image, (8, 8))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(type(gray))
print(gray)
print(gray.flatten())