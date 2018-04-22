# 1. 1. Пресмятане на лице на квадрат
a = int(input('a = '))
area = a * a
print('Square = ', area)

# 2. От инчове към сантиметри
inches = float(input('Inches = '))
centimeters = inches * 2.54
print('Centimeters = ', centimeters)

# 3. Поздрав по име
name = input('Enter your name: ')
print('Hello, ' + name + '!')

# 4. Съединяване на текст и числа
firstName = input()
lastName = input()
age = int(input())
town = input()
print('You are ' + firstName + ' ' + lastName + ', a ' + str(age) + '-years old person from ' + town + '.')

# 5. Лице на трапец
b1 = float(input())
b2 = float(input())
h = float(input())
result = (b1 + b2) * h / 2
print(result)

# 6. Периметър и лице на кръг
import math
r = float(input('Въведете радиуса на кръга: '))
area = math.pi * r * r
perimeter = 2 * math.pi * r
print(area)
print(perimeter)

# 7. Лице на правоъгълник в равнината
x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
rectWidth = max(x1, x2) - min(x1, x2)
rectHeight = max(y1, y2) - min(y1, y2)
rectArea = rectWidth * rectHeight
rectPerim = (rectWidth + rectHeight) * 2
print('Area =', rectArea)
print('Perimeter =', rectPerim)

# 8. Лице на триъгълник
a = float(input())
h = float(input())
result = a * h / 2
print('Triangle area = ', float("{0:.2f}".format(result)))

# 9. Конзолен конвертор: от градуси °C към градуси °F
celsiusTemp = float(input('Въведете температурата в градуси по Целзии: '))
farenheitTemp = celsiusTemp * (9 / 5) + 32
print('Температурата в градуси по Фаренхайт: ', float("{0:.2f}".format(farenheitTemp)))

# 10. Конзолен конвертор: от радиани в градуси
import math
radians = float(input('Въведете радианите за превръщане в градуси: '))
degrees = (180 / math.pi) * radians
print('Радианите в градуси: ', float("{0:.2f}".format(degrees)))

# 11. Конзолен конвертор: USD към BGN
usd = float(input('Въведете сумата в американски долари: '))
bgn = usd * 1.79549
print('Сумата в лева: ', float("{0:.2f}".format(bgn)))

# 12. * Конзолен междувалутен конвертор
import sys
amount = float(input('Въведете сума за обмяна: '))
inputCurrency = input('Въведете входна валута: ')
outputCurrency = input('Въведете изходна валута: ')
if not (inputCurrency in ['BGN', 'USD', 'EUR', 'GBP']):
    sys.exit('Невалидна входна валута.')
if not (outputCurrency in ['BGN', 'USD', 'EUR', 'GBP']):
    sys.exit('Невалидна изходна валута.')
bgnToUsd = 1 / 1.79549
bgnToEur = 1 / 1.95583
bgnToGbp = 1 / 2.53405

usdToBgn = 1.79549
usdToEur = usdToBgn * bgnToEur
usdToGbp = usdToBgn * bgnToGbp

eurToBgn = 1.95583
eurToUsd = eurToBgn * bgnToUsd
eurToGbp = eurToBgn * bgnToGbp

gbpToBgn = 2.53405
gbpToUsd = gbpToBgn * bgnToUsd
gbpToEur = gbpToBgn * bgnToEur

if (inputCurrency == 'BGN' and outputCurrency == 'USD'):
    print(float("{0:.2f}".format(bgnToUsd * amount)), 'USD')
    sys.exit()
if (inputCurrency == 'BGN' and outputCurrency == 'EUR'):
    print(float("{0:.2f}".format(bgnToEur * amount)), 'EUR')
    sys.exit()
if (inputCurrency == 'BGN' and outputCurrency == 'GBP'):
    print(float("{0:.2f}".format(bgnToGbp * amount)), 'GBP')
    sys.exit()

if (inputCurrency == 'USD' and outputCurrency == 'BGN'):
    print(float("{0:.2f}".format(usdToBgn * amount)), 'BGN')
    sys.exit()
if (inputCurrency == 'USD' and outputCurrency == 'EUR'):
    print(float("{0:.2f}".format(usdToEur * amount)), 'EUR')
    sys.exit()
if (inputCurrency == 'USD' and outputCurrency == 'GBP'):
    print(float("{0:.2f}".format(usdToGbp * amount)), 'GBP')
    sys.exit()

if (inputCurrency == 'EUR' and outputCurrency == 'BGN'):
    print(float("{0:.2f}".format(eurToBgn * amount)), 'BGN')
    sys.exit()
if (inputCurrency == 'EUR' and outputCurrency == 'USD'):
    print(float("{0:.2f}".format(eurToUsd * amount)), 'USD')
    sys.exit()
if (inputCurrency == 'EUR' and outputCurrency == 'GBP'):
    print(float("{0:.2f}".format(eurToGbp * amount)), 'GBP')
    sys.exit()

if (inputCurrency == 'GBP' and outputCurrency == 'BGN'):
    print(float("{0:.2f}".format(gbpToBgn * amount)), 'BGN')
    sys.exit()
if (inputCurrency == 'GBP' and outputCurrency == 'USD'):
    print(float("{0:.2f}".format(gbpToUsd * amount)), 'USD')
    sys.exit()
if (inputCurrency == 'GBP' and outputCurrency == 'EUR'):
    print(float("{0:.2f}".format(gbpToEur * amount)), 'EUR')
    sys.exit()

# 13. Добавяне на 1000 дни към датата на раждане
import time
dob = input('Въведете дата на раждане: ')
# '23-03-1998'
resultTs = int(time.mktime(time.strptime(dob, "%d-%m-%Y"))) + 86400000
resultDate = time.strftime("%d-%m-%Y", time.localtime(resultTs))
print('Result timestamp: ', resultTs)
print('Result date: ', resultDate)