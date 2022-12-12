#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 12
# 55139 Daniela Correia Coelho
# 56593 Inês Franco Calheiros



def readSkippersFile(fileName):
    """
    Reads a file with a list of skippers into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of skippers organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a skipper listed in
    the file fileName (with all the info pieces belonging to that skipper),
    following the order provided in the lines of the file.
    """



def readRequestsFile(fileName):
    """
    Reads a file with a list of requested cruises with a given file name into a collection.

    
    """

    inFile = removeHeader(open(fileName, "r"))       

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        

    return requestsList


