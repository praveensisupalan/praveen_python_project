import json

with open("post.json", encoding="utf-8") as f:
    data = json.load(f)
    print(len(data))
# num of post by user 1
onepost = [post for post in data if post["userId"] == 1]
print("no of post by 1 = ", len(onepost))

# total num of like for postId 6

tlike = [len(post["liked_by"]) for post in data if post["postId"] == 6]
print(tlike)
# for post in data:
#     if post["postId"] == 6:
#         tlike=post["liked_by"]
#         print(len(tlike))
#         break

# num of post like by user 2

tlike = len([post for post in data if 2 in post["liked_by"]])
print(tlike)
