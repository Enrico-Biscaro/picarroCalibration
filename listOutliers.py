from detectOutliersMAD import detect_outliers_mad
import pandas as pd
import time
from datetime import datetime
import matplotlib.pyplot as plt


def list_outliers(df, df_raw, col, threshold, ylabel):
    colline = []
    col0, col1, col2, col3 = [], [], [], []
    warning_printed = False

    for i in df['Analysis'].unique():
        mad = detect_outliers_mad(df[col][df['Analysis'] == i], threshold)

        if mad.sum() > 0:
            if not warning_printed:
                if col == 'd(18_16)Mean':
                    print(f'🛑 Outliers detected for oxygen-18! 🛑')
                elif col == 'd(D_H)Mean':
                    print(f'🛑 Outliers detected for hydrogen! 🛑')
                elif col == 'd(17_16)Mean':
                    print(f'🛑 Outliers detected for oxygen-17! 🛑')
                warning_printed = True

            k = mad[mad].index[0]
            line = k + 1
            mask = df['Line'] == line

            col0.append(df.loc[mask, 'Analysis'].values[0])
            colline.append(int(df.loc[mask, 'Line'].values[0]))
            col1.append(df.loc[mask, 'Identifier1'].values[0])
            col2.append(df.loc[mask, 'Identifier2'].values[0])
            col3.append(df.loc[mask, 'InjNr'].values[0])

    if not warning_printed:
        if col == 'd(18_16)Mean':
            print('✅ No outliers identified for oxygen-18!')
        elif col == 'd(D_H)Mean':
            print('✅ No outliers identified for hydrogen!')
        elif col == 'd(17_16)Mean':
            print('✅ No outliers identified for oxygen-17!')

    list_outliers_df = pd.DataFrame({
        'Analysis': col0,
        'Identifier': col1,
        'Type': col2,
        'Injection Number': col3,
        'Line': colline
    })

    if len(list_outliers_df) > 0:
        display(list_outliers_df)
        while True:
            graph = input("Do you want to see the graphs?\n[A] Yes\n[B] No\n").strip().upper()
            if graph in ['A', 'B']:
                while True:
                    confirm = input("Are you sure?\n[A] Yes\n[B] No\n").strip().upper()
                    if confirm in ['A', 'B']:
                        if graph == 'A' and confirm == 'A':
                            for j in range(len(list_outliers_df)):
                                outliers_plot = df_raw[df_raw['Analysis'] == list_outliers_df['Analysis'].iloc[j]]
                                plt.figure(figsize=(len(outliers_plot)/0.85, 5))
                                plt.scatter(
                                    outliers_plot['InjNr'],
                                    outliers_plot[col],
                                    color=[
                                        '#C15141' if line in list_outliers_df['Line'].tolist() else 'k'
                                        for line in outliers_plot['Line']
                                    ],
                                    marker='X',
                                    alpha=0.75
                                )
                                plt.plot(
                                    outliers_plot['InjNr'],
                                    outliers_plot[col],
                                    linestyle='--',
                                    color='k',
                                    alpha=0.25,
                                    linewidth=1.25
                                )
                                plt.ylim(
                                    outliers_plot[col].min() - ((outliers_plot[col].max() - outliers_plot[col].min()) * 0.25),
                                    outliers_plot[col].max() + ((outliers_plot[col].max() - outliers_plot[col].min()) * 0.25)
                                )
                                plt.ylabel(ylabel)
                                plt.xlim(0, len(outliers_plot) + 1)
                                plt.xlabel('Injection number')
                                plt.title(f"{list_outliers_df['Identifier'][j]} ({list_outliers_df['Type'][j]}) - "
                                          f"Vial number {int(outliers_plot['vial'].iloc[-1])} "
                                          f"[{list_outliers_df['Analysis'][j]}]")
                                for i, row in outliers_plot.iterrows():
                                    label_line = row['Line']
                                    label_value = row[col]
                                    plt.annotate(
                                        f'{label_value:.3f} ‰ \n ({label_line})',
                                        (row['InjNr'], row[col]),
                                        textcoords="offset points",
                                        xytext=(0, 10),
                                        color='#C15141' if row['Line'] in list_outliers_df['Line'].tolist() else 'black',
                                        ha='center',
                                        size=9
                                    )
                                ax = plt.gca()
                                ax.grid(False)
                                ax.ticklabel_format(style='plain', axis='y')
                                ax.get_yaxis().get_offset_text().set_visible(False)
                                ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%.3f'))
                                plt.show()
                        break
                break
            else:
                print("❌ Invalid input. Please enter A or B!")

    return colline
