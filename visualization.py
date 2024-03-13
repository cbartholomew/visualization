import os 
print("Content-type: text/html", end="\r\n\r\n", flush=True) 
f = os.system("curl https://www.google.com")
print(f)