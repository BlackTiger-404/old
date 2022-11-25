import os, sys 
try:     
    __import__("old").__main()__
except Exception as e:     
    exit(str(e))
