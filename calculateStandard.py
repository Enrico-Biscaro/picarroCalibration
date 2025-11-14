def calculate_standard_cal(picarro_df, std_value, regression_results):
    df = picarro_df[(picarro_df['Identifier2'].isin(['STD', 'STANDARD'])) & (picarro_df['Identifier1'] == std_value)] # Updated 2025-05-08
    columns = ['d(18_16)Mean', 'd(D_H)Mean']
    if 'd(17_16)Mean' in picarro_df.columns:
        columns.append('d(17_16)Mean')
    standard_cal = df.groupby('Analysis')[columns].mean()
    standard_cal["d18O_cal"] = standard_cal["d(18_16)Mean"] * regression_results["Slope"].iloc[0] + regression_results['Intercept'].iloc[0]
    standard_cal["dD_cal"] = standard_cal["d(D_H)Mean"] * regression_results["Slope"].iloc[1] + regression_results['Intercept'].iloc[1]
    if 'd(17_16)Mean' in columns:
        standard_cal["d17O_cal"] = standard_cal["d(17_16)Mean"] * regression_results["Slope"].iloc[2] + regression_results['Intercept'].iloc[2]
        standard_cal["D17O_cal"] = 1000000 * (np.log(standard_cal["d17O_cal"]/1000 + 1) - 0.528 * np.log(standard_cal["d18O_cal"]/1000 + 1))
    return standard_cal