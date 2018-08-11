# coding:utf-8
import sys
from importlib import reload

import pyttsx3

reload(sys)
# __author__ = '郭 璞'
# __date__ = '2016/8/6'
# __Desc__ = 文字转语音输出

engine = pyttsx3.Engine

engine.say('hello world')
engine.say('你好，郭璞')
engine.runAndWait()
# 朗读一次
engine.endLoop()