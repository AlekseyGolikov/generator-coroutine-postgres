# Программа иллюстрирует конвейерную обработку данных,
# реализованную на поочередной работе корутин

# Источник данных
def producer(givenSentence, nextCoroutine):
    print('Функция-источник данных')
    tokens = givenSentence.split(' ')
    for token in tokens:
        nextCoroutine.send(token)
    nextCoroutine.close()

# Определение шаблона для конвейерной структуры
def pattern_filter(searchPattern='ing', nextCoroutine=None):
    print('Функция pattern_filter отыскивает во входном предложении слова, оканчивающиеся на \'{}\''.format(searchPattern))
    try:
        while True:
            token = (yield)
            if searchPattern in token:
                nextCoroutine.send(token)
    except GeneratorExit:
        print('Фильтрация входного предложения закончена!')

# Приемник данных
def print_token():
    print('Вызвана функция print_token')
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print('Работа завершена!')

printToken = print_token()
next(printToken)
patternFilter = pattern_filter(nextCoroutine=printToken)
next(patternFilter)

givenSentence = 'Steve rogers is running very fast to chase down a train moving with high speed'
producer(givenSentence, patternFilter)
