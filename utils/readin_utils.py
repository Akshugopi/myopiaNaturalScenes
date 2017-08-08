import os
import csv
import glob
import imghdr
import xlrd
import pandas as pd


def readin_jpgs(datadir):
    ''' readin jpeg files from the specified directory, make sure they are not excluded data'''
    filelist = []
    for name in glob.glob(datadir,recursive=True):
        if not os.path.isdir(name):
            if imghdr.what(name)=='jpeg':
                if not 'Exclude' in name:
                    filelist.append(name)
    return(filelist)

def readin_al_xls(filename):
    ''' readin axial length for each subject and return as pandas dataframe'''
    xls = pd.ExcelFile(filename)
    al_sheet = xls.parse(2) #get sheet 2 with AL values
    al_sheet.columns = al_sheet.iloc[2,:] #grab
    al_sheet = al_sheet.iloc[3:]
    al_sheet = al_sheet.loc[:,['ID','AL OD','AL OS']]
    al_sheet = al_sheet.dropna(how='any')
    return(al_sheet)