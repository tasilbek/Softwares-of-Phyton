#mehmonlar = ['Ali','Vali','Hasan','Husan','Olim']
#for mehmon in mehmonlar:
    #print(mehmon)
    
#print(mehmonlar) #bu qator tsikl tashqarisida bo'lishi kerak edi
   # print(f"Hurmatli {mehmon}, sizni 20-dekabr kuni nahorga oshga taklif qilamiz")
#print("Hurmat bilan, Palonchiyevlar oilasi\n")
#sonlar = list(range(1, 11))
#for son in sonlar:
   # print(f"{son} ning kvadrati {son**2} ga teng")
#sonlar = list(range(11)) # 1dan 10 gacha sonlar ro'yxatini yaratamiz
#sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
#for son in sonlar: # sonlardagi har bir son uchun
   # sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadratiga yuklaymiz
    
    
#print(sonlar)
#print(sonlar_kvadrati)
##dostlar = [] # bo'sh ro'yxat
#print("5 ta eng yaqin do'stingiz kim?")
#for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
   # dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
#print(dostlar)
#ismlar = ['Anvar','Azamat','Ali','Mehroj','Temur']
#for ism in ismlar:
    #print(f"Assalomu alaykum  {ism}, biz sizni buyuk inson Tojiyev Asilbekning 7-dekabrda bo'lib o'tadigan 22 yillik tug'ilgan kunlariga taklif qilamiz!")
    #print("Hurmat bilan, Saparov va Tojiyevlar oilasi 😊 ")
#print("Kod", len(ism), "marta takrorlandi")
#toq_sonlar = list(range(11,100,2))
#for toq_son in toq_sonlar:
   # print(toq_son**3)
#kinolar = []
#print("5 ta eng sevimli kinolaringiz qaysilar?")
#for kino in range(5):
   #kinolar.append(input(f"{kino+1}-kinoning nomini kiriting: "))
#print(kinolar)
#n_people = int(input("Necha kishi bilan suhbatlashdingiz?\n>>> "))
#ismlar =[]
#for k in range(n_people):
    #ismlar.append(input(f"{k+1}-suhbat qilgan odamingiz kim edi?\n>>> "))
#print(ismlar)
#avtolar = ['audi','bmw','volvo','kia','hyundai']
#for avto in avtolar: # avtolar ichidagi har bir avto uchun...
   # if avto == 'bmw': # ... agar avto bmw ga teng bo'lsa
      #  print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
   # else: # aks holda ...
     #   print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.
#ism = 'Ali'
#ism.lower() == 'ali'
#ism = input('Ismingiz nima?\n>>> ') # Foydalanuvchi ismini so'raymiz
#if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
  # print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
#else: 
  # print("Salom, Ali")
#javob =  float(input("12x6 nechaga teng?>>> "))
#if javob!=72:
   # print("Javob xato!")
##yosh = int(input("Yoshingiz nechada?>>> "))
#login = input("Yangi login kiriting: ")
#if len(login)<=5: # login uzunligini tekshiramiz
   # print("Login 5 ta harfdan ko'proq bo'lishi shart!")
#yil = int(input("Tug'ilgan yilingizni kiriting: "))
#if 2023-yil<18: # foydalanuvchining yoshini hisoblaymiz
   #print(f"Yoshingiz {2023-yil} da ekan.")
  # print("Kirish mumkin emas!")
#else:
   # print("Xush kelibsiz!")
#yosh = int(input("Yoshingiz nechada?>>> "))
#if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")
#x, y = 25, 50 # x=25 va y=50
#print("x>y") if x>y else print("x<y")
#cars = ['toyota','mazda','hyundai','gm','kia']
#for car in cars:
   # if car != 'gm':
     #  print(car.title())
  #  else:
    #   print(car.upper())
#login = input("Yangi login kiriting: ")
#if login == 'Admin':
   # print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
    #print("Xush kelibsiz,", login,"!")
