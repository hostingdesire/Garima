import os
def ISO():
        a=int(input("enter your choice u want to download:\npress 1 for windows\npress 2 for centos\npress 3 for ubuntu\npress 4 for kali linux\npress 5 for parrot os\n"))
        if a==1:
            os.system('wget -O windows2K19.iso https://software-download.microsoft.com/download/pr/17763.737.190906-2324.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_en-us_1.iso')
        if a==2:
             os.system('wget -O centos.iso http://centos.mirror.snu.edu.in/centos/8.3.2011/isos/x86_64/CentOS-8.3.2011-x86_64-boot.iso')
        if a==3:
             os.system('wget -O ubuntu.iso https://releases.ubuntu.com/16.04/ubuntu-16.04.6-desktop-i386.iso')
        if a==4:
             os.system('wget -O kaliLinux.iso https://cdimage.kali.org/kali-2021.1/kali-linux-2021.1-installer-amd64.iso')
        if a==5:
             os.system('wget -O parrotOS.iso https://download.parrot.sh/parrot/iso/4.10/Parrot-home-4.10_amd64.iso')
ISO()
