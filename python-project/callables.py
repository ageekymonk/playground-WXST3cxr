class Log:
    def __call__(self, pstr):
        print(pstr)

log = Log()
log("hello world")
