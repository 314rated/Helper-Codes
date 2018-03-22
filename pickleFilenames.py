# Packages = os, pickle

def getFileNamesOnly(allowAll=True, filterList=[]):
    from os import walk
    f = []
    for (dirpath, dirnames, filenames) in walk('./'):
        for file in filenames:
            if allowAll or file.endswith(tuple(filterList)):
                f.append(file)
        break
    return f

def createPickle(listToPickle, pathToPickle):
    import pickle
    pickle.dump(listToPickle, open(pathToPickle, "wb"))
    return

listOfFiles = getFileNamesOnly(allowAll=False, filterList=['.png','.jpg', '.jpeg', '.gif'])
print(listOfFiles)
createPickle(listOfFiles, './filenames.pickle')


