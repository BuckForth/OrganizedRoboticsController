sudo apt-get -y purge wolfram-engine
sudo apt-get -y purge libreoffice*
sudo apt-get -y clean
sudo apt-get -y autoremove
echo "OpenCV installation by BuckForth cause  learnOpenCV.com cant make a website to save their god damn life"
cvVersion="master"

# install the dependencies
$ sudo apt-get install mesa-common-dev libglu1-mesa-dev freeglut3-dev

# clean build directories
$ rm -rf opencv/build
$ rm -rf opencv_contrib/build

# Create directory for installation
mkdir installation
mkdir installation/OpenCV-"$cvVersion"

# Save current working directory
cwd=$(pwd)

sudo apt -y update
sudo apt -y upgrade

sudo apt-get -y remove x264 libx264-dev
## Install dependencies
sudo apt-get -y install build-essential checkinstall cmake pkg-config yasm
sudo apt-get -y install git gfortran
sudo apt-get -y install libjpeg8-dev libjasper-dev libpng12-dev
sudo apt-get -y install libtiff5-dev
sudo apt-get -y install libtiff-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
sudo apt-get -y install libxine2-dev libv4l-dev
cd /usr/include/linux
sudo ln -s -f ../libv4l1-videodev.h videodev.h
cd $cwd
sudo apt-get -y install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get -y install libgtk2.0-dev libtbb-dev qt5-default
sudo apt-get -y install libatlas-base-dev
sudo apt-get -y install libmp3lame-dev libtheora-dev
sudo apt-get -y install libvorbis-dev libxvidcore-dev libx264-dev
sudo apt-get -y install libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt-get -y install libavresample-dev
sudo apt-get -y install x264 v4l-utils
sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev

# Optional dependencies
sudo apt-get -y install libprotobuf-dev protobuf-compiler
sudo apt-get -y install libgoogle-glog-dev libgflags-dev
sudo apt-get -y install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen

sudo apt-get -y install python3-dev python3-pip
sudo -H pip3 install -U pip numpy
sudo apt-get -y install python3-testresources


cd $cwd
# Install virtual environment
python3 -m venv OpenCV-"$cvVersion"-py3
echo "# Virtual Environment Wrapper" >> ~/.bashrc
echo "alias workoncv-$cvVersion=\"source $cwd/OpenCV-$cvVersion-py3/bin/activate\"" >> ~/.bashrc
source "$cwd"/OpenCV-"$cvVersion"-py3/bin/activate
#############

############ For Python 3 ############
# now install python libraries within this virtual environment
sudo sed -i 's/CONF_SWAPSIZE=100/CONF_SWAPSIZE=1024/g' /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
pip install numpy dlib
# quit virtual environment
deactivate

git clone https://github.com/opencv/opencv.git
cd opencv
git checkout $cvVersion
cd ..
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout $cvVersion
cd ..

cd opencv
mkdir build
cd build

sudo cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \ -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D WITH_TBB=ON -D WITH_V4L=ON -D OPENCV_PYTHON3_INSTALL_PATH=$cwd/OpenCV-py3/lib/python3.5/site-packages -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules -D BUILD_opencv_python3=yes ..

sudo make -j$(nproc)
sudo make install

sudo sed -i 's/CONF_SWAPSIZE=1024/CONF_SWAPSIZE=100/g' /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start

echo "sudo modprobe bcm2835-v4l2" >> ~/.profile