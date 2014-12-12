from tools import str_unicode

__author__ = 'linw'

from factory_celery import add, task_load_config, task_cmd
from flask import Flask, request
from config_manager import configs

from flask import flash, render_template, jsonify

from factory_celery import _app
app = _app

from config_manager import load_sub_cfg

@app.route("/")
def hello_world():
    return """Hello world---: \
                <a href="/load_config/">加载配置文件</a><br/>\
                <a href="/exe_cmd/">执行命令行</a><br/>\
                """

@app.route("/load_config/")
def load_config():
    res2 = task_load_config.apply_async()
    context = {"id": res2.task_id}
    return """Hello world---: \
                RS\
                <a href="/result2/%(id)s">%(id)s</a><br/>\
                """ % context

@app.route("/exe_cmd/")
def exe_cmd():
    if configs is None:
        return "Please Load"
    for cfg_name in configs:
        flash(configs[cfg_name])
    return render_template(
        'index.html'
    )

TASKS_DIC = {}

@app.route("/exe_cmd/<path:cmd>")
def exe_cmd_imp(cmd):
    if cmd is None:
        return "None cmd"
    task_id = task_cmd.apply_async([cmd]).task_id
    return render_template('exe_cmd.html', key = task_id)

@app.route("/exe_cmd_js/")
def exe_cmd_imp_js():
    global TASKS_DIC
    cmd_id = request.args.get('cmd_id', None, type=str)
    if cmd_id is None:
        return "None cmd"
    if TASKS_DIC.has_key(cmd_id):
        task_id = TASKS_DIC[cmd_id]
    else:
        cmd_group = configs[cmd_id]
        task_id = task_cmd.apply_async([cmd_group.cmd]).task_id
        TASKS_DIC[cmd_id] = task_id
    return render_template('exe_cmd.html', key = task_id)

@app.route("/result/<task_id>")
def show_result(task_id):
    retval = add.AsyncResult(task_id).get(timeout=1.0)
    return repr(retval)

@app.route("/result2/<task_id>")
def show_result2(task_id):
    global configs
    retval, cfgs = task_load_config.AsyncResult(task_id).get(timeout=21.0)
    configs = cfgs
    return repr(retval)

@app.route("/result_exe_cmd/<task_id>")
def show_result_exe_cmd(task_id):
    retval = task_cmd.AsyncResult(task_id).get(timeout=11.0)
    return str_unicode(retval)

@app.route("/result_exe_cmd_js/")
def result_exe_cmd_js():
    task_id = request.args.get('task_id', None, type=str)
    retval = task_cmd.AsyncResult(task_id).get(timeout=1.0)
    rs = str_unicode(retval).split(u'\n')
    line_rs = []
    for line in rs:
        if u'\r' == line or len(line) < 1:
            continue
        line_rs.append(line.replace('\r', ''))

    html = render_template('layoutcontent.html', entries = line_rs)
    #html = html.replace('\n', '')
    return jsonify(result = html)

if __name__ == "__main__":
    global configs
    app.config.from_object('SETTINGS')
    cfgs, root_dir = load_sub_cfg()
    configs = cfgs
    app.run(debug=True)
