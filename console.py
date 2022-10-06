from main import *
import os
import hashlib
import csv


def __unknown() -> None:
    print("Неизвестная команда, пропишите --help для помощи.\n" + __getcwd(), end='')


def __getcwd() -> str:
    return os.getcwd()[os.getcwd().index('maindir'):] + '>'


def __help():
    pass


comms = {'rmdir': rmdir, 'cd': cd, 'mkdir': mkdir, 'mkfile': mkfile, '--help': __help, 'ls': ls, 'show': show,
         'rm': rm, 'copy': copy, 'move': move, 'rename': rename}

os.chdir('maindir')
command = input(__getcwd()).split()
while True:
    if not command:
        __unknown()
    elif command[0] in ('mkdir', 'mkfile', '--help', 'ls', 'show', 'rm'):
        try:
            comms[command[0]](command[1]) if len(command) == 2 else comms[command[0]]()
        except (TypeError, ):
            __unknown()
    elif command[0] in ('rmdir', 'cd', 'copy', 'move', 'rename'):
        try:
            comms[command[0]](command[1]) if len(command) == 2 else comms[command[0]](command[1], command[2])
        except (TypeError, ):
            __unknown()
    elif command[0] == 'tell':
        if len(command) >= 3:
            text, file = " ".join(command[1:-1]), command[-1]
            tell(text, file)
        else:
            __unknown()
    elif command[0] == 'exit':
        print("Выход.")
        break
    else:
        __unknown()
    command = input().split()
