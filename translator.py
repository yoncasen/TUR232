import random
import time

words = {'Hi': 'Merhaba',
         'Bye': 'Hoşça kalın',
         'Task': 'Görev',
         'Program': 'Program'}

# eng_words = ['Hi','Bye','Task', 'Programm']
#tr_words = ['Merhaba','Hoşça kalın','Görev', 'Program']

score = 0

mode = input("Bir mod seçin: Yeni kelimeler eklemek için 0, çeviri yapmak için 1: \n")
while ((mode != '0') and (mode != '1')):
    mode = input("Geçersiz sembol! Sadece 0 veya 1 yazın (Yeni kelimeler eklemek için 0, çeviri yapmak için 1) \n")

if mode == "1":
    print("Çevirebildiğiniz kadar kelime çevirin! 10 hakkınız var!")
    for i in range(10):
        word = random.choice(list(words.keys()))
        print("Bu kelimenin tercümesi ne: " + word)
        if input() == words[word]:
            print("Harika!!!")
            score += 1
        else:
            print("Bir yanlışlık var... Doğru kelime - " + words[word])

        #number = random.randint(0, len(eng_words)-1)
        # print("Tercümesi bu şekilde olmalı: " + eng_words[number])
        # if input() == tr_words[number]:
        #     print("Harika!!!")
        #     score += 1
        # else:
        #     print("Bir yanlışlık var... Doğru kelime - " + eng_words[number])
    print("score:" , score)
else:
    word = input("İngilizce bir kelime yazın: ")
    translate = input("Kelimenin tercümesini yazın: ")
    if len(word) > 0 and len(translate) > 0:
        words[word] = translate
        print("Kelime başarıyla eklendi!")
        print(words)

