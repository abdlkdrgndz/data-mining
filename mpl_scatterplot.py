import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv('iris.csv')

# Id alanına ihtiyaç olmadığı için çıkaralım

df1 = df.drop(["Id"], axis=1)

# önce dataları alalım
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

# iki feature karşılaştırmak için scatterplot kullanılır
plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color="red")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color="blue")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color="green")
plt.xlabel('PetalLengthCm')
plt.ylabel('PetalWidthCm')
plt.title("Scatter Plot")
plt.show()