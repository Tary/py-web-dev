from flask import Flask
from celery import Celery
from command_tool import *
from config_manager import load_sub_cfg, load_group_cfg, cfg_info, cfg_group
from command_tool import exe_cmd

TASK_GROUPS_DIC = {}
TASK_CMD_DIC = {}

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
    global TASK_CMD_DIC
    TASK_CMD_DIC, dir = load_sub_cfg()
    if TASK_CMD_DIC is not None:
        rss = []
        for r in TASK_CMD_DIC:
            if type(r) is cfg_info:
                rss.append(r.to_str())
            else:
                rss.append(r)
        if dir is not None:
            rss.append('ROOT_DIR %s' % dir)
        if len(rss) > 0:
            return '\n'.join(rss), TASK_CMD_DIC
    return "", TASK_CMD_DIC

@celery.task(name="__main__.load_task_group")
def load_task_group():
    global TASK_GROUPS_DIC
    TASK_GROUPS_DIC, dir = load_group_cfg()
    if TASK_GROUPS_DIC is not None:
        rss = []
        for r in TASK_GROUPS_DIC:
            if type(r) is cfg_info:
                rss.append(r.to_str())
            else:
                rss.append(r)
        if dir is not None:
            rss.append('ROOT_DIR %s' % dir)
        if len(rss) > 0:
            return '\n'.join(rss), TASK_GROUPS_DIC
    return "", TASK_GROUPS_DIC

@celery.task(name="__main__.task_cmd_group")
def task_cmd(group_is):
    global TASK_CMD_DIC
    global TASK_GROUPS_DIC
    if group_is is not None and TASK_GROUPS_DIC.has_key(group_is):
        group = TASK_GROUPS_DIC[group_is]
        rs = []
        for cmd in group.cmds:
            cmd_rs = cmd.split(':')
            cmd_id = cmd_rs[0]
            if TASK_CMD_DIC.has_key(cmd_id):
                cmd_cfg = TASK_CMD_DIC[cmd_id]
                cmd = cmd_cfg.cmd
                if len(cmd_rs) == 2:
                    cmd = cmd % cmd_rs[1]
                crs = parser_cmd(exe_cmd(cmd))
                rs.extend(crs)

        if rs is not  None:
            return '\n'.join(rs)
    return "失败"
