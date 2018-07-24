# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
from google.appengine.api import urlfetch
import json
import urllib
import random
import jinja2

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)

class MainPage(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name')
        self.response.headers['Content-Type'] = 'text/html'
        # self.response.write('Hello')
        random_text = ['sand', 'FTW', 'bwahh', 'weird', 'ohmergerd', 'darude', 'storm', 'cap', 'sleep', 'cats', 'Catss', 'CATS', 'boogiewoogiewoogie', 'i am your dad', 'sodium', 'be careful chiren', 'i want to see my']

        url = 'https://api.imgflip.com/get_memes'
        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                # self.response.write(type(result.content))
                json_dict = json.loads(result.content)
                # pict_url = json_dict['data']['memes'][0]['url']
                # pict_id = json_dict['data']['memes'][0]['id']
                random_meme = random.choice(json_dict['data']['memes'])['id']
                # self.response.write('<img src="{pic}"/>'.format(pic=pict_url))
            else:
                self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
        caption_url = 'https://api.imgflip.com/caption_image'
        caption_dict = {
            'template_id': random_meme,
            'username': 'aimingarrows',
            'password': 'qwerty123',
            'text0': random.choice(random_text),
            'text1': random.choice(random_text),
        }
        # # result = urlfetch.post(caption_url, data=caption_dict)
        result = urlfetch.fetch(
            url=caption_url,
            payload=urllib.urlencode(caption_dict),
            method=urlfetch.POST,
        )
        # self.response.write(result.content)
        new_meme_dict = json.loads(result.content)
        pict_url = new_meme_dict['data']['url']
        self.response.write('<img src="{pic}"/>'.format(pic=pict_url))

class MemeTemp(webapp2.RequestHandler):
    def get(self):
        # self.response.write('howdoigethere')
        template = template_env.get_template('templates/home.html')
        self.response.write(template.render())

class MemeResult(webapp2.RequestHandler):
    # def post(self):
    #     meme_type = self.request.get('meme-type')
    #     self.response.write('Your meme is {meme}'.format(meme=meme_type))

    def post(self):
        url = 'https://api.imgflip.com/get_memes'
        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                json_dict = json.loads(result.content)
                chose_meme = self.request.get('meme-type')
                self.response.write('Your meme is {meme}'.format(meme=chose_meme))

# dictionary_name['key1']['key2'][index]['key for the indexed object']
                meme_chosen = json_dict['data']['memes'][35]['id']

            else:
                self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

# allows inputs to be used for the text on meme
        input1=self.request.get('user-first-ln')
        input2=self.request.get('user-second-ln')

        caption_url = 'https://api.imgflip.com/caption_image'
        caption_dict = {
            'template_id': meme_chosen,
            'username': 'aimingarrows',
            'password': 'qwerty123',
            'text0': input1,
            'text1': input2,
        }
        result = urlfetch.fetch(
            url=caption_url,
            payload=urllib.urlencode(caption_dict),
            method=urlfetch.POST,
        )
        new_meme_dict = json.loads(result.content)
        pict_url = new_meme_dict['data']['url']
        self.response.write('<img src="{pic}"/>'.format(pic=pict_url))


class RecipeBrowser(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/recipes.html')
        recipe = {'ingredients': ['cottage cheese', 'pineapple'], 'cuisine': 'nixonian'}
        self.response.write(template.render(recipe))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/memetemp', MemeTemp),
    ('/recipe', RecipeBrowser),
    ('/meme_result', MemeResult)

], debug=True)
