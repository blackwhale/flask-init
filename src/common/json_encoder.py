import datetime
import json


class CustomJsonEncoder(json.JSONEncoder):
    TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime(self.TIME_FORMAT)
        return super(CustomJsonEncoder, self).default(obj)