# 파일 이름 일괄 변경 (1.jpg, 2.jpg, 3.jpg .....)

import os

dir_path = 'archive/images'
dir_names = os.listdir(dir_path)

def get_directory():
    for dir_name in dir_names :
        if dir_name != ".DS_Store" :
            file_path = f"{dir_path}/{dir_name}"
            file_names = os.listdir(file_path)
            changes_file_name(file_names, file_path)


def changes_file_name(file_names, file_path) :
    i = 1
    for name in file_names :
        src = os.path.join(file_path, name)
        dst = str(i) + '.jpg'
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)
        i += 1

