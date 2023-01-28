class format():
    field = ""
    type = ""
    index = 0
    options = ""
    model = ""
    compare = ""

    def __init__(self, field, type, index, options, model, compare):
        self.field = field
        self.type = type
        self.index = index
        self.options = options
        self.compare = compare
        self.model = model

        