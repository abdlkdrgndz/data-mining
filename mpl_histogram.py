import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv('iris.csv')

# Id alanına ihtiyaç olmadığı için çıkaralım

df1 = df.drop(["Id"], axis=1)

# önce dataları alalım
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

# histogram ile varolan değerleri analiz edebiliriz. PetalLengthCm i 1.4 olan kaç değer var gibi.
plt.hist(setosa.PetalLengthCm, bins=15, color="red") # bins ile grafik aralıkları belirlenir. default 10
plt.xlabel("PetalLengthCm")
plt.ylabel("Values")
plt.title("Histogram")
plt.show()
