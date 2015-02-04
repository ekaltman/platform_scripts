
class Platformclass:
    ordered_headers = ['concept',
'pref_label',
'alt_label',
'definition',
'related',
'broader',
'note']
    def __init__(self,concept, pref_label, alt_label, definition, related, broader, note):
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
        file = open(self.concept + ".txt", "w")
        for key in Platformclass.ordered_headers:
            write_property(file, key)
        file.close()
    def toStringCSV(self):
        return [self.__dict__[header].encode('utf-8') for header in Platformclass.ordered_headers]

if __name__ == "__main__":
    p = Platformclass(*['test'+str(x) for x in range(7)])
    p.toFile()
    print p.toStringCSV()