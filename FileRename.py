# ver_01

import os
import threading
import time
from tqdm import tqdm

import pandas as pd
from colorama import init, Fore, Back, Style
from tabulate import tabulate

renamed_file = 0
total_file = 0
step = 0

def count_files(path):
    number_of_files = 0
    for root, dirs, files in os.walk(path):
        number_of_files += len(files)
    return number_of_files

def file_rename(pDir_path):

    global renamed_file, total_file
    global step

    print(f'ROOT: {pDir_path}')
    print("=" * 100)

    if os.path.exists(pDir_path):
        print(f"The file '{Back.LIGHTBLACK_EX+pDir_path+Style.RESET_ALL}' exists.")
        print(f'{Fore.LIGHTWHITE_EX+Back.RED}START{Style.RESET_ALL}  ʕ㋛\'͡༼~~\'♥ \n')

        for (path, dir, files) in os.walk(pDir_path):
            file_list = []
            root_folder = []
            step += 1

            if step == 1:
                root_folder = dir
                dir_tb = tabulate(pd.DataFrame(root_folder), headers=['Folder'], showindex=False, tablefmt="pretty")
                print(dir_tb)
                print("=" * 100)

            if path == f'{pDir_path}\MVN_Link': break

            if len(files) != 0:
                print(f'{Back.LIGHTBLACK_EX}SRC PATH{Style.RESET_ALL}: {path}')
                split_path = path.split('\\')

                for filename in files:
                    full_filename = os.path.join(path, filename)
                    base = os.path.basename(full_filename)
                    ext = os.path.splitext(base)[1]

                    if ext == '.bin':
                        file_name = os.path.splitext(base)[0]  # file name
                        new_file_name = '_'.join(file_name.split('_')[2:8])
                        file_list.append(new_file_name)
                print(f'   >>> {len(file_list)} 개의 파일 존재')

                if len(split_path) == 5:  # path: # ['01_Dataset', 'FRT_Xsens', '20230720', 'p01', 'c01']
                    # dst = [pDir_path , 'MVN_Link' ,split_path[2] ,split_path[3].upper(), split_path[4].upper()]
                    dst = [pDir_path, 'MVN_Link', split_path[2], split_path[4].upper() + '_CSV']
                    dst = ('/').join(dst)
                    print(f'{Back.LIGHTBLACK_EX}DST PATH{Style.RESET_ALL}: {dst}')

                    if os.path.exists(dst):
                        index = 0
                        for (p, d, f) in os.walk(dst):
                            # print(f'    DST FILES : {f}\n')
                            print(f'   >>> {len(f)} 개의 파일 존재')

                            # -------------RENAME-------------#
                            try:
                                if len(f) != len(file_list):
                                    print(f'   >>> [ERROR] 파일 개수 일치 하지 않음')
                                    print("-" * 100)
                                    break

                                for old_name in f:
                                    ext = old_name.split('.')[1]
                                    new_name = 'MVN_' + file_list[index] + '.' + ext
                                    _src = dst + f'\{old_name}'
                                    _dst = dst + f'\{new_name}'

                                    if os.path.exists(_src):
                                        # print(f'{Fore.LIGHTWHITE_EX + Back.LIGHTRED_EX}WARNING{Style.RESET_ALL}'
                                        print(f'    '
                                               f' {Fore.BLUE + new_name + Style.RESET_ALL} is already exist.')
                                    else:
                                        os.rename(_src, _dst)
                                        time.sleep(0.05)
                                        print(f'   >>> {old_name} -> {Fore.GREEN + new_name + Style.RESET_ALL}')
                                        index += 1
                                        renamed_file += 1

                                print("-" * 100)

                            except Exception as e:
                                print(f'   >>> [ERROR] {e}')

                    else:
                        print(f'{Fore.LIGHTWHITE_EX+Back.LIGHTRED_EX}WARNING{Style.RESET_ALL} File does not exist.')
                        print("-" * 100)


        print(f'{renamed_file} 개의 파일 처리 완료\n')
        print(f' ʕ㋛\'͡༼~~\'♥  {Fore.BLACK + Back.RED}BYE{Style.RESET_ALL}')
        print("=" * 100)

    else:
        print(f"The file '{Back.LIGHTBLACK_EX+pDir_path+Style.RESET_ALL}' does not exist.")
        print(f' ʕ㋛\'͡༼~~\'♥  {Fore.BLACK+Back.RED}BYE{Style.RESET_ALL}')
        print("=" * 100)


if __name__ == "__main__":

    # root 폴더 입력
    # file_rename('01_Dataset')
    file_rename('02 Research/02 Research_rename/02_Pilot_Dataset_for_Intern')

