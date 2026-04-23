import json
import os
import shutil
from pathlib import Path

class Data_json:
    CHOICE_STOP = 'stop'
    CHOICE_Y = 'Y'
    CHOICE_N = 'N'
    CHOICE_CREATE = 'create'
    CHOICE_WRITE = 'write'
    CHOICE_DEL = 'delete'
    CHOICE_COPY = 'copy'
    CHOICE_READ = 'read'
    CHOICE_SHOW = 'show'
    dict_copy = {}
    def __init__(self, choice):
        self.choice = choice
        self.data = {}
        self.jsonname = ''
        self.dict_copy = {}
        self.types = {
        'str': str,
        'int': int,
        'float': float,
        'bool': bool
         }


    def check_json(self):
        self.jsonname = input("Введите имя файла без расширения: ") + '.json'
        if os.path.exists(self.jsonname) and os.path.isfile(self.jsonname):
            return True
        else:
            return False

    def create_json(self):
        count_create = 0
        self.jsonname = input("Введите имя нового файла без расширения: ").strip()
        if not self.jsonname:
            count_create += 1
            self.jsonname = f'default{count_create}.json'
        else:
            self.jsonname += '.json'

        if os.path.exists(self.jsonname):
            print(f"Файл {self.jsonname} уже существует")
        else:
            try:
                with open(self.jsonname, 'w', encoding = 'utf-8') as f:
                    json.dump({}, f)
            except OSError as e:
                print(f"Недопустимое имя файла - {e}")


    def read_json(self):
        if self.check_json():
            with open(self.jsonname, 'r', encoding = 'utf-8') as f:
                print(json.load(f))
        else:
            print(f"Файла {self.jsonname} не существует")

    def write_json(self):
        if self.check_json():
            with open(self.jsonname, 'w', encoding = 'utf-8') as f:
                print("Подготовка буферных данных к записи в файл")
                choice_write = None
                while True:
                    choice_write = input("Нажмите Enter для продолжения или напишите stop для остановки: ")
                    if choice_write == self.CHOICE_STOP:
                        break
                    else:
                        pass
                    key = input("Введите имя ключа: ")
                    print("Если вы ввели существуещий ключ то его значение изменится")
                    type_choice = input("Введите тип значения (str/int/float/bool): ")
                    value = None
                    try:
                        if type_choice in self.types.keys():
                            value = self.types[type_choice](input(f"Введите {type_choice} значение: "))
                        else:
                            value = input("Такой тип не записан, значит будет str: ")
                    except ValueError as e:
                        print(f"Ошибка преобразования - {e}")
                    except Exception as e:
                        print(f"Ошибка - {e}")
                    self.data[key] = value
                    print(self.data)
                json.dump(self.data, f, indent = 2, ensure_ascii = False)
                print(f"Данные {self.data} записаны в файл")
                self.data.clear()
        else:
            print(f"Файла {self.jsonname} не существует")
    def delete_json(self):
        if self.check_json():
            os.remove(self.jsonname)
            print("Файл удален")
        else:
            print(f"Файла {self.jsonname} не существует")
    def copy_json(self):
        if self.check_json():
            try:
                if self.jsonname in self.dict_copy.keys():
                    self.dict_copy[self.jsonname] += 1
                else:
                    self.dict_copy[self.jsonname] = 1

                shutil.copy(self.jsonname, f'{os.path.splitext(self.jsonname)[0]}{self.dict_copy[self.jsonname]}.json')
            except Exception as e:
                print(f"Ошибка - {e}")


    def show_files(self):
        current_folder = Path(".")
        json_files = list(current_folder.glob("*.json"))
        print(json_files)

    def choice_action(self):
        if self.choice == self.CHOICE_CREATE:
            self.create_json()
        elif self.choice == self.CHOICE_WRITE:
            self.write_json()
        elif self.choice == self.CHOICE_READ:
            self.read_json()
        elif self.choice == self.CHOICE_DEL:
            self.delete_json()
        elif self.choice == self.CHOICE_COPY:
            self.copy_json()
        elif self.choice == self.CHOICE_SHOW:
            self.show_files()




choice_json = ''
while choice_json != 'stop':
    choice_json = input("Выберите действие show/delete/create/read/copy/write: ")
    Data_json(choice_json).choice_action()





