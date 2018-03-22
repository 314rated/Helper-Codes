def getFileNamesOnly():
    from os import walk

    f = []
    for (dirpath, dirnames, filenames) in walk('./'):
        f.extend(filenames)
        break
    return f

def createPickle(listToPickle, pathToPickle):
    import pickle
    pickle.dump(listToPickle, open(pathToPickle, "wb"))
    return

listOfFiles = getFileNamesOnly()
print(listOfFiles)
createPickle(listOfFiles, './filenames.pickle')


