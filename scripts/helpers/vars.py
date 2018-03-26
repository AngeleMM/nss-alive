class InitVars(object):
    def __init__(self):
        self.prompt = '\033[96m\033[1m[iterate-hackerspace]>\033[0m'
        self.color = '\033[91m\033[1m'
        self.qname = '{}---type:[yes/no]---\033[0m'.format(self.color)
        self.db_name = 'nss-live.db'
        self.hello_message = '''
                ____________________________________________________
         (__)  .\ Hi! To see all commands of this shell, run 'help'/
         (**) .  --------------------------------------------------
   /------() .
  / |    ||
 *  /\---/\
        '''
        self.exit_message = '''
                ______________________________________
         (__)  .\ are you sure you want to leave me? /
         (@@) .  ------------------------------------
   /------\/ .
  / |    ||
 *  /\---/\
    \n{}
'''.format(self.qname)
        self.exit = '''
                ____________
         (__)  .\ byee...../
         (vv) .  ----------
   /------** .
  / |    ||
 *  /\---/\
'''