# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.


# Function to count sum of digits


def sum_digits(value):
    res_sum = 0

    while value != 0:
        res_sum += value % 10
        value //= 10
    return res_sum


# task a - Create a list with odd numbers^3

odd_numbers = []
for i in range(1, 1001):
    if i % 2 != 0:
        odd_numbers.append(i**3)
print(odd_numbers)

# task b - Calculate the sum of those numbers from this list, the sum of the digits of which is divisible by 7

sum_res1 = 0
for num in odd_numbers:
    if sum_digits(num) % 7 == 0:
        sum_res1 += num
print(f"The sum of elements, the sum of digits of which is divisible by 7 = {sum_res1}")

sum_res2 = 0  # new variable for new sum when we + 17 for each element of the list
for num in odd_numbers:
    if sum_digits(num+17) % 7 == 0:
        sum_res2 += num
print(f"The sum of  new elements (+17) , the sum of digits of which is divisible by 7 = {sum_res2}")
