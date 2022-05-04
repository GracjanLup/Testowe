def porownaj(slowo1,slowo2):
    if "slowo1" == "slowo2":
        return "słowa są takie same"
    else:
        return "slowa różnią się od siebie"
print("podaj pierwsze slowo")
slowo1 = input()
print("podaj drugie slowo")
slowo2 = input()
print(porownaj(slowo1,slowo2))
print
slowo1.find(slowo2)
