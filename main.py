from sys import dont_write_bytecode
import instaloader
import os
from termcolor import colored

def cleanSort():
       # Iterate directory
       for file in os.listdir(dir_path):
           if file.endswith(".txt") or file.endswith(".xz"):
                   print(colored(f"Removing {file}", "red"))
                   os.remove(os.path.join(dir_path, file))
                   waiter = input("Press any key to exit.")
   
def customizeMessage(pf_name):
    global misc
    misc = input("Do you want the descriptions and post names of posts? (Y/N): ")
    stories = input("Do you want to download the story reels too?: ")
    other = input("Download things like location, followers, following, etc.? ")
    contin = input("If you wish to download other parts of instagram like suggested posts or by hashtag press Y: ")
    
    try:
        if stories == "Y":
            L.download_stories(pf_name)   
    except:
        print(colored("To download stories you need to be logged in!" , "blue"))

    if other == "Y":
        print(colored("Too bad! You wont get shit.", "red"))

    if contin == "Y":
        customDownload()

def customDownload():
    input("Download by hashtag")

# TODO: Add a name list so the user can download multiple accounts, then make it better by having sepparate threads for each download to maximize efficiency
# Setup
os.system('color')

# Get instance
L = instaloader.Instaloader()
while True:
   # nfx.lyria
   print(colored("Welcome to my Instagram profile downloader!", "yellow"))
   print(colored("With this tool and the instaloader library you can easily download any instagram profile! \n", "yellow"))
   choice = input(colored("If you want to download private accounts please login (Y/N): ", "blue"))
   if choice == "Y":
        name = input("Put in the name of your Account. ")
        password = input("Put in the password of your account. ") 
        print("Logging in...")
        L.login(name, password)       
        print("Logged in!")

   profile_name = input("Write the name of the account you wish to download: ")
   dir_path = r"{folder}".format(folder = profile_name)
   down_type = input("If you wish to customize your download type (Y/N), else the entire profile will be dowloaded.")

   if down_type == "Y":
        customizeMessage(profile_name)

# Begin download of vannila form
   L.download_profile(f"{profile_name}")
   if misc == "N":
     cleanSort()

  
   

   

   