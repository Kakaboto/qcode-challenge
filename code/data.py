import pyreadr as pyr

def getData(data): #'../dataverse_files/UNVotes.RData'
    csvData = pyr.read_r(data)
    return csvData

