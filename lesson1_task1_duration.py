# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


duration = int(input("Enter a number to calculate duration: "))

if duration >= 0:
    days = duration // 86400
    hours = (duration - days * 86400) // 3600
    minutes = (duration - days * 86400 - hours * 3600) // 60
    seconds = duration % 60
    if duration < 60:
        print(f"{duration} sec")
    elif duration <= 3600:
        print(f"{duration // 60} min {seconds} sec ")
    elif duration <= 86400:
        print(f"{hours} hours {minutes} min {seconds} sec ")
    else:
        print(f"{days} days {hours} hours {minutes} min {seconds} sec ")
else:
    print("You entered negative number, the time cannot be negative")
