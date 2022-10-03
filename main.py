import os
import shutil


def mkdir(name='new_folder') -> None:
    """создание папки"""
    path = os.getcwd() + '\\'
    path = path[path.index('maindir'):-1]
    try:
        os.mkdir(path=name)
        print(f"Папка {name} создана.\n{path}>")
    except (FileExistsError, ):
        print(f"Папка с таким именем уже существует.\n{path}> ")


def rmdir(name: str, flag=None) -> None:
    """Удаление папки"""
    path = os.getcwd() + '\\'
    path = path[path.index('maindir'):-1]
    if flag is None:
        try:
            os.rmdir(name)
            print(f"Папка {name} удалена.\n{path}> ")
        except (OSError, ):
            print(f"Папка имеет содержимое, её нельзя удалить.\n{path}> ")
    elif flag == '-a':  # all
        shutil.rmtree(name)
        print(f"Папка {name} удалена со всем её содержимым.\n{path}> ")
    else:
        print(f"Неизвестный флаг.\n{path}> ")


def cd(name: str, flag=None) -> None:
    """Перемещение между папками"""
    path = os.getcwd() + '\\' + name
    path = path[path.index('maindir'):]
    if flag is None:
        try:
            if name != '..':
                os.chdir(name)
                print(path + '>')
            elif name == '..' and not os.getcwd().endswith('maindir'):
                os.chdir(name)
                print(os.getcwd()[os.getcwd().index('maindir'):] + '>')
            else:
                print('Папка maindir является корневой.')
        except (FileNotFoundError, ):
            print("Папки с таким именем не существует.")
    elif flag == '-c':  # create
        os.mkdir(os.getcwd() + '\\' + name)
        print(path + '>')




if __name__ == '__main__':
    os.chdir('maindir')  # файл начинает всегда работать в D:\pythonProject_file_manager


