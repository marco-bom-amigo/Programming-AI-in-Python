import matplotlib.pyplot as plt
import seaborn as sns

batidas = sns.load_dataset("car_crashes").sort_values("total", ascending=False)
batidas_seg = batidas[(batidas["abbrev"] == 'SC') | (batidas["abbrev"] == 'ND') | (batidas["abbrev"] == 'AR')]
print(batidas_seg.head(5))

sns.set(style="whitegrid")
sns.set_color_codes("pastel")
sns.barplot(x="total", y="abbrev", data=batidas_seg, label="Total", color="b")
sns.barplot(x="alcohol", y="abbrev",data=batidas_seg, label="Alcohol-involved",color="r")
sns.despine(left=True, bottom=True)
plt.show()