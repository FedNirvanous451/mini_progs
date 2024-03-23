"""Алгоритмы.3. Дано: матрица D(m,n), m<=10, n<=12. В каждой строке D найти элемент, для
которого минимален модуль разности этого элемента и среднего
арифметического элементов строки. Вывести D так, чтобы после элементов
строки матрицы располагались найденный элемент, среднее арифметическое и
модуль их разности."""


from random import randint


def start():
    """Функция, записывающая начальные данные"""

    # ввод начальных данных с обработкой исключений
    global strs
    while True:
        try:
            strs = int(input("Введите количество строк (<= 10): "))
            if strs < 1 or strs > 10:
                raise Exception("Введенное число вне допустимого диапазона. Повторите попытку.")
            break
        except ValueError:
            print("Введенное значение не целое число. Повторите попытку.")
        except Exception as e:
            print(e)
            
    global columns        
    while True:
        try:
            columns = int(input("Введите количество стобцов (<= 12): "))
            if columns < 1 or columns > 12:
                raise Exception("Введенное число вне допустимого диапазона. Повторите попытку.")
            break
        except ValueError:
            print("Введенное значение не целое число. Повторите попытку.")
        except Exception as e:
            print(e)

    global enter
    while True:
        try:
            enter = int(input("Каким образом желаете вводить значения (самостоятельно - 1, автоматически - 2): "))
            if enter not in (1, 2):
                raise Exception("Введенное число вне допустимого диапазона. Повторите попытку.")
            break
        except ValueError:
            print("Введенное значение не целое число. Повторите попытку.")
        except Exception as e:
            print(e)
    

def random_input(object):
    """Функция, которая случайным образом заполняет матрицу числами из диапазона
    от -100 до 100"""

    for string in object: # перебираем строки string в матрице object
        for i in range(columns): # перебираем элементы строки string циклом со счетчиком
            string[i] = randint(-100, 100) # случаным образом присваиваем элементу значение из диапазона
    return object # возвращаем матрицу object

def user_input(object):
    """Функция, которая механическим способом заполняет матрицу числами из диапазона
    от -100 до 100"""

    matr = 1 # переменная для определения номера элемента в строке string
    for string in object: # перебираем строки string в матрице object
        for i in range(columns): # перебираем элементы строки string циклом со счетчиком
            print(f"Введите число (-100, 100) для {i + 1} позиции {matr} строки: ")
            # пользовательский ввод элемента string[i] с обработкой исключений
            while True:
                try:
                    string[i] = int(input())
                    if string[i] < -100 or string[i] > 100:
                        raise Exception("Введенное число вне допустимого диапазона. Повторите попытку.")
                    break
                except ValueError:
                    print("Введенное значение не целое число. Повторите попытку.")
                except Exception as e:
                    print(e)

        matr += 1 # инкрементируем переменную matr
    return object # возвращаем матрицу object

def realization(object):
    """Функция, реализующая идею поставленной задачи"""

    list_means = [] # создаем списки результирующих значений
    list_min_abses = []
    list_elems = []
    for string in object: # перебираем матрицу построчно
        ar_mean = (sum(string) / columns) # ищем среднее арифметическое
        min_abs = 1000 # присваиваем минимальному модулю максимальное значение
        for j in range(columns): # перебираем элементы строки 
            abs_elem = abs(ar_mean - string[j]) # модуль разности ср. арифм. и соответствующего элемента
            if abs_elem < min_abs: # если наш модуль разности меньше минимального - записываем данный в минимальный
                min_abs = abs_elem
                elem = string[j]
        list_min_abses.append(min_abs) # добавляем результирующие данные в соответствующие массивы
        list_means.append(ar_mean)
        list_elems.append(elem)
    results = [list_elems, list_means, list_min_abses] # записываем и вовзращаем результат
    return results

def print_results(matrix, results):
    """Функция, выводящая результирующие данные согласно поставленной формулировке"""

    str_ = 1 # индекс первого элемента (1.1)
    col_ = 1
    for i in range(strs): # перебираем элементы и выводим данные в нужном формате
        for el in matrix[i]:
            print(f"{str_}.{col_}: {el}", end="  ")
            col_ += 1
        print(f"Найденный элемент: {results[0][i]} ", end="   ")
        print(f"Среднее: {results[1][i]} ", end="      ")
        print(f"Модуль разности: {results[2][i]} ", end=" ")
        print()
        str_ += 1 # инкремент индексов 
        col_ = 1




if __name__ == "__main__":
    """Архитектура программы"""

    start() # запуск программы и ввод первых данных
    matrix = [[0 for x in range(columns)] for y in range(strs)] # создание нулевой матрицы нужного размера
    if enter == 1: # если матрица заполняется пользователем
        user = user_input(matrix)
        results = realization(user)
        print_results(user, results)

    else: # если матрица заполняется механически
        auto = random_input(matrix)
        results = realization(auto)
        print_results(auto, results)
