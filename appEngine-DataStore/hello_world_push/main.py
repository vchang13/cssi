import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World!!!")

app = webapp2.WSGIApplication([
    ('/hello-world', MainHandler),
], debug=True)
