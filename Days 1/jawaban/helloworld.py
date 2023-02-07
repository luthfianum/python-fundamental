print("soal1")
print(5+6)
print(5-6)
print(5*6)
print(5%6)
print(5/6)
print(5**6)
print(5//6)
print()
print("soal2")
print("Muhammad Tijan")
print("105220023")
print("Banten")
print()

print(type(12))
print(type(7.4))
print(type(3.14))
print(type(5-6j))
print(type(['Budi','15201001','jakarta']))
print(type("Tijan"))
print(type("105220023"))
print(type("Banten"))
print()

#number
print(1)
print(1.1)
print(1j)

#string
print("Tijan")

#Bolean
print(1==1)
print(1==2)

#List
print(['Budi','15201001','jakarta'])

#Tuple
Genap = (2,4,6,8)
print(Genap,type(Genap))#tidak bisa diubah nialnya atai sisnya yang artinya fix

#Set
himpunan = set()

himpunan.add(5)
himpunan.add(6)
himpunan.add(5j)
himpunan.add("Tijan")

print(himpunan)

#Dictionary
peserta = {
    "NIM":105220023,
    "Nama":"Muhammad Tijan",
    "Class":"Data Engineer",
    "Status":"Active"
}

print(peserta["NIM"])
print(peserta.keys())
print(peserta.values())
print()

#Eclucidian
x1 = float(2)
y1 = float(3)
x2 = float(10)
y2 = float(8)

def Jarak(x1, y1, x2, y2):
    titik = ((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))
    jarak = titik ** (1 / 2)
    return jarak

print("( ", x1, " , ", y1, " ) ", " & ", " ( ", x2, " , ", y2, " ) ")
print("Jarak 2 titik: ", Jarak(x1, y1, x2, y2))