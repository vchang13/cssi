#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#generally, imports happen at the top

import requests

ingredients = []

enter_more = input("Do you have any specific ingredients to enter? [y|n]:").lower()

while enter_more == "y":
    ingredients.append(input("What is the ingredient? One word only please:").lower())
    enter_more = input("Do you have any more ingredients to enter? [y|n]:").lower()

recipe = input("What kind of recipe do you want to find?")

# Write your code below!

api_string = 'http://www.recipepuppy.com/api/?i={ingredients}&q={recipe_type}'

print(ingredients)

ingredients_str = ','.join(ingredients)
new_api_string = api_string.format(ingredients=ingredients_str, recipe_type=recipe)

print(new_api_string)

r = requests.get(new_api_string)
# print(r.status_code)
# print(r.json)
# print(type(r.json))
# print(r.json()['results'])
# print(type(r.json()['results']))
# print(r.json()['results'][0])
# print(type(r.text))
# print(dir(r.text))
