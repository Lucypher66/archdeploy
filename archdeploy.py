import os

def systeminstallation():
   print("FUNCTION NOT IMPLEMENTED")

def harddriveformat():
    harddrive = input("Type the device path of the hard drive (/dev/sdX): ")
    formatstring = "mkfs.ext4 " + harddrive
    option = input("Is this the correct path? " + harddrive + " Y/N ")
    if option == "Y" or option == "y":
        os.system(formatstring)
        option1 = input("The hard drive was formatted with the ext4 filesystem. Should it be mounted to /mnt? Y/N ")
        if option1 == "Y" or option == "y":
            mountstring = "mount " + harddrive + " /mnt"
            os.system(mountstring)
            print("Hard drive was mounted to /mnt.")
            menu()
        else:
            menu()
    else:
        harddriveformat()





def harddrivelist():
    print("")
    print("")
    os.system("fdisk -l")
    print("")
    print("")

    option = input("Are there hard drives to format? Y/N ")
    if option == "Y" or option == "y":
        harddriveformat()



def menu():
    print("##############################################")
    print("#              ARCH AUTOINSTALL              #")
    print("##############################################")

    print("1. List and format hard drives")
    print("2. Update live-system")
    print("3. Install system")
    print("4. Exit program")

    option = input("Choose option: ")

    if int(option) == 1:
        harddrivelist()
        menu()
    if int(option) == 2:
        print("")
        print("")
        os.system("pacman -Syyu")
        print("")
        print("")
        menu()
    if int(option) == 3:
        print("")
        print("")
        systeminstallation()
        print("")
        print("")
        menu()
    if int(option) == 4:
        exit()



def main():
    menu()

main()