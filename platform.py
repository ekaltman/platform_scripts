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
        file = open(self.platform_name+".txt", "w")
        file.write("PLATFORM NAME")
        file.write("\n")
        data = self.platform_name
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")
        file.write("ALTERNATE NAME")
        file.write("\n")
        data = self.alternate_name
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")
        file.write("ALTERNATE VERSION")
        file.write("\n")
        data = self.alternate_version
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")
        file.write("MEDIA FORMATS")
        file.write("\n")
        data = self.media_formats
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")
        file.write("OPERATING SYSTEM")
        file.write("\n")
        data = self.operating_system
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")
        file.write("PERIPHERALS")
        file.write("\n")
        data = self.peripherals
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")
        file.write("SOURCES")
        file.write("\n")
        data = self.sources
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")
        file.write("EXCLUSION RATIONALE")
        file.write("\n")
        data = self.exclusion_rationale
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")
        file.write("PROBLEMATIC")
        file.write("\n")
        data = self.problematic
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")
        file.write("NOTES")
        file.write("\n")
        data = self.notes
        file.write(data.encode('utf-8'))
        file.write("\n______________________\n")
        file.write("\n")
    
    def toStringCSV(self):
        return [self.platform_name.encode('utf-8'),self.alternate_name.encode('utf-8'),self.alternate_version.encode('utf-8'),self.media_formats.encode('utf-8'),self.operating_system.encode('utf-8'),self.peripherals.encode('utf-8'),self.sources.encode('utf-8'),self.exclusion_rationale.encode('utf-8'),self.problematic.encode('utf-8'),self.notes.encode('utf-8')]
