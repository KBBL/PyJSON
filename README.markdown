# PyJSON #

Use decorators to specify how to serialize arbitrary objects.

I wrote this a while back and is currently half complete.

This api is likely to change though I promise to alway allow the first parameter to
be a list of field names.

Deserialization hasn't been implemented yet.

## Usage ##

> from PyJSON import json_serializable, serialize
>
> @json_serializable(["field1","field2", "field3", "field4"])
> class Class:
>     def __init__(self):
>        self.field1 = "Field1"
>        # serialize dates, times, and datetimes
>        self.field2 = datetime.datetime(2013, 1, 2, 12, 3)
>        self.field3 = datetime.date(2020, 2, 20)
>        self.field4 = datetime.time()
>        self.field3 = "Field 3"
>
> @json_serializable(["anotherField"])
> class AnotherClass:
>     def __init__(self):
>        self.anotherField = ["Item", Class(), 43.23, "This list has another serializable class in it"]
>
> 
> obj = AnotherClass()
>
> \# serializes obj to a string and prints it.
> print (serialize(obj))
>
> \# writes the generated json text to output-file.json
> fp = open("output-file.json", "w")
> serialize(obj, fp)
> fp.close()
>

## Future plans and todos ##

* Implement deserialization
* Decorator should take a list of keyword arguments specifying the types of fields

> @json_serializable(field1="str", field2="datetime", field3="date", field4="time")

* Specify formatters and format strings for dates and times

> def dt_formatter(d):
>     return unicode(d)
>
> PyJSON.set_type_formatter("date", dt_formatter)
> PyJSON.set_date_format_string("%Y-%m-%d")

