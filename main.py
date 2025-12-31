def bubble_sort(arr):
    """
    Сортировка пузырьком по возрастанию.
    """
    n = len(arr)
    # Проходим по массиву n-1 раз
    for i in range(n - 1):
        # Каждый проход уменьшаем область сравнения
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j + 1]:
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

        # Сортируем массив
        sorted_numbers = bubble_sort(numbers.copy())

        print("\nОтсортированный массив (по возрастанию):")
        print(sorted_numbers)

        # Красивый вывод
        print("\nРезультат сортировки:")
        for i, num in enumerate(sorted_numbers):
            print(f"{i + 1}. {num}")

    except ValueError:
        print("Ошибка: пожалуйста, введите целое число для количества!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()