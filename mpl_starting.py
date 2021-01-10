# Görselleştirme Kütüphanesidir
# bir csv dosyasını okuyarak başlayalım ve onu data frames e dönüştürelim
# iris.csv dosyası çiçek türlerine ait bir dosya. 150 adet örnek datayı barındırıyor. Data içeriğini inceleyerek sütun ve data bilgilerini görebiliriz.


import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('iris.csv')

# tüm türleri gösterelim. 
print(df.Species)

# kaç farklı tür olduğunu listeleyelim.
print("-- Kaç Tür Var? ---")
print(df.Species.unique())

# elimizdeki cvs dosyası ile ilgili genel bilgileri öğrenelim.
print("--- Genel Bilgiler ---")
print(df.info())

# mesela numeric değerleri listeleyelim
print("--- Numeric Değerler ve Özellikler ---")
print(df.describe())

# bir türe ait dataları listeleyelim ve karşılaştıralım
print("-- Iris-setosa ve Iris-virginica Karşılaştırması --")
setosa = df[df.Species == "Iris-setosa"]
virginica = df[df.Species == "Iris-virginica"]

print(setosa.describe()) # bir property e ait sonuç istersek setosa.SepalLengthCm.describe().mean() şeklinde çağırabiliriz. 
print(virginica.describe())

# MATPLOTLIB E BAŞLAYALIM
