x = int(input("Введи количество строк:"))
#Проверка для строк
if x>0:
    print("Строки введены верно")
else:
    print("строки введены неверно")
    quit()
#создание строк
text = [[str(input("Введи строку:"))]for i in range(x)] 
print(text)
sum_words = 0
for i in text:
    for k in i:
        words = k.split()
        sum_words += len(words)
print("Количество слов =", sum_words)

