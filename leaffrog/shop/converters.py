class FourDigitConverter: # бесполезный класс конвертор для выделения года или 4 цифр, создан для демонстрации конверт.
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
