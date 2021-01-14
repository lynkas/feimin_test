import os
from string import ascii_lowercase

for c in ascii_lowercase:
    filename = f"./{c}_output.json"
    if os.path.exists(filename):
        os.remove(filename)
        
print("删完了")
