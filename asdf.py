class Self:
    def __init__(self):
        self.self =self
self = Self()
print (exec("self" +".self" *10000))