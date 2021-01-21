# 계절별 온도 바차트
import matplotlib.pyplot as plt

temperatures = [3.3, 34.5, 14.2, -10]
x = list(range(4))
x_labels = ['Spring', 'Summer', 'Fall', 'Winter']

plt.title("Bar Chart")
plt.bar(x, temperatures)
plt.xticks(x,x_labels)
plt.yticks(sorted(temperatures))
plt.xlabel("season")
plt.ylabel("temperature")
plt.show()