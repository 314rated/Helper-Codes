# Packages = os, pickle

import os
def getFileNamesOnly(pathToData, allowAll=True, filterList=[], discardExtension=False):
    from os import walk
    fileList = []
    for (dirpath, dirnames, filenames) in walk(pathToData):
        for file in filenames:
            if allowAll or file.endswith(tuple(filterList)):
                if discardExtension:
                    file = os.path.splitext(file)[0]
                fileList.append(file)
        break
    return fileList

def createPickle(listToPickle, pathToPickle):
    import pickle
    pickle.dump(listToPickle, open(pathToPickle, "wb"))
    return


pathToData = './'
pathToPickle = './filenames.pickle'
listOfFiles = getFileNamesOnly(pathToData, allowAll=False, filterList=['.png','.jpg', '.jpeg', '.gif'], discardExtension=True)
print(listOfFiles)
createPickle(listOfFiles, pathToPickle)
