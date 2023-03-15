# 导入数据分析包：numpy（科学计算）、pandas（处理数据框）和 matplotlib/seaborn(可视化)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 导入数据
hist_worldcup= pd.read_csv('WorldCupsSummary.csv')
# 根据表内信息进行一定的数据处理
# 统一"Germany FR"和"Germany"
hist_worldcup = hist_worldcup.replace('Germany FR','Germany')
print(hist_worldcup.head())
# 查看数据表类型，进行必要的类型转化
# hist_worldcup.dtypes

# 将字符串类型转化为整形
hist_worldcup['GoalsScored']= hist_worldcup["GoalsScored"].astype(int)
hist_worldcup['QualifiedTeams']= hist_worldcup["QualifiedTeams"].astype(int)
hist_worldcup['MatchesPlayed']= hist_worldcup["MatchesPlayed"].astype(int)
hist_worldcup['Attendance']= hist_worldcup["Attendance"].astype(int)

# 分析历年现场观众人数变化趋势
# 设置全局绘图参数
font = {
  'weight': 'bold',
  'size': '20'
}

plt.rc('font', **font)

fig, ax= plt.subplots(figsize=(12,8))
plt.title('Attendance Number')

hist_worldcup.plot.scatter(x='Attendance',y='Year',ax=ax,zorder=2,s=100)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.grid(visible=True)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_yticks(hist_worldcup['Year'].tolist())
ax.set_xticks([500000,1000000,1500000,2000000,2500000,3000000,3500000,4000000])
ax.ticklabel_format(style='plain')

plt.tick_params(bottom=False, left=False)
plt.show()

# 参赛队伍数变化趋势
fig, ax= plt.subplots(figsize=(12,8))
plt.title('QualifiedTeams Numbers')
hist_worldcup.plot.scatter(x='QualifiedTeams',y='Year',ax=ax,zorder=2,s=100)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.grid(visible=True)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_yticks(hist_worldcup['Year'].tolist())
ax.set_xticks([0,16,24 ,32,48])
plt.tick_params(bottom=False, left=False)
plt.show()

# 历年进球数变化趋势
fig, ax= plt.subplots(figsize=(12,8))
plt.title('Goals Number')
hist_worldcup.plot.scatter(x='GoalsScored',y='Year',ax=ax,zorder=2,s=100)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.grid(visible=True)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_yticks(hist_worldcup['Year'].tolist())
ax.set_xticks([50,75,100,125,150,175,200])
plt.tick_params(bottom=False, left=False)
plt.show()

# 夺冠次数分析
palette=['yellow','red','red','blue','purple','coral','coral','purple']
fig, ax= plt.subplots(figsize=(16,8))

plt.title('Champion Number Statistic')
sns.countplot(x = hist_worldcup['Winner'], palette=palette,linewidth=2.5, edgecolor=".2")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
plt.tick_params(labelleft=False, left=False,labelsize=14)

for i in ax.containers:
    plt.bar_label(i, fontsize=15)

plt.show()

# 半决赛(4强)队伍次数统计
countries = hist_worldcup[['Winner','Second','Third','Fourth']].apply(pd.value_counts).reset_index().fillna(0)
countries['SemiFinal'] = countries['Winner'] + countries['Second']+countries['Third']+countries['Fourth']
countries['Final'] = countries['Winner']+countries['Second']
print(countries.head())

# 设置颜色
clrs= ['blue' if (i>=8) else 'y' if (5<=i<8) else 'purple' if (3<=i<5) else 'orangered' if (i==2) else 'red' for i in countries['SemiFinal']]

fig, ax= plt.subplots(figsize=(20,8))
plt.title('SemiFinal Statistic')
sns.barplot(data=countries,x='index',y='SemiFinal',palette=clrs,linewidth=2.5, edgecolor=".2")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
plt.tick_params(labelleft=False, left=False,labelsize=14)
plt.xticks(rotation=45)

for i in ax.containers:
    ax.bar_label(i,fontsize=15)
plt.show()

# 决赛队伍次数统计
# 去掉没进入过决赛的队伍：
finalist = countries.drop(countries[(countries['Winner']==0) & (countries['Second']==0)].index)


clrs= ['blue' if (i>=6) else 'y' if (i==5) else 'yellow' if (3<=i<5) else 'purple' if (i==2) else 'red' for i in finalist['Final']]


fig, ax= plt.subplots(figsize=(20,8))
plt.title('Final Statistic')
sns.barplot(data=finalist,x='index',y='Final',palette=clrs,linewidth=2.5, edgecolor=".2")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
plt.tick_params(labelleft=False, left=False,labelsize=14)


plt.xticks(rotation=45)

for i in ax.containers:
    ax.bar_label(i,fontsize=15)
plt.show()

