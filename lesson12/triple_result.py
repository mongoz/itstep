def triple_result(func):
    def wrapper(*args):
        return func(*args) * 3

    return wrapper


@triple_result
def add(a, b):
    return a + b


print(add(5, 5))
# Я делал по примерам из learnbyexamples.com туго догодит
# Правильно ли я понимаю в def triple_result() мы параметром передаем a,b ?
# Не совсем понимаю для чего его использовать