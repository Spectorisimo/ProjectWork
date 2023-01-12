import datetime
import os
import shutil
import sys


# Так как использую мак,то по-просту не смог задать начальную директорию начинающуюся с диска C:
def base_dir():
    os.chdir('/Users/daniyar/')  # Здесь можете сменить путь начальной директории


class Shell:

    def cd(self, path=None) -> None:
        if path == None:
            base_dir()
        else:
            os.chdir(path)

    @staticmethod
    def get_info_about_files(files, path: str | None) -> None:

        if path == None:
            for file in files:
                print(datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y-%m-%d %H:%M"),
                      f"{os.path.getsize(file):>10}", file)

        else:
            for file in files:
                print(datetime.datetime.fromtimestamp(os.path.getmtime(path + f'/{file}')).strftime("%Y-%m-%d %H:%M"),
                      f"{os.path.getsize(path + f'/{file}'):>10}", file)

    def ls(self, path=None) -> None:
        files = os.listdir(path)
        self.get_info_about_files(files, path)

    def mkdir(self, filename: str) -> None:
        os.mkdir(filename)

    def touch(self, filename: str) -> None:
        file = open(filename, "w")
        file.close()

    def mv(self, old_name: str, new_name: str) -> None:
        os.renames(old_name, new_name)

    def rm(self, filename: str) -> None:
        if os.path.isfile(filename):
            os.remove(filename)
        else:
            shutil.rmtree(filename)

    def cat(self, filename: str) -> None:
        with open(filename, "r") as file:
            print(file.read())


shell = Shell()

base_dir()
while True:
    command = input(f'{os.getcwd()}: ').split()
    match command:
        case ['cd']:
            shell.cd()
        case 'cd', path:
            try:
                shell.cd(path)
            except:
                print('Директория не найдена')
        case ['ls']:
            shell.ls()
        case 'ls', path:
            try:
                shell.ls(path)
            except:
                print('Директория не найдена')
        case 'mkdir', filename:
            try:
                shell.mkdir(filename)
            except:
                print('Директория не найдена')
        case 'touch', filename:
            try:
                shell.touch(filename)
            except:
                print('Директория не найдена')
        case 'cat', filename:
            try:
                shell.cat(filename)
            except:
                print('Файл не найдена')
        case 'rm', filename:
            try:
                shell.rm(filename)
            except:
                print('Директория или файл не найдены')
        case 'mv', old_name, new_name:
            try:
                shell.mv(old_name, new_name)
            except:
                print('Директория или файл не найдены')
        case ['exit']:
            sys.exit()
        case _ as unknown_command:
            print(f'Команда не найдена: {unknown_command[0]}')