# 进入决赛后夺冠以来分析
# 选择进入决赛的队伍
ratios = np.round(finalist[(finalist['Second']>0) | (finalist['Winner']>0)],decimals=2)
finalist['champion_prob'] = finalist['Winner']/finalist['Final']
#Set the color
clrs= ['blue' if (i==1) else 'y' if (0.5<i<1) else 'purple' if (i==0.5) else 'yellow' if (0<i<0.5) else 'red' for i in ratios['champion_prob']]


fig, ax= plt.subplots(figsize=(20,8))
plt.title('Percentage of winning reaching the final')
sns.barplot(data=ratios,x='index',y='champion_prob',palette=clrs,linewidth=2.5, edgecolor=".2")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
plt.tick_params(labelleft=False, left=False,labelsize=14)


plt.xticks(rotation=45)
for i in ax.containers:
    ax.bar_label(i,fontsize=15)
plt.show()

# 夺冠队伍所在大洲分布
index1 = hist_worldcup['WinnerContinent'].value_counts().index.tolist()
value1 = hist_worldcup['WinnerContinent'].value_counts().values.tolist()

palette = ['yellow', 'blue']

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

sns.countplot(ax=ax[0], x=hist_worldcup['WinnerContinent'], palette=palette, linewidth=2.5, edgecolor=".2")
ax[0].set_title('Champion Continent Numbers')
ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False, labelsize=14)

for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15)

plt.pie(value1, labels=index1, autopct='%.0f%%', colors=['blue', 'yellow'],
        wedgeprops={"edgecolor": "0", 'linewidth': 2.5,
                    'antialiased': True}, startangle=90, textprops={'fontsize': 20})
ax[1].set_title('Champion Continent Ratios', size=20, weight='bold')
plt.show()

# 东道主进入半决赛/决赛/夺冠概率统计
# 增加一列判断东道主（主办国）是否进入半决赛（4强）
hist_worldcup['HostTop4'] = hist_worldcup[['Winner','Second','Third','Fourth']].eq(hist_worldcup['HostCountry'],axis=0).any(1)


# 增加一列判断东道主（主办国）是否进入决赛
hist_worldcup['HostTop2'] = hist_worldcup[['Winner','Second']].eq(hist_worldcup['HostCountry'],axis=0).any(1)


# 增加一列判断东道主（主办国）是否夺冠
hist_worldcup['HostWinner']= hist_worldcup['HostCountry']== hist_worldcup['Winner']
# 东道主进入半决赛（4强）概率

index = hist_worldcup['HostTop4'].value_counts().index.tolist()
values = hist_worldcup['HostTop4'].value_counts().values.tolist()

palette = ['blue', 'yellow']

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

sns.countplot(ax=ax[0], x=hist_worldcup['HostTop4'], palette=palette, linewidth=2.5, edgecolor=".2")
ax[0].set_title('Host in Top4')
ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False, labelsize=14)
for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15)

plt.pie(values, labels=index, autopct='%.0f%%', colors=['yellow', 'blue'],
        wedgeprops={"edgecolor": "0", 'linewidth': 2.5,
                    'antialiased': True}, startangle=90, textprops={'fontsize': 20})
ax[1].set_title('Percentage', size=20, weight='bold')
plt.show()

# 东道主进入决赛概率

index = hist_worldcup['HostTop2'].value_counts().index.tolist()
values = hist_worldcup['HostTop2'].value_counts().values.tolist()

palette = ['blue', 'yellow']

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

sns.countplot(ax=ax[0], x=hist_worldcup['HostTop2'], palette=palette, linewidth=2.5, edgecolor=".2")
ax[0].set_title('Host in Top2')
ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False, labelsize=14)
for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15)


plt.pie(values, labels=index, autopct='%.0f%%', colors=['blue', 'yellow'],
        wedgeprops={"edgecolor": "0", 'linewidth': 2.5,
                    'antialiased': True}, startangle=90, textprops={'fontsize': 20})
ax[1].set_title('Percentage', size=20, weight='bold')
plt.show()

# 东道主夺冠概率

index = hist_worldcup['HostWinner'].value_counts().index.tolist()
value = hist_worldcup['HostWinner'].value_counts().values.tolist()

palette = ['blue', 'yellow']

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

sns.countplot(ax=ax[0], x=hist_worldcup['HostWinner'], palette=palette, linewidth=2.5, edgecolor=".2")
ax[0].set_title('Champion Number', size=20, weight='bold')
ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False, labelsize=14)
for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15)

plt.pie(value, labels=index, autopct='%.0f%%', colors=['blue', 'yellow'],
        wedgeprops={"edgecolor": "0", 'linewidth': 2.5,
                    'antialiased': True}, startangle=90, textprops={'fontsize': 20})
ax[1].set_title('Champion Probability', size=20, weight='bold')
plt.show()



