import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_excel('dataset/Dataset_Bridges_Full.xlsx')
table = table[(table['Result'] != 'Not applicable')]
magnitudes_earthquake = [5.0, 6.0, 7.0, 7.5] # For now 3 magnitude since other magnitude is fail

no_reinforcements = []
bearings = []
ductile_materials = []
shock_absorbers = []
shear_links = []

####################################
# Hayward
for mg in magnitudes_earthquake:
    filtertble = table[(table['Magnitude'] == mg) & (table['Places'] == 'Hayward')]

    no_r_suc_count = 0
    no_r_fail_count = 0

    bear_suc_count = 0
    bear_fail_count = 0

    dm_suc_count = 0
    dm_fail_count = 0

    sa_suc_count = 0
    sa_fail_count = 0

    sl_suc_count = 0
    sl_fail_count = 0

    for index, row in filtertble.iterrows():
        if row['Reinforcement'] == 'No reinforcement':
            if row['Result'] == 'Pass':
                no_r_suc_count += 1
            elif row['Result'] == 'Fail':
                no_r_fail_count += 1

        if row['Reinforcement'] == 'Bearings':
            if row['Result'] == 'Pass':
                bear_suc_count += 1
            elif row['Result'] == 'Fail':
                bear_fail_count += 1

        if row['Reinforcement'] == 'Ductile materials':
            if row['Result'] == 'Pass':
                dm_suc_count += 1
            elif row['Result'] == 'Fail':
                dm_fail_count += 1

        if row['Reinforcement'] == 'Shock absorbers':
            if row['Result'] == 'Pass':
                sa_suc_count += 1
            elif row['Result'] == 'Fail':
                sa_fail_count += 1

        if row['Reinforcement'] == 'Shear links':
            if row['Result'] == 'Pass':
                sl_suc_count += 1
            elif row['Result'] == 'Fail':
                sl_fail_count += 1

    if no_r_fail_count + no_r_suc_count == 0:
        no_r_successRate = 0
    else:
        no_r_successRate = no_r_suc_count / (no_r_fail_count + no_r_suc_count) * 100

    if bear_fail_count + bear_suc_count == 0:
        bear_successRate = 0
    else:
        bear_successRate = bear_suc_count / (bear_fail_count + bear_suc_count) * 100

    if dm_fail_count + dm_suc_count == 0:
        dm_successRate = 0
    else:
        dm_successRate = dm_suc_count / (dm_fail_count + dm_suc_count) * 100

    if sa_fail_count + sa_suc_count == 0:
        sa_successRate = 0
    else:
        sa_successRate = sa_suc_count / (sa_fail_count + sa_suc_count) * 100

    if sl_fail_count + sl_suc_count == 0:
        sl_successRate = 0
    else:
        sl_successRate = sl_suc_count / (sl_fail_count + sl_suc_count) * 100

    no_reinforcements.append(round(no_r_successRate))
    bearings.append(round(bear_successRate))
    ductile_materials.append(round(dm_successRate))
    shock_absorbers.append(round(sa_successRate))
    shear_links.append(round(sl_successRate))

print("Hayward :")
print(no_reinforcements)
print(bearings)
print(ductile_materials)
print(shock_absorbers)
print(shear_links)

dfHayward = pd.DataFrame({'no reinforcements': no_reinforcements,
                          'bearings': bearings, 'ductile materials': ductile_materials,
                          'shock absorbers': shock_absorbers, 'shear links': shear_links},
                         index=magnitudes_earthquake)
ax = dfHayward.plot.bar(rot=0)
ax.set_xlabel("Magnitudes of Earthquake")
ax.set_ylabel("Success rate of bridges survived (%)")
ax.set_title("Hayward")

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005), fontsize=8, rotation=45)
#################################

no_reinforcements = []
bearings = []
ductile_materials = []
shock_absorbers = []
shear_links = []

####################################
# San Andreas
for mg in magnitudes_earthquake:
    filtertble = table[(table['Magnitude'] == mg) & (table['Places'] == 'San Andreas')]

    no_r_suc_count = 0
    no_r_fail_count = 0

    bear_suc_count = 0
    bear_fail_count = 0

    dm_suc_count = 0
    dm_fail_count = 0

    sa_suc_count = 0
    sa_fail_count = 0

    sl_suc_count = 0
    sl_fail_count = 0

    for index, row in filtertble.iterrows():
        if row['Reinforcement'] == 'No reinforcement':
            if row['Result'] == 'Pass':
                no_r_suc_count += 1
            elif row['Result'] == 'Fail':
                no_r_fail_count += 1

        if row['Reinforcement'] == 'Bearings':
            if row['Result'] == 'Pass':
                bear_suc_count += 1
            elif row['Result'] == 'Fail':
                bear_fail_count += 1

        if row['Reinforcement'] == 'Ductile materials':
            if row['Result'] == 'Pass':
                dm_suc_count += 1
            elif row['Result'] == 'Fail':
                dm_fail_count += 1

        if row['Reinforcement'] == 'Shock absorbers':
            if row['Result'] == 'Pass':
                sa_suc_count += 1
            elif row['Result'] == 'Fail':
                sa_fail_count += 1

        if row['Reinforcement'] == 'Shear links':
            if row['Result'] == 'Pass':
                sl_suc_count += 1
            elif row['Result'] == 'Fail':
                sl_fail_count += 1

    if no_r_fail_count + no_r_suc_count == 0:
        no_r_successRate = 0
    else:
        no_r_successRate = no_r_suc_count / (no_r_fail_count + no_r_suc_count) * 100

    if bear_fail_count + bear_suc_count == 0:
        bear_successRate = 0
    else:
        bear_successRate = bear_suc_count / (bear_fail_count + bear_suc_count) * 100

    if dm_fail_count + dm_suc_count == 0:
        dm_successRate = 0
    else:
        dm_successRate = dm_suc_count / (dm_fail_count + dm_suc_count) * 100

    if sa_fail_count + sa_suc_count == 0:
        sa_successRate = 0
    else:
        sa_successRate = sa_suc_count / (sa_fail_count + sa_suc_count) * 100

    if sl_fail_count + sl_suc_count == 0:
        sl_successRate = 0
    else:
        sl_successRate = sl_suc_count / (sl_fail_count + sl_suc_count) * 100

    no_reinforcements.append(round(no_r_successRate))
    bearings.append(round(bear_successRate))
    ductile_materials.append(round(dm_successRate))
    shock_absorbers.append(round(sa_successRate))
    shear_links.append(round(sl_successRate))

print("San Andreas :")
print(no_reinforcements)
print(bearings)
print(ductile_materials)
print(shock_absorbers)
print(shear_links)

dfSanAndreas = pd.DataFrame({'no reinforcements': no_reinforcements,
                             'bearings': bearings, 'ductile materials': ductile_materials,
                             'shock absorbers': shock_absorbers, 'shear links': shear_links},
                            index=magnitudes_earthquake)
ax = dfSanAndreas.plot.bar(rot=0)
ax.set_xlabel("Magnitudes of Earthquake")
ax.set_ylabel("Success rate of bridges survived (%)")
ax.set_title("San Andreas")
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005), fontsize=8, rotation=45)
#################################
plt.show()

