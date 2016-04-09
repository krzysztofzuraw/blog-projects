class decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print('Called {func} with args: {args}'.format(func=self.func.func_name, args=args))
        self.func(*args)

@decorator
def func(x,y):
    return x,y

if __name__ == '__main__':
    func(1,2)
