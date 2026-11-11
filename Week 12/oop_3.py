class user:
    # Constructor Function
    def __init__ (self, u, p):
        self.username = u
        self.password = p

    def greet_user(self):
        print(f"Hello {self.username}")

class post:
    def __init__(self, user, media, caption):
        self.OP = user
        self.media = media
        self.caption = caption
        self.comments = []
        self.likes = 1

        print(f"{self.OP.username} has posted a {self.post_description()}")

    def give_like(self, user):
        self.likes += 1
        print(f"{user.username} gave a like to a {self.post_description()}")

    def add_comment(self, user, comment):
        self.comments.append(f"{user.username}: {comment}")
        print(f"{user.username} left a comment to a {self.post_description()}")

    def post_description(self): 
        return f"{self.media} with the caption \"{self.caption}\" with {self.likes} likes"

    def print_comments(self):
        print(f"These are the comments for a {self.post_description()}:")

        for comment in self.comments:
            print(comment)

        print()

def main():
    user_1 = user("ekim54", "123")
    user_2 = user("jdoe01", "qwerty")

    user_1.greet_user()
    user_2.greet_user()

    print()

    post_1 = post(user_1, "picture", "This is my cat")
    post_1.give_like(user_2)
    post_1.add_comment(user_2, "Your cat is ugly")
    post_1.add_comment(user_1, "You are ugly")
    post_1.print_comments()

if __name__ == "__main__":
    main()