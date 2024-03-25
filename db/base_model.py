#!/usr/bin/env python3
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import class_mapper

class Base(DeclarativeBase):
    def as_dict(self):
        mapper = class_mapper(self.__class__)
        columns = [column.key for column in mapper.columns]
        return {c: getattr(self, c) for c in columns}
