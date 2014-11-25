__author__ = 'linw'

from sqlite3 import dbapi2 as sqlite3


class LogDatabaseTool(object):
    def __init__(self, database):
        self.database = database

    def init_db(self, schema_file):
        if schema_file is not None:
            db = self.get_db()
            db.cursor().executescript(schema_file.read())
            db.commit()

    def get_db(self):
        cur_db = sqlite3.connect(self.database)
        cur_db.row_factory = sqlite3.Row
        return cur_db

    def add_log(self, project, version, log):
        u"""
        添加日志
        :type project: str
        :type version: int
        :param project: 项目名
        :param version: 版本号  数字
        :param log: 日志
        """
        db = self.get_db()
        db.execute('insert into entries (project, version, log) values (?, ?, ?)',
                   [project, version, log])
        db.commit()

    def get_log(self, project, version):
        u"""
        获取版本大于version的日志
        :param project: 工程名
        :param version:最小版本号
        :return: [version:log,version:log,version:log]格式的list
        """
        db = self.get_db()
        cur = db.execute(
            'select version, log from entries \
            where version>=%d and project=\'%s\'\
            order by version desc' % (version, project))
        entries = cur.fetchall()
        return ["%d: %s" % (row['version'], row['log']) for row in entries]

    def clear(self, project):
        """
        清理指定项目的日志
        :type project: str
        :param project:
        """
        db = self.get_db()
        db.execute('delete from entries where project = \'%s\'' % project)
        db.commit()