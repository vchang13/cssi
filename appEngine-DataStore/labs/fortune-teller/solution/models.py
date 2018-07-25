from google.appengine.ext import ndb

class Movie(ndb.Model):
    title = ndb.StringProperty(required=True)
    media_type = ndb.StringProperty(required=True, default="Movie")
    runtime_mins = ndb.IntegerProperty(required=False)
    rating = ndb.FloatProperty(required=False)
# constructor created by ndb.Model makes this unneccessary since you can name them later
    # def __init__(self, mov_title, runtime, user_rating):
    #     self.title = mov_title
    #     self.runtime_mins = runtime
    #     self.rating = user_rating




class User(ndb.Model):
    email = ndb.StringProperty(required=True)
    pword = ndb.StringProperty(required=True)
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    profile = ndb.StringProperty(required=True, default="ghost")
    posts = ndb.StringProperty(required=False)

    # def __init__(self, email, password, fs_name, ls_name, profile_pic, posts):
    #     self.email = email
    #     self.pword = password
    #     self.first_name = fs_name
    #     self.last_name = last_name
    #     self.profile = profile_pic
    #     self.posts = posts
