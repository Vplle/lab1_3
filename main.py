def bubble_sort(arr, ascending=True):
    """
    Сортировка пузырьком.
    Если ascending=True - по возрастанию, иначе - по убыванию.
    """
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if ascending:
                # Для сортировки по возрастанию
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                # Для сортировки по убыванию
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    print("Сортировка пузырьком")
    print("=" * 30)

    try:
        # Запрашиваем количество чисел
        n = int(input("Сколько чисел вы хотите отсортировать? "))

        if n <= 0:
            print("Количество чисел должно быть положительным!")
            return

        numbers = []
        print(f"\nВведите {n} чисел:")

        # Запрашиваем n чисел
        for i in range(n):
            while True:
                try:
                    num = float(input(f"Число {i + 1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Пожалуйста, введите число!")

        print("\nИсходный массив:")
        print(numbers)

        # Запрашиваем направление сортировки
        print("\n" + "=" * 30)
        print("Выберите направление сортировки:")
        print("1. По возрастанию (от меньшего к большему)")
        print("2. По убыванию (от большего к меньшему)")

        while True:
            try:
                choice = int(input("Ваш выбор (1 или 2): "))
                if choice == 1:
                    ascending = True
                    direction_text = "по возрастанию"
                    break
                elif choice == 2:
                    ascending = False
                    direction_text = "по убыванию"
                    break
                else:
                    print("Пожалуйста, введите 1 или 2!")
            except ValueError:
                print("Пожалуйста, введите число 1 или 2!")

        # Сортируем массив в выбранном направлении
        sorted_numbers = bubble_sort(numbers.copy(), ascending)

        print(f"\nОтсортированный массив ({direction_text}):")
        print(sorted_numbers)

        # Красивый вывод
        print(f"\nРезультат сортировки {direction_text}:")
        for i, num in enumerate(sorted_numbers):
            print(f"{i + 1}. {num}")

    except ValueError:
        print("Ошибка: пожалуйста, введите целое число для количества!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()