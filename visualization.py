import os 

def main():
    print("Content-type: text/html", end="\r\n\r\n", flush=True) 
    f = os.system("curl https://www.google.com")
    print(f)

if __name__ == '__main__':
  main()