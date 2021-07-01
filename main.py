# mad_libs template
import json

import os




class MadLibs:
    def __init__(self, word_description, templates):
        self.word_description = word_description
        self.templates = templates
        self.user_input = []
        self.story = None

    @classmethod
    def get_story(cls, name, path="./template"):
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib

# user input
    def get_from_user(self):

        print("please provide the following words : ")
        for words in self.word_description:
            user = input(words + " ")
            self.user_input.append(user)
        return self.user_input





# build the story
    def build_story(self):
        self.story = self.templates.format(*self.user_input)
        return self.story




temp_name = "madlibs.json"
mad_lib = MadLibs.get_story(temp_name)
word = mad_lib.get_from_user()
story = mad_lib.build_story()
print(story)

