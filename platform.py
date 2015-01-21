class Platform:
    ordered_headers = ['platform_name',
               'alternate_name',
               'alternate_version',
               'media_formats',
               'operating_system',
               'peripherals',
               'sources',
               'exclusion_rationale',
               'problematic',
               'notes']

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


    def toFile(self):

        def write_property(file, property):
            info = self.__dict__[property]
            prop_name = " ".join(property.split('_')).upper()
            file.write(prop_name + "\n" + info.encode('utf-8'))
            file.write("\n_________________\n")

        file = open(self.platform_name + ".txt", "w")
        for key in Platform.ordered_headers:
            write_property(file, key)
        file.close()

    def toStringCSV(self):
        return [self.__dict__[header].encode('utf-8') for header in Platform.ordered_headers]


if __name__ == "__main__":
    p = Platform(*['test'+str(x) for x in range(10)])
    p.toFile()
    print p.toStringCSV()
