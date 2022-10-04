import os
import shutil


def __getcwd() -> str:
    return os.getcwd()[os.getcwd().index('maindir'):] + '>'


def __getfulname(s: str) -> str:
    fulname = os.getcwd() + '\\' + s
    if not s.endswith('.txt'):
        fulname += '.txt'
    return fulname


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
                print(__getcwd())
            else:
                print('Папка maindir является корневой.')
        except (FileNotFoundError, ):
            print("Папки с таким именем не существует.")
    elif flag == '-c':  # create
        os.mkdir(os.getcwd() + '\\' + name)
        print(path + '>')


def mkfile(name='new_file') -> None:
    """Создание пустого текстового файла"""
    name = name + '.txt'
    fulname = os.getcwd() + '\\' + name
    if name not in os.listdir(os.getcwd()):
        open(fulname, 'a').close()
        print(f"Файл {name} создан.\n" + __getcwd())
    else:
        print(f"Файл {name} уже есть в данной директории.\n" + __getcwd())


def tell(text: str, file: str) -> None:
    """Запись строк в существующий файл"""
    fulname = __getfulname(file)
    if fulname[fulname.rindex('\\')+1:] in os.listdir(os.getcwd()):
        with open(fulname, 'a') as f:
            f.write(text + '\n')
            print(f"Файл {file} обновлён.\n" + __getcwd())
    else:
        print(f"Файла с таким именем нет в данной директории.\n" + __getcwd())


def show(file: str) -> None:
    """Вывод содержимого существующего файла"""
    fulname = __getfulname(file)
    if fulname[fulname.rindex('\\')+1:] in os.listdir(os.getcwd()):
        with open(fulname, 'r') as f:
            print(f.read() + '\n' + __getcwd())
    else:
        print(f"Файла с таким именем нет в данной директории.\n" + __getcwd())


def rm(file: str) -> None:
    """Удаление существующего файла"""
    fulname = __getfulname(file)
    try:
        os.remove(fulname)
        print(f'Файл {file} удалён\n' + __getcwd())
    except (FileNotFoundError, ):
        print(f"Файла с таким именем нет в данной директории.\n" + __getcwd())


def copy(file: str, path: str) -> None:
    """Копирование файла из одной директории в другую"""
    pass


def move(file: str, path: str) -> None:
    """Перемещение файла из одной директории в другую"""
    pass


def rename(file: str, new_name: str) -> None:
    """Переменование файла в данной директории"""
    fulname = __getfulname(file)
    new_name = __getfulname(new_name)
    new_name = new_name[new_name.rindex('\\')+1:]
    if fulname not in os.listdir(os.getcwd()):
        print(f"Файла с таким именем нет в данной директории.\n" + __getcwd())
    elif new_name in os.listdir(os.getcwd()):
        print(f"Другому файлу в данной директории присвоено такое имя.\n" + __getcwd())
    else:
        os.rename(fulname, new_name)



if __name__ == '__main__':
    os.chdir('maindir')  # файл начинает всегда работать в D:\pythonProject_file_manager\maindir