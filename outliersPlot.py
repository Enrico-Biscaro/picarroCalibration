import matplotlib.pyplot as plt


def outliers_plot_stdev(df_raw, array, col, ylabel):
    if len(array) > 0:
        if col == 'd(18_16)Mean':
            print(f'🛑 Warning: For the last 3 injections, a standard deviation greater than 0.05 was found for oxygen-18! 🛑')
        elif col == 'd(D_H)Mean':
            print(f'🛑 Warning: For the last 3 injections, a standard deviation greater than 0.2 was found for hydrogen! 🛑')
        elif col == 'd(17_16)Mean':
            print(f'🛑 Warning: For the last 3 injections, a standard deviation greater than 0.05 was found for oxygen-17! 🛑')
        while True:
            user_input = input('''Do you want to see the graphs?
                [A] Yes
                [B] No
            ''').strip().upper()
            if user_input == 'A':
                confirm_input = input('''Are you sure? 🤔
                    [A] Yes
                    [B] No
                    ''').strip().upper()
                if confirm_input == 'A':
                    break
                elif confirm_input == 'B':
                    continue
                else:
                    print(f'''❌  Invalid input. Please enter A or B! ❌ ''')
            elif user_input == 'B':
              confirm_input = input('''Are you sure? 🤔
                    [A] Yes
                    [B] No
                    ''').strip().upper()
              if confirm_input == 'A':
                return
              elif confirm_input == 'B':
                continue
            else:
                print(f'''❌  Invalid input. Please enter A or B! ❌ ''')
        for analysis_value in array:
            outliers_plot = df_raw[df_raw['Analysis'] == analysis_value]
            plt.figure(figsize=(len(outliers_plot)/0.85,5))
            plt.scatter(outliers_plot['InjNr'], outliers_plot[col], marker='X', color='k')
            plt.plot(outliers_plot['InjNr'], outliers_plot[col], linestyle='--', color='k', alpha=0.25, linewidth=1.25)
            ID = outliers_plot['Identifier1'].iloc[1]
            Type = outliers_plot['Identifier2'].iloc[1]
            Vial = outliers_plot['vial'].iloc[1]
            Analysis = outliers_plot['Analysis'].iloc[1]
            plt.title(f'{ID} ({Type}) - Vial number {Vial} [{Analysis}]')
            plt.ylim(outliers_plot[col].min() - ((outliers_plot[col].max() - outliers_plot[col].min()) * 0.25),
                     outliers_plot[col].max() + ((outliers_plot[col].max() - outliers_plot[col].min()) * 0.25))
            plt.ylabel(ylabel)
            plt.xlabel('Injection number')
            plt.xlim(0,len(outliers_plot )+1)
            for i, row in outliers_plot.iterrows():
                label_line = row['Line']
                label_value = row[col]
                plt.annotate(f'{label_value} ‰ \n ({label_line})',
                             (row['InjNr'], row[col]),
                             textcoords="offset points",
                             xytext=(0, 10),
                             ha='center',
                             size=9)
            plt.show()
    else:
        if col == 'd(18_16)Mean':
            print('''✅ No outliers identified for oxygen! 🏞️ Keep going! 🚙
            ''')
        elif col == 'd(D_H)Mean':
            print('''✅ No outliers identified for hydrogen! 🏞️ Keep going! 🚙
            ''')