# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:19:08 2021

@author: evane
"""
import os
import csv
import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

#label_path= "C:/Users/ChangGun Choi/Team Project/TeamProject/SVG_Logo/Model/Label/LLD_majorityVote.csv"
label_path= "/content/ConditionalStyleGAN/data/LLD_majorityVote.csv"

labels = pd.read_csv(label_path, sep=',')
encoder = LabelEncoder()
labels['tf_cluster'] = encoder.fit_transform(labels['cluster'])

list_of_file_paths = []
class_condition_labels = []
list_of_file_paths = labels['Name'].values.tolist()    
class_condition_labels = labels['tf_cluster'].values.tolist()

mypickle = {"Filenames": list_of_file_paths, "Labels": class_condition_labels}
# Pickle path = '../data/mypickle.pickle'
with open('C:/Users/ChangGun Choi/Team Project/StyleGAN Logo/ConditionalStyleGAN/data/mypickle.pickle', 'wb') as handle:
    pickle.dump(mypickle, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
# The script is run from the terminal and 
# takes the paths to your images and the path of your TF-record directory as flags
# python dataset_tool.py create_from_images dataset/logos ../data/my_images 1

# python C:/Users/evane/Documents/GitHub/ConditionalStyleGAN/dataset_tool.py create_from_images C:/Users/evane/Documents/GitHub/ConditionalStyleGAN/dataset/logos C:/Users/evane/Documents/GitHub/ConditionalStyleGAN/data/w/ 1

print(len(list(labels['cluster'].unique()))) #6
