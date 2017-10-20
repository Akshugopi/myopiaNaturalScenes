import os
import csv
import glob
import imghdr
import xlrd
import pandas as pd
import numpy as np
from scipy.misc import imread

def readin_jpgs(datadir):
    ''' readin jpeg files from the specified directory, make sure they are not excluded data'''
    filelist = []
    for name in glob.glob(datadir,recursive=True):
        if not os.path.isdir(name):
            if imghdr.what(name)=='jpeg':
                if not 'Exclude' in name:
                    filelist.append(name)
    return(filelist)

def read_ims(filelist,mindim):
    # read in images
    min_h = 10000
    min_w = 10000

    raws = []
    rawfnames = []

    for pf in filelist:
        im = np.asarray(imread(pf))
        #print(np.shape(im)[0])
        
        #if the dimensions are too small, don't use the photo
        if np.shape(im)[0] > mindim and np.shape(im)[1] > mindim:
            
            raws.append(im)
            rawfnames.append(pf)

            #ccalc new min width and height
            if(min_h) > np.shape(im)[0]:
                min_h = np.shape(im)[0]
            if(min_w) > np.shape(im)[1]:
                min_w = np.shape(im)[1]
        
    #cast to an array
    raws = np.array(raws)
    return(raws,rawfnames,min_h,min_w)


def readin_al_xls(filename):
    ''' readin axial length for each subject and return as pandas dataframe'''
    xls = pd.ExcelFile(filename)
    al_sheet = xls.parse(2) #get sheet 2 with AL values
    al_sheet.columns = al_sheet.iloc[2,:] #grab real column names
    al_sheet = al_sheet.iloc[3:]
    al_sheet = al_sheet.set_index(al_sheet.loc[:,'ID']) #use ID as row names
    al_sheet = al_sheet.loc[:,['AL OD','AL OS']]
    al_sheet = al_sheet.dropna(how='any')
    return(al_sheet)