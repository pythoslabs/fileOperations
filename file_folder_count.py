import os 

def count_files(DIR):
    return len(os.listdir(Path(DIR)))
    
#Usage:
#nfiles = count_files(FOLDER_PATH)

