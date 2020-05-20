# unix-file-modes.py
# A quick and dirty script to build a csv of all possible *nix file permission modes
import csv

csv_list = [['mode_hr', 'mode_num', 'mode_oct', 'mode_hex', 'mode_hex_minus_prefix']]
mode_start = [0, 1, 2, 4]
for i in mode_start:
    for j in range(0,8):
        for k in range(0,8):
            for l in range(0,8):
                mode_oct = str(0) + str(i) + str(j) + str(k) + str(l)
                mode_hr = ['-','-','-']
                for m in range(2, len(mode_oct)):
                    mode_index = m - 2
                    if mode_oct[m] == '0':
                        perms = '---'
                        mode_hr[mode_index] = perms
                    elif mode_oct[m] == '1':
                        perms = '--x'
                        mode_hr[mode_index] = perms
                    elif mode_oct[m] == '2':
                        perms = '-w-'
                        mode_hr[mode_index] = perms
                    elif mode_oct[m] == '3':
                        perms = '-wx'
                        mode_hr[mode_index] = perms
                    elif mode_oct[m] == '4':
                        perms = '-r-'
                        mode_hr[mode_index] = perms
                    elif mode_oct[m] == '5':
                        perms = 'r-x'
                        mode_hr[mode_index] = perms
                    elif mode_oct[m] == '6':
                        perms = 'rw-'
                        mode_hr[mode_index] = perms
                    elif mode_oct[m] == '7':
                        perms = 'rwx'
                        mode_hr[mode_index] = perms
                mode_hr = ''.join(mode_hr)
                mode_hr = list(mode_hr)
                if mode_oct[1] == '1':
                    mode_hr[8] = 't'
                if mode_oct[1] == '2':
                    mode_hr[5] = 's'
                if mode_oct[1] == '4':
                    mode_hr[2] = 's'
                mode_hr = ''.join(mode_hr)
                mode_num = mode_oct[1:]
                mode_hex = hex(int(mode_num, 8))
                mode_hex_minus_prefix = str(mode_hex)[2:]

                entry = [mode_hr, mode_num, mode_oct, mode_hex, mode_hex_minus_prefix]
                csv_list.append(entry)
try:
    with open('unix_file_permissions.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_list)
    print('File \'unix_file_permissions.csv\' written.')
except:
    print("[ERROR] Could not write csv.")
