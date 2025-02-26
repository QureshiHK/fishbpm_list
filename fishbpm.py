from os import listdir, walk
import pandas as pd
from statistics import fmean
from csv import writer

#filepath = 'C:/Users/hkqur/Documents/python_A/fishbpm/'
filepath = input('input full directory path here, remember to end directory in /')


directory_files = listdir(filepath)
directory_files = [b for b in directory_files if b.endswith('.csv') is True]
directory_files

with open(filepath+'fishbpm/fishbpm.csv', 'w', newline='') as csvfile:
    writer_object = writer(csvfile)
    writer_object.writerow(['filename','bpm'])
    
    for a in directory_files:
        if filepath.endswith('/') is True:
            fish_df = pd.read_csv(filepath+a)
        else:    
            fish_df = pd.read_csv(filepath+'/'+a)
        frametimelist = fish_df['Unnamed: 2'].tolist()
        print(frametimelist)
        fishbpm = ((fish_df.iloc[len(fish_df)-1,1]-fish_df.iloc[0,1])*fmean(frametimelist[1:]))/60
        #print(fishbpm)
        
    
        writer_object.writerow([a,fishbpm])
        