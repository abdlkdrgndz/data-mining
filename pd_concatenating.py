import pandas

mydatas = {
    "name" : ['Ahmet', 'Mehmet', 'Cemil', 'Hasan'],
    "age" : [23,26,27,29],
    "price" : [1250, 2000, 3000, 6000],
    "currency" : ["USD", "EURO", "EURO", "TRY"]
}

myFrame = pandas.DataFrame(mydatas)

# DROP
# Currency field i drop edelim
myFrame.drop(["currency"] , axis=1, inplace=True) # axis 1 ise yukarıdan aşağı, 0 ise satırın başından sonuna drop eder, inplace=True property verilirse myFrame e eşitler. 
print("--- DROP CURRENCY FIELD ---")
print(myFrame)

# CONCATENATING - NUMPY DEKİ VSTACK VEYA HSTACK İŞLEMLERİNİN BENZERİDİR - İKİ DF Yİ BİRLEŞTİRELİM
first = myFrame.head(1) # ilk değer  -> Ahmet
last = myFrame.tail(1) # son değer -> Hasan

print("--- CONCAT ---")
print(pandas.concat([first,last], axis=0)) # axis ile yukarıdan aşağıya ya da soldan sağa birleştirebiliriz

print("--- YAŞ VE PRICE I BİRLEŞTİRELİM") # DİKEY
print(pandas.concat([myFrame.age, myFrame.price], axis=1))