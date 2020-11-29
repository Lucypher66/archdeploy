import os
import sys

sys.argv[0] == 'archdeploy.py'
sys.argv[1] == 'live'






def systeminstallation():
   chroot = ""

   print("FUNCTION NOT IMPLEMENTED")
   harddrive = input("Type the device path of the hard drive (/dev/sdX): ")
   mountstring = "mount " + harddrive + " /mnt"
   os.system(mountstring)
   pacstrapstring = "pacstrap /mnt linux linux-firmware dhcpcd nano bash-completion python "


   option = input("Install the base-devel package? Mandatory if you want to build your own packages or use the AUR. Y/N: ")
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
   copystring = "cp " + sys.argv[0] + " /mnt"
   os.system(copystring)
   sys.argv[1] == 'chroot'
   os.system("arch-chroot /mnt python /archdeploy.py chroot")






def harddriveformat():
    harddrive = input("Type the device path of the hard drive (/dev/sdX): ")
    umountstring = "umount " + harddrive + " /mnt"
    formatstring = "mkfs.ext4 " + harddrive
    option = input("Is this the correct path? " + "(" + harddrive + ")" + " Y/N ")
    if option == "Y" or option == "y":
        os.system(umountstring)
        os.system(formatstring)
        mountstring = "mount " + harddrive + " /mnt"
        os.system(mountstring)
        print("Hard drive was mounted to /mnt.")
        menu()

    else:
        harddriveformat()

def chrootinstall():
    hostnamestring = input("Enter the hostname that this device should have later: ")
    hostnamestring = "echo " + hostnamestring + " > /etc/hostname"
    langstring = input("Enter your locale String (example: de_DE for germany): ")
    langstringtopaste = langstring + ".UTF-8"
    os.system(hostnamestring)
    #os.system("cat /etc/hostname")
    packagestring = "pacman -S "



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


if sys.argv[1] == "chroot":
    chrootinstall()
    exit()



menu()