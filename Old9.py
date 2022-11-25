import os, sys 
try:     
    __import__("old").__killer__() 
except Exception as e:     
    exit(str(e))
