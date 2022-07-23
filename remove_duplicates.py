""" Створіть функцію def remove_duplicates(array) яка приймає цілочисельний масив, 
відсортований у порядку зростання, видаліть дублікати чисел, щоб кожен унікальний 
елемент з’являвся лише один раз. Функція має повертати новий массив без дуплікатів чисел, 
відносний порядок елементів має бути незмінним

Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми, 
або за допомогою input() або в результаті викликів функції. Але в файлі 
remove_duplicates.py повина бути створена функція def remove_duplicates(array) 
яка виконує необхідну логіку.

Приклади:

remove_duplicates([1,1,2]) -> [1,2]
remove_duplicates([0,0,1,1,1,2,2,3,3,4]) -> [0,1,2,3,4]
remove_duplicates([1,1,1,1,1,1,1,1]) -> [1] """


def remove_duplicates(array):
    arrey_new = []
    for num in array:
        if num in array and num not in arrey_new:
            arrey_new.append(num)
    return arrey_new


print(remove_duplicates([1,1,2]))
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
print(remove_duplicates([1,1,1,1,1,1,1,1]))