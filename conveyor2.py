
def main(sentence):
    """
        Программа подсчитывает количество слов, состоящих из одних цифр
        и выводит значение в главную функцию

        >>> main('rfger 324 srgfgtr 2 gerge454 sd21 fsdfe 2323 45343 ergferg')
        Общее число цифровых выражений 4
    """
    def procuder(sentence, nextCoro):
        # print('producer')
        tokens = sentence.split(' ')
        for token in tokens:
            count = nextCoro.send(token)
        nextCoro.close()
        return count

    def pattern_filter(nextCoro=None):
        # print('pattern_filter')
        count = 0
        while True:
            token = yield count
            if token.isdigit():
                nextCoro.send(token)
                count += 1

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
    import doctest
    doctest.testmod(verbose=True)