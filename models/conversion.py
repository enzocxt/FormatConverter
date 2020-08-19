import time
from models import Model


class Conversion(Model):
    @classmethod
    def get(cls, id):
        m = cls.find_by(id=id)
        m.save()
        return m

    def __init__(self, form):
        self.id = None
        self.from_fmt = form.get('from', '')
        self.to_fmt = form.get('to', '')
        self.input_data = form.get('input_data', '')
        self.output_data = form.get('output_data', '')
        self.datetime = form.get('datetime', int(time.time()))
        self.user_id = form.get('user_id', '')