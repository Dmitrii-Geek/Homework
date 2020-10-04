def div(*arg):
    try:
        arg1 = int(input("Введите числитель"))
        arg2 = int(input("Введите знаменатель"))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Вы не можете использовать ноль как делитель!"

    return res

    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Вы не можете использовать ноль как делитель!")

print(f'result  {div()}')
