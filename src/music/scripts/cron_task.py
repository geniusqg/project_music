# coding=utf8

u'''
添加方法前，请先看一下这个说明：
    现在这种方式有个小问题，如果你的方法回和 MYSQL 有交互
    请务必在查询前调用下django.db 的 close_old_connections 方法
'''

# django apps
import include
import django.db
# 初始化djagno环境
django.setup()



if __name__ == '__main__':
    pass
