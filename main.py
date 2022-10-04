import os
import shutil
import hashlib
import csv


def user_register(name: str, password: str) -> None:
    """Регистрация пользователей"""
    with open('users.csv', 'a') as users:
        pass
    pass


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
            print(f"Папки с таким: {name} именем не существует.\n" + __getcwd())
    elif flag == '-c':  # create
        try:
            os.mkdir(os.getcwd() + '\\' + name)
            os.chdir(os.getcwd() + '\\' + name)
            print(path + '>')
        except (FileExistsError, ):
            print("Папка уже существует, флаг -c не требуется.\n" + __getcwd())


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


def __pathmaker(file: str, path: str) -> tuple:
    startpath = '.\\' + file
    endpath = '.\\' + path
    if '' in file:
        startpath = file
    if '' in path:
        endpath = path
    return (startpath, endpath)


def copy(file: str, path: str) -> None:
    """Копирование файла из одной директории в другую"""
    startpath, endpath = __pathmaker(file, path)
    try:
        shutil.copy(startpath, endpath)
        print(f"Файл успешно скопирован.\n" + __getcwd())
    except (FileExistsError, ):
        print(f"В директории назначения уже имеется файл с таким же именем.\n" + __getcwd())
    except (BaseException, ):
        print(f"Файл не удалось скопировать.\n" + __getcwd())


def move(file: str, path: str) -> None:
    """Перемещение файла из одной директории в другую"""
    startpath, endpath = __pathmaker(file, path)
    try:
        shutil.move(startpath, endpath)
        print(f"Файл успешно перемещён.\n" + __getcwd())
    except (FileExistsError, ):
        print(f"В директории назначения уже имеется файл с таким же именем.\n" + __getcwd())
    except (BaseException, ):
        print(f"Файл не удалось переместить.\n" + __getcwd())


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


def arch() -> None:
    """Архивирование текущей директории"""
    current = os.getcwd()
    if current.endswith('maindir'):
        print('Папка maindir является корневой.')
    elif current[current.rindex('\\') + 1:] + '.zip' not in os.listdir(os.getcwd()[:os.getcwd().rindex('\\')]):
        os.chdir('..')
        pre_current = os.getcwd()
        shutil.make_archive(current[current.rindex('\\') + 1:], format='zip', root_dir=current, base_dir=pre_current)
        print("Успешная архивация.")
        cd(current[current.rindex('\\') + 1:])
    else:
        print("Архив уже создан.\n" + __getcwd())


def darch() -> None:
    """Разархивирование архива по имени в текущую директорию"""
    pass


if __name__ == '__main__':
    os.chdir('maindir')  # файл начинает всегда работать в D:\pythonProject_file_manager\maindir
