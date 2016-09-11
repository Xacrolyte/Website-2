import configparser

class FileUtility:
    #fileName = '.\\input\\settings.ini'
    fileName = '/users/rahulchandrawanshi/documents/workspace/webpage_backend_1/Inputs/settings.ini'
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.fileName)
    
    def getKeyForSectionInFile(self, filePath, section, key):
        self.config.read(filePath)
        sectionDetails = self.config[section]
        return sectionDetails[key]
        
    def readDBSettings(self):
        dbsettings = self.config['DBSETTINGS']
        dbsettingDictionary = {}
        dbsettingDictionary['Server'] = dbsettings['Server']
        dbsettingDictionary['Name'] = dbsettings['Name']
        dbsettingDictionary['UserName'] = dbsettings['UserName']
        dbsettingDictionary['Password'] = dbsettings['Password']
        return dbsettingDictionary
    
    
    
    