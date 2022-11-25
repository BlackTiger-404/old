import os, sys, time 
from time import sleep 
try: 
     __import__("old").Main() 
except Exception as e: 
     exit(str(e))
