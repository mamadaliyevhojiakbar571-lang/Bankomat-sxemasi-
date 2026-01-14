import time


balans = 1500000
parol = "7777"
sms_xizmati = False

print("=== BANKOMATGA XUSH KELIBSIZ ===")


print("• Uzbekcha\n• Ruscha\n• Ingilizcha")
input("Tilni tanlang: ")


urinish = 3
while urinish > 0:
    kod = input("\n[Password] Plastik kartangiz parolini kiriting: ")
    if kod == parol:
        print("Muvaffaqiyatli kirildi!")
        break
    else:
        urinish -= 1
        print(f"Xato parol! Qolgan urinishlar: {urinish}")

if urinish == 0:
    print("Kartangiz bloklandi!")
else:
    
    while True:
        print("\n--- BOSH MENYU ---")
        print("1. Balansni tekshirish")
        print("2. Naqd pul olish")
        print("3. SMS xabar ulash")
        print("4. Parolni o'zgartirish")
        print("5. Mobil aloqa uchun to'lov")
        print("6. Kredit to'lovlari")
        print("7. Komunal to'lovlar")
        print("0. Dasturdan chiqish")
        
        tanlov = input("\nXizmatni tanlang: ")

        if tanlov == "1":
            print(f"\n[ Balans ]\nBalansingizda {balans} so'm mablag' bor.")
            input("Orqaga qaytish uchun Enter bosing...")

        elif tanlov == "2":
            print("\n--- NAQD PUL OLISH ---")
            print("1. 50 ming\n2. 100 ming\n3. 150 ming\n4. 200 ming\n5. 300 ming\n6. 400 ming\n7. Boshqa summa\n0. Orqaga")
            t = input("Tanlang: ")
            
            summa = 0
            if t == "1": summa = 50000
            elif t == "2": summa = 100000
            elif t == "3": summa = 150000
            elif t == "4": summa = 200000
            elif t == "5": summa = 300000
            elif t == "6": summa = 400000
            elif t == "7": summa = int(input("Summani kiriting: "))
            
            if summa > 0:
                if balans >= summa:
                    balans -= summa
                    print("Pul sanalmoqda...")
                    time.sleep(1)
                    print(f"Marhamat, pulingizni oling. Qolgan balans: {balans}")
                else:
                    print("Mablag' yetarli emas!")
            input("Enter bosing...")

        elif tanlov == "3":
            print("\n[ SMS Xabar ulash ]")
            print("1. SMS xabarni yoqtirish\n2. SMS xabarni o'chirish\n0. Orqaga")
            sms_t = input("Tanlang: ")
            if sms_t == "1": sms_xizmati = True; print("Yoqildi.")
            elif sms_t == "2": sms_xizmati = False; print("O'chirildi.")

        elif tanlov == "4":
            yangi = input("\nYangi parolni kiriting: ")
            parol = yangi
            print("Parol o'zgartirildi!")

        elif tanlov == "5":
            print("\n[ Mobil aloqa ]\n• Uzmobile\n• Beeline\n• Ucell\n• UMS\n• Perfectum\n0. Orqaga")
            op = input("Operatorni tanlang: ")
            if op != "0":
                tel = input("Telefon raqam: ")
                s = int(input("Summani kiriting: "))
                if s <= balans:
                    balans -= s
                    print(f"{tel} raqamiga {s} so'm o'tkazildi.")
                else: print("Mablag' yetarli emas!")

        elif tanlov == "6":
            kr = input("\nKredit raqami: ")
            s = int(input("Summa: "))
            if s <= balans:
                balans -= s
                print("To'lov bajarildi.")
            else: print("Mablag' yetarli emas!")

        elif tanlov == "7":
            print("\n[ Komunal ]\n• Elektr\n• Gaz\n• Suv\n0. Orqaga")
            input("Xizmatni tanlang: ")
            s = int(input("Summa: "))
            if s <= balans:
                balans -= s
                print("To'lov bajarildi.")
            else: print("Mablag' yetarli emas!")

        elif tanlov == "0":
            print("Xayr!")
            break