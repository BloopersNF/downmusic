class Videos:
    def __init__(self, titles, links):
        self.titles = titles
        self.links = links
        self.video = {}
        for title in self.titles:
            self.video[title] = self.links[titles.index(title)]
