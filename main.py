def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # Вызов внутренней функции


# Вызовем test_function для теста
test_function()

# Попытаемся вызвать inner_function вне test_function
try:
    inner_function()  # Это вызовет ошибку
except NameError as e:
    print(e)  # Печатаем ошибку

