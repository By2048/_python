import time

from _package_._celery_._app1_ import app


@app.task
def add(x, y):
    time.sleep(2)
    return x + y
