#!/usr/bin/python
# -*- coding:utf-8 -*-

# 每行最多显示的字符数
MAX_LINE_LEN = 100

import os
import collections

search_result = collections.namedtuple("search_result", "file, line, text")

# ---<搜索一个文件夹下所有文件中包含search_content的内容>-------------------
def global_search(folder_path, search_content, browse_line, extend_name):
    """
    :param folder_path: string, target folder path
    :param search_content: string, content will be searched
    :param browse_line: int, number of lines could be browsed in GUI
    :param extend_name: string, file extend name constrains while searching
    :return: list of collections.namedtuple("search_result", "file, line, text")
    """
    print_header()

    # ---<异常处理>--------------------------
    if folder_path == '':
        print 'Error: Folder path is empty.'
        return
    print 'Start searching in:', folder_path

    if not search_content:
        print("Can't search for nothing, please input some text which will be searched.")

    # ---<开始搜索并返回搜索结果>-----------------------------------------------------------------------
    matches = search_folders(folder_path, search_content, browse_line, extend_name)

    return matches

# ---<打印搜索结果>---------------
def print_results(matches):
    """
    :param matches: list of collections.namedtuple("search_result", "file, line, text")
    :return: void
    """
    total_matches = 0
    for match in matches:
        total_matches += 1
        print("\n" + str(total_matches)+": MATCH-----------------------------------------------------")
        print("File: {}".format(match.file))
        print("Line: {} ".format(match.line))
        print("Match text: {}".format(match.text.strip()))
    print("\n-------------------------------------------------------------------")
    print("\nSearch is done!\nTotal number of matches is {}".format(total_matches))

# ---<打印标题>------------------------------------------------------
def print_header():
    print("-----------------------------------------------------")
    print("                  GlobalSearch                        ")
    print("-----------------------------------------------------")

# ---<检查是否为可搜索文件>--------------------
def check_if_textual_file(file):
    """
    :param file: string, file name checked
    :return: string bool, file name and whether this file is searchable
    """
    # ---<可搜索文件格式>--------------------------------
    acceptedFilesFormatslLen4 = [".json"]
    acceptedFilesFormatslLen3 = [".txt", ".ccs", ".php"]
    acceptedFilesFormatslLen2 = [".py", ".md", ".js"]
    # ---<隐藏文件不搜索>-----
    if file[:1] == ".":
        return file, False
    # --<文件夹>-------------
    if os.path.isdir(file):
        return file, True
    # ---<为任意一种可搜索的文件格式>-------------
    elif file[-5:] in acceptedFilesFormatslLen4:
        return file, True
    elif file[-4:] in acceptedFilesFormatslLen3:
        return file, True
    elif file[-3:] in acceptedFilesFormatslLen2:
        return file, True
    # ---<剩余的文件种类皆不搜索>----------------
    else:
        return file, False

# --<检查文件是否为csd文件>---------------
def is_csd_file(file):
    """
    :param file: string, file name checked
    :return: string bool, file name and whether this file is searchable
    """
    # ---<隐藏文件不搜索>-----
    if file[:1] == ".":
        return file, False
    # --<文件夹>-------------
    if os.path.isdir(file):
        return file, True
    # ---<csd文件>-------------
    if file[-4:] == '.csd':
        return file, True
    else:
        return file, False

# ---<全局搜索>----------------------------------------------------
def search_folders(folder_path, text, browse_line, extend_name):
    """
    :param folder_path: string, target folder path
    :param text: string, content will be searched
    :param browse_line: int, number of lines could be browsed in GUI
    :param extend_name: string, file extend name constrains while searching
    :return: list of collections.namedtuple("search_result", "file, line, text")
    """
    all_matches=[]
    # ---<获得当前文件夹下的文件名>---------
    filesInFolder = os.listdir(folder_path)
    # ---<确定文件过滤方式>-----------------
    # ---<仅搜索csd文件>--------------------
    if extend_name == 'CSD Files (*.csd)':
        check_func = is_csd_file
    # ---<未做限定>------------------------
    else:
        check_func = check_if_textual_file
    # ---<判断文件是否在搜索范围内>--------------------------------------
    for file in filesInFolder:
        file, is_target = check_func(folder_path + '\\' + file)
        if not is_target:
            continue
        else:
            fullFilePath = os.path.join(folder_path, file)
            # ---<若为文件夹，则进入文件夹进行搜索>-----------------------------------------
            if os.path.isdir(fullFilePath):
                    matches = search_folders(fullFilePath, text, browse_line, extend_name)
                    all_matches.extend(matches)
            # ---<若为文件，则打开文件搜索目标字段>-------------------------
            else:
                #if its a file search it
                matches = search_file(fullFilePath, text, browse_line)
                all_matches.extend(matches)
    return all_matches

# ---<进入文件搜索>------------------------------------------
def search_file(full_file_path, search_text, browse_line):
    """
    :param full_file_path: string, path of file will be searched
    :param search_text: string, content will be searched
    :param browse_line: int, number of lines could be browsed in GUI
    :return: collections.namedtuple("search_result", "file, line, text")
    """
    import linecache
    import io
    matches = []
    # ---<打开文件，逐行读取搜索>-----------------
    with io.open(full_file_path, "rb") as fin:
        lineNumber = 0
        for line in fin:
            line = line.decode(errors='ignore')
            lineNumber += 1
            if line.find(search_text) < 0:
                continue
            browse_part = []
            index = lineNumber - browse_line
            if index < 0:
                index = 0
            while index <= lineNumber + browse_line:
                l = linecache.getline(full_file_path, index).strip()
                l = l.replace('<', '＜')
                l = l.replace('>', '＞')
                if len(l) >= MAX_LINE_LEN and index == lineNumber:
                    pos = l.find(search_text)
                    l = l[:pos + len(search_text)] + ' ...... ' + l[-(MAX_LINE_LEN - pos - len(search_text)) / 2:]
                elif len(l) > MAX_LINE_LEN:
                    l = l[:MAX_LINE_LEN/2] + '...... ' + l[-MAX_LINE_LEN/2:]
                if index == lineNumber:
                    l = l.replace(search_text, "<font style='color:red;'>{}</font>".format(search_text))
                browse_part.append(l)
                index += 1
            m = search_result(line=lineNumber, file=full_file_path, text=browse_part)
            matches.append(m)
    return matches

# ---<获取csd文件对应的ccs文件名>-----------------
def get_project_name(csd_file_name, ccs_path):
    """
    :param csd_file_name: string, csd file name
    :param ccs_path: string, ccs file path
    :return: string bool, matched ccs file name and whether found it
    """
    # listdir gives only filenames in this folder, not full path name
    filesInFolder = os.listdir(ccs_path)

    for file in filesInFolder:

        if not file[-4:] == '.ccs':
            continue
        fullFilePath = os.path.join(ccs_path, file)
        if os.path.isdir(fullFilePath):
            continue
        matches = search_file(fullFilePath, csd_file_name, 0)
        if len(matches):
            return file, True

    return 'No css project contain ' + csd_file_name, False

# ---<打开ccs文件>------------------------
def open_project(project_name, ccs_path):
    """
    :param project_name: string, ccs file name
    :param ccs_path: string, ccs file path
    :return: void
    """
    original_path = os.getcwd()
    os.chdir(ccs_path)
    os.system(project_name)
    os.chdir(original_path)