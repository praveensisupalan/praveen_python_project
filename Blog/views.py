from praveenpythonwork.Blog.models import users, posts

session = {}


def SigninRequired(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            return None

    return wrapper


# authenticate
def authenticate(**kwargs):
    username = kwargs.get("username")
    password = kwargs.get("password")

    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user


class LoginViews:

    def post(self, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user = authenticate(username=username, password=password)

        if user:
            session["user"] = user[0]
        # print(session)


class PostListViews:
    @SigninRequired
    def get(self, *args, **kwargs):
        return posts


class MyPostViews:
    @SigninRequired
    def get(self, *args, **kwargs):
        userid=session["user"]["id"]
        mypost=[post for post in posts if post["userId"]==userid]
        return mypost

login = LoginViews()
login.post(username="richard", password="Password@123")

# all_post = PostListViews()
# print(all_post.get())

mypost= MyPostViews()
print(mypost.get())