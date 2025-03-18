#1.1总体概述
本系统部署需要经过环境初始化、CUDA安装、数据库初始化、源代码配置等过程。以下过程在ubuntu22.04和ubuntu20.04上成功测试，不建议在Windows server上进行部署。
部署软件准备：
服务器三台、产品源代码（vue项目文件需要进行发布为html）
#1.2系统配置要求
硬件要求：云服务器2H4G5M一台，6g显存NVIDIA显卡以上配置本地服务器两台以上配置
系统要求：Ubuntu18.04以上。
#1.3 Cuda11.8安装
采用二进制文件编译安装
##1）环境准备ubuntu：
sudo apt update
sudo apt instal  gcc gcc-c++ kernel-devel  build-essential
##2)Nvidia驱动版本建议520以上
禁用nouveau驱动
Sudo nano /etc/modprobe.d/blacklist-nvidia-nouveau.conf
写入以下内容
blacklist nouveau
options nouveau modeset=0
保存之后编译内核并重启
sudo update-initramfs -u & reboot
##3)下载Cuda11.8的二进制文件，内包含了520版本的驱动
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run  
##4)编译安装
sudo sh cuda_11.8.0_520.61.05_linux.run
##5)修改环境变量
Sudo nano ~/.bashrc  
添加如下内容
export PATH=/usr/local/cuda-11.8/bin${PATH:+:${PATH}}  
export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}  
source ~/.bashrc  
##6)安装验证
Nvcc -V查看cuda版本信息  
Nvidia-smi查看显卡相关信息
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Wed_Sep_21_10:33:58_PDT_2022
Cuda compilation tools, release 11.8, V11.8.89
Build cuda_11.8.r11.8/compiler.31833905_0
显示信息类似上图即为安装成功
#1.4 miniconda环境的安装和配置
##1）wget下载源文件
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  
##2）sh命令执行编译安装
sh Miniconda3-latest-Linux-x86_64.sh  
安装提示进行安装即可
##3）创建python3.8.10环境
conda create -n your_env_name python=3.8.10
##4）安装pytorch cuda版本
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  
