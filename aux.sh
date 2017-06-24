add-apt-repository ppa:openjdk-r/ppa
apt-get install -y python-pip && python-pil
apt-get update
apt-get install -y openjdk-8-jdk && pyqt4-dev-tools && xdotool && scrot
pip install -y pyscreenshot
update-alternatives --config java
apt-get upgrade -y
apt-get update

eval $(dbus-launch --sh-syntax)
export DBUS_SESSION_BUS_ADDRESS
export DBUS_SESSION_BUS_PID
export QT_X11_NO_MITSHM=1


