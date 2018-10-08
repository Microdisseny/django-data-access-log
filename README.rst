=====
Django data access log
=====

Django data access log is a simple Django app to log the data accessed in a DRF viewset.


Quick start
-----------

1. Add "data_access_log" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'data_access_log',
    ]

2. Run `python manage.py migrate` to create the models.

3. Add the `@data_access_log` decorator to any viewset you'd like to log::
    from data_access_log.decorators import data_access_log

    @data_access_log
    class MyLoggedViewSet(ModelViewSet):
        # [...]

4. Visit http://127.0.0.1:8000/admin/ to see the logs.
