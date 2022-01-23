# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:32:00 2022

@author: ChangGun Choi
"""


import os
import csv
import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

label_path= "C:/Users/ChangGun Choi/Team Project/TeamProject/SVG_Logo/Model/Label/LLD_weighted_eliminated.csv"
labels = pd.read_csv(label_path, sep=',', skiprows=0)
list_of_file_paths = []
class_condition_labels = []
png_path = 'C:/Users/ChangGun Choi/Team Project/TeamProject/SVG_Logo/Data/Conditional_StyleGAN_Logo/'


for name in labels['0']:
    path = png_path + name
    list_of_file_paths.append(path)
list_of_file_paths

class_condition_labels = labels['1'].values.tolist()
class_condition_labels
mypickle = {"Filenames": list_of_file_paths, "Labels": class_condition_labels}
# Pickle path = '../data/mypickle.pickle'
with open('../data/mypickle.pickle', 'wb') as handle:
    pickle.dump(mypickle, handle, protocol=pickle.HIGHEST_PROTOCOL)




image_dir = "C:/Users/ChangGun Choi/Team Project/StyleGAN Logo/ConditionalStyleGAN/data/Conditional_StyleGAN_Logo/"
img = np.asarray(PIL.Image.open(image_dir + df["Filenames"].iloc[0]))
img = img.transpose([2, 0, 1])
#img
#tfr.add_image(img)
#TFRecordExporter(tfrecord_dir, len(df)).add_image(img)
#tfrecord_dir= "C:/Users/ChangGun Choi/Team Project/StyleGAN Logo/ConditionalStyleGAN/dataset/logo"
img.shape
for i in range(len(df["Filenames"])):
    img = np.asarray(PIL.Image.open(image_dir + df["Filenames"].iloc[i]))
    channels = img.shape[2] if img.ndim == 3 else 1
    print(channels)
    print(img.shape[2])
    
    #img = img.reshape((128,128,-1))
    #print(img.shape)
    if channels == 1:
        print(channels) 
    if channels == 1:
        img = img[np.newaxis, :, :] # HW => CHW
        print("fine")
    else:
        try:
            img = img.transpose([2, 0, 1]) # HWC => CHW

            print("added")
        except:
            drop.append(i)
            print("deleted")
            continue

img
