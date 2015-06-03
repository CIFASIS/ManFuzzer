'''
Created on Dec 30, 2012

@author: Peter
'''
import os
import os.path
import binascii
import logging
import random

class SeedGenerator(object):
    '''
    
    '''

    logger = logging.getLogger('seedgen')

    def __init__(self,directory):
        self.directory = str(directory)
        self.seeds = []

        for dirpath, dirnames, filenames in os.walk(directory):
          for filename in filenames:
            if not ("index.html" in filename):
              self.seeds.append(os.path.join(dirpath, filename))
            #else:
            #  print(os.path.join(dirpath, filename))
         
       
    def generate(self):
        return "file:"+random.choice(self.seeds) 
        
        
