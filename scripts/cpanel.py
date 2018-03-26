import click, cmd
from query_handler import QueryHandler
from helpers import helper

class Cpanel(cmd.Cmd, helper.Helper):
    def __init__(self):
        super(Cpanel, self).__init__()
        # this is really magic!! dont you even think to change this!! I can see youu o_O!!
        helper.Helper.__init__(self)

        self.db = QueryHandler(self.db_name)
        self.cmdloop(self.hello_message)

        self.return_result('extend is working yet', 'blue', 'bold')

    def do_use_default(self, item):
        self.db.default()

    def emptyline(self):
        if self.lastcmd:
            return None

    def do_link(self, args):
        self.db.insert_link(args)

    def do_drop(self, table):
        self.db.drop(table)

    # def do_clean(self,table):
        # self.db.delete(table)

    def do_show(self, table):
        self.db.show(table)

    def do_use(self, table):
        self.db.table = table
        self.return_result(self.db.table, 'yellow')

    def do_exit(self, args):
        answer = input(self.exit_message)
        if answer == 'yes':
            self.return_result(self.exit)
            raise SystemExit

def main():
    console = Cpanel()
    console.emptyline()

if __name__ == '__main__':
    main()
