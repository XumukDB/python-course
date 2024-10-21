money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

survived = 0

while True:
    money_capital += salary
    if money_capital < spend:
        break
    money_capital -= spend
    survived += 1
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", survived)
