# 系统部署说明
## 一、总体概述
本系统部署包含环境初始化、CUDA安装、数据库初始化、源代码配置等步骤。已在ubuntu22.04和ubuntu20.04上成功测试，不推荐在Windows server上部署。

### 部署软件准备
1. 服务器三台
2. 产品源代码（vue项目文件需发布为html）

## 二、系统配置要求
### 硬件要求
1. 一台云服务器：2H4G5M配置
2. 两台及以上本地服务器：配置6g显存NVIDIA显卡及以上

### 系统要求
Ubuntu 18.04及以上版本

## 三、Cuda11.8安装
采用二进制文件编译安装方式，具体步骤如下：
### 1. 环境准备（ubuntu）
```bash
sudo apt update
sudo apt install gcc gcc-c++ kernel-devel build-essential
```
### 2. Nvidia驱动版本要求
建议使用520以上版本。
#### 禁用nouveau驱动
1. 打开配置文件：
```bash
sudo nano /etc/modprobe.d/blacklist-nvidia-nouveau.conf
```
2. 写入以下内容：
```
blacklist nouveau
options nouveau modeset=0
```
3. 保存后编译内核并重启：
```bash
sudo update-initramfs -u & reboot
```
### 3. 下载Cuda11.8二进制文件
该文件包含520版本的驱动，执行以下命令下载：
```bash
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
```
### 4. 编译安装
```bash
sudo sh cuda_11.8.0_520.61.05_linux.run
```
### 5. 修改环境变量
1. 打开环境变量配置文件：
```bash
sudo nano ~/.bashrc
```
2. 添加如下内容：
```bash
export PATH=/usr/local/cuda-11.8/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
3. 使配置生效：
```bash
source ~/.bashrc
```
### 6. 安装验证
1. 查看cuda版本信息：
```bash
nvcc -V
```
2. 查看显卡相关信息：
```bash
nvidia-smi
```
当显示信息类似以下内容时，即为安装成功：
```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Wed_Sep_21_10:33:58_PDT_2022
Cuda compilation tools, release 11.8, V11.8.89
Build cuda_11.8.r11.8/compiler.31833905_0
```

## 四、miniconda环境的安装和配置
### 1. 下载源文件
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
### 2. 执行编译安装
```bash
sh Miniconda3-latest-Linux-x86_64.sh
```
根据安装提示进行安装。
### 3. 创建python3.8.10环境
```bash
conda create -n your_env_name python=3.8.10
```
### 4. 安装pytorch cuda版本
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
### 5. 检查cuda加速的torch是否安装成功
编写Python脚本进行检查：
```python
import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.version.cuda)
```
若pytorch安装成功即可导入，同时可查看CUDA是否可用、可用的CUDA数量及CUDA的版本号。

## 五、apache网页环境和springboot环境准备
### 1. 安装相关包
```bash
sudo apt update
sudo apt install openjdk-8-jdk apache2
```
### 2. Jar文件部署
由于文件大小原因，未提供Jar文件，需使用idea通过maven进行打包。使用以下命令让程序在后台运行：
```bash
nohup java -jar xxx.jar > jar_back.out 2>&1 &
```
### 3. Html网页部署
将提供的网页文件复制到/var/www目录下，并删除或更名原来的index.html网页。

## 六、系统运行和其他注意事项
### 1. 系统运行
完成前后端模块部署后，可通过安装了apache2的网页进行访问。需检查部署服务器的相关端口是否打开以及防火墙是否放行。
### 2. 设置内网穿透
#### frp安装
由于使用两台本地服务器作为gpu运算服务器，需为这两台本地服务器配置frp内网穿透以实现外网正常访问。若仅在内网测试，则无需安装和配置。 
