#%% Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from matplotlib import cm, colors

#%% Data Aquisition
path = os.path.join(os.getcwd(), r"LiteratureData_20220809.xlsx")
df = pd.read_excel(path, sheet_name='MTC Comparison').dropna(subset=['Fit'])#,inplace=False
df["Paper"] = df['Year'].map(str) + ' ' + df['Author'].map(str)
#%% Diffusivity  Vs Temperatures, groupby Papers

Paperlist3=[];Paperlist2=[];Paperlist1=[];Paperlist=[]
for i in range(len(set(df["Paper"]))): 
    dfbyAuthor = df[(df["Paper"] == sorted(list(df["Paper"].unique()))[i])]
    if len(list(set(dfbyAuthor['Temp']))) >= 3:
        Paperlist3.append(list(dfbyAuthor['Paper'])[0])
    elif len(list(set(dfbyAuthor['Temp']))) == 2:
        Paperlist2.append(list(dfbyAuthor['Paper'])[0])
    else:
        Paperlist1.append(list(dfbyAuthor['Paper'])[0])
Paperlist = sorted(Paperlist3) + sorted(Paperlist2) + sorted(Paperlist1) 
#% Plot

colors = ['indianred', 'darkred',     'tomato',    'coral',      'sienna', 
          'chocolate', 'saddlebrown', 'peru',      'darkorange', 'goldenrod',
          'olive',     'yellow',      'olivedrab', 'chartreuse', 'forestgreen',
          'darkgreen', 'seagreen',    'teal',      'steelblue',  'royalblue',
          'midnightblue', 'navy', 'blue', 'indigo', 'darkorchid', 'purple',
          'magenta', 'deeppink', 'crimson', 'salmon', 'darkkhaki', 'springgreen',
          'dodgerblue', 'hotpink', 'aqua', 'cyan', 'gold', 'darkgreen']
colors += colors; colors += colors

fig, ax = plt.subplots(figsize=(6, 5), squeeze=True, dpi = 300)
for i in range(len(set(df["Paper"]))):
    print("Plotting for paper:", Paperlist[i] )
    dfbyAuthor = df[(df["Paper"] == Paperlist[i])].drop_duplicates(subset="Temp", keep='first', inplace=False, ignore_index=False)
    Deff = np.array(dfbyAuthor["Diff_m"]) *1E-3
    Temp = np.array(dfbyAuthor["Temp"])
    
    
    if len(Temp) >= 3:
        mark  = "o"
        lstyl = 'dashed'
        alf   = 0.5
    elif len(Temp) == 2:
        mark  = "s"
        lstyl = 'dashdot'
        alf   = 0.6
    else:
        mark  = "+"
        lstyl = 'dotted'
        alf   = 0.8
        
    ax.scatter(Temp, Deff, s=30, marker=mark, linewidth=1, label=Paperlist[i], 
               c=colors[i], alpha=alf, edgecolor=colors[i])
    
    if len(Temp) >= 2:
        a,b = np.polyfit(Temp.tolist(), Deff.tolist(), 1)
        tl =  a*np.arange(20,90) + b
        plt.plot(np.arange(20,90), tl, c=colors[i], 
                 linestyle=lstyl ,linewidth=0.5,  alpha=0.2)
    else: pass
    
