import os, stat
from pathlib import Path

def lists(pathstr:str='.', ignore_list:list=['desktop.ini']):
    os.chdir(pathstr)
    print('dir: ', os.getcwd())
    entries = os.listdir()
    dir_list = [entry for entry in entries if (entry not in ignore_list and Path(entry).is_dir())]
    file_list = [entry for entry in entries if (entry not in ignore_list and entry not in dir_list)]
    dir_list = sorted(dir_list, key=str.lower)
    file_list = sorted(file_list, key=str.lower)
    return dir_list, file_list


def read_write(pathstr:str='.archive-new.txt'):
    pathlike = Path(pathstr)
    os.chmod(pathlike, stat.S_IREAD | stat.S_IWRITE | stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH )
    

def save_lists(dir_list:list, file_list:list, append_text:str='', filename:str='.archive-new.txt'):
    try:
        with open(filename, 'x') as file:
            for entry in dir_list:
                file.write('[] ' + entry + append_text + '\n')
            for entry in file_list:
                file.write('-  ' + entry + append_text + '\n')
        read_write(filename)
        return True
    except FileExistsError:
        print('File already exists: "' + filename + '"')
        return False


def new_archive(pathstr:str='.', append_text:str='', filename:str='.archive-new.txt'):
    dir_list, file_list = lists(pathstr)
    archive_success = save_lists(dir_list, file_list, append_text, filename)
    if archive_success:
        print('>>> REMEMBER TO REMOVE THE "-new" FROM THE FILE NAME!')

def make_archive(pathstr:str='.', append_text:str='', filename:str='.archive-new.txt'):
    new_archive(pathstr, append_text, filename)


def cd(pathstr:str):
    os.chdir(pathstr)

def ls(pathstr:str='.'):
    dir_list, file_list = lists(pathstr)
    for entry in dir_list:
        print('[] ' + entry)
    for entry in file_list:
        print('   ' + entry)

def pwd():
    print(os.getcwd())


help = 'new_archive(pathstr, append_text="text", filename=".archive-new.txt'