#Oyunda 4 haneli bir sayıyı tahmin etmeye çalışıyorsunuz 
#Eğer yazdığınız sayıdaki bir rakam tahmin etmeye çalıştığınız sayıda varsa 1 puan alıyorsunuz eğer tahmin ettiğiniz yerdeyse 2 puan alıyorsunuz 
#hangi rakamın doğru yerde olduğunuzu tahmin etmeniz gerekiyor


#Oyunun Yapması gerekenler

#4 Tane rastgele sayı üretmeli sayılar aynı olmamalı başlangıç sayısı 0 olmamalı
#Burası 4 tane rastgele sayı üretiyor

from random import randint #Rastgele sayı üretici
while(True):
    random_number0 = (randint(1,9))
    random_number1 = (randint(0,9))
    random_number2 = (randint(0,9))
    random_number3 = (randint(0,9))
    
    if random_number0 not in (random_number1,random_number2,random_number3) and random_number1 not in (random_number2,random_number3) and random_number2 != random_number3:
    #if (random_number1 != random_number2 and random_number1 != random_number3 and random_number1 != random_number4 and random_number2 != random_number3 and random_number2 != random_number4 and random_number3 != random_number4):
        break

#---------------------------------------------------------------------------------------------------------------------------
score = 0
while (True):
    user_input = input("Enter Number")
    #for debug
    if user_input == "break":
        break
    
    if not(user_input.isnumeric()): #Burda hepsinin sayı olup olmadığını kontrol ettim
        print("Number must be number not string or special characters")
        continue
    elif(len(user_input) != 4):     #Burda 4 haneli olmasını kontrol ettim
        print("Number must be equal to 4")
        continue

    elif (user_input[0] == user_input[1] or user_input[0] == user_input[2] or user_input[0] == user_input[3] or user_input[1] == user_input[2] or user_input[1] == user_input[3] or user_input[2] == user_input[3]):
        print("Number should be different") #burda sayıların farklı olması gerektiğini yazdırdım
        continue
   
 
#---------------------------------------------------------------------------------------------------------------------------   
#Şimdi burda if ler at koşturcak
#Şimdi burda 2,1  döndürmeliyim ve skor tutmalıyım kaç defada buldu diye önce 2 1 döndürmeyi yapcam



    liste = []
    #Burda Kullanıcının girdiği ilk rakamı kontrol ettim aynı işlemleri diğer rakamlar içinde kontrol etcem
    if int(user_input[0]) == random_number0:
        liste.append(2) #girdiği sayı var ve doğru yerde o yüzden 2 puan
    elif int(user_input[0]) in (random_number1,random_number2,random_number3):
        liste.append(1) #girdiği sayı var ama yanlış yerde o yüzden 1 puan
    
    #2
    if int(user_input[1]) == random_number1:
        liste.append(2)
    elif int(user_input[1]) in (random_number0,random_number2,random_number3):
        liste.append(1)
    
    #3    
    if int(user_input[2]) == random_number2:
        liste.append(2)
    elif int(user_input[2]) in (random_number0,random_number1,random_number3):
        liste.append(1)
    
    #4
    if int(user_input[3]) == random_number3:
        liste.append(2)
    elif int(user_input[3]) in (random_number0,random_number1,random_number2):
        liste.append(1)

#---------------------------------------------------------------------------------------------------------------------------   
    
    if liste == [2,2,2,2]:
        print("Congratulations you find the number!",user_input)
        print(liste)
        print("Score:",score)
        break
    else:
        score += 1
        print(user_input,":",liste)    