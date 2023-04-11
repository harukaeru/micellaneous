import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 平均と標準偏差のリスト
mean_std_list = [
    (3.0, 0.7),
    (3.0, 0.5),
    (3.0, 0.25)
]

# x軸の値の範囲を定義
x = np.linspace(0, 6, 1000)

# グラフの描画
plt.figure(figsize=(8, 6))
for mean, std in mean_std_list:
    y = norm.pdf(x, mean, std)
    plt.plot(x, y, label=f'平均: {mean}, 標準偏差: {std}')

plt.title('正規分布')
plt.xlabel('x')
plt.ylabel('確率密度')
plt.legend()
plt.grid()
plt.show()
