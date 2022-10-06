import os
import shutil
import hashlib
import csv


def help() -> None:
    print("Доступные команды (для взаимодействия с файлами нужно находится в той же директории, что и они):\n",
          "·ls - вывод содержимого текущей папки\n",
          "·mkdir [<name>] - создание папки с именем name, по умолчанию - new_folder\n",
          "·rmdir <name> [<flag>] - удаление папки с именем name; флаг -a удаляет папку, если в ней есть содержимое\n",
          "·cd <name> [<flag>] - перещение в директорию name; если name = .., то перемещение на директорию выше;\n",
          " флаг -c позволяет создать папку с именем name и переместится в неё\n",
          "·mkfile [<name>] - создание текстового файла с именем name, по умолчанию - new_file\n",
          "·tell <text> <name> - запись строки text в файл с именем name\n",
          "·show <name> - вывод содержимого текстового файла с именем name\n",
          "·rm <name> - удаление текстового файла с именем name\n",
          "·copy <name> <path> - копирование файла с именем name в директорию по пути path\n",
          "·move <name> <path> - перемещение файла с именем name в директорию по пути path\n",
          "·rename <name> <new name> - переименование текстового файла с именем name на имя new name.\n"
          + __getcwd(), end='')


def unknown() -> None:
    print("Неизвестная команда, пропишите --help для помощи.\n" + __getcwd(), end='')


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
        print(f"Папка с таким именем уже существует.\n{path}>", end='')


def rmdir(name: str, flag=None) -> None:
    """Удаление папки"""
    path = __getcwd()
    if flag is None:
        try:
            os.rmdir(name)
            print(f"Папка {name} удалена.\n{path}", end='')
        except (FileNotFoundError, ):
            print(f"Неизвестная папка.\n{path}", end='')
        except (OSError, ):
            print(f"Папка имеет содержимое, её нельзя удалить.\n{path}", end='')
    elif flag == '-a':  # all
        shutil.rmtree(name)
        print(f"Папка {name} удалена со всем её содержимым.\n{path}", end='')
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
            print(__getcwd(), end='')
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
        try:
            os.rename(fulname, new_name)
            print("Успешное переименование файла.\n" + __getcwd(), end='')
        except (FileNotFoundError, ):
            print("Файл для переименования не найден\n" + __getcwd(), end='')


comms = {'rmdir': rmdir, 'cd': cd, 'mkdir': mkdir, 'mkfile': mkfile, '--help': help, 'ls': ls, 'show': show,
         'rm': rm, 'copy': copy, 'move': move, 'rename': rename}


def __namechecker(name: str) -> bool:
    for symbol in '/\":;|=[]\\?\'<>*':
        if symbol in name:
            return False
    return True


def user_inter() -> (str, bool):
    flag, attempts = False, 3
    name = input("Hello! Enter your name: ")
    while True:
        f = __namechecker(name)
        if f:
            break
        else:
            name = input("Impossible name! Try another:")
    if name == '--exit':
        return name
    with open('users.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['name'] == name:
                user_password, user_name, user_dir, flag = row['password'], row['name'], row['directory'], not flag
                break
    if flag:  # известный пользователь
        print(f"Hello, {user_name}! Validate your password, please.")
        while True:
            password = input("Password: ")
            if hashlib.md5(password.encode()).hexdigest() == user_password:
                return user_dir
            else:
                print("Wrong password! Try again. ", end='')
                attempts -= 1
            if attempts == 0:
                return False
    else:  # неизвестный пользователь
        user_name = name
        print(f"Hello, {user_name}! Register, please!")
        user_password = hashlib.md5(input("Input your password: ").encode()).hexdigest()
        user_dir = 'maindir_' + user_name
        os.mkdir(user_dir)
        with open('users.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name', 'password', 'directory'])
            writer.writerow({'name': user_name, 'password': user_password, 'directory': user_dir})
        return user_dir
