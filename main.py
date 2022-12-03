#Check If Installed
try: 
    import requests  
except ImportError: 
    print("Requests Not Found...\nInstalling...")
    os.system("pip install requests")
    print("Requests Installed")
#import
import os
import requests
print("Christmas Joke Generator")
response = requests.get(
                "https://christmascountdown.live/api/joke")
data = response.json()
print(data["question"] + "\n" + data["answer"])
