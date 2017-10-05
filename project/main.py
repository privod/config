import json
import os
import sys

# def singleton(cls):
#     instances = {}
#
#     def get_instance(conf_arg=None):
#         if cls not in instances:
#             instances[cls] = cls(conf_arg)
#         return instances[cls]
#     return get_instance


class Conf(object):
    instance = None
    file_name = 'default.cfg'
    file_name_bad = file_name + '.bad'
    # _default = {
    #     'path': 'data',
    #     'level': Level.WARN.value,
    #     'patterns': ['*.log'],
    # }
    default = []

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Conf, cls).__new__(cls)
        return cls.instance

    def __init__(self, conf_arg=None):
        cls = self.__class__
        self._conf = {}

        # Значения по умолчанию, самый низкий приоритет
        self._conf = {key: val for key, val, comment in cls.default}

        conf_load = {}
        # Значения из конфигурационного файла, более высокий приоритет
        try:
            s = open(cls.file_name).read()
            conf_load = json.loads(s)
        except FileNotFoundError:
            pass
        except ValueError:
            os.rename(cls.file_name, cls.file_name_bad)
        self._conf.update(conf_load)
        # Новые пареметры по умочанию добавляются в конфигурационный файл
        json.dump(self._conf, open(cls.file_name, 'w'), indent=2, sort_keys=True)

        # Агрумены командной строки, более высокий приоритет
        conf_sys = {key: arg for (key, val, comment), arg in zip(cls.default, sys.argv)}
        self._conf.update(conf_sys)

        # Агрумены конструктора, более высокий приоритет
        self._conf.update(conf_sys)

    def get(self, key):
        return self._conf.get(key)
