from django.db import models

TYPE_MAP = {u'BigIntegerField': long,
            u'FloatField': float,
            u'PositiveIntegerField': int,
            u'CharField': str,
            u'DateTimeField': str,
            u'NullBooleanField': bool,
            u'BooleanField': bool,
            u'ForeignKey': long}

NULL_MAP = {u'BigIntegerField': long(0),
            u'FloatField': float(0.0),
            u'PositiveIntegerField': int(0),
            u'NullBooleanField': False,
            u'CharField': ''}

HBS_MAP = {
    models.ForeignKey: 'int',
    models.CharField: 'string',
    models.FloatField: 'float',
    models.DateTimeField: 'string',
    models.NullBooleanField: 'bool',
    models.BooleanField: 'bool',
    models.IntegerField: 'int',
    models.TextField: 'string',
    models.BigIntegerField: 'long'
}
