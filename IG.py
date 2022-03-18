import instaloader

hello = instaloader.Instaloader()

hai = input("[+] Enter Your Username: ")

hello.download_profile( hai, profile_pic_only = True)
