from tqdm import tqdm
import requests

chunk_size = 1024
a=int(input("press 1 for ubuntu\npress 2 for centos\npress 3 for windows\npress 4 for kali linux\n"))


ubuntu_url = "https://releases.ubuntu.com/16.04/ubuntu-16.04.6-desktop-i386.iso"
centos_url = "http://centos.mirrors.estointernet.in/8.3.2011/isos/x86_64/CentOS-8.3.2011-x86_64-boot.iso"
windows_server_2k19_url="https://software-download.microsoft.com/download/pr/17763.737.190906-2324.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_en-us_1.iso"
kali_linux_url="https://cdimage.kali.org/kali-2021.1/kali-linux-2021.1-installer-amd64.iso"


def ISO():

    r = requests.get(url, stream = True)


    total_size = int(r.headers['content-length'])
    filename = url.split('/')[-1]

    with open(filename, 'wb') as f:
	    for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'KB'):
		    f.write(data)


if a==1:
    url=ubuntu_url
    ISO()

if a==2:
    url=centos_url
    ISO()

if a==3:
    url=windows_server_2k19_url
    ISO()

if a==4:
    url=kali_linux_url
    ISO()

print("Download complete!")
