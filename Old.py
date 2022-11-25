import os, sys 
try:     
    __import__("old").__main__() 
except Exception as e:     
    exit(str(e))
