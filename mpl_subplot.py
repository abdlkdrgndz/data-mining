import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv('iris.csv')

# Id alanına ihtiyaç olmadığı için çıkaralım

df1 = df.drop(["Id"], axis=1)

df1.plot(grid=True, alpha=0.9, subplots = True)
#plt.show()

# önce dataları alalım
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

# şimdi manuel olarak çizelim, iki değeri karşılaştıralım. 
plt.subplot(2,1,1) # 1. column un 1. satırını çiziyoruz
plt.plot(setosa.Id, setosa.PetalLengthCm, color="blue", label="setosa")
plt.ylabel('setosa - pelcm')

plt.subplot(2,1,2) # 1. column un 2. satırını çiziyoruz
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="red", label="versicolor")
plt.ylabel('versicolor - pelcm')
plt.show()