import os

try:
    print(f"remove result:{os.remove('../chapter8/test2.txt')}")
except Exception:
    print('file not found')
