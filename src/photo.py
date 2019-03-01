class Photo():

    def __init__(self, photoid, orientation, tags_list):
        self.photoid = str(photoid)
        self.orientation = orientation
        self.tags = set(tags_list)

    @classmethod
    def from_str(cls, photoid, line: str):
        #print(line)
        args = line.split(" ")
        orient = args[0]
        howmanytags = int(args[1])
        args = args[2:]
        #calma mari
        if orient not in ("H", "V"):
            raise ValueError("wrong orient")

        if len(args) != howmanytags:
            raise ValueError("not all tags were found")

        return cls(photoid, orient, args)