#son1 = int(input("Birinchi sonni kiriting: "))
#son2 = int(input("Ikkinchi sonni kiriting: "))
#if son1 == son2: 
  # print("Sonlar teng:", float(son1),"=",  float(son2))
#son = int(input("Istalgan sonni kiriting: "))
#if son>=0:
   # print("Son musbat")
#else:
   # print("Son manfiy")
#ildiz = float(input("Istalgan son kiriting, men uning ildizini topib beraman 😊\n>>> "))
#if ildiz>=0:
   # print("Bu sonning ildizi:",ildiz**(1/2), " ga teng")
#else:
  # print("Musbat son yozing, manfiy emas!")
#yosh = int(input('Yoshingiz nechada? '))
#if yosh<=4: # yosh bolalarga bepul
   # price = 0 
 #   print('Sizga kirish bepul.')
#elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
   # price = 5000
#elif yosh<65: # 12 dan katta va 65 dan kichiklarga narx 10000 so'm
    # price = 10000
 ##   print('Sizga kirish 5000 so\'m')
#elif yosh>=65: # qariyalarga esa 8000 so'm
   # price = 8000
#print(f"Sizga kirish {price} so'm")
#print(f"Sizga kirish {price} so'm")
   # print('Sizga kirish 10000 so\'m')
#kun = input("Bugun nima kun? ")
#harorat = float(input("Havo harorati qanday?"))
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
   # print('Bugun dam olish kuni.')
#else:
   # print('Bugun ish kuni.')
#if kun.lower()=='yakshanba' and harorat>
#if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
 #   print("Cho'milgani ketdik!")
#elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
 #   print("Uyda dam olamiz!")
#narx = 15000 # mijoz 15000 so'mga ovqat oldi.
#choy = True 
#salat = False 
#non = True
#kompot = True
#assorti = False
# Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
#if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
  # narx = narx + 10000 # narxga 10000 so'm qo'shamiz
#elif choy or salat: # agar choy yoki salat olgan bo'lsa
    # narx = narx + 5000 # narxga 5000 so'm qo'shamiz
#if choy: # agar choy olsa
#   print("Mijoz choy oldi.")
##   narx = narx + 3000
#if salat: # agar salat olsa
#   print("Mijoz salat oldi.")
#   narx = narx + 5000
#if non: # agar non olsa     
#   print("Mijoz non oldi.") 
#   narx = narx + 2000
#if kompot: # agar kompot olsa
#    print("Mijoz kompot oldi.")
 #   narx = narx + 5000
##if assorti: # agar assorti olsa
 #   print("Mijoz assorti oldi.")
#    narx = narx + 15000
    
    
#print(f"Jami {narx} so'm") 
#menu = ['osh','qozonkabob','shashlik','norin','somsa']
#'manti' in menu # menu da manti bormi?
#ovqat = input('Nima ovqat yeysiz?>>> ')
#if ovqat.lower() in menu:
 #   print('Buyurtma qabul qilindi.')
#else:
 #   print('Afsuski bizda bunday ovqat yo\'q')
#'manti' not in menu # menu da manti yo'qmi? 
#if ovqat.lower() not in menu:
  #  print('Afsuski bizda bunday ovqat yo\'q')
#else:
 #   print('Buyurtma qabul qilindi.')
#buyurtmalar = []


#if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#   for taom in buyurtmalar:
#       if taom in menu:
#          print(f"Menuda {taom} bor")
#       else:
 #         print(f"Kechirasiz, menuda {taom} yo'q")
#else: # agar ro'yxat bo'sh bo'lsa
#          print("Savatchangiz bo'sh!")

#mevalar = ['olma','anor','uzum']
#print(mevalar[2])
#son = float(input("Istalgan son kiriting: "))
#ildiz = son**(1/2)
#print(f"{son} ning ildizi {ildiz} ga teng")

































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































