
class Platform:
    def __init__(self,platform_name, alternate_name, alternate_version, media_formats, operating_system, peripherals, sources, exclusion_rationale, problematic, notes):
        self.platform_name       = platform_name
        self.alternate_name      = alternate_name
        self.alternate_version   = alternate_version
        self.media_formats       = media_formats
        self.operating_system    = operating_system
        self.peripherals         = peripherals
        self.sources             = sources
        self.exclusion_rationale = exclusion_rationale
        self.problematic         = problematic
        self.notes               = notes


    def toString(self):
        
        file.write("PLATFORM NAME")
        file.write("\n")
        data = platformList.index(platformindex).platform_name
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("ALTERNATE NAME")
        file.write("\n")
        data = platformList.index(platformindex).alternate_name
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("ALTERNATE VERSION")
        file.write("\n")
        data = platformList.index(platformindex).alternate_version
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("MEDIA FORMATS")
        file.write("\n")
        data = platformList.index(platformindex).media_formats
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("OPERATING SYSTEM")
        file.write("\n")
        data = platformList.index(platformindex).operating_system
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("PERIPHERALS")
        file.write("\n")
        data = platformList.index(platformindex).peripherals
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("SOURCES")
        file.write("\n")
        data = platformList.index(platformindex).sources
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("EXCLUSION RATIONALE")
        file.write("\n")
        data = platformList.index(platformindex).exclusion_rationale
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("PROBLEMATIC")
        file.write("\n")
        data = platformList.index(platformindex).problematic
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

        file.write("NOTES")
        file.write("\n")
        data = platformList.index(platformindex).notes
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")

