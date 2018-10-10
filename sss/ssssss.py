t = [0, 8, 7, 6, 5, 4]
print(sum(t))

exit(1)

a = [x for x in range(10)]  # 10个值
print(a)
print(sum(a))

b = []  # 7个值

c = []  # 5个值
e = []  # 5个值
f = []  # 5个值

for i in range(10):
    # 第一步 随机取 a 的一个值给所以的集合,
    b.append()
    # 第二步 随机取 a剩下的值 的三个值给到 b 和 cef的两个
    # 第三步 随机取 a剩下的值 的三个值给到 b 和 cef的一个
    # 第四步 随机取 a剩下的值 的三个值给到 cef

    s_b = sum(b)
    s_c = sum(c)
    s_e = sum(e)
    s_f = sum(f)

    all_eq = (s_b == s_c == s_e == s_f)

    if all_eq:
        print(b, c, e, f)
        print(s_b)
    else:
        print('not equals, so', all_eq)

# s = x7+x3+x6+x8+x2+x4+x9
# s = x1+x2+x3+x6+x7
# s = x4+x5+x3+x7+x8
# s = x7+x8+x6+x9+x0
# 45 = x0+x1+x2+x3+x4+x5+x6+x7+x8+x9
