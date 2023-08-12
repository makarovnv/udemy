class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


post_about_politicians = BlogPost('John', 'I like politicians', 0)
post_about_cats = BlogPost('Jane', 'I like cats', 0)

post_about_cats.number_of_likes = 1000

print(post_about_politicians.number_of_likes)
print(post_about_cats.number_of_likes)