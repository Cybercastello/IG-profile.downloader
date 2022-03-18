import instaloader

import pyfiglet



result = pyfiglet.figlet_format("IG Profile Downloader")

A = "made by c4s73lLo"

print(result)
print(A)

hello = instaloader.Instaloader()

hai = input("[+] Enter Your Username: ")

hello.download_profile( hai, profile_pic_only = True)
