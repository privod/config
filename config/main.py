import json
import os
import sys


class Conf(object):
    instance = None
    file_name = 'default.cfg'
    file_name_bad = file_name + '.bad'
    default = []

    def __new__(cls, conf_arg={}):
        if cls.instance is None:
            cls.instance = super(Conf, cls).__new__(cls)
            cls.instance._conf = {}
            cls.instance.file_created = False
            cls.instance.init()
        return cls.instance

    def __init__(self, conf_arg={}):
        # Агрумены конструктора, самый высокий приоритет
        self._conf.update(conf_arg)

    def init(self):
        # Значения по умолчанию, самый низкий приоритет
        self._conf.update(self.init_default(self.__class__))

        # Значения из конфигурационного файла, более высокий приоритет
        self._conf.update(self.init_load())
        # Новые пареметры по умочанию добавляются в конфигурационный файл
        with open(self.__class__.file_name, 'w') as f:
            json.dump(self._conf, f, indent=2, sort_keys=True)

        # Агрумены командной строки, более высокий приоритет
        self._conf.update(self.init_sys(self.__class__))

    @staticmethod
    def init_default(cls):
        return {key: val for key, val, comment in cls.default}

    def init_load(self):
        cls = self.__class__
        conf_load = {}
        try:
            with open(cls.file_name) as f:
                conf_load = json.loads(f.read())
        except FileNotFoundError:
            self.file_created = True
        except ValueError:
            os.rename(cls.file_name, cls.file_name_bad)
        return conf_load

    @staticmethod
    def init_sys(cls):
        return {key: arg for (key, val, comment), arg in zip(cls.default, sys.argv)}

    def get(self, key):
        return self._conf.get(key)
