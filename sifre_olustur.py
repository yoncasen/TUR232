import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 

#print(karakterler[:5])
while True:
  parola_uzunlugu = int(input("Kaç haneli bir parola istersiniz: "))

  parola = ""

  for i in range(parola_uzunlugu):
    parola += random.choice(karakterler)

  print(parola)