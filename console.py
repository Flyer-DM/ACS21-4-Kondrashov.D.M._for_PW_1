from main import *
import os


def __getcwd() -> str:
    return os.getcwd()[os.getcwd().index('maindir'):] + '>'


while True:
    dir = user_inter()
    if isinstance(dir, bool):
        print("Login error! Try again later.")
    elif dir == '--exit':
        print("End of work. Thanks you!")
        break
    else:
        os.chdir(dir)
        command = input(__getcwd()).split()
        while True:
            if not command:
                unknown()
            elif command[0] in ('mkdir', 'mkfile', '--help', 'ls', 'show', 'rm'):
                try:
                    comms[command[0]](command[1]) if len(command) == 2 else comms[command[0]]()
                except (TypeError, ):
                    unknown()
            elif command[0] in ('rmdir', 'cd', 'copy', 'move', 'rename'):
                try:
                    comms[command[0]](command[1]) if len(command) == 2 else comms[command[0]](command[1], command[2])
                except (TypeError, ):
                    unknown()
            elif command[0] == 'tell':
                if len(command) >= 3:
                    text, file = " ".join(command[1:-1]), command[-1]
                    tell(text, file)
                else:
                    unknown()
            elif command[0] == 'exit':
                print("Выход.")
                break
            else:
                unknown()
            command = input().split()
        os.chdir('D:\pythonProject_file_manager')