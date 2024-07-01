from sklearn.model_selection import train_test_split
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import cross_validate
from sklearn.metrics import mean_absolute_error, make_scorer


path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'data','Eagg_data.xlsx')

# pandas DataFrame object
df = pd.read_excel(path)


#define x and y
y= df['DFT_Eagg'].values
x=df[['ΔnCEbulk/CN','Δr','ΔEA', 'ΔBE/CNads']].values


#Standardize X
st_x= StandardScaler()

X_train, X_test, y_train, y_test = train_test_split(x,y, train_size=0.85, shuffle=True,random_state=49)
st_xtrain= st_x.fit_transform(X_train)
st_xtest= st_x.fit_transform(X_test)

# # # Calculating the mean absolute error using 5-FoldCV
mae= make_scorer(mean_absolute_error)
kfold = 5


regressor= SVR(kernel='rbf',C=0.8,epsilon=0.09,gamma=0.1437142857142857)


regressor.fit(st_xtrain, y_train)
scores_svr = cross_validate(regressor ,st_xtrain, y_train, scoring= mae,cv = kfold,return_train_score=True)
svr_test_mae = mean_absolute_error(y_test,regressor.predict(st_xtest))


df_test= df[df['DFT_Eagg'].isin(y_test)]
index_list = []
for x in y_test:
    index_list.append(df_test.DFT_Eagg[df_test.DFT_Eagg == x].index.tolist()[0])
df_new= df_test.reindex(index_list)
df_new['regressor.predict(st_xtest)'] = regressor.predict(st_xtest)


mec = ['aqua','magenta','lime']
shapes = ['*', 'P','X','o','v','d']
colors = ['blue','red','green','orange','purple','brown']
for i, host in enumerate(['Ag','Au','Cu','Ni','Pd','Pt']):
    tempdf = df_new[df_new['Host'] == host]
    for j, dopant in enumerate(['Ag','Au','Cu','Ni','Pd','Pt']):
        z1=tempdf[tempdf['Dopant']== dopant]
        for k, ligand in  enumerate(['R-S','R-NH','Non-ligated']):
            z = z1[z1['Ligand'] == ligand]
            plt.scatter(z['DFT_Eagg'].dropna().values, z['regressor.predict(st_xtest)'], c=colors[i],marker=shapes[j],edgecolors=mec[k],label='%s Host' % host, zorder=0, s=50)
parity=np.linspace(y.min(),y.max())
plt.plot(parity,parity,color='black',zorder=0)
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), title=f'Test MAE = {svr_test_mae:.3f} eV', ncol=2, frameon=False)
plt.ylabel('$\\rm E_{agg,model} (eV)$',fontsize=22)
plt.xlabel('$\\rm E_{agg,DFT} (eV)$',fontsize=22)
plt.tight_layout()
plt.show()


