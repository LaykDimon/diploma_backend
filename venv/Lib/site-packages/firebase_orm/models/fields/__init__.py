from firebase_orm.exceptions import CanNotBeChanged


class Field:
    def __init__(self, db_column=None, *args, **kwargs):
        self.db_column = db_column

    def __get__(self, obj, objtype):
        return obj._meta.get(self.db_column)

    def __set__(self, obj, val):
        if val is None:
            obj._meta[self.db_column] = val
        elif not str(val).strip():
            obj._meta[self.db_column] = None


class TextField(Field):
    pass


class AutoField:
    def __init__(self):
        self.db_column = "id"

    def __get__(self, obj, objtype):
        return obj._meta.get(self.db_column)

    def __set__(self, obj, val):
        raise CanNotBeChanged


class CharField(Field):
    pass


class DateTimeField:
    pass


class DateField:
    pass


class TimeField:
    pass


class ForeignKey:
    pass


class ManyToManyField:
    pass


class OneToOneField:
    pass


class UUIDField:
    pass


class PhonenumberField(CharField):
    pass


class DecimalField(Field):
    pass


class IntegerField(Field):
    pass


class FloatField(Field):
    pass
