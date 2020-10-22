#!/usr/bin/env python3
# coding=utf-8

# from os.path import dirname
import getopt
import os
import sys
from base64 import b64encode
from multiprocessing import Pool
from urllib.request import Request, urlopen

# 使用说明
description = '''
        使用方法 
        1. python3 tinypng.py -r picPath
            -r 参数会压缩文件夹内的图片并替换原图片
            eg: python3 tinypng.py -r /Users/unnous/project/git-clone/Document/mysql/image
        2. python3 tinypng.py -i inputPath -o outputPath
            -o 参数可以为空，默认存在 inputPath/tinypng 内
            eg: python3 tinypng.py -i /Users/unnous/Downloads/images -o /Users/unnous/Downloads/images1
        去 https://tinypng.com/developers 申请自己的key 每key每月免费压缩500个图
        默认并发数为10 可以自己调整
        若想直接调试可以给 input_doc_path、output_doc_path 赋值
        eg：
            input_doc_path = '/Users/unnous/project/git-clone/Document/mysql/image'
            output_doc_path = '/Users/unnous/project/git-clone/Document/mysql/image'
        '''
pool_limit = 10

# 去 https://tinypng.com/developers 申请自己的key 每key每月免费压缩500个图
key = "x7nBp4w1WmmnmsDzbD0nrwJRxy82FGkT"
# 获取命令中的参数
opts, args = getopt.getopt(sys.argv[1:], "hi:o:r:")
# input = "large-input.png"
# output = "tiny-output.png"
input_doc_path = ''
output_doc_path = ''
filePaths = []

for op, value in opts:
    if op == "-r":
        input_doc_path = value
        output_doc_path = value
    elif op == "-i":
        input_doc_path = value
    elif op == "-o":
        output_doc_path = value
    elif op == "-h":
        print(description)


def abs_file_path(file_name):
    return os.path.join(input_doc_path, file_name)


def get_tiny_png(file_path):
    print('开始' + file_path)
    request = Request("https://api.tinify.com/shrink", open(file_path, "rb").read())

    ca_file = None

    auth = b64encode(bytes("api:" + key, "ascii")).decode("ascii")
    request.add_header("Authorization", "Basic %s" % auth)

    response = urlopen(request, cafile=ca_file)
    if response.status == 201:
        # Compression was successful, retrieve output from Location header.
        result = urlopen(response.getheader("Location"), cafile=ca_file).read()

        output = os.path.join(output_doc_path, os.path.relpath(file_path, input_doc_path))
        open(output, "wb").write(result)
        print('完成' + output)
    else:
        print('失败' + file_path)
        # Something went wrong! You can parse the JSON body for details.
        print("Compression failed")


def main():
    global output_doc_path
    if output_doc_path == '':
        output_doc_path = os.path.join(os.path.split(input_doc_path)[0], 'outputTinyPng')
    if not os.path.exists(output_doc_path):
        os.mkdir(output_doc_path)

    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for parent, dir_names, file_names in os.walk(input_doc_path):
        for dir_name in dir_names:  # 输出文件夹信息
            outDir = os.path.join(output_doc_path, os.path.relpath(os.path.join(parent, dir_name), input_doc_path))
            if not os.path.exists(outDir):
                os.mkdir(outDir)

        for filename in file_names:  # 输出文件信息
            filePaths.append(os.path.join(parent, filename))

    pngFilePaths = filter(lambda x: os.path.splitext(x)[1] == '.png' or os.path.splitext(x)[1] == '.jpg', filePaths)
    print('Parent process %s.' % os.getpid())
    p = Pool(pool_limit)
    for fileName in pngFilePaths:
        p.apply_async(get_tiny_png, args=(fileName,))
    print('Waiting for all sub processes done...')
    p.close()
    p.join()
    print('All sub processes done.')


if __name__ == '__main__':
    if os.path.isdir(input_doc_path):
        main()