plt.ylabel('Diffusivity (m$^{2}$/s)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
plt.yscale("log");plt.grid(True)
plt.legend(bbox_to_anchor=(1.25, 1.0), fontsize=5)
plt.ylim((20,90)); plt.ylim((1E-8,1E-5)); plt.tight_layout(); #plt.show()
plt.savefig("Deff_vs_Temp.png", dpi=300,pad_inches=0.01, format='png')
#%% Diffusivity  Vs Temperatures, groupby Variety

grp_Variety = df.groupby('Variety')
    
colors_dict = { "Thomson":"indianred",
               "Ruby":"darkred",
               "Emerald":"tomato",
               "Delight":"coral",
               "Rodi":"sienna",
               "Unreported":"black",
               "Flame":"saddlebrown",
               "Muscatel":"peru",
               "Italia":"darkorange",
               "Aledo":"goldenrod",
               "Nevado":"olive",
               "Chasselas":"yellow",
               "Red":"olivedrab",
               "Tunisian":"chartreuse",
               "Seeded":"forestgreen",
               "Perlette":"darkgreen",
               "Black":"seagreen",
               "Monukka ":"teal",
               "Monukka":"steelblue",
               "Globe":"royalblue",
               "Sugraone":"midnightblue",
               "Tempranillo":"navy",
               "Asgari":"blue",
               "Crimson":"indigo",
               "Centennial":"darkorchid",}

markers_dict = { "Thomson":"x",
               "Ruby":"o",
               "Emerald":"o",
               "Delight":"o",
               "Rodi":"o",
               "Unreported":"o",
               "Flame":"o",
               "Muscatel":"o",
               "Italia":"o",
               "Aledo":"o",
               "Nevado":"o",
               "Chasselas":"o",
               "Red":"o",
               "Tunisian":"o",
               "Seeded":"o",
               "Perlette":"o",
               "Black":"o",
               "Monukka ":"o",
               "Monukka":"o",
               "Globe":"o",
               "Sugraone":"o",
               "Tempranillo":"o",
               "Asgari":"o",
               "Crimson":"o",
               "Centennial":"o",}


fig, ax = plt.subplots(figsize=(7, 5), squeeze=True, dpi = 300)
for name, group in grp_Variety:
    ax.scatter(group['Temp'], group['Diff_m']*1E-3, 
               marker = markers_dict[str(name)],  
               s = 30, label=name,
               color = colors_dict[str(name)], 
               alpha=0.5, 
               edgecolor=colors_dict[str(name)])
    
plt.ylabel('Diffusivity (m$^{2}$/s)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
plt.yscale("log");plt.grid(True)
plt.legend(bbox_to_anchor=(1.25, 1.0), fontsize=5)
plt.ylim((20,90)); plt.ylim((1E-8,1E-5)); plt.tight_layout(); #plt.show()
plt.savefig("Deff_vs_Temp_byVariety.png", dpi=300,pad_inches=0.0051, format='png')
#%% Diffusivity  Vs Temperatures, groupby Pretreatments

grp_Pretreatment = df.groupby('Pretreatment')
    
colors_dict = {"Chemical" : "steelblue" ,
               "Untreated": "tomato",
               "Chemical + Microwave": "darkgreen",
               "Microwave": "crimson",
               "Physical": "red",
               "Ohmic": "aqua",
               "Electric": "darkorange",
               "Hot Air": "navy",
               "Plasma": "coral",
               "Freezing": "gold",
               "Cryogenic": "peru" }

markers_dict = {"Chemical" : "o" ,
               "Untreated": "x",
               "Chemical + Microwave": "s",
               "Microwave": "s",
               "Physical": "s",
               "Ohmic": "s",
               "Electric": "s",
               "Hot Air": "s",
               "Plasma": "s",
               "Freezing": "s",
               "Cryogenic": "s" }


fig, ax = plt.subplots(figsize=(7, 5), squeeze=True, dpi = 300)
for name, group in grp_Pretreatment:
    ax.scatter(group['Temp'], group['Diff_m']*1E-3, 
               marker = markers_dict[str(name)],  
               s = 30, label=name,
               color = colors_dict[str(name)], 
               alpha=0.5, 
               edgecolor=colors_dict[str(name)])
    
plt.ylabel('Diffusivity (m$^{2}$/s)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
plt.yscale("log");plt.grid(True)
plt.legend(bbox_to_anchor=(1.25, 1.0), fontsize=5)
plt.ylim((20,90)); plt.ylim((1E-8,1E-5)); plt.tight_layout(); #plt.show()
plt.savefig("Deff_vs_Temp_byPretreatment.png", dpi=300,pad_inches=0.005, format='png')

#%% Diffusivity  Vs Temperatures, groupby Pretreatments Temperatures
pTemp = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable') & (df['Pretreatment'] == 'Chemical')]['P_temp']#.dropna()
Temp  = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable') & (df['Pretreatment'] == 'Chemical')]['Temp']#.dropna()
Deff  = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable') & (df['Pretreatment'] == 'Chemical')]['Diff_m']#.dropna()

fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(Temp,Deff*1E-3, marker='o', s = 50, c= pTemp, cmap = 'seismic',)
plt.ylabel('Diffusivity (m$^{2}$/s)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
my_norm = colors.Normalize(vmin=pTemp.min(), vmax=pTemp.max())
fig.colorbar(cm.ScalarMappable(norm=my_norm, cmap='seismic'), 
             orientation="vertical", label='Pretreatment Temperature ($^{o}$C)')
plt.yscale("log");plt.grid(True)
plt.legend(bbox_to_anchor=(1.25, 1.0), fontsize=5)
plt.xlim((20,90)); plt.ylim((1E-8,1E-5)); plt.tight_layout(); #plt.show()
plt.savefig("Deff_vs_Temp_byPreTemp.png", dpi=300,pad_inches=0.005, format='png')

#%% Diffusivity  Vs Temperatures, groupby Pretreatments Time
pTime = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable') & (df['Pretreatment'] == 'Chemical')]['P_time']#.dropna()
Temp  = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable') & (df['Pretreatment'] == 'Chemical')]['Temp']#.dropna()
Deff  = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable') & (df['Pretreatment'] == 'Chemical')]['Diff_m']#.dropna()

fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(Temp,Deff*1E-3, marker='o', s = 50, c= pTime, cmap = 'seismic',)
plt.ylabel('Diffusivity (m$^{2}$/s)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
my_norm = colors.Normalize(vmin=pTemp.min(), vmax=pTemp.max())
fig.colorbar(cm.ScalarMappable(norm=my_norm, cmap='seismic'), 
             orientation="vertical", label='Pretreatment Time (s)')
plt.yscale("log");plt.grid(True)
plt.legend(bbox_to_anchor=(1.25, 1.0), fontsize=5)
plt.xlim((20,90)); plt.ylim((1E-8,1E-5)); plt.tight_layout(); #plt.show()
plt.savefig("Deff_vs_Temp_byPreTime.png", dpi=300,pad_inches=0.005, format='png')

#%% Diffusivity  Vs Temperatures, groupby Techniques
grp_Technique = df.groupby('Technique')

colors_dict = {'MicroWave'        : 'red',
          'Convective'            : 'limegreen',
          'Convective + Microwave': 'maroon',
          'Fluidized bed'         : 'blue',
          'Open Sun'              : 'orangered',
          'Shade'                 : 'brown',
          'Dark'                  : 'black',}

markers_dict = {'MicroWave'       : 'o',
          'Convective'            : 'o',
          'Convective + Microwave': 'o',
          'Fluidized bed'         : 'o',
          'Open Sun'              : 'x',
          'Shade'                 : 'x',
          'Dark'                  : 'x',}

fig, ax = plt.subplots(figsize=(7, 5), squeeze=True, dpi = 300)
for name, group in grp_Technique:
    ax.scatter(group['Temp'], group['Diff_m']*1E-3, 
               marker = markers_dict[str(name)],  
               s = 30, label=name,
               color = colors_dict[str(name)], 
               alpha=0.5, 
               edgecolor=colors_dict[str(name)])
    
plt.ylabel('Diffusivity (m$^{2}$/s)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
plt.yscale("log");plt.grid(True)
plt.legend(bbox_to_anchor=(1.25, 1.0), fontsize=5)
plt.ylim((20,90)); plt.ylim((1E-8,1E-5)); plt.tight_layout(); #plt.show()
plt.savefig("Deff_vs_Temp_byTechnique.png", dpi=300,pad_inches=0.005, format='png')

#%% MassTranCoef Vs Velocity    , groupby Papers

Paperlist3=[];Paperlist2=[];Paperlist1=[];Paperlist=[]

for i in range(len(df["Paper"].unique())): 
    dfbyAuthor = df[(df["Paper"] == sorted(list(df["Paper"].unique()))[i])]
    if len(list(dfbyAuthor['Vel'].unique())) >= 3:
        Paperlist3.append(list(dfbyAuthor['Paper'])[0])
    elif len(list(dfbyAuthor['Vel'].unique())) == 2:
        Paperlist2.append(list(dfbyAuthor['Paper'])[0])
    else:
        Paperlist1.append(list(dfbyAuthor['Paper'])[0])
Paperlist = sorted(Paperlist3) + sorted(Paperlist2) + sorted(Paperlist1) 
#% Plot

colors = ['indianred', 'darkred',     'tomato',    'coral',      'sienna', 
          'chocolate', 'saddlebrown', 'peru',      'darkorange', 'goldenrod',
          'olive',     'yellow',      'olivedrab', 'chartreuse', 'forestgreen',
          'darkgreen', 'seagreen',    'teal',      'steelblue',  'royalblue',
          'midnightblue', 'navy', 'blue', 'indigo', 'darkorchid', 'purple',
          'magenta', 'deeppink', 'crimson', 'salmon', 'darkkhaki', 'springgreen',
          'dodgerblue', 'hotpink', 'aqua', 'cyan', 'gold', 'darkgreen']
colors += colors; colors += colors

fig, ax = plt.subplots(figsize=(6, 5), squeeze=True, dpi = 300)
for i in range(len(set(df["Paper"]))):
    print("Plotting for paper:", Paperlist[i] )
    dfbyAuthor = df[(df["Paper"] == Paperlist[i])]#.drop_duplicates(subset="Vel", keep='first', inplace=False, ignore_index=False)
    kg   = np.array(dfbyAuthor["kg_m"]) * 1E-9
    Vel  = np.array(dfbyAuthor["Vel"])
    
    
    if i < 25:
        mark  = "o"
        lstyl = 'dashed'
        alf   = 0.5
    elif (i > 24) & (i < 42):
        mark  = "s"
        lstyl = 'dashdot'
        alf   = 0.6
    else:
        mark  = "+"
        lstyl = 'dotted'
        alf   = 0.8
        
        
    ax.scatter(Vel, kg, s=30, marker=mark, linewidth=1, label=Paperlist[i], 
               c=colors[i], alpha=alf, edgecolor=colors[i])
    
    if len(Vel) >= 3:
        a,b = np.polyfit(Vel.tolist(), kg.tolist(), 1)
        tl  =  a*np.arange(0,15) + b
        # tl =  a*np.arange(0,15)**b + c
        #tl =  a*np.arange(0,15)**2 +  b*np.arange(0,15) + c
        plt.plot(np.arange(0,15), tl, c=colors[i], 
                  linestyle=lstyl ,linewidth=1,  alpha=0.2)
    else: pass
    
plt.ylabel('kg (kmols / m$^{2}$-Pa-s)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Velocity (m/s)', fontsize=15); plt.xticks(fontsize=10)
plt.yscale("log");plt.grid(True)
plt.legend(bbox_to_anchor=(1.25, 1.0), fontsize=5)
plt.xlim((0,10)); plt.ylim((1E-9,1E-5)); 
plt.tight_layout(); #plt.show()
plt.savefig("kg_vs_Vel.png", dpi=300,pad_inches=0.01, format='png')

#%% MassTranCoef Vs Velocity    , groupby Velocity
df3 = pd.DataFrame(); df2 = pd.DataFrame(); df1 = pd.DataFrame()
Paperlist3=[];Paperlist2=[];Paperlist1=[];Paperlist=[]

for i in range(len(df["Paper"].unique())): 
    dfbyAuthor = df[(df["Paper"] == sorted(list(df["Paper"].unique()))[i])]
    if len(list(dfbyAuthor['Vel'].unique())) >= 3:
        Paperlist3.append(list(dfbyAuthor['Paper'])[0])
    elif len(list(dfbyAuthor['Vel'].unique())) == 2:
        Paperlist2.append(list(dfbyAuthor['Paper'])[0])
    else:
        Paperlist1.append(list(dfbyAuthor['Paper'])[0])
Paperlist = sorted(Paperlist3) + sorted(Paperlist2) + sorted(Paperlist1) 

for i in range(len(df["Paper"].unique())):
    print("Plotting for paper:", Paperlist[i] )
    dfbyAuthor = df[(df["Paper"] == Paperlist[i])]
    for i in dfbyAuthor['Temp'].unique():
        dfVel  = dfbyAuthor[df['Temp'] == i]
        if len(dfVel['Vel'].unique()) >= 3:
            df3 = df3.append(dfVel)
        elif len(dfVel['Vel'].unique()) == 2:
            df2 = df2.append(dfVel)   
        else:
            df1 = df1.append(dfVel)
df3.to_excel('Vel3.xlsx')
df2.to_excel('Vel2.xlsx')
df1.to_excel('Vel1.xlsx')
#%% MassTranCoef Vs Velocity    , groupby Individual Papers
df["VelUnique"] = df['Year'].map(str) + ' ' + df['Author'].map(str) + ' ' + df['Vel'].map(str) + ' ' + df['Temp'].map(str)
Paperlist3=[];Paperlist2=[];Paperlist1=[];Paperlist=[]

for i in range(len(df["Paper"].unique())): 
    dfbyAuthor = df[(df["Paper"] == sorted(list(df["Paper"].unique()))[i])]
    if len(list(dfbyAuthor['Vel'].unique())) >= 3:
        Paperlist3.append(list(dfbyAuthor['Paper'])[0])
    elif len(list(dfbyAuthor['Vel'].unique())) == 2:
        Paperlist2.append(list(dfbyAuthor['Paper'])[0])
    else:
        Paperlist1.append(list(dfbyAuthor['Paper'])[0])
Paperlist = sorted(Paperlist3) + sorted(Paperlist2) + sorted(Paperlist1)

for i in range(len(df["Paper"].unique())):
    print(Paperlist[i])
    dfbyAuthor = df[(df["Paper"] == Paperlist[i])].drop_duplicates(subset="Vel", keep='first', inplace=False, ignore_index=False)
    kg   = np.array(dfbyAuthor["kg_m"]) * 1E-9
    Vel  = np.array(dfbyAuthor["Vel"])
    
    plt.figure(figsize=(6,4))
    plt.scatter(Vel, kg, s=60, marker='o', linewidth=1,# label=Paperlist[i], 
               c='k', alpha=0.2, edgecolor='k')
    
    if len(Vel) >= 2:
        a,b = np.polyfit(Vel.tolist(), kg.tolist(), 1)
        #tl =  a*np.arange(0,15)**b + c
        #tl =  a*np.arange(0,15)**2 +  b*np.arange(0,15) + c
        #tl =  a*np.arange(0,15) + b +c*0
        tl  =  a*np.arange(0,15) + b
        plt.plot(np.arange(0,15), tl, c='k', 
                  linestyle='-' ,linewidth=1,  alpha=0.2)
    else: pass
    plt.ylabel('kg (mols/m$^{2}$ s Pa)', fontsize=15); plt.yticks(fontsize=10)
    plt.xlabel('Velocity (m/s)', fontsize=15); plt.xticks(fontsize=10)
    plt.yscale("log");plt.grid(True)
    # plt.legend(fontsize=10)
    plt.xlim((0,10)); plt.ylim((1E-9,1E-5));
    plt.title(f'{Paperlist[i]}')
    plt.tight_layout(); #plt.show()
    plt.savefig(f'kgPlot_{Paperlist[i][:9]}.png', dpi=100,pad_inches=0.01, format='png')

#%% Process time Vs Temperatures, groupby Technique
grp_Techique = df.groupby('Technique')

colors = {'MicroWave'             : 'red',
          'Convective'            : 'limegreen',
          'Convective + Microwave': 'maroon',
          'Fluidized bed'         : 'blue',
          'Open Sun'              : 'orangered',
          'Shade'                 : 'brown',
          'Dark'                  : 'black',}
   

fig, ax = plt.subplots(figsize=(6, 5), dpi=300)
for name, group in grp_Techique:
    ax.scatter(group['Temp'], group['hours'], marker='o', s = 50, label=name,
               color = colors[str(name)], alpha=0.7, edgecolor=colors[str(name)])
    
plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
plt.legend(fontsize=10); plt.grid(True); plt.tight_layout()
plt.savefig("hours_vs_Temp_by_Technique.png", dpi=300,pad_inches=0.005, format='png')

#%% Process time Vs Temperatures, groupby Pretreatments
groups = df.groupby('Pretreatment')

colors = ['steelblue', 'tomato', 'darkgreen',  'crimson', 'red',  
          'aqua', 'darkorange',  'navy', 'coral', 'gold', 'peru'  ]


fig, ax = plt.subplots(figsize=(6, 5), dpi=300)
for (name, group), color in zip(groups, colors):
    ax.scatter(group['Temp'], group['hours'], marker='o', s = 50, label=name,
               color = color, alpha=0.8, edgecolor=color)
plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
plt.legend(fontsize=10); plt.grid(True);plt.tight_layout()
plt.savefig("hours_vs_Temp_by_Pretreatments.png", dpi=300,pad_inches=0.005, format='png')
#%% Process time Vs Temperatures, groupby Pretreatments Temperatures
hours = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable')]['hours']#.dropna()
pTemp = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable')]['P_temp']#.dropna()
Temp  = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable')]['Temp']#.dropna()

fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(Temp, hours, marker='o', s = 50, c= pTemp, cmap = 'seismic',)
plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
my_norm = colors.Normalize(vmin=pTemp.min(), vmax=pTemp.max())
fig.colorbar(cm.ScalarMappable(norm=my_norm, 
                               cmap='seismic'), 
              orientation="vertical", 
              label='Pretreatment Temperature ($^{o}$C)')

plt.legend(fontsize=10); plt.grid(True); plt.tight_layout()
plt.savefig("hours_vs_Temp_by_pTemp.png", dpi=300,pad_inches=0.005, format='png')

#%% Process time Vs Temperatures, groupby Pretreatments Temperatures Subplot for Chemical only
hours = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable') & (df['Pretreatment'] == 'Chemical')]['hours']#.dropna()
pTemp = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable') & (df['Pretreatment'] == 'Chemical')]['P_temp']#.dropna()
Temp  = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable') & (df['Pretreatment'] == 'Chemical')]['Temp']#.dropna()

fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(Temp, hours, marker='o', s = 50, c= pTemp, cmap = 'seismic',)
plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
my_norm = colors.Normalize(vmin=pTemp.min(), vmax=pTemp.max())
fig.colorbar(cm.ScalarMappable(norm=my_norm, cmap='seismic'), 
             orientation="vertical", label='Pretreatment Temperature ($^{o}$C)')
plt.legend(fontsize=10); plt.grid(True);plt.tight_layout()
plt.savefig("hours_vs_Temp_by_Chemical.png", dpi=300,pad_inches=0.005, format='png')

#%% Process time Vs Temperatures, groupby Pretreatments Temperatures Subplot for Chemical Cold only
co = 50 # v
dfcc = df.loc[(df['P_temp'] != 'Untreated') & (df['P_temp'] != 'NotApplicable') & (df['Pretreatment'] == 'Chemical')]
hours = dfcc.loc[(dfcc['P_temp'] <= co) & (df['hours']<=200) & (df['Temp']<=40)]['hours']#.dropna()
pTemp = dfcc.loc[(dfcc['P_temp'] <= co) & (df['hours']<=200) & (df['Temp']<=40)]['P_temp']#.dropna()
Temp  = dfcc.loc[(dfcc['P_temp'] <= co) & (df['hours']<=200) & (df['Temp']<=40)]['Temp']#.dropna()

fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(Temp, hours, marker='o', s = 50, c= pTemp, cmap = 'seismic',)
plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
my_norm = colors.Normalize(vmin=20, vmax=50)
fig.colorbar(cm.ScalarMappable(norm=my_norm, cmap='seismic'), 
             orientation="vertical", label='Pretreatment Temperature ($^{o}$C)')
plt.legend(fontsize=10); plt.grid(True);plt.tight_layout()
plt.savefig("hours_vs_Temp_by_ChemicalCold.png", dpi=300,pad_inches=0.005, format='png')

#%% Process time Vs Temperatures, groupby Variety
groups = df.groupby('Variety')

colors = {'indianred', 'dodgerblue', 'darkred',  'aqua', 'tomato', 'darkgreen',
          'coral', 'purple', 'sienna', 'seagreen', 'chocolate', 'deeppink', 
          'saddlebrown', 'midnightblue', 'peru', 'steelblue', 'darkorange', 'teal',
          'goldenrod', 'darkgreen', 'gold', 'olive', 'yellow', 'olivedrab', 
          'chartreuse','royalblue', 'forestgreen', 'magenta', 'darkkhaki', 'salmon',
          'navy', 'hotpink', 'blue', 'springgreen', 'indigo', 'darkorchid', 'crimson',
          'cyan',}

fig, ax = plt.subplots(figsize=(7, 7), dpi=300)
for (name, group), color in zip(groups, colors):
    ax.scatter(group['Temp.'], group['hours'], marker='o', s = 50, label=name,
               color = color, alpha=0.7, edgecolor=color)
plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
# plt.legend(fontsize=15); plt.grid(True); ;plt.tight_layout()
plt.savefig("hours_vs_Temp_by_variety.png", dpi=300,pad_inches=0.005, format='png')
#%% Process time Vs Temperatures, groupby Velocity
hours = df.loc[df['Vel'] != 0.01]['hours']
Vel   = df.loc[df['Vel'] != 0.01]['Vel']
Temp  = df.loc[df['Vel'] != 0.01]['Temp']

hours_a = df.loc[df['Vel'] == 0.01]['hours']
Temp_a  = df.loc[df['Vel'] == 0.01]['Temp']
Vel_a   = df.loc[df['Vel'] == 0.01]['Vel']

fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(Temp, hours, marker='o', s = 50, c= Vel, cmap = 'seismic',)
ax.scatter(Temp_a, hours_a, marker='x', s = 50, c= Vel_a, cmap = 'seismic', label = 'Ambient')
plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
my_norm = colors.Normalize(vmin=df.Vel.min(), vmax=df.Vel.max())
fig.colorbar(cm.ScalarMappable(norm=my_norm, cmap='seismic'), 
             orientation="vertical", label='Velocity (m/s)')
plt.legend(fontsize=10); plt.grid(True);plt.tight_layout()
plt.savefig("hours_vs_Temp_by_Vel.png", dpi=300,pad_inches=0.005, format='png')

#%% Process time Vs Temperatures, groupby Velocity Subplot 40degC X 200hours
hours = df.loc[(df['Vel'] != 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['hours']
Vel   = df.loc[(df['Vel'] != 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['Vel']
Temp  = df.loc[(df['Vel'] != 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['Temp']

hours_a = df.loc[(df['Vel'] == 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['hours']
Temp_a  = df.loc[(df['Vel'] == 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['Temp']
Vel_a   = df.loc[(df['Vel'] == 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['Vel']

fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(Temp, hours, marker='o', s = 50, c= Vel, cmap = 'seismic',)
ax.scatter(Temp_a, hours_a, marker='x', s = 50, c= Vel_a, cmap = 'seismic', label = 'Ambient')

plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
plt.xlim([20, 45]); plt.ylim([0, 240])
my_norm = colors.Normalize(vmin=Vel.min(), vmax=Vel.max())
fig.colorbar(cm.ScalarMappable(norm=my_norm, cmap='seismic'), 
             orientation="vertical", label='Velocity (m/s)')
plt.legend(fontsize=10); plt.grid(True);plt.tight_layout()
plt.savefig("hours_vs_Temp_by_Vel_Zoom.png", dpi=300,pad_inches=0.005, format='png')

#%% Process time Vs Temperatures, groupby Velocity Subplot 40degC X 200hours, below Velocity 
co = 0.5 #( m/s)
hours = df.loc[(df['Vel'] != 0.01) & (df['hours']<=200) & (df['Temp']<=40) & (df['Vel'] <= co)]['hours']
Vel   = df.loc[(df['Vel'] != 0.01) & (df['hours']<=200) & (df['Temp']<=40) & (df['Vel'] <= co)]['Vel']
Temp  = df.loc[(df['Vel'] != 0.01) & (df['hours']<=200) & (df['Temp']<=40) & (df['Vel'] <= co)]['Temp']

hours_a = df.loc[(df['Vel'] == 0.01) & (df['hours']<=200) & (df['Temp']<=40) & (df['Vel'] <= co)]['hours']
Temp_a  = df.loc[(df['Vel'] == 0.01) & (df['hours']<=200) & (df['Temp']<=40) & (df['Vel'] <= co)]['Temp']
Vel_a   = df.loc[(df['Vel'] == 0.01) & (df['hours']<=200) & (df['Temp']<=40) & (df['Vel'] <= co)]['Vel']

fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(Temp, hours, marker='o', s = 50, c= Vel, cmap = 'seismic',)
ax.scatter(Temp_a, hours_a, marker='x', s = 50, c= Vel_a, cmap = 'seismic', label = 'Ambient')

plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Temperature ($^{o}$C)', fontsize=15); plt.xticks(fontsize=10)
plt.xlim([20, 45]); plt.ylim([0, 240])
my_norm = colors.Normalize(vmin=Vel.min(), vmax=Vel.max())
fig.colorbar(cm.ScalarMappable(norm=my_norm, cmap='seismic'), 
             orientation="vertical", label='Velocity (m/s)')
plt.legend(fontsize=10); plt.grid(True);plt.tight_layout()
plt.savefig("hours_vs_Temp_by_Vel_Zooml1.png", dpi=300,pad_inches=0.005, format='png')

#%% Process time Vs Velocity    , groupby Temperature

hours = df.loc[df['Vel'] != 0.01]['hours']
Vel   = df.loc[df['Vel'] != 0.01]['Vel']
Temp  = df.loc[df['Vel'] != 0.01]['Temp']

hours_a = df.loc[df['Vel'] == 0.01]['hours']
Vel_a   = df.loc[df['Vel'] == 0.01]['Vel']


fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(Vel, hours, marker='o', s = 50, c= Temp, cmap = 'seismic',)
ax.scatter(Vel_a, hours_a, marker='x', s = 50, c= Temp_a, cmap = 'seismic', label = 'Ambient')

plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Velocity (m/s)', fontsize=15); plt.xticks(fontsize=10)
plt.legend(fontsize=10); 

my_norm = colors.Normalize(vmin=10, vmax=90)
fig.colorbar(cm.ScalarMappable(norm=my_norm, cmap='seismic'), 
             orientation="vertical", label='Temperature ($^{o}$C)')

plt.grid(True);plt.tight_layout(); # plt.xscale("log"); plt.yscale("log")
plt.savefig("hours_vs_Vel_by_Temperature.png", dpi=300,pad_inches=0.005, format='png')

#%% Process time Vs Velocity    , groupby Temperature SubPlot
hours = df.loc[(df['Vel'] != 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['hours']
Vel   = df.loc[(df['Vel'] != 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['Vel']
Temp  = df.loc[(df['Vel'] != 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['Temp']

hours_a = df.loc[(df['Vel'] == 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['hours']
Temp_a  = df.loc[(df['Vel'] == 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['Temp']
Vel_a   = df.loc[(df['Vel'] == 0.01) & (df['hours']<=200) & (df['Temp']<=40)]['Vel']

fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(Vel, hours, marker='o', s = 50, c= Temp, cmap = 'seismic',)
ax.scatter(Vel_a, hours_a, marker='x', s = 50, c= Temp_a, cmap = 'seismic', label = 'Ambient')
plt.xlim([0, 2.5]); plt.ylim([0, 240])
plt.ylabel('Process Time (hours)', fontsize=15); plt.yticks(fontsize=10)
plt.xlabel('Velocity (m/s)', fontsize=15); plt.xticks(fontsize=10)
plt.legend(fontsize=10); 

my_norm = colors.Normalize(vmin=10, vmax=40)
fig.colorbar(cm.ScalarMappable(norm=my_norm, cmap='seismic'), 
             orientation="vertical", label='Temperature ($^{o}$C)')

plt.grid(True);plt.tight_layout(); # plt.xscale("log"); plt.yscale("log")

plt.savefig("hours_vs_Vel_by_Temperature_zoom.png", dpi=300,pad_inches=0.005, format='png')
#%%

