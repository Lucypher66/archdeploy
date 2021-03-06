import os
import sys

sys.argv[0] == 'archdeploy.py'
sys.argv[1] == 'live'






def systeminstallation():
   chroot = ""

   print("FUNCTION NOT IMPLEMENTED")
   harddrive = input("Type the device path of the hard drive (/dev/sdXY): ")
   mountstring = "mount " + harddrive + " /mnt"
   os.system(mountstring)
   pacstrapstring = "pacstrap /mnt linux linux-firmware dhcpcd nano bash-completion python grub "


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
    formatstring = "parted -s -a optimal " + harddrive + " mklabel msdos -- mkpart primary ext4 100%"

    option = input("Is this the correct path? " + "(" + harddrive + ")" + " Y/N ")
    if option == "Y" or option == "y":

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
    legacylibs = input("Should 32-bit libraries be supported? Y/N ")
    uefi = input("Do you use UEFI? Y/N ")
    harddrive = input("Type the device path of the hard drive where the bootlaoder will be installed (/dev/sdX): ")
    os.system("passwd")
    if legacylibs == "Y" or legacylibs == "y":
        legacylibs = True
    else:
        legacylibs = False
    if uefi == "Y" or uefi == "y":
        uefi = True
    else:
        uefi = False

    langstring = input("Enter your locale String (example: de_DE for germany), leave blank for USA (en_US): ")
    if langstring == "":
        langstring = "en_US"
    langstringutf = langstring + ".UTF-8"

    timezonestring = input("Enter your Timezone (for example Europe/Berlin): ")
    timezonestring = "ln -sf /usr/share/zoneinfo/" + timezonestring + " /etc/localtime"

    os.system(hostnamestring)

    os.system("rm /etc/locale.gen")
    os.system("touch /etc/locale.gen")
    langpaste = "echo " + langstring + " UTF-8 >> /etc/locale.gen"
    os.system(langpaste)
    langpaste = "echo " + langstring + " ISO-8859-1 >> /etc/locale.gen"
    os.system(langpaste)
    langpaste = "echo " + langstring + "@euro ISO-8859-15 >> /etc/locale.gen"
    os.system(langpaste)
    print("")
    os.system("locale-gen")

    if langstring == "de_DE":
        os.system("KEYMAP=de-latin1 > /etc/vconsole.conf")
    else:
        os.system("KEYMAP=us")

    os.system("echo FONT=lat9w-16 >> /etc/vconsole.conf")

    if legacylibs == True:
        os.system("echo [multilib] >> /etc/pacman.conf")
        os.system("echo SigLevel = PackageRequired TrustedOnly >> /etc/pacman.conf")
        os.system("echo Include = /etc/pacman.d/mirrorlist >> /etc/pacman.conf")
        os.system("pacman -Sy")
    else:
        pass

    os.system("mkinitcpio -p linux")


    if uefi == True:
        os.system("pacman -S efibootmgr")
        os.system("grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=Grub2 ")
    else:
        bootloaderstring = "grub-install " + harddrive
        os.system(bootloaderstring)

    os.system("grub-mkconfig -o /boot/grub/grub.cfg")


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