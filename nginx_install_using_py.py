import os
def install_nginx():
      os.system('apt-get update -y')
      os.system('apt install nginx -y')
      os.system('systemctl start nginx')
      os.system('systemctl status nginx')
install_nginx()
