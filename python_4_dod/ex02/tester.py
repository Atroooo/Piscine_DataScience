from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


try:
    @callLimit("lala")
    def h():
        print("h()")
except Exception as e:
    print(e)


for i in range(3):
    f()
    g()
