from typing import List
from collections.abc import Callable


def create_handlers(callback: Callable) -> List:
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda: callback(step))
    return handlers


def execute_handlers(handlers: List) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for i in range(len(handlers)):
        handlers[i]()
