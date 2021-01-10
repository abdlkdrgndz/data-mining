import pandas

mydatas = {
    "unames" : ['Ali', 'Ahmet', 'Mehmet', 'Cemil', 'Kerim'],
    "age" : [21,30,53,45,34],
    "price": [1700,2200,3400,1100,1000],
    "currency" : ["TRY", "USD","TRY","USD","USD"],
    "created_at" : ["12.11.2019", "11.02.2020", "09.07.2019", "09.09.2018", "02.01.2017"]
}

df = pandas.DataFrame(mydatas)

# FILTERING -
print("---------  YAŞI 30 VE DAHA KÜÇÜK OLANLARI GÖSTERELİM ---------")
filter1 = df.age <=30
print(filter1)

print("--- TRUE FALSE YERİNE FİLTRELENMİŞ DATALARI LİSTELEYELİM ---")
print(df[filter1])

# BİRDEN FAZLA FİLTREYİ BİRLİKTE KULLANALIM 
# Yaşı 30 ve daha küçük olup aynı zamanda 1500 USD den fazla maaş alanları bulalım
print("------- Yaşı 30 ve daha küçük olup aynı zamanda 1500 $ dan fazla maaş alanları bulalım ---------")
filter2 = df.price > 1500
filter3 = df.currency == "USD"
print(df[filter1 & filter2 & filter3])


# DİĞER YÖNTEM
print("--- Yaşı 40 tan büyük olanları göster ---")
print(df[df.age > 40]) 
