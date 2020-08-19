import os
import time
import json

curdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.abspath(os.path.join(curdir, os.pardir))


def timestamp():
    return int(time.time())


def save(data, path):
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as fout:
        fout.write(s)


def load(path):
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as fout:
            fout.write('[]')

    with open(path, 'r', encoding='utf-8') as fin:
        s = fin.read()
        data = []
        try:
            data = json.loads(s)
        except Exception as err:
            print(err)
        return data


class Model(object):
    @classmethod
    def db_path(cls):
        classname = cls.__name__
        path = os.path.join(rootdir, 'data')
        if not os.path.exists(path):
            os.makedirs(path)
        path = os.path.join(path, f'{classname}.txt')
        return path

    @classmethod
    def _new_from_dict(cls, d):
        m = cls({})
        for k, v in d.items():
            setattr(m, k, v)
        return m

    @classmethod
    def all(cls):
        path = cls.db_path()
        models = load(path)
        ms = [cls._new_from_dict(m) for m in models]
        return ms

    @classmethod
    def find_by(cls, **kwargs):
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value
        all = cls.all()
        for m in all:
            if v == m.__dict__[k]:
                return m
        return None

    @classmethod
    def find(cls, id):
        return cls.find_by(id=id)

    def json(self):
        d = self.__dict__.copy()
        return d

    def save(self):
        models = self.all()
        if self.id is None:
            if len(models) == 0:
                self.id = 1
            else:
                m = models[-1]
                self.id = m.id + 1
            models.append(self)
        else:
            index = -1
            for i, m in enumerate(models):
                if m.id == self.id:
                    index = i
                    break
            models[index] = self
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)
