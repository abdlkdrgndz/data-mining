import pandas

mydatas = {
    "unames" : ['Ali', 'Ahmet', 'Mehmet', 'Cemil', 'Kerim'],
    "age" : [50,30,53,45,34],
    "created_at" : ["12.11.2019", "11.02.2020", "09.07.2019", "09.09.2018", "02.01.2017"]
}

df = pandas.DataFrame(mydatas)
# INDEXING
# NUMPY kütüphanesinden farkı Pandas ta her zaman index ler yazılır.
print("------ UNAMES DEĞERLERİNİ ALALIM -------- ")
print(df['unames'])

print("------ DİĞER ŞEKİLDE ÖRNEĞİN YAŞ DEĞERLERİNİ ALALIM -------- ")
print(df.age)

# DİĞER GÖSTERİM ŞEKLİ LOC -> LOCATION
print("---- lOC İLE GÖSTER -----")
print(df.loc[:, "age"]) ## age sütununun tüm satırlarını al
print(df.loc[:2, "age"]) ## age sütununun 2 ye kadar olanını al. aynı slicing mantığı

# FIELD LER ARASINDAKİ DEĞERLERİ ALALIM ÖRNEĞİN UNAMES DEN AGE E KADAR
print("------- FIELD İSİMLERİ ARALIĞINDAKİ DEĞERLERİ ALALIM ------")
print(df.loc[:, "unames":"age"]) # unames den age e kadar tüm değerleri alır. 
print(df.loc[:2, "unames":"age"]) # unames den age e kadar ilk 2 satırı alır.
print("---------- FIELD SEÇEREK GÖSTERELİM -----------")
print(df.loc[:3, ["unames", "created_at"]]) # unames ve created_at ilk 2 satırı alır. !# PANDAS ta son değer dahildir, normalde hiçbirinde dahil değil !

## DEĞERLERİ TERSTEN YAZDIRALIM
print("----- DEĞERLERİ TERSTEN YAZDIRALIM ------")
print(df.loc[::-1,:]) # tüm satırlardaki değerleri tersten yazdırır.

# TÜM SATIRLARI YAZDIR BELİRLEDİĞİM FIELD E KADAR
print("----- TÜM SATIRLARI YAZDIR BELİRLEDİĞİM FIELD age'e KADAR (age dahil) ------")
print(df.loc[:,:"age"])

# iloc ile fieldname yerine index belirterek de erişebiliriz.
print("--- ILOC ILE INDEX YAZARAK ERİŞİM")
print(df.iloc[:,1]) # 1. indeks -> age olduğuna göre age değerleri gelir.

## YENİ BİR COLUMN EKLEYELİM - UPDATED_AT COLUMN EKLEYELİM
df['updated_at'] = ["13.11.2019", "15.02.2020", "16.07.2019", "11.09.2018", "10.01.2017"]
print("----- GÜNCEL HALİ ------ ")
print(df)