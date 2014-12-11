from flask import Flask
from celery import Celery
from command_tool import *
from config_manager import load_cfg, cfg_info
from command_tool import exe_cmd

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

_app = Flask("__main__")
_app.config.update(
    CELERY_BROKER_URL='amqp://guest:guest@localhost:5672//',
    CELERY_RESULT_BACKEND='amqp://guest:guest@localhost:5672//'
)
celery = make_celery(_app)


@celery.task(name="__main__.add")
def add(x, y):
    return x + y

@celery.task(name="__main__.task_cmd")
def task_cmd(cmd):
    if cmd is not None:
        p = exe_cmd(cmd)
        rs = parser_cmd(p)
        if rs is not  None:
            return '\n'.join(rs)
    return ""
@celery.task(name="__main__.task_load_config")
def task_load_config():
    rs, dir = load_cfg()
    if rs is not None:
        rss = []
        for r in rs:
            if type(r) is cfg_info:
                rss.append(r.to_str())
            else:
                rss.append(r)
        if dir is not None:
            rss.append('ROOT_DIR %s' % dir)
        if len(rss) > 0:
            return '\n'.join(rss), rs
    return "", rs
