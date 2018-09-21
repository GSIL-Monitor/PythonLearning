#!/bin/bash
# -*- coding: utf-8 -*-
import sys
import time

def test_main(st):
    ###### 毫秒数转字符串
    # dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(st)/1000.0))
    print(st,"-->",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(st)/1000.0)))


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) > 2:
        for st in sys.argv[1:]:
            test_main(st)
    elif len(sys.argv) == 2:
        test_main(sys.argv[1])
    else:
        print("input a timestmp like 1505923200000.")

