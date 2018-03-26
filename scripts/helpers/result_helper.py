class ResultHelper(object):
    def __init__(self):
        self.colors = {
         'brown': '\033[90m',
         'red': '\033[91m',
         'green': '\033[92m',
         'yellow': '\033[93m',
         'dark blue': '\033[94m',
         'purple': '\033[95m',
         'blue': '\033[96m',
         'white': '\033[97m',
         'none': '\033[98m',
         'bold': '\033[1m'
        }

    def return_result(self, data, color = 'none', style = False):

        return_type = style != False and self.colors[style] or ''
        colored_text = '{}{}{}\033[0m'.format(self.colors[color], return_type, data)
        print(colored_text)

    def throw_error(self, exeption):
        self.return_result(exeption, 'red')
