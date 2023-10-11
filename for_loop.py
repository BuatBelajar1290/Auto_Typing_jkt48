# Taking input from the user for the number of iterations
angka = int(input("Masukkan Angka Yang Ingin Di Ulang : "))
nama = input("Masukkan Nama Membernya : ")

# Using a for loop to iterate from angka to 1 in reverse order
for i in range(angka, 1, -1):
    print("/dl " + nama + " " + str(i - 1))
    print("/vn " + nama + " " + str(i - 1))

print("Loop completed!")
