import random
import os
import shutil
if __name__=="__main__":
    folder_path = "./2_LamaH-CE_daily/A_basins_total_upstrm/2_timeseries/daily/"
    files = os.listdir(folder_path)
    # print(files)
    random_files = random.sample(files,100)
    for file in random_files:
        src = folder_path+file
        dst = "./dataset/"
        shutil.copy(src,dst)
