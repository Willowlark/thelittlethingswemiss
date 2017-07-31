import os
import sys
from datetime import datetime
from shutil import copyfile

postsIn = "./_posts/steno/"
tempsAt = "./_drafts/"

template, fname = sys.argv[1:3]
today = datetime.today()
date = '-'.join([repr(x) for x in [today.year, today.month, today.day]])

copyfile(tempsAt+template+'.md', postsIn+date+"-"+fname+'.md')
