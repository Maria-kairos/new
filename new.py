def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

# inner_functijn() - функцию невозможно вызвать самотстоятельно, так как она существует только в зоне работы функции test_function
test_function()