import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# git statusenerovanie simulovaných teplotných dát (30 dní)
np.random.seed(42)
days = np.arange(1, 31)
temperatures = np.random.normal(loc=15, scale=5, size=30)  # priemer 15°C, odchýlka 5°C

data = pd.DataFrame({'Day': days, 'Temperature': temperatures})

# =============================================================================================

# Výpočty základných štatistík
mean_temp = np.mean(temperatures)
median_temp = np.median(temperatures)
std_temp = np.std(temperatures)
var_temp = np.var(temperatures)

# Lineárna regresia
slope, intercept, r_value, p_value, std_err = linregress(days, temperatures)
trendline = slope * days + intercept

# Vizualizácia dát
plt.figure(figsize=(12, 6))

# Histogram teplôt
plt.subplot(2, 2, 1)
plt.hist(temperatures, bins=8, color='skyblue', edgecolor='black')
plt.xlabel('Teplota (°C)')
plt.ylabel('Frekvencia')
plt.title('Histogram teplôt')

# =============================================================================================

# Čiarový graf teplôt
plt.subplot(2, 2, 2)
plt.plot(days, temperatures, marker='o', linestyle='-', color='red', label='Teplota')
plt.plot(days, trendline, linestyle='--', color='blue', label='Trendová priamka')
plt.xlabel('Deň')
plt.ylabel('Teplota (°C)')
plt.title('Teplotný trend')
plt.legend()

# Boxplot
plt.subplot(2, 2, 3)
sns.boxplot(y=temperatures, color='lightgreen')
plt.ylabel('Teplota (°C)')
plt.title('Boxplot teplôt')

# Zobrazenie
plt.tight_layout()
plt.show()

# ==================================================================

# Výstup štatistických výpočtov
print(f"Priemerná teplota: {mean_temp:.2f}°C")
print(f"Medián teploty: {median_temp:.2f}°C")
print(f"Smerodajná odchýlka: {std_temp:.2f}°C")
print(f"Rozptyl teplôt: {var_temp:.2f}°C")
print(f"Korelačný koeficient trendovej priamky: {r_value:.2f}")