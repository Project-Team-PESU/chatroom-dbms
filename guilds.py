class Guild():

    count = 1

    def __init__(self,name):
        self.name = name
        self.id = Guild.count
        Guild.count += 1
