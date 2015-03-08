from os.path import join as pjoin
import os
class Platformclass:
    ordered_headers = ['concept',
                       'pref_label',
                       'alt_label',
                       'definition',
                       'related',
                       'broader',
                       'note']
    folder_name = "platform_txt"

    def __init__(self, concept, pref_label, alt_label, definition, related, broader, note=None):
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
        filenamecol = ''
        for colon in self.concept.split(":"):
            filenamecol += colon
        for slash in filenamecol.split("/"):
            filename += slash
        folder = self.__class__.folder_name
        path_to_folder = pjoin("D:\\", "Python Projects", "github", "platform_scripts", folder)
        #make folder if it doesn't exist
        try:
            os.makedirs(path_to_folder)
        except OSError:
            if not os.path.isdir(path_to_folder):
                raise
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



class MediaFormat(Platformclass):
    ordered_headers = ['concept',
                       'pref_label',
                       'alt_label',
                       'definition',
                       'related',
                       'broader']
    folder_name = 'media_format_txt'

    def __init__(self, concept, pref_label, alt_label, definition, related, broader):
        Platformclass.__init__(self,concept, pref_label, alt_label, definition, related, broader)