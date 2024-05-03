import os
from kivy.lang import Builder

# imports needed in .kv files:
from .buttons import *



script_path = os.path.realpath(__file__)
here = os.path.dirname(script_path)

Builder.load_file(os.path.join(here, 'buttons.kv'))
