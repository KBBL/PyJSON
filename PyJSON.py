import json
import datetime

## Decorator used to specify how an object of a class should be serialized
#
# \param fields Sequence of fields to serialize.
#
# \todo If fields is not given all fields should be serialized
# \todo at type parameter to specify json type
def json_serializable(fields):
	def decorator(cls, *args, **kwds):
		setattr(cls, 'json_fields', fields)
		return cls
	return decorator
	
## Function that actually serializes the object
#
# \param obj object to serialize
# \param f [optional] a file like object to serialize to.
# \return if f is not given, a string is returned, otherwise the return is None.
#
def serialize(obj, f=None):
	# c is a set of objects that have been added to the result dict.  c is used to
	# detect circular references
	c = {}
	jsond = _todict(obj,c)
	if f == None:
		return json.dumps(jsond)
	else:
		json.dump(jsond,f)

def _convert_date(d):
	return unicode(d)

def _convert_time(t):
	return unicode(t)

def _convert_datetime(dt):
	return unicode(dt)

def _toobj(v,c):
	if isinstance(v,basestring):
		return unicode(v)
	if hasattr(v, 'json_fields'):
		return _todict(v,c)

	try:
		return [_toobj(i,c) for i in v]
	except:
		pass
	
	# date/time conversions
	if isinstance(v,datetime.datetime):
		return _convert_datetime(v)
	if isinstance(v,datetime.date):
		return _convert_date(v)
	if isinstance(v,datetime.time):
		return _convert_time(v)

	return v

def _todict(obj,c):
	# if we've seen the object before, reject serialization
	if id(obj) in c:
		raise Exception(u"There is a circular reference in object tree!: {0}".format(unicode(obj)))
	c[id(obj)] = True
	jsond = {k:_toobj(v,c) for k,v in vars(obj).items() if k in obj.json_fields}
	return jsond


