procesory = [
    ("Intel Core i3-12100", 4, 3.3, 4.3),
    ("Intel Core i5-12400", 6, 2.5, 4.4),
    ("Intel Core i7-12700K", 12, 3.6, 5.0),
    ("Intel Core i9-12900K", 16, 3.2, 5.2),

    ("AMD Ryzen 3 5300G", 4, 4.0, 4.2),
    ("AMD Ryzen 5 5600", 6, 3.5, 4.4),
    ("AMD Ryzen 7 5800X", 8, 3.8, 4.7),
    ("AMD Ryzen 9 5900X", 12, 3.7, 4.8),

    ("Apple M1", 8, 3.2, 3.5),
    ("Apple M2", 8, 3.5, 3.9)
]

vice_jader = [p for p in procesory if p[1] > 8]
vice_jader

rychle = [p for p in procesory if p[3] > 4.5]
rychle


serazeno_max = sorted(procesory, key=lambda x: x[3], reverse=True)
serazeno_max

serazeno_jadra = sorted(procesory, key=lambda x: x[1], reverse=True)
serazeno_jadra


import statistics as stats

jadra = [p[1] for p in procesory]
frekvence_base = [p[2] for p in procesory]
frekvence_max = [p[3] for p in procesory]

statistiky = {
    "prumer_jadra": stats.mean(jadra),
    "median_max_ghz": stats.median(frekvence_max),
    "nejvice_jader": max(jadra),
    "nejvyssi_max_frekvence": max(frekvence_max)
}

statistiky


import matplotlib.pyplot as plt

plt.hist(frekvence_max, bins=5, color="skyblue", edgecolor="black")
plt.title("Histogram maximálních frekvencí procesorů")
plt.xlabel("Max frekvence (GHz)")
plt.ylabel("Počet procesorů")
plt.grid(axis='y', alpha=0.3)
plt.show()
