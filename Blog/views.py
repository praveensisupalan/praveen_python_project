from praveenpythonwork.Blog.models import users, posts

session = {}


def SigninRequired(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            return print("invalid section you must login")

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

    @SigninRequired
    def post(self, *args, **kwargs):
        userid = session["user"]["id"]
        post = kwargs.get("data")
        post["userId"] = userid
        posts.append(post)
        print("posted successfully")
        print(posts[-1])


class MyPostViews:
    @SigninRequired
    def get(self, *args, **kwargs):
        userid = session["user"]["id"]
        mypost = [post for post in posts if post["userId"] == userid]
        return mypost


class Addlikes:
    @SigninRequired
    def post(self, *args, **kwargs):
        userid = session["user"]["id"]
        postid = kwargs.get("postid")
        post = [post for post in posts if post["postId"] == postid]
        if post:
            post = post[0]
            post["liked_by"].append(userid)
            print(post)


login = LoginViews()
login.post(username="richard", password="Password@123")

allpost = PostListViews()

mypost = {"postId": 9, "title": "hai ", "content": "content", "liked_by": []}
allpost.post(data=mypost)

like = Addlikes()
like.post(postid=1)

all_post = PostListViews()
print(all_post.get())

mypost= MyPostViews()
print(mypost.get())
