# int() = Mengubah value ke integer
# str() = Mengubah value ke string
# float() = Mengubah value ke float

# 2 + 2 = Tambah || Hasil: 4
# 2 * 2 = Kali || Hasil: 4
# 2 / 2 = Bagi || Hasil Bagi, tipe datanya berubah jadi float
# 2 - 2 = Kurang || Hasil: 0
# 2 ** 3 = Pangkat ||  Hasil: 8 

# round(2.6666666666666, 2) || Result: 2.67
# 8 // 2 || Automatis langsung ke integer tidak float 

# f - string
# Contoh Code:
# nama = "Ibnu Shevayanto"
# umur = 21
# jumlahMantan = 0
# print(f"Halo Nama Saya {nama}, Umur Saya {umur}, Dan Jumlah Mantan Saya {jumlahMantan}")

print("Welcome to the tip calculator.")
totalBil = float(input("What was the total bill? "))
percentageBil = float(input("What percentage tip would you like to give? "))
howManyPeople = float(input("How many people to split the bill? "))


percentage = totalBil * percentageBil / 100
result = round((totalBil + percentage) / howManyPeople, 2)
print(f"Each person should pay: {result}")
