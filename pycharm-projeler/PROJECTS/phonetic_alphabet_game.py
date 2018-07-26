import random

phonetic_alphabet = {"A":"alpha",
                     "B":"bravo",
                     "C":"charlie",
                     "D":"delta",
                     "E":"echo",
                     "F":"foxtrot",
                     "G":"golf",
                     "H":"hotel",
                     "I":"india",
                     "J":"juliett",
                     "K":"kilo",
                     "L":"lima",
                     "M":"mike",
                     "N":"november",
                     "O":"oscar",
                     "P":"papa",
                     "Q":"quebec",
                     "R":"romeo",
                     "S":"sierra",
                     "T":"tango",
                     "U":"uniform",
                     "V":"victor",
                     "W":"whiskey",
                     "X":"xray",
                     "Y":"yankee",
                     "Z":"zulu"}

puan = 0
print("Oyun başlıyor")
while True:
    for k,v in zip(phonetic_alphabet.keys(), phonetic_alphabet.values()):
        harf = random.choice(k)
        print(harf)
        karsilik = input()
        if v == karsilik:
            puan += 10
            print("DOĞRU!  Puan: ",puan)
            continue
        else:
            print("YANLIŞ!, OYUN BİTTİ.  Toplam Puan: ",puan)
            decision = input("Tekrar oynamak ister misin ? (Y/N)")
            if decision == "y":
                continue
            else:
                break
       
            
     
