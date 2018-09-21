# coding:utf-8
# import sys
# sys.encoding('utf8')

# __author__ = '郭 璞'
# __date__ = '2016/8/6'
# __Desc__ = 文字转语音输出
# pyttsx仅在Python2.7版本适用
# Python3.5要用 pyttsx3
import pyttsx3

engine = pyttsx3.init()
engine.say('hello world')
engine.say('你好，郭璞')
engine.runAndWait()
# 朗读一次
engine.endLoop()
