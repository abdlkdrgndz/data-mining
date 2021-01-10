import pandas
import numpy

myDatas =  {
    "name" : ["Kerim", "Cemil", "Ali"],
    "price" : [4000,6000,5500],
    "age" : [22,34,30],
    "created_at" : ["12.11.2020", "11.02.2019", "09.09.2020"],
    "updated at" : ["13.11.2020", "12.02.2019", "11.09.2020"]
}

df = pandas.DataFrame(myDatas)

## ORTALAMA MAAŞI ALALIM
print("--- Ortalama Maaş ---")
print(df.price.mean())

# istersek numpy ile de yapalım
print("--- numpy ile ortalama maaş")
print(numpy.mean(df.price))

# koşullu ifadeler ile yeni bir field tanımlayalım
print("--- KOŞULLU İFADELER -> MAAŞI 5000 DEN BÜYÜK OLANLARI YENİ BİR ALANDA GÖSTERELİM ---") 
df["price_status"] = ["high" if each > 5000 else "low" for each in df.price]
print(df)

# column name lere erişelim
print("--- column names ---")
column_names = [i.lower() for i in df.columns]
print(column_names)

# biraz zorlaştıralım ve diyelim ki boşluklu bir field name var ve _ çizgi ile onu birleştirip öyle render edeceğiz.
print("--- UPDATE SUTÜNUNA BİR GÖZAT ---")
new_format = [i.split()[0] + "_" + i.split()[1] if len(i.split()) > 1 else i for i in df.columns ]
print(new_format)