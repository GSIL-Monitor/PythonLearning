a = """<span class="f-fr kstime">14:58</span>
<span class="f-fr kstime">10:33</span>
<span class="f-fr kstime">21:38</span>
<span class="f-fr kstime">13:49</span>
<span class="f-fr kstime">24:50</span>
<span class="f-fr kstime">13:14</span>
<span class="f-fr kstime">09:36</span>
<span class="f-fr kstime">12:19</span>
<span class="f-fr kstime">12:10</span>
<span class="f-fr kstime">13:25</span>
<span class="f-fr kstime">13:12</span>
<span class="f-fr kstime">07:14</span>
<span class="f-fr kstime">08:37</span>
<span class="f-fr kstime">09:17</span>
<span class="f-fr kstime">05:32</span>
<span class="f-fr kstime">13:57</span>
<span class="f-fr kstime">05:07</span>
<span class="f-fr kstime">07:04</span>
<span class="f-fr kstime">10:25</span>
<span class="f-fr kstime">06:31</span>
<span class="f-fr kstime">11:49</span>
<span class="f-fr kstime">08:37</span>
<span class="f-fr kstime">14:02</span>
<span class="f-fr kstime">06:33</span>
<span class="f-fr kstime">07:32</span>
<span class="f-fr kstime">05:52</span>
<span class="f-fr kstime">04:50</span>
<span class="f-fr kstime">07:33</span>
<span class="f-fr kstime">06:55</span>
<span class="f-fr kstime">05:07</span>
<span class="f-fr kstime">06:39</span>
<span class="f-fr kstime">08:27</span>
<span class="f-fr kstime">09:07</span>
<span class="f-fr kstime">13:03</span>
<span class="f-fr kstime">06:01</span>
<span class="f-fr kstime">08:44</span>
<span class="f-fr kstime">10:23</span>
<span class="f-fr kstime">04:43</span>
<span class="f-fr kstime">05:55</span>
<span class="f-fr kstime">08:23</span>
<span class="f-fr kstime">13:48</span>
<span class="f-fr kstime">07:13</span>
<span class="f-fr kstime">04:51</span>
<span class="f-fr kstime">09:28</span>
<span class="f-fr kstime">08:45</span>
<span class="f-fr kstime">11:06</span>
<span class="f-fr kstime">06:23</span>
<span class="f-fr kstime">08:39</span>
<span class="f-fr kstime">04:08</span>
<span class="f-fr kstime">06:44</span>
<span class="f-fr kstime">13:54</span>
<span class="f-fr kstime">22:43</span>
<span class="f-fr kstime">09:46</span>
<span class="f-fr kstime">14:26</span>
<span class="f-fr kstime">10:05</span>
<span class="f-fr kstime">07:04</span>
<span class="f-fr kstime">09:41</span>
<span class="f-fr kstime">12:33</span>
<span class="f-fr kstime">11:46</span>
<span class="f-fr kstime">13:14</span>
<span class="f-fr kstime">10:58</span>
<span class="f-fr kstime">08:11</span>
<span class="f-fr kstime">16:14</span>
<span class="f-fr kstime">10:52</span>
<span class="f-fr kstime">09:16</span>
<span class="f-fr kstime">13:10</span>
<span class="f-fr kstime">10:00</span>
<span class="f-fr kstime">09:52</span>
<span class="f-fr kstime">13:56</span>
<span class="f-fr kstime">18:36</span>
<span class="f-fr kstime">06:23</span>"""

import re
b='<span class="f-fr kstime">06:23</span>'
print(b)
print(re.findall('\d\d\:\d\d',a))
mtime=0
stime=0
for t in re.findall('\d\d\:\d\d',a):
    mtime= float(t.split(":")[0])+mtime
    stime = stime+ float(t.split(":")[1])

print(mtime,stime,(mtime+stime/60)/60)

# exit(0)
# 将正则表达式编译成Pattern对象


pattern = re.compile("\d\d")

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match(a)

if match:
    # 使用Match获得分组信息
    print(match.groups().count())

# tt=re.match(r'\d', a).groups()
# print(tt)

# encoding: UTF-8


