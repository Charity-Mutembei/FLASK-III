class Articles:
    '''
    Class that define the news articles objects
    '''

    def __init__(self, source, author, title, url, urlToImage, publishedAt, content):
        self.source = source
        self.author = author 
        self.title = title
        self.url = url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
