import os, sys 
try:     
    __import__("old").main()
except Exception as e:     
    exit(str(e))
