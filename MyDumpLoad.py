import json
import gzip

import pickle


class MyDumpLoadPickle():
    @staticmethod
    def pickle_dump(path, data):
        with open(path, 'wb') as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

        return True

    @staticmethod
    def pickle_load(path):
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data


class MyDumpLoadJsonGzip():
    @staticmethod
    def gzip_to_dict(path=''):
        '''распаковывает gzip и десериализирует json'''
        with gzip.open(path, 'rb') as f:
            file_content = f.read()

        try:
            fe = file_content.decode('utf-8')
            d = json.loads(fe)
            return d
        except:
            print(path)
            return False

    @staticmethod
    def dict_to_gzip(path='', dictionary=None):
        '''сериализирует словарь в json и сжимает в gzip'''

        if not path:
            return False

        if dictionary is None:
            dictionary = dict()

        str_dict = json.dumps(dictionary, ensure_ascii=False)
        b_str_dict = str_dict.encode('utf-8')

        with gzip.open(path, 'wb') as outfile:
            outfile.write(b_str_dict)


class MyDumpLoadJson():
    @staticmethod
    def json_to_dict(path=None):
        '''десериализирует json'''

        with open(path) as file:
            d = json.load(file)
        return d

    @staticmethod
    def dict_to_json(path=None, dictionary=None):
        '''сериализирует словарь в json '''

        if path is None:
            return False

        if dictionary is None:
            dictionary = dict()

        with open(path, 'w') as outfile:
            json.dump(obj=dictionary, fp=outfile, indent=4)


class MyDumpLoad(MyDumpLoadPickle, MyDumpLoadJsonGzip, MyDumpLoadJson):
    pass