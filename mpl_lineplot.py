import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv('iris.csv')

# Id alanına ihtiyaç olmadığı için çıkaralım

df1 = df.drop(["Id"], axis=1)

# print(df1)

# şimdi görselleştirme zamanı

#df1.plot()
#plt.show()

# önce dataları alalım
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color="blue", label="setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="red", label="versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color="orange", label="virginica")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
#plt.show()

df1.plot(grid=True, linestyle=":", alpha=0.8) # grafikte grid göstermek istersek,  grafiklere stil verebiliriz. alpha ile opaklık,
plt.show()

# setosa.Id x ekseni, setosa.PetalLengthcm y eksenidir. color grafiğin rengi, label ise etikettir. Legend ile label etiketinin nerede gösterileceği yani pozisyonu
# ayarlanır. show ile de gösterilir.