from praveenpythonwork.Blog.models import users,posts

session={}

         # authenticate

def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")

    user=[user for user in users  if user["username"]==username and user["password"]==password]
    return user

class LoginViews:

    def post(self,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)

        if user:
            session["user"]=user[0]
        print(session)


class PostListViews:

    def get(self,**kwargs):

        return posts

login=LoginViews()

login.post(username="akhil", password="Password@123")
posts=PostListViews()

