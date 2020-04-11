import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_excel('dataset/Dataset_Bridges_2.xlsx')
table = table[(table['Result'] != 'Not applicable')]

combinations_bridge = table['Combinations'].unique()
sorted_bridges = sorted(combinations_bridge)

print(sorted_bridges)
print(len(sorted_bridges))


passrate_each_bridge = []

for cb in sorted_bridges:

    bridgeTable = table[(table['Magnitude'] == 7.0) & (table['Combinations'] == cb)]

    pass_count = 0
    fail_count = 0

    for index, row in bridgeTable.iterrows():

        if row['Result'] == 'Pass':
            pass_count += 1
        elif row['Result'] == 'Fail':
            fail_count += 1

    if pass_count + fail_count == 0:
        successRate = 0
    else:
        successRate = pass_count / 10 * 100

    passrate_each_bridge.append(round(successRate))

print(passrate_each_bridge)

dfHayward = pd.DataFrame({'combinations': sorted_bridges, 'Pass Rate': passrate_each_bridge})
ax = dfHayward.plot.bar(x='combinations', y='Pass Rate', rot=0)
ax.set_xlabel("Combinations of bridges")
ax.set_ylabel("Success rate of bridges withstand (%)")
ax.set_title("Combination Bridge that survived in 7.0 with any reinforcement")

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005), fontsize=8, rotation=45)

plt.show()
