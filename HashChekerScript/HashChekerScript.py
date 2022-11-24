import subprocess
import time
from simple_file_checksum import get_checksum # name of lib is simple_file_checksum


path = input("Enter the full path: ")
last_hash = ""
while True:
    if last_hash == "":
        last_hash = get_checksum(path)
        proc = subprocess.Popen(["python", path])
        print("Start file")
        
    if last_hash != get_checksum(path):
        print("Reloading file")
        proc.terminate()
        proc = subprocess.Popen(["python", path])
        last_hash = get_checksum(path)
        
    time.sleep(3)    
    