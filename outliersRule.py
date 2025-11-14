import pandas as pd 
import numpy as np
import re

def outliers_rule(df, out_dD, out_d18O, out_d17O):
    
    global removed_outlier
    remove = None
    while True:
        if remove is None:
            remove = input('''📝 Which outliers do you want to remove?
                  [A] All the detected outliers
                  [B] Select outliers
                  [C] None
            ''').strip().upper()
            if remove not in ['A', 'B', 'C']:
                print('''❌  Invalid input. Please enter A, B, or C! ❌ ''')
                remove = None
                continue
        confirm = input('''Are you sure? 🤔
              [A] Yes
              [B] No
              ''').strip().upper()
        if confirm == 'B':
            remove = None
            continue
        elif confirm not in ['A', 'B']:
            print(f'''❌  Invalid input. Please enter A or B! ❌ ''')
            continue
        elif confirm == 'A':
            if remove == 'A':
                for l in out_dD:
                    df.loc[df['Line'] == l, 'd(D_H)Mean'] = np.nan
                for l in out_d18O:
                    df.loc[df['Line'] == l, 'd(18_16)Mean'] = np.nan
                if 'd(17_16)Mean' in df.columns :
                   for l in out_d17O:
                    df.loc[df['Line'] == l, 'd(17_16)Mean'] = np.nan
                print('✅ All the identified outliers have been delated!')
                print(f'• {out_d18O} outliers have been delated for oxygen-18;')
                print(f'• {out_dD} outliers have been delated for hydrogen.')
                if 'd(17_16)Mean' in df.columns:
                  max_length = max(len(out_d18O), len(out_dD),len(out_d17O))
                else:
                  max_length = max(len(out_d18O), len(out_dD))
                out_d18O_padded = out_d18O + [np.nan] * (max_length - len(out_d18O))
                out_dD_padded = out_dD + [np.nan] * (max_length - len(out_dD))
                if 'd(17_16)Mean' in df.columns:
                  out_d17O_padded = out_d17O + [np.nan] * (max_length - len(out_d17O))
                  removed_outlier = pd.DataFrame({
                          'Removed outlier oxygen-18': out_d18O_padded,
                          'Removed outlier oxygen-17': out_d17O_padded,
                          'Removed outlier hydrogen': out_dD_padded})
                  print(f'• {out_d17O} outliers have been delated for oxygen-17;')
                else:
                    removed_outlier = pd.DataFrame({
                          'Removed outlier oxygen-18': out_d18O_padded,
                          'Removed outlier hydrogen': out_dD_padded})
                break
            elif remove == 'C':
              print('✅ No outliers have been delated! ')
              if 'd(17_16)Mean' in df.columns:
                removed_outlier = pd.DataFrame({ 'Removed outlier oxygen-18': [], 'Removed outlier hydrogen': [], 'Removed outlier oxygen-17': []})
              else:
                removed_outlier = pd.DataFrame({ 'Removed outlier oxygen-18': [], 'Removed outlier hydrogen': []})
              break
            elif remove == 'B':
                while True:
                    out_d18O_to_be_removed = input("📝 Enter outlier line numbers (comma-separated) for oxygen-18: ")
                    out_d18O_to_be_removed = re.findall(r'\d+', out_d18O_to_be_removed)
                    print(f'You are going to remove the following outlier: {out_d18O_to_be_removed}')
                    check_O = input('''Are you sure? 🤔
                    [A] Yes
                    [B] No
                    ''').strip().upper()
                    if check_O not in ['A', 'B']:
                        print(f'''❌  Invalid input. Please enter A or B! ❌ ''')
                        continue
                    if check_O == 'A':
                        out_d18O_to_be_removed = [int(x) for x in out_d18O_to_be_removed]
                        break
                    elif check_O == 'B':
                      continue
                    break
                while True:
                    out_dD_to_be_removed = input("📝 Enter outlier line numbers (comma-separated) for hydrogen: ")
                    out_dD_to_be_removed = re.findall(r'\d+', out_dD_to_be_removed)
                    print(f'You are going to remove the following outlier: {out_dD_to_be_removed}')
                    check_D = input('''Are you sure? You are going to remove
                    [A] Yes
                    [B] No
                    ''').strip().upper()
                    if check_D not in ['A', 'B']:
                        print(f'''❌ Invalid input. Please enter A or B! ❌
                        ''')
                        continue
                    if check_D == 'A':
                        out_dD_to_be_removed = [int(x) for x in out_dD_to_be_removed]
                        break
                    else:
                        print("Please confirm your selection again.")
                if 'd(17_16)Mean' in df:
                  while True:
                      out_d17O_to_be_removed = input("📝 Enter outlier line numbers (comma-separated) for oxygen-17: ")
                      out_d17O_to_be_removed = re.findall(r'\d+', out_d17O_to_be_removed)
                      print(f'You are going to remove the following outlier: {out_d17O_to_be_removed}')
                      check_17O = input('''Are you sure? You are going to remove
                      [A] Yes
                      [B] No
                      ''').strip().upper()
                      if check_17O not in ['A', 'B']:
                          print(f'''❌ Invalid input. Please enter A or B! ❌
                          ''')
                          continue
                      if check_17O == 'A':
                          out_d17O_to_be_removed = [int(x) for x in out_d17O_to_be_removed]
                          break
                      else:
                          print("Please confirm your selection again.")
            for l in out_dD_to_be_removed:
                df.loc[df['Line'] == l, 'd(D_H)Mean'] = np.nan
            for l in out_d18O_to_be_removed:
                df.loc[df['Line'] == l, 'd(18_16)Mean'] = np.nan
            if 'd(17_16)Mean' in df:
                for l in out_d17O_to_be_removed:
                  df.loc[df['Line'] == l, 'd(17_16)Mean'] = np.nan
            print(f'✅ For oxygen-18 the following outliers have been removed: {out_d18O_to_be_removed}')
            print(f'✅ For hydrogen the following outliers have been removed: {out_dD_to_be_removed}')
            if 'd(17_16)Mean' in df:
              print(f'✅ For oxygen-17 the following outliers have been removed: {out_d17O_to_be_removed}')
              max_length = max(len(out_d18O_to_be_removed), len(out_dD_to_be_removed), len(out_d17O_to_be_removed))
              out_d18O_padded = out_d18O_to_be_removed + [np.nan] * (max_length - len(out_d18O_to_be_removed))
              out_dD_padded = out_dD_to_be_removed + [np.nan] * (max_length - len(out_dD_to_be_removed))
              out_d17O_padded = out_d17O_to_be_removed + [np.nan] * (max_length - len(out_d17O_to_be_removed))
            else:
              max_length = max(len(out_d18O_to_be_removed), len(out_dD_to_be_removed))
              out_d18O_padded = out_d18O_to_be_removed + [np.nan] * (max_length - len(out_d18O_to_be_removed))
              out_dD_padded = out_dD_to_be_removed + [np.nan] * (max_length - len(out_dD_to_be_removed))

            if 'd(17_16)Mean' in df.columns:
              removed_outlier = pd.DataFrame({
                      'Removed outlier oxygen-18': out_d18O_padded,
                      'Removed outlier oxygen-17': out_d17O_padded,
                      'Removed outlier hydrogen': out_dD_padded})
            else:
                removed_outlier = pd.DataFrame({
                      'Removed outlier oxygen-18': out_d18O_padded,
                      'Removed outlier hydrogen': out_dD_padded})
            break
    return removed_outlier