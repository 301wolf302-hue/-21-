"""
Задание №1. Калькулятор min/max
Автор: Пустосмехов М.А.
Группа: ИТ-10
"""

import re


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def evaluate(expr):
    expr = expr.replace(" ", "")
    
    # Проверка на отрицательные числа
    if '-' in expr:
        raise ValueError("Отрицательные числа не поддерживаются")
    
    # Проверка на недопустимые символы
    allowed = set('0123456789mM(),')
    for ch in expr:
        if ch not in allowed:
            raise ValueError(f"Недопустимый символ: '{ch}'")
    
    tokens = re.findall(r'\d+|[mM()]|,', expr)
    
    if not tokens:
        raise ValueError("Пустое выражение")
    
    stack = Stack()
    
    for token in reversed(tokens):
        if token.isdigit():
            stack.push(int(token))
        elif token in ('m', 'M'):
            if stack.is_empty():
                raise ValueError(f"Недостаточно аргументов для '{token}'")
            a = stack.pop()
            if stack.is_empty():
                raise ValueError(f"Недостаточно аргументов для '{token}'")
            b = stack.pop()
            result = min(a, b) if token == 'm' else max(a, b)
            stack.push(result)
    
    if stack.is_empty():
        raise ValueError("Не удалось вычислить выражение")
    
    result = stack.pop()
    if not stack.is_empty():
        raise ValueError("Лишние элементы")
    
    return result


def main():
    print("=" * 50)
    print("Калькулятор m(число,число) и M(число,число)")
    print("Пример: M(15,m(16,8))")
    print("Введите 'exit' для выхода")
    print("=" * 50)
    
    while True:
        try:
            expr = input("\nВведите выражение: ").strip()
            
            if expr.lower() == 'exit':
                print("До свидания!")
                break
            
            if not expr:
                print("Ошибка: Пустое выражение")
                continue
            
            result = evaluate(expr)
            print(f"Результат: {result}")
            
        except ValueError as e:
            print(f"Ошибка: {e}")
        except IndexError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()