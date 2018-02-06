"""All unit tests for SciUnit"""

import sys
import unittest
from . import *

def main():
    buffer = 'buffer' in sys.argv
    sys.argv = sys.argv[:1] # Args need to be removed for __main__ to work.  
    unittest.main(buffer=buffer)

if __name__ == '__main__':
    main()
        

