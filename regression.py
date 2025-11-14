import statsmodels.api as sm
import matplotlib.pyplot as plt 

def regression(df,mesured,real,parameter, x_label, y_label, standard):
    x = df[f'{mesured}']
    y = df[f'{real}']
    X = sm.add_constant(x)
    model = sm.OLS(y,X).fit()
    m = model.params[X.columns[1]]
    q = model.params['const']
    R = model.rsquared
    y_pred = model.predict(X)
    sorted_indices = x.argsort()
    x_sorted = x.iloc[sorted_indices]
    y_sorted = y.iloc[sorted_indices]
    y_pred_sorted = y_pred.iloc[sorted_indices]



    plt.figure(figsize=(6, 6))
    plt.scatter(x_sorted, y_sorted, color='red', marker='X')
    plt.plot(x_sorted, m * x_sorted + q, color='k', label=f'y = {m:.5f}x + {q:.5f} \n' r'$R^{2}$' f'= {R}', linewidth=0.75, linestyle='--')
    plt.title(parameter)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    standardLabel = [idx[:] for idx in standard.index]
    for i, txt in enumerate(standardLabel):
        plt.text(x.iloc[i], y.iloc[i]-0.5, txt)
    plt.tight_layout()
    plt.show()
    return m, q