import numpy as np

# SHAPE MANIPULATIONS

# 3 vektörü / diziyi birleştirelim
arr = np.array([ [1,3,4], [4,5,6], [9,0,3] ])
imp = arr.ravel()
print("birleştirilmiş hali:" , imp)

# birleştirdiğimi tekrardan 3 e 3 lük matris yapayım  - RESHAPE
print("3 e 3lük:" , imp.reshape((3,3)) )

# TRANSPOS NE DEMEK 
# 1 8 11
# 4 7 12
# 5 9 13 şekline getirmektir.
arr2 = np.array(
    [
        [1,4,5], 
        [8,7,9],
        [11,12,13] 
    ]
)
print("Transpos: " , arr2.T)

print("-----------")

# RESIZE -RESHAPE DEN FARKLI AYNI DEĞERE ATIYOR YENİ BİR DEĞİŞKENE ATAMAMIZA GEREK KALMIYOR
# RESHAPE işlemiyle işlem yaptığımız array değişmez. en önemli fark bu.

arr5 = np.array([ [3,4,5], [9,8,7] ])
arr5.resize((2,3)) # 2 satırlı 3 sütunlu yap. bu işlem aslında şu: arr5 = arr5.resize((2,3))
print(" 2 satırlı 3 sütunlu hali: " , arr5)

