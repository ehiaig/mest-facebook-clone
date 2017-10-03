class Post:

    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author

    def save(self):
        with open('posts.csv') as file:
            file.write('{},{},{}'.format(self.title, self.body, self.author))
