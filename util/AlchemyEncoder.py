# -*- coding: UTF-8 -*-
from sqlalchemy.ext.declarative import DeclarativeMeta
import json


class AlchemyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o.__class__, DeclarativeMeta):
            #an sqlalchemy class
            fields = {}
            for field in [x for x in dir(o) if not x.startswith('__') and x != 'metadata']:
                data = o.__getattribute__(field)
                try:
                    json.dump(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self,o)