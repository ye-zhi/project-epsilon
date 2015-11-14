import numpy as np
import pandas as pd

project_location="../../"
data_location=project_location+"data/ds005/"

"""load and combine 3 behavior datas from 3 runs"""
def load_behav_txt(subject_number):

	#load texts
	behav1=np.loadtxt(data_location+'sub00%s/behav/task001_run001/behavdata.txt'%(subject_number),skiprows=1)
	behav2=np.loadtxt(data_location+'sub00%s/behav/task001_run002/behavdata.txt'%(subject_number),skiprows=1)
	behav3=np.loadtxt(data_location+'sub00%s/behav/task001_run003/behavdata.txt'%(subject_number),skiprows=1)
	
	#concatenate them to be 1
	behav_total_run=np.concatenate((behav1,behav2,behav3),axis=0)

	#delete the rows that contain -1 in respcat (these are errors in experiment so we should take them out
	behav_total_run=np.delete(behav_total_run, np.where(behav_total_run[:,5]==-1),axis=0)		
		
	print('your behav_total_run is ready to use!')

	return behav_total_run

"""load in pandas data frame"""
def load_in_dataframe(subject_number):


	#convert 3 behavior datas in 1 subject into data frames.
	run1 = pd.read_table(data_location+'sub00%s/behav/task001_run001/behavdata.txt'%(subject_number))
	run2 = pd.read_table(data_location+'sub00%s/behav/task001_run002/behavdata.txt'%(subject_number))
	run3 = pd.read_table(data_location+'sub00%s/behav/task001_run003/behavdata.txt'%(subject_number))

	#append all the runs in one pandas data frame
	r=run1.append(run2)
	run_total=r.append(run3) 
	
	return run_total
	