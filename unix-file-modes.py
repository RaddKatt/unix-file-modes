# unix-file-modes.py
# A quick and dirty script to build a csv of all possible *nix file permission modes

mode_start = [0, 1, 2, 4]
for i in mode_start:
    for j in range(0,8):
        for k in range(0,8):
            for l in range(0,8):
                mode_num = str(i) + str(j) + str(k) + str(l)
                mode_hr = ['-','-','-']
                for m in range(1, len(mode_num)):
                    mode_index = m - 1
                    if mode_num[m] == '0':
                        perms = '---'
                        mode_hr[mode_index] = perms
                    elif mode_num[m] == '1':
                        perms = '--x'
                        mode_hr[mode_index] = perms
                    elif mode_num[m] == '2':
                        perms = '-w-'
                        mode_hr[mode_index] = perms
                    elif mode_num[m] == '3':
                        perms = '-wx'
                        mode_hr[mode_index] = perms
                    elif mode_num[m] == '4':
                        perms = '-r-'
                        mode_hr[mode_index] = perms
                    elif mode_num[m] == '5':
                        perms = 'r-x'
                        mode_hr[mode_index] = perms
                    elif mode_num[m] == '6':
                        perms = 'rw-'
                        mode_hr[mode_index] = perms
                    elif mode_num[m] == '7':
                        perms = 'rwx'
                        mode_hr[mode_index] = perms
                mode_hr = ''.join(mode_hr)
                mode_hr = list(mode_hr)
                if mode_num[0] == '1':
                    mode_hr[8] = 't'
                if mode_num[0] == '2':
                    mode_hr[5] = 's'
                if mode_num[0] == '4':
                    mode_hr[2] = 's'
                mode_hr = ''.join(mode_hr)
                print(mode_num, mode_hr)
