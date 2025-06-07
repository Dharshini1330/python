def greet(func):
    def wrap():
        print("hello")
        func()
        print("thanks for visiting")
    return wrap()


@greet
def ocean():
    print("this is ocean academy")

ocean()
