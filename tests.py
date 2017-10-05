from unittest import TestCase
from datetime import datetime
from project.main import Conf


class TestConf(Conf):
    file_name = 'test.cfg'
    default = [
        ('param1', 101, 'Первый параметр, целое число'),
        ('param2', '../path/file', 'Второй параметрб текстовый'),
        ('param3', ['name@server.com', 'name2@server.com'], 'Треттий параметр, список'),
        ('param4', {'a': 3, 'f': 55, 'd': 23}, 'Четвертый параметр, словарь'),
    ]


class ConfTestCase(TestCase):
    def test_conf(self):

        conf = Conf()
        conf._conf['param1'] = 222

        conf2 = Conf()

        print(conf2.get('param1'))

