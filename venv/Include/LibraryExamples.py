import reprlib

reprlib.repr(set('blahblahboopbeep'))

import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
'yellow'], 'blue']]]


import textwrap

doc = """this would text wrap if it was long ehough"""


import locale

from string import Template

t = Template('${village}folk send $$10 to $cause.')

t.substitute(village = 'texas', cause='yo ho')


import time, os.path

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style(%d-date %n-seqnum %f-format):')

