import random
import string
import re


class Osm53 :
    arrayList = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", 
                 "n", "o", "ö", "p", "q", "r", "s", "ş", "t", "u", "ü", "v", "w", "x", "y", "z", 
                 "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    arrayList2 = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", 
                  "N", "O", "Ö", "P", "Q", "R", "S", "Ş", "T", "U", "Ü", "V", "W", "X", "Y", "Z"]
    arrayList3 = ['!',   '@',   '#',  '$',  '%',  '^',  '&',  '*',  '(',  ')',  '-',  '_',  '=',  '+',
                     '[',  ']',  '{',  '}',  '|',  ';',  ':',  "'",  '"',  ', ',  '.',  '<',  '>',  '?', 
                     '/',  '\\',  '`',  '~', ' ']

    def crypt(data):
        crypt =""
        for i in range (len(data)) :
            for j in range(len(Osm53.arrayList)) :
                if (data[i] == Osm53.arrayList[j]) :
                    crypt = crypt + str(j)
                    crypt = crypt + random.choice(string.ascii_letters)
                    break
            for k in range(len(Osm53.arrayList2)):
                if (data[i] == Osm53.arrayList2[k]) :
                    crypt = crypt + str(k+50)
                    crypt = crypt + random.choice(string.ascii_letters)
                    break
            for m in range(len(Osm53.arrayList3)) :
                if(data[i] == Osm53.arrayList3[m]):
                    crypt = crypt + str(m+100)
                    crypt = crypt + random.choice(string.ascii_letters)
        return crypt

    def decrypt(data):
        item = re.split(r'[a-zA-Z*?]',  data)
        item = item[:-1]
        decrypt = ""
        for i in range (len(item)):
            if (int(item[i]) >= 50):
                if (int(item[i]) >= 100):
                    item[i] = int(item[i]) - 100
                    for m in range(len(Osm53.arrayList3)):
                        if (Osm53.arrayList3.index(Osm53.arrayList3[m]) == int(item[i])):
                            decrypt = decrypt + Osm53.arrayList3[m]
                            break
                item[i] = int(item[i]) - 50
                for j in range(len(Osm53.arrayList2)) :
                    if (Osm53.arrayList2.index(Osm53.arrayList2[j]) == int(item[i])):
                        decrypt = decrypt + Osm53.arrayList2[j]
                        break
            else:
                for k in range(len(Osm53.arrayList)) :
                    if (Osm53.arrayList.index(Osm53.arrayList[k]) == int(item[i])):
                        decrypt = decrypt + Osm53.arrayList[k]
                        break
        return decrypt