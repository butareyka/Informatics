import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('Table.csv', sep=';')

colors = ['#78C850', '#F08030', '#6890F0', '#F8D030']

fig, axes = plt.subplots(1, 16, figsize=(15, 15))
sns.boxplot(x=dataframe["<DATE>"], y=dataframe["<OPEN>"], orient='v', ax=axes[0], palette=colors)
sns.boxplot(x=dataframe["<DATE>"], y=dataframe["<HIGH>"], orient='v', ax=axes[1], palette=colors)
sns.boxplot(x=dataframe["<DATE>"], y=dataframe["<LOW>"], orient='v', ax=axes[2], palette=colors)
sns.boxplot(x=dataframe["<DATE>"], y=dataframe["<CLOSE>"], orient='v', ax=axes[3], palette=colors)
sns.boxplot(x=dataframe["<DATE1>"], y=dataframe["<OPEN1>"], orient='v', ax=axes[4], palette=colors)
sns.boxplot(x=dataframe["<DATE1>"], y=dataframe["<HIGH1>"], orient='v', ax=axes[5], palette=colors)
sns.boxplot(x=dataframe["<DATE1>"], y=dataframe["<LOW1>"], orient='v', ax=axes[6], palette=colors)
sns.boxplot(x=dataframe["<DATE1>"], y=dataframe["<CLOSE1>"], orient='v', ax=axes[7], palette=colors)
sns.boxplot(x=dataframe["<DATE2>"], y=dataframe["<OPEN2>"], orient='v', ax=axes[8], palette=colors)
sns.boxplot(x=dataframe["<DATE2>"], y=dataframe["<HIGH2>"], orient='v', ax=axes[9], palette=colors)
sns.boxplot(x=dataframe["<DATE2>"], y=dataframe["<LOW2>"], orient='v', ax=axes[10], palette=colors)
sns.boxplot(x=dataframe["<DATE2>"], y=dataframe["<CLOSE2>"], orient='v', ax=axes[11], palette=colors)
sns.boxplot(x=dataframe["<DATE3>"], y=dataframe["<OPEN3>"], orient='v', ax=axes[12], palette=colors)
sns.boxplot(x=dataframe["<DATE3>"], y=dataframe["<HIGH3>"], orient='v', ax=axes[13], palette=colors)
sns.boxplot(x=dataframe["<DATE3>"], y=dataframe["<LOW3>"], orient='v', ax=axes[14], palette=colors)
sns.boxplot(x=dataframe["<DATE3>"], y=dataframe["<CLOSE3>"], orient='v', ax=axes[15], palette=colors)

plt.rcParams.update({'font.size': 30})
plt.show()
