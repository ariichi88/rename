#! /usr/bin/env python3
# coding: UTF-8

import os
import sys


FROM_DIR = '~/ダウンロード/'


def usage():
    print('使用法: rename 拡張子 新しい名前')
    print('拡張子は大文字小文字を区分します。')
    exit(1)


def rename(ext, new_name):
    from_files = [f for f in os.listdir(FROM_DIR) if ext in f]
    from_files.sort()
    for index, from_file in enumerate(from_files):
        os.rename(from_file, new_name + '-' + format(index, '02') + ext)


def main(arg):
    if len(arg) == 3:
        ext = arg[1]
        new_name = arg[2]
        rename(ext, new_name)
    else:
        usage()
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
