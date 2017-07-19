class businessException(Exception):
    def __init__(self, msg):
        self.msg = '### BusinessException [ ' + msg + ' ]'

    def __str__(self):
        return self.msg