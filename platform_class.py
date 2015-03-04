from os.path import join as pjoin
class Platformclass:
    ordered_headers = ['concept',
                       'pref_label',
                       'alt_label',
                       'definition',
                       'related',
                       'broader',
                       'note']
    folder_name = "platform_txt"

    def __init__(self, concept, pref_label, alt_label, definition, related, broader, note):
        self.concept = concept
        self.pref_label = pref_label
        self.alt_label = alt_label
        self.definition = definition
        self.related = related
        self.broader = broader
        self.note = note

    def toFile(self):
        def write_property(file, property):
            info = self.__dict__[property]
            prop_name = " ".join(property.split('_')).upper()
            file.write(prop_name + "\n" + info.encode('utf-8'))
            file.write("\n_________________\n")
        filename = ''
        for slash in self.concept.split("/"):
            filename += slash

        folder = self.__class__.folder_name

        path_to_file = pjoin("D:\\", "Python Projects", "github", "platform_scripts", folder, filename+".txt")
        file = open(path_to_file, "w")
        for key in self.__class__.ordered_headers:
            write_property(file, key)
        file.close()

    def toHtml(self):
        platformInfo = []
        def write_property(property):
            info = self.__dict__[property]
            prop_name = " ".join(property.split('_')).upper()
            platformInfo.append(prop_name + "\n")
            platformInfo.append(info.encode('utf-8'))
            for key in self.__class__.ordered_headers:
                write_property(key)
        return platformInfo

    def toStringCSV(self):
            return [self.__dict__[header].encode('utf-8') for header in self.__class__.ordered_headers]

if __name__ == "__main__":
    p = Platformclass(*['test'+str(x) for x in range(8)])
    p.toFile()
    print p.toStringCSV()

    #Something to commit

class MediaFormat(Platformclass):
    ordered_headers = ['concept',
                       'pref_label',
                       'alt_label',
                       'definition',
                       'related',
                       'broader']
    folder_name = 'media_format_txt'

    def __init__(self, concept, pref_label, alt_label, definition, related, broader):
        super(MediaFormat, self).__init__(concept, pref_label, alt_label, definition, related, broader, note=None)