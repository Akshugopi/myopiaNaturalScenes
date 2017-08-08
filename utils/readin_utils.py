import os
import csv


def readin_jpgs(datadir):
    filelist = []
    for name in glob.glob(datadir,recursive=True):
        if not os.path.isdir(name):
            if imghdr.what(name)=='jpeg':
                if not name.split('/')[-4] == 'Excluded':
                    filelist.append(name)
    return(filelist)