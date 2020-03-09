# 4. Напишите функцию которая будет определять
# полигдром ли введенная строка. Если да 2 то печатать
# “True”, если нет “False”.

def word():
    your_word = input("Enter a word: ")
    for i in your_word:
        if i == your_word[-1]:
            return True
        else:
            return False

print(word())