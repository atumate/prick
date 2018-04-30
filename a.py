#!/usr/bin/env python
#execfile("a_lib.py")

import argparse
import requests
from pprint import pprint

targetURL = "http://192.168.125.139/sqli-labs-master/Less-2/?id=1./a.py'"

def confirm_type():
    guess_lists=['\'','"','#','--+']
    for i,x in enumerate(guess_lists):
        print i,x


confirm_type()








