import sqlite3 as db
from helpers import helper

class QueryHandler(helper.Helper):
    def __init__(self, db_name):
        '''this is really magic!! dont you even think to change this!! I can see youu o_O!!'''
        helper.Helper.__init__(self)

        self.table = ''
        self.conn = db.connect(db_name)
        self.sqlpath = './backend/setup-database.sql'
        with open(self.sqlpath, 'r') as sql:
            self.sql = sql.read()
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.executescript(self.sql)
            self.conn.commit()

    def run(self, query, qtype = 1):
        try:
            if qtype & qtype > 1 :
                return self.cursor.executescript(query)
            return self.cursor.execute(query)
        except Exception as e:
            self.throw_error(e) 
            

    def show(self, table):
        if table:
            if(table == 'all'):
                res = self.run('''SELECT name FROM
       (SELECT * FROM sqlite_master UNION ALL
        SELECT * FROM sqlite_temp_master)
    WHERE type='table'
    ORDER BY name''').fetchall()
                res = '\n-'.join('-'.join(val) for val in res)
                return self.return_result(res, 'white')
            else:
                return self.get(table)
        self.return_result('no table pointed', 'yellow')

    def _get_(self, table):
        query = 'PRAGMA table_info(`{}`)'.format(table)
        res = self.run(query).fetchall()
        cols = ''
        for r in res:
            cols += '| {} '.format(r[1])
        cols += '|'

        data_query = '''SELECT * FROM {} '''.format(table)
        data = self.run(data_query).fetchall()
        ds = ''
        for d in data:
            for s in d:
                ds += '| {} '.format(s)
            ds += '|\n'

        self.return_result(cols, 'red')
        self.return_result(ds, 'green')

    def get(self, table=''):
        try:
            self._get_(table)
        except Exception as exeption:
            self.return_result(exeption, 'red')

    def insert(self, table, values):
        query = """INSERT INTO {table}
          values({values})""".format(tabl =table, values=values)
        self.execute(query)

    def insert_link(self, item):
        val = item.split(' ')
        query = """
        INSERT INTO source_link (data_category, descr, link_url)
        values {values}""".format(values=(val[0], val[1], val[2]))
        self.run(query)

    def drop(self, table):
        if table:
            query = 'DROP TABLE IF EXISTS {}'.format(table)
            return self.run(query)
        self.return_result('please point the table to drop', 'yellow')

    def delete(self, table):
        query = 'DELETE FROM {} '.format(table)
        self.run(query)

    def default(self):
        with open('./backend/default.sql', 'r') as sql:
            query = sql.read()
        self.run(query, 2)