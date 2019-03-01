class Slide():

    def __init__(self, photo1, photo2 = None):
        if photo2 != None: #se ho due foto verticali
            self.photo1 = photo1
            self.photo2 = photo2
            self.tags = self.photo1.tags.union(photo2.tags)
            self.id = [photo1.photoid, photo2.photoid]
        else: #Se la foto e' orizzontale
            self.photo1 = photo1
            self.id = [photo1.photoid]
            self.tags = self.photo1.tags

    def __repr__(self):
        return " ".join(self.id)

    def getTags(i):
        return self.tags

    # def __lt__(self, obj):
    #     return (len(self.tags) < len(obj.tags))

    # del __gt__(self, obj):
    #     return (len(self.tags) > len(obj.tags))
          