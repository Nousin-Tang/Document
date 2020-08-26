# coding = utf-8
import os
# 到 Document 层
root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def clear_blank_line():
    file1 = open(root_path + '/java/jdk/JavaSe.md', 'r', encoding='utf-8')  # 要去掉空行的文件
    file2 = open(root_path + '/java/jdk/JavaSe2.md', 'w', encoding='utf-8')  # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clear_blank_line()
