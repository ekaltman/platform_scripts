
class platform:
    def __init__(self, platformName, alternateName, alternateVersion, mediaFormats, operatingSystem, peripherals, sources, exclusionRationale, problematic, notes):
        self.__platformName = platformName
        self.__alternateName = alternateName
        self.__alternateVersion = alternateVersion
        self.__mediaFormats = mediaFormats
        self.__operatingSystem = operatingSystem
        self.__peripherals = peripherals
        self.__sources = sources
        self.__exclusionRationale = exclusionRationale
        self.__problematic = problematic
        self.__notes = notes

    def getPlatformName(self):
        return self.__platformName

    def getAlternateName(self):
        return self.__alternateName

    def getAlternateVersion(self):
        return self.__alternateVersion

    def getMediaFormats(self):
        return self.__mediaFormats

    def getOperatingSystem(self):
        return self.__operatingSystem

    def getPeripherals(self):
        return self.__peripherals

    def getSources(self):
        return self.__sources

    def getExclusionRationale(self):
        return self.__exclusionRationale

    def getProblematic(self):
        return self.__problematic

    def getNotes(self):
        return self.__notes

    def toString(self):
        
        file.write("PLATFORM NAME")
        file.write("\n")
        data = platformList.index(platformindex).getPlatformName
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("ALTERNATE NAME")
        file.write("\n")
        data = platformList.index(platformindex).getAlternateName
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("ALTERNATE VERSION")
        file.write("\n")
        data = platformList.index(platformindex).getAlternateVersion
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("MEDIA FORMATS")
        file.write("\n")
        data = platformList.index(platformindex).getMediaFormats
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("OPERATING SYSTEM")
        file.write("\n")
        data = platformList.index(platformindex).getOperatingSystem
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("PERIPHERALS")
        file.write("\n")
        data = platformList.index(platformindex).getPeripherals
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("SOURCES")
        file.write("\n")
        data = platformList.index(platformindex).getSources
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("EXCLUSION RATIONALE")
        file.write("\n")
        data = platformList.index(platformindex).getExclusionRationale
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("PROBLEMATIC")
        file.write("\n")
        data = platformList.index(platformindex).getProblematic
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("NOTES")
        file.write("\n")
        data = platformList.index(platformindex).getNotes
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

