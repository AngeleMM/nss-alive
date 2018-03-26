from helpers.result_helper import ResultHelper
from helpers.vars import InitVars

class Helper(ResultHelper, InitVars):
    def __init__(self):
        ResultHelper.__init__(self)
        InitVars.__init__(self)