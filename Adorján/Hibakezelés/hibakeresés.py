

lista=["Bence","László","Hunor"]
lista.append("valami")
try:
    print(lista[31])
except:
    print("valami nem jó!")
else:
    print("sikeres lefutás!")
finally:
    print("ez a vége!")

try:
    szam=int (input("Kérek egy számot: "))
except:
    pass

print(szam)
