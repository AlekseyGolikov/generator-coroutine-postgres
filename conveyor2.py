# функция-декоратор отмечает в терминале, какая функция работает в данный момент
def decor(step):
    def function(func):
        def wrapper(*args):
            if step == 'producer':
                print('producer')
            elif step == 'pattern_filter':
                print('pattern_filter')
            elif step == 'print_token':
                print('print_token')
            return func(*args)
        return wrapper
    return function

def main(sentence):
    """
        Программа подсчитывает количество слов, состоящих из одних цифр
        и выводит значение в главную функцию

        >>> main('rfger 324 srgfgtr 2 gerge454 sd21 fsdfe 2323 45343 ergferg')
        print_token
        pattern_filter
        producer
        Общее число цифровых выражений 4
    """

    @decor('producer')
    def procuder(sentence, nextCoro):
        # print('producer')
        tokens = sentence.split(' ')
        for token in tokens:
            count = nextCoro.send(token)
        nextCoro.close()
        return count

    @decor('pattern_filter')
    def pattern_filter(nextCoro=None):
        # print('pattern_filter')
        count = 0
        while True:
            token = yield count
            if token.isdigit():
                nextCoro.send(token)
                count += 1

    @decor('print_token')
    def print_token():
        while True:
            token = (yield)

    printToken = print_token()
    printToken.__next__()
    patternFilter = pattern_filter(printToken)
    patternFilter.__next__()

    # sentence = 'rfger 324 srgfgtr 2 gerge454 sd21 fsdfe 2323 45343 ergferg'
    count = procuder(sentence, patternFilter)
    print('Общее число цифровых выражений %d' % count)

if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    sentence = 'rfger 324 srgfgtr 2 gerge454 sd21 fsdfe 2323 45343 ergferg'
    main(sentence)