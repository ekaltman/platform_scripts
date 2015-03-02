from os.path import join as pjoin
class Platformclass:
    ordered_headers_platform = ['concept',
                       'pref_label',
                       'alt_label',
                       'definition',
                       'related',
                       'broader',
                       'note']
    ordered_headers_formats = ['concept',
                       'pref_label',
                       'alt_label',
                       'definition',
                       'related',
                       'broader']
    def __init__(self,which,concept, pref_label, alt_label, definition, related, broader, note):
        self.which = which
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
        if self.which == 0:
            folder = "platform txt"
        elif self.which == 1:
            folder = "media platform txt"
        path_to_file = pjoin("D:\\", "Python Projects", "github", "platform_scripts", folder, filename+".txt")
        file = open(path_to_file, "w")
        if self.which == 0:
            for key in Platformclass.ordered_headers_platform:
                write_property(file, key)
        elif self.which == 1:
            for key in Platformclass.ordered_headers_formats:
                write_property(file, key)
        file.close()

    def toHtml(self):
        platformInfo = []
        def write_property(property):
            info = self.__dict__[property]
            prop_name = " ".join(property.split('_')).upper()
            platformInfo.append(prop_name + "\n")
            platformInfo.append(info.encode('utf-8'))
        if self.which == 0:
            for key in Platformclass.ordered_headers_platform:
                write_property(key)
        elif self.which == 1:
            for key in Platformclass.ordered_headers_formats:
                write_property(key)
        return platformInfo

    def toStringCSV(self):
        if self.which == 0:
            return [self.__dict__[header].encode('utf-8') for header in Platformclass.ordered_headers_platform]
        elif self.which == 1:
            return [self.__dict__[header].encode('utf-8') for header in Platformclass.ordered_headers_formats]

if __name__ == "__main__":
    p = Platformclass(*['test'+str(x) for x in range(8)])
    p.toFile()
    print p.toStringCSV()