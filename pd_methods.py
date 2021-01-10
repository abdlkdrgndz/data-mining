import pandas as pd

# PANDAS DATAFRAMES
# Pandas dataframes leri kullanmak için hızlı ve etkili bir kütüphanedir.
# Datayı içinde depoladığımız yapılara DataFrame denir
# Pandas kütüphanesinde dosyalar arası geçiş kolaydır, örneğin csv veya txt dosyasını açıp inceleyebilir ve içerisine işlemler gerçekleştirebiliriz.
# Olmayan Datalar (missing data - NaN ) için işimizi kolaylaştırır. 
# reshape ile datayı daha etkili bir şekilde kullanabiliriz.
# Slice ve Indexing işlemleri daha basit
# time series data analizinde çok yardımcı
# hız

# Ex. Data Frames:
# username   age   created_at
# ali        24    21.11.2020 

# Başlayalım - Data Frame Oluşturma

df = {
    'names' : ['Ali', 'Kerim', 'Cemalettin', 'Ayşe', 'Fatma', 'Kadir'],
    'age' : ['34', '23', '19', '22', '28', '33'],
    'price' : ['10', '25', '35', '42', '59', '11'],
    } 

dataFrame = pd.DataFrame(df)
print(dataFrame)

# Import ettiğimiz dosyalarda ilk 5 değeri görmek istersek head ile bunu yaparız . Yüklü bir data olduğunu düşünürsek hız / performans açısından verimli. 
print("--------------")
head = dataFrame.head() # ilk 5 -> içerisine değer vererek istediğmiz sayıda datayı çekebiliriz.
head = dataFrame.tail() # son 5 -> içerisine değer vererek istediğmiz sayıda datayı çekebiliriz.
print(head)

print("--------------")
# PANDAS BASIC METHODS

mydatas = {
    "unames" : ['Ali', 'Ahmet', 'Mehmet', 'Cemil', 'Kerim'],
    "age" : [50,30,53,45,34],
    "created_at" : ["12.11.2019", "11.02.2020", "09.07.2019", "09.09.2018", "02.01.2017"]
}

createDF = pd.DataFrame(mydatas)
print(createDF)

# SÜTUNLARI GÖSTER
print("DF SÜTUNLAR -> ", createDF.columns)

print("-------------- INFOS -----------")
# DATA İLE İLGİLİ BİLGİLERİ ALALIM
print(createDF.info())

print("------------- GET TYPES ------------") # ! Pandas Library string leri object olarak gösterir !
print(createDF.dtypes)

print("---------- SADECE NUMERIC DEĞERLERİ ALALIM ---------")
# bu numeric değerlerin adetinden min, max ve ortalama değerine kadar birçok bilgiyi aynı anda verir.
print(createDF.describe())