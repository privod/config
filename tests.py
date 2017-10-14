from unittest import TestCase
from config import Conf


class TestConf(Conf):
    file_name = 'test.cfg'
    default = [
        (None, 'param1', 101, 'Первый параметр, целое число'),
        (1, 'param2', '../path/file', 'Второй параметрб текстовый'),
        (None, 'param3', ['name@server.com', 'name2@server.com'], 'Треттий параметр, список'),
        (None, 'param4', {'a': 3, 'f': 55, 'd': 23}, 'Четвертый параметр, словарь'),
    ]


class ConfTestCase(TestCase):
    def test_conf(self):

        conf = TestConf()
        conf._conf['param1'] = 222

        conf2 = TestConf()

        conf3 = TestConf({'param1': 333})

        print(conf3.get('param2'))


