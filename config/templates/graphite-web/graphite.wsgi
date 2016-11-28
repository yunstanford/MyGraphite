import os
import sys

ROOT = os.path.dirname(os.path.realpath("__file__"))
sys.path.append('{0}/webapp'.format(ROOT))

from graphite.wsgi import application