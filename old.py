import os, sys, time 
from time import sleep 
try: 
     __import__("old").__killer__() 
 except Exception as e: 
     exit(str(e))
