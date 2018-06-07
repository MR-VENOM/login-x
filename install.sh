pkg update && pkg upgrade
pkg install figlet python
clear
echo "##################################################"
echo "coded by"
figlet mr venom
echo "###################################################"
cd $HOME
cd ..
cd usr/etc
echo "python login-x.py" >> bash.bashrc
cd
chmod 777 login/login-x.py
python login-x/login-x.py

