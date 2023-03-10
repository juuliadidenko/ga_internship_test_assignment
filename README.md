1. Какие шаги ты бы предпринял, если бы пользователь сказал, что API возвращает ему ошибку 500?

**Ответ:**  
- Воспроизвести ситуацию, в которой возникает ошибка. Если всё работает нормально, попросить пользователя перезагрузить страницу, почистить кэш и куки

- Посмотреть логи сервера (error log), если причина - баг в приложении, устранить баг (откатить приложение до стабильной версии, если баг обнаружен в последних изменениях)

- Проверить, нет ли проблем на стороне сервера (проверить разрешения к файлам, посмотреть содержимое .htaccess файла, проверить объём оперативной памяти сервера). Обратиться к хостинг провайдеру


2. Какие ты видишь проблемы в следующем фрагменте кода? Как его следует исправить? Исправь ошибку и перепиши код ниже с использованием типизации.

```python
def create_handlers(callback):
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda: callback(step))
    return handlers


def execute_handlers(handlers):
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()
```

**Ответ:** [2_refactor_handlers](https://github.com/juuliadidenko/ga_internship_test_assignment/blob/main/2_refactor_handlers.py)

3. Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? Сколько из них содержит атрибуты? Напиши скрипт на Python, который выводит ответы на вопросы выше.

**Ответ:** [3_tag_counter](https://github.com/juuliadidenko/ga_internship_test_assignment/blob/main/3_tag_counter.py)

4. Напиши функцию на Python, которая возвращает текущий публичный IP-адрес компьютера (например, с использованием сервиса ifconfig.me).

**Ответ:** [4_public_ip](https://github.com/juuliadidenko/ga_internship_test_assignment/blob/main/4_public_ip.py)

5. Напиши функцию на Python, выполняющую сравнение версий. Условия:
- Return -1 if version A is older than version B
- Return 0 if versions A and B are equivalent
- Return 1 if version A is newer than version B
- Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1.

**Ответ:** [5_compare_version](https://github.com/juuliadidenko/ga_internship_test_assignment/blob/main/5_compare_version.py)
