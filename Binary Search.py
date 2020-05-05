import time
import os

def start():
    while True:
        os.system('clear')
        print("-----------------------------")
        print("                             ")
        print("   Masukkan Bilangan Array   ")
        print("    Pisahkan dengan koma     ")
        print("                             ")
        print("-----------------------------")
        arr = input()
        if arr.replace(',', '').isnumeric():
            A = arr.split(',')
            for i in range(len(A)):
                min_idx = i
                for j in range(i + 1, len(A)):
                    if int(A[min_idx]) > int(A[j]):
                        min_idx = j

                temp = A[i]
                A[i] = A[min_idx]
                A[min_idx] = temp

            print("Data Array : %s" % A)
            print()
            while True:
                print("Masukkan bilangan yang ingin dicari: ")
                x = input()
                if x.isnumeric():
                    def binSearch(array, kiri, kanan, target):
                        while kiri <= kanan:
                            tengah = kiri + (kanan - kiri) // 2
                            if int(array[tengah]) == target:
                                return tengah
                            elif int(array[tengah]) < target:
                                kiri = tengah + 1
                            else:
                                kanan = tengah - 1
                        return -1

                    start = time.time()
                    hasil = binSearch(A, 0, len(A) -1, int(x))
                    end = time.time()

                    if hasil != -1:
                        print("Bilangan {} ada di array index ke {}" .format(x, hasil))
                    else:
                        print("Bilangan {} tidak ada didalam array" .format(x))

                    print("Selesai dalam %f detik" % (end - start))
                    input("(Enter untuk melanjutkan)")
                    return False
                else:
                    print("Data yang anda masukkan bukan angka")
                    input("(Enter untuk mengulangi)")
        else:
            print("Data yang anda masukkan bukan angka")
            input("(Enter untuk mengulangi)")

while True:
    os.system('clear')
    print("-----------------------------")
    print("-       BINARY SEARCH       -")
    print("-         ALGORITHM         -")
    print("-                           -")
    print("-  1. Start Program         -")
    print("-  2. Exit                  -")
    print("-----------------------------")
    pil = int(input("Masukkan pilihan: "))
    if pil == 1 :
        start()
    elif pil == 2:
        exit()
    else:
        print("Pilihan salah..")
        input("(Enter untuk melanjutkan)")
