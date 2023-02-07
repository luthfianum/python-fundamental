#Hari ke-2: Fundamental Python
#1
nama = "Tijan"
jurusan = "Ilmu Komputer"
angaktan = "2020"
umur = 20
asal_daerah = "Banten"
money_amout = 1000000000
is_mahasiswa = True
is_alien = False

tup = name, subject, year, age, city, bank_balance, is_collage_sutendt, is_monster = "Tijan", "Ilmu Komputer","2020",20,"Banten",1000000000,True,False

#2
print(type(nama))
print(type(jurusan))
print(type(angaktan))
print(type(umur))
print(type(asal_daerah))
print(type(is_mahasiswa))
print(type(is_alien))
print(type(tup))

print("\nPanjang Nama :",len(nama))

num_one = 5
num_two = 4

total = num_one+num_two
diff = num_two-num_one
product = num_one*num_two
division = num_one/num_two
reminder = num_two%num_one
exp = num_one**num_two
floor_division = num_one//num_two

print("\n",total, diff, product, division, reminder, exp, floor_division)

nama2 = input("\nNama :")
umur2 = input("Umur :")
asal_daerah2 = input("Asal Derah :")
print("\nnama saya :",nama2,"\numur saya :",umur2,"\nAsal : ",asal_daerah2)

r = float(input("\nInput Radius :"))
phi = 3.14
area_of_circle = phi*(r*r)
circum_of_circle = 2*phi*r

print("Luas Lingkaran :",area_of_circle)
print("Keliling Lingkaran :",circum_of_circle)

