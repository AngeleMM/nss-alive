import click
import cmd
import sqlite3 as db

class QueryHandler:
    def __init__(self, db_name):
        # self.table = ''
        self.conn = db.connect(db_name)
        self.sqlpath = './backend/setup-database.sql'
        with open(self.sqlpath, 'r') as sql:
            self.sql = sql.read()
        with self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.executescript(self.sql)
            self.conn.commit()

    def run(self,query,qtype = 1):
        try:
            if qtype & qtype > 1 :
                return self.cursor.executescript(query)
            return self.cursor.execute(query)
        except Exception as e:
            self.make_str(e, 'red')

    def show(self,table):
        if table:
            table = table.split(' ')
            if(table[0] == 'all'):
                res = self.run('''SELECT name FROM
       (SELECT * FROM sqlite_master UNION ALL
        SELECT * FROM sqlite_temp_master)
    WHERE type='table'
    ORDER BY name''').fetchall()
                res = ', '.join(''.join(val) for val in res)
                return self.make_str(res, 'white')
            else:
                return self.get(table[0])
        self.get()

    def make_str(self,data,color):
        colors = {
         'brown': '\033[90m',
         'red': '\033[91m',
         'green': '\033[92m',
         'yellow': '\033[93m',
         'dark blue': '\033[94m',
         'purple': '\033[95m',
         'blue': '\033[96m',
         'white': '\033[97m',
         'none': '\033[98m',
         }
        string = '{}{}\033[0m'.format(colors[color],data)
        print(string)

    def _get_(self,table):
        query = 'PRAGMA table_info(`{}`)'.format(table)
        res = self.run(query).fetchall()
        self.cols = ''
        for r in range(len(res)):
            self.cols+='| {} '.format(res[r][1])
        self.cols+='|'
        data_query = '''SELECT * FROM {} '''.format(table)
        data = self.run(data_query).fetchall()
        self.ds = ''
        for d in range(len(data)):
            for s in range(len(data[d])):
                self.ds+='| {} '.format(data[d][s])
            self.ds+='|\n'

    def get(self,table=''):
        try:
            if not (table):
                if not (self.table):
                    self._get_(self.table)
            self.make_str(self.cols, 'green')
            self.make_str(self.ds, 'green')
        except Exception as e:
            self.make_str(e, 'red')

    def insert(self,table,values):
        query = """INSERT INTO {table}
          values ({values})""".format(table = table,values=values)
        self.execute(query)

    def insert_link(self,item):
        val = item.split(' ')
        query = """
        INSERT INTO source_link (data_category, descr, link_url)
        values {values}""".format(values=(val[0],val[1],val[2]))
        self.run(query)

    def drop(self,table):
        query = 'DROP TABLE IF EXISTS {}'.format(table)
        self.run(query)

    def delete(self,table):
        query = 'DELETE FROM {} '.format(table)
        self.run(query)

    def default(self):
        with open('./backend/default.sql', 'r') as sql:
            query = sql.read()
        self.run(query, 2)

#     def source_links(self):
#         '''Produce all the link that we need to download from'''
#         self.cursor.execute('select * from source_link')
#         return self.cursor.fetchall()
#
#     def persist_hash_result(self, digest, record):
#         '''Persist the hash of a download from a source for today'''
#         self.cursor.execute('''
# insert into query_source_result (id, download_date, checksum)
# values (?, ?, ?)
# ''', (record['id'], datetime.datetime.now().timestamp(), digest))
#
#     def run_query(self, query):
#         '''Get back all the records for a query'''
#         self.cursor.execute(query)
#         return self.cursor.fetchall()

class Cpanel(cmd.Cmd):
    def __init__(self):
        super(Cpanel, self).__init__()
        self.db = QueryHandler('nss-live.db')
        self.prompt = '\033[96m\033[1m[iterate]>\033[0m'
        self.color = '\033[91m\033[1m'
        self.qname = '{}---type:[yes/no]---\033[0m'.format(self.color)
        self.it = '''
                ______________________________________
         (__)  .\ are you sure you want to leave me? /
         (@@) .  ------------------------------------
   /------\/ .
  / |    ||
 *  /\---/\
    \n{}
'''.format(self.qname)
        self.cmdloop('''
                ____________________________________________________
         (__)  .\ Hi! To see all commands of this shell, run 'help'/
         (**) .  --------------------------------------------------
   /------() .
  / |    ||
 *  /\---/\
        ''')

    def do_use_default(self,item):
        self.db.default()

    def emptyline(self):
        if self.lastcmd:
            return None

    def do_link(self,args):
        self.db.insert_link(args)

    def do_drop(self,table):
        self.db.drop(table)

    def do_clean(self,table):
        self.db.delete(table)

    def do_show(self, table):
        self.db.show(table)

    def do_use(self, table):
        self.db.table = table
        print(self.db.table)

    def do_exit(self, args):
        answer = input(self.it)
        if(answer == 'yes'):
            print ('''
                ____________
         (__)  .\ byee...../
         (vv) .  ----------
   /------** .
  / |    ||
 *  /\---/\
''')
            raise SystemExit

if __name__ == '__main__':
    console = Cpanel()
    console.emptyline()
