def decorator(F):
    def wrapper(*args):
        print('Called {}'.format(args))
    return wrapper

@decorator
def func(x, y):
    print(x,y)

class C(object):
    @decorator
    def method(self, x, y):
        print(x,y)

if __name__ == '__main__':
    c = C()
    c.method(1,2)
    func(3,4)
