from google.appengine.ext import ndb

class Transaction(ndb.Model):
    amount = ndb.IntegerProperty(required=True)


# alternative way to do this
# class Balance(ndb.Model):
#     balance = ndb.IntegerProperty(required=True)
