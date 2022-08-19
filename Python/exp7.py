from cmath import sqrt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('/Users/ayushshah/Downloads/student.xlsx')
# # frequency = dict()
# # # print(df['mark'].describe())
# # x = list(df['mark'])
# # y = list(df['id'])

# # plt.figure(figsize=(y.__len__, x.__len__))

# # plt.subplot(131)#subplot(nrows, ncols, index, **kwargs)
# # plt.bar(x,y)
# # plt.xlabel("Marks")
# # plt.ylabel("Student")

# mu, sigma = df['mark'].mean() , df['mark'].std()
# x = mu + sigma * np.random.randn(10000)

# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


# plt.xlabel('Marks')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.05])
# plt.grid(True)

# plt.show()

y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mylabels = list(df['mark'])

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 