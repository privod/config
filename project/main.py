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
            cls.instance.init(conf_arg)
        return cls.instance

    def init(self, conf_arg):
        # Значения по умолчанию, самый низкий приоритет
        self._conf.update(self.init_default(self.__class__))

        # Значения из конфигурационного файла, более высокий приоритет
        self._conf.update(self.init_load(self.__class__))
        # Новые пареметры по умочанию добавляются в конфигурационный файл
        json.dump(self._conf, open(self.__class__.file_name, 'w'), indent=2, sort_keys=True)

        # Агрумены командной строки, более высокий приоритет
        self._conf.update(self.init_sys(self.__class__))

        # Агрумены конструктора, более высокий приоритет
        self._conf.update(conf_arg)

    @staticmethod
    def init_default(cls):
        return {key: val for key, val, comment in cls.default}

    @staticmethod
    def init_load(cls):
        conf_load = {}
        try:
            s = open(cls.file_name).read()
            conf_load = json.loads(s)
        except FileNotFoundError:
            pass
        except ValueError:
            os.rename(cls.file_name, cls.file_name_bad)
        return conf_load

    @staticmethod
    def init_sys(cls):
        return {key: arg for (key, val, comment), arg in zip(cls.default, sys.argv)}

    def get(self, key):
        return self._conf.get(key)
