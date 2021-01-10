import numpy as np
import matplotlib.pyplot as plt
x = np.array([6.2,40.8,29.02,31.2,22.1,20.03])
countries = ["Turkey", "USA", "Germany", "Netherlands", "Japan", "Belgium"]

y = x * 2 + 100

plt.bar(countries,y, color="orange")
plt.title('Bar Plot')
plt.xlabel('Ülkeler')
plt.ylabel('Gelir Dağılımı ($)')
plt.show()

# Bar Plot ile ilk vermiş olduğum değerlerin 2katının +10 fazlasını aldım. Bunu grafiksel olarak bir çıktıya veriyorum.