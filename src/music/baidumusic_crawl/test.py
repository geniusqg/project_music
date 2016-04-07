# -*- coding: utf-8 -*-

import os
import string
def backread(file,size=100):
    '''倒读文件内容'''
    file.seek(0,os.SEEK_END)
    file_size=int(file.tell())
    read_circle = file_size/size+1 if file_size%size else file_size/size
    read_size = size
    for i in range(read_circle):
        buf = file_size-(i+1)*size
        if buf < 0:
            buf = 0
            read_size = file_size-i*size
        file.seek(buf,0)
        print file.read(read_size)


def backreadline(file,size=30):
    '''倒读文件内容，按行输出'''
    file.seek(0,os.SEEK_END)
    str_buf = ''
    while True:
        find = str_buf.rfind('\n')
        pointer = file.tell()
        if find != -1:
            line = str_buf[find+1:]
            str_buf = str_buf[:find]
            #if line:
             #   line += '\n'
            yield line
        else:
            if pointer == 0:
                break
            else:
                read_buf = min(size, pointer)
                file.seek(-read_buf,1)
                str_buf = file.read(read_buf) + str_buf
                file.seek(-read_buf,1)
                if pointer == read_buf:
                    str_buf = '\n' + str_buf

def toreadline(file,size=30):
    '''正读文件内容，按行输出'''
    file.seek(0,os.SEEK_END)
    file_size = file.tell()
    file.seek(0,0)
    str_buf = ''
    while True:
        find = str_buf.find('\n')
        pointer = file.tell()
        if find != -1:
            line = str_buf[:find]
            str_buf = str_buf[find+1:]
            #if line:
             #   line += '\n'
            yield line
        else:
            if pointer == file_size:
                break
            else:
                read_buf = min(size, file_size-pointer)
                str_buf += file.read(read_buf)
                #print 'str_buf=',str_buf
                if file_size-pointer < size:
                    str_buf += '\n'



class BackwardsReader:
    """Read a file line by line, backwards"""
    BLKSIZE = 1024
    def readline(self):
        while 1:
            newline_pos = string.rfind(self.buf, "\n")
            print 'buf=',self.buf
            pos = self.file.tell()
            print 'pos=',pos
            if newline_pos != -1:
                # Found a newline
                line = self.buf[newline_pos+1:]
                self.buf = self.buf[:newline_pos]
                if pos != 0 or newline_pos != 0 or self.trailing_newline:
                    line += "\n"
                yield line
            else:
                if pos == 0:
                    # Start-of-file
                    break
                else:
                    # Need to fill buffer
                    toread = min(self.BLKSIZE, pos)
                    self.file.seek(-toread, 1)
                    self.buf = self.file.read(toread) + self.buf
                    self.file.seek(-toread, 1)
                    if pos - toread == 0:
                        self.buf = "\n" + self.buf
    def __init__(self, file):
        self.file = file
        self.buf = ""
        self.file.seek(-1, 2)
        self.trailing_newline = 0
        lastchar = self.file.read(1)
        if lastchar == "\n":
            self.trailing_newline = 1
            self.file.seek(-1, 2)

if __name__=="__main__":
    #br = BackwardsReader(open('items.py'))
    #for i in br.readline():
        #print i

    for line in toreadline(open('items.py'),50):
        print 'line=',line

