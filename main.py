import os
import shutil


def __getcwd() -> str:
    return os.getcwd()[os.getcwd().index('maindir'):] + '>'


def __getfulname(s: str) -> str:
    fulname = os.getcwd() + '\\' + s
    if not s.endswith('.txt'):
        fulname += '.txt'
    return fulname


def ls() -> None:
    """Содержимое текущей папки"""
    print(os.listdir(os.getcwd()), '\n' + __getcwd(), end='')


def mkdir(name='new_folder') -> None:
    """создание папки"""
    path = os.getcwd() + '\\'
    path = path[path.index('maindir'):-1]
    try:
        os.mkdir(path=name)
        print(f"Папка {name} создана.\n{path}>", end='')
    except (FileExistsError, ):
        print(f"Папка с таким именем уже существует.\n{path}> ", end='')


def rmdir(name: str, flag=None) -> None:
    """Удаление папки"""
    #path = os.getcwd() + '\\'
    #path = path[path.index('maindir'):-1]
    path = __getcwd()
    if flag is None:
        try:
            os.rmdir(name)
            print(f"Папка {name} удалена.\n{path} ", end='')
        except (OSError, ):
            print(f"Папка имеет содержимое, её нельзя удалить.\n{path} ", end='')
        except (FileNotFoundError, ):
            print(f"Неизвестная папка.\n{path} ", end='')
    elif flag == '-a':  # all
        shutil.rmtree(name)
        print(f"Папка {name} удалена со всем её содержимым.\n{path} ", end='')
    else:
        print(f"Неизвестный флаг.\n{path} ", end='')


def cd(name: str, flag=None) -> None:
    """Перемещение между папками"""
    if flag is None:
        try:
            if name == '..' and os.getcwd().endswith('maindir'):
                print('Папка maindir является корневой.\n' + __getcwd(), end='')
            else:
                os.chdir(name)
                print(__getcwd(), end='')
        except (FileNotFoundError, ):
            print(f"Папки с таким: {name} именем нет в данной директории.\n" + __getcwd(), end='')
    elif flag == '-c':  # create
        try:
            os.mkdir(os.getcwd() + '\\' + name)
            os.chdir(os.getcwd() + '\\' + name)
            print(__getcwd())
        except (FileExistsError, ):
            print("Папка уже существует, флаг -c не требуется.\n" + __getcwd(), end='')


def mkfile(name='new_file') -> None:
    """Создание пустого текстового файла"""
    name = name + '.txt'
    fulname = os.getcwd() + '\\' + name
    if name not in os.listdir(os.getcwd()):
        open(fulname, 'a').close()
        print(f"Файл {name} создан.\n" + __getcwd(), end='')
    else:
        print(f"Файл {name} уже есть в данной директории.\n" + __getcwd(), end='')


def tell(text: str, file: str) -> None:
    """Запись строк в существующий файл"""
    fulname = __getfulname(file)
    if fulname[fulname.rindex('\\')+1:] in os.listdir(os.getcwd()):
        with open(fulname, 'a') as f:
            f.write(text + '\n')
            print(f"Файл {file} обновлён.\n" + __getcwd(), end='')
    else:
        print(f"Файла с таким именем нет в данной директории.\n" + __getcwd(), end='')


def show(file: str) -> None:
    """Вывод содержимого существующего файла"""
    fulname = __getfulname(file)
    if fulname[fulname.rindex('\\')+1:] in os.listdir(os.getcwd()):
        with open(fulname, 'r') as f:
            print(f.read() + '\n' + __getcwd(), end='')
    else:
        print(f"Файла с таким именем нет в данной директории.\n" + __getcwd(), end='')


def rm(file: str) -> None:
    """Удаление существующего файла"""
    fulname = __getfulname(file)
    try:
        os.remove(fulname)
        print(f'Файл {file} удалён\n' + __getcwd(), end='')
    except (FileNotFoundError, ):
        print(f"Файла с таким именем нет в данной директории.\n" + __getcwd(), end='')


def __pathmaker(file: str, path: str) -> tuple:
    startpath = '.\\' + file
    if not file.endswith('.txt'):
        startpath += '.txt'
    endpath = '.\\' + path
    return (startpath, endpath)


def copy(file: str, path: str) -> None:
    """Копирование файла из одной директории в другую"""
    startpath, endpath = __pathmaker(file, path)
    try:
        shutil.copy(startpath, endpath)
        print(f"Файл успешно скопирован.\n" + __getcwd(), end='')
    except (FileExistsError, ):
        print(f"В директории назначения уже имеется файл с таким же именем.\n" + __getcwd(), end='')
    except (BaseException, ):
        print(f"Файл не удалось скопировать.\n" + __getcwd(), end='')


def move(file: str, path: str) -> None:
    """Перемещение файла из одной директории в другую"""
    startpath, endpath = __pathmaker(file, path)
    try:
        shutil.move(startpath, endpath)
        print(f"Файл успешно перемещён.\n" + __getcwd(), end='')
    except (FileExistsError, ):
        print(f"В директории назначения уже имеется файл с таким же именем.\n" + __getcwd(), end='')
    except (BaseException, ):
        print(f"Файл не удалось переместить.\n" + __getcwd(), end='')


def rename(file: str, new_name: str) -> None:
    """Переменование файла в данной директории"""
    fulname = __getfulname(file)
    new_name = __getfulname(new_name)
    new_name = new_name[new_name.rindex('\\')+1:]
    if new_name in os.listdir(os.getcwd()):
        print(f"Другому файлу в данной директории присвоено такое имя.\n" + __getcwd(), end='')
    else:
        os.rename(fulname, new_name)
        print("Успешное переименование файла.\n" + __getcwd(), end='')


if __name__ == '__main__':
    os.chdir('maindir')  # файл начинает всегда работать в D:\pythonProject_file_manager\maindir