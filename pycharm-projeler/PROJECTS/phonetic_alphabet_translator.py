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

def decrypt():
    firsts = []
    print("Type encrypted message: ")
    kelime = input()
    wordss = kelime.split()
    
    for i in wordss:
        first = i[0]
        firsts.append(first)
        
    for letter in firsts:
        letters = "".join(firsts)
    print(letters)
    

def encrypt():
    print("Type your message: ")
    string = input()
    string_list = []
    new_list = []


    for harf in string:
        string_list.append(harf.upper())

    for i in string_list:
        for k,v in phonetic_alphabet.items():
            if k == i:
                new_list.append(v)

    for kelime in new_list:
        words = " ".join(new_list)
    print(words)

while True:
    encrypt()
    decision = input("Again ? (Y/N)")
    if decision == "y":
        continue
    else:
        decision2 = input("Do you want to decrypt a message ? (Y/N)")
        if decision2 == "y":
            decrypt()
            continue
        else:
            break
    
