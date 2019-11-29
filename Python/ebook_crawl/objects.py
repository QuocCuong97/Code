class ObjectCrawl:

    def __init__(self, title, link, images, source):
        self.title = title
        self.link = link
        self.images = images
        self.source = source

    def show_object(self):
        message = 'Title - {}, Link - {}, Source - {}'.format(
            self.title,
            self.link,
            self.source
        )
        print(message)

    def to_dict(self):
        return {
            "title": self.title,
            "link": self.link,
            "images": self.images,
            "source": self.source
        }
