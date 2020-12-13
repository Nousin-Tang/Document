# coding = utf-8
import os
import shutil
from openpyxl import load_workbook

# 到 Document 层
root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# # /Users/unnous/temp
source_path = '/Users/unnous/temp'
target_path = '/Users/unnous/temp'

# 大类名称	小类名称	货号
# 123	456	789
excel_path = '新建文件.xlsx'

# 获取原文件夹内容
source_path_list = os.listdir(source_path)


def remove_file(source_file_contents):
    for file_content in source_file_contents:
        src = os.path.join(file_content.path)
        dst = os.path.join(target_path, os.sep, file_content.sub_path)
        if not os.path.exists(dst):
            os.makedirs(dst)
        # 拷贝文件夹
        shutil.copytree(src, dst)
        # 移动文件
        # shutil.copy(src, dst)
        # 移动文件（夹）
        # shutil.move(src, dst)
        # 删除文件夹及内容
        # shutil.rmtree(src)


# 读取 Excel 中内容
def read_source_path():
    # 获取项目根目录
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    # 文件路径
    filePath = os.path.join(PROJECT_ROOT, excel_path)
    # 打开一个workbook
    wb = load_workbook(filename=filePath, data_only=True)
    # 获取第一张工作表（通过索引的方式）
    table = wb.get_sheet_by_name(wb.get_sheet_names()[0])
    # values 用来存放数据
    values = []
    for rowNum in range(2, table.max_row + 1):
        val1 = str(table.cell(row=rowNum, column=1).value)
        val2 = str(table.cell(row=rowNum, column=2).value)
        val3 = str(table.cell(row=rowNum, column=3).value)
        values.append(val1 + os.sep + val2 + os.sep + val3)
    # 将table中第一行的数据读取并添加到data_list中
    return values


# Excel 中文件内容
class FileContent:
    def __init__(self, path, sub_path):
        # 目标文件夹
        self.path = path
        # 包含路径
        self.sub_path = sub_path


def match_path(files):
    result = []
    for f in source_path_list:
        for s in files:
            if f.endswith(s):
                result.append(FileContent(f, s))
                break
    return result


if __name__ == '__main__':
    file_path_list = read_source_path()
    if len(file_path_list) > 0:
        source_result = match_path(file_path_list)
        remove_file(source_result)
