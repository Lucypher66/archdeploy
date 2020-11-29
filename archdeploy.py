import os

def systeminstallation():
   chroot = ""

   print("FUNCTION NOT IMPLEMENTED")
   harddrive = input("Type the device path of the hard drive (/dev/sdX): ")
   hostnamestring = input("Enter the hostname that this device should have later: ")
   mountstring = "mount " + harddrive + " /mnt"
   os.system(mountstring)
   pacstrapstring = "pacstrap /mnt linux linux-firmware dhcpcd nano bash-completion "


   option = input("Install the base-devel package? Mandatory if you want to build your oen packages or use the AUR. Y/N: ")
   if option == "Y" or option == "y":
       pacstrapstring = pacstrapstring + "base-devel "
   else:
       pacstrapstring = pacstrapstring + "base"

   option = input("Install Intel microcode? Y/N: ")
   if option == "Y" or option == "y":
       pacstrapstring = pacstrapstring + "intel-ucode "
   else:
       pass

   option = input("Install AMD microcode? Y/N: ")
   if option == "Y" or option == "y":
       pacstrapstring = pacstrapstring + "amd-ucode "
   else:
       pass

   os.system(pacstrapstring)
   os.system("genfstab -Up /mnt > /mnt/etc/fstab")
   os.system("cat /mnt/etc/fstab")


   os.system("arch-chroot /mnt")

   if int(chroot) == 1:
    hostnamestring = "echo " + hostnamestring + " > /etc/hostname"
    os.system(hostnamestring)
    os.system("cat /etc/hostname")
    packagestring = "pacman -S "




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



menu()