# -*- coding: utf-8 -*-
"""IMT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yd7DXOEZ4SRieJGCgek6lS0zwzZ9BRxL
"""

beratbadan = float(input("Berapa berat badan (kg) anda: "))
tinggibadan = float(input("Berapa Tinggi badan (m) anda: "))


# Menghitung Indeks Massa Tubuh (IMT)
tinggibadan = tinggibadan / 100
imt = beratbadan / (tinggibadan ** 2)


# Output IMT
print("Indeks Massa Tubuh Anda adalah:", imt)

# Memeriksa kategori IMT
if imt < 18.5:
    print('Underweught')
elif 18.5 <= imt < 25:
    print('Normal Range')
elif 25 <= imt < 30:
    print('Overweight')
elif 30 <= imt < 35:
    print('Obese Class 1')
elif 35 <= imt < 40:
    print('Obese Class 2')
else:
    print('Obese Class 3')

"""NO 2"""