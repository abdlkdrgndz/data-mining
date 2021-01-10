import pandas

myDatas = {
    "name" : ['Kadir', 'Kerim', 'Mehmet'],
    "age" : [12,15,18],
    "created_at" : ["12.10.1988","11.10.1988","13.10.1988"]
}

df = pandas.DataFrame(myDatas)

# örneğin yeni sutünda yaşların iki katını alalım

df['age_two'] = [i *2 for i in df.age]

# şimdi bunu transforming data yöntemi ile yapalım
def transfer(age):
    return age * 3

# şimdi bu fonksiyonu çağıralım
df['age_three'] = df.age.apply(transfer)

print(df)
