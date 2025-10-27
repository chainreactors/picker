---
title: pixel 3a编译安装android12
url: https://saucer-man.com/android/986.html
source: SAUCERMAN
date: 2022-11-21
fetch_date: 2025-10-03T23:19:27.903190
---

# pixel 3a编译安装android12

* [Home](https://saucer-man.com/)
* [Archives](https://saucer-man.com/archives.html)
* [About](https://saucer-man.com/about.html)
* [Github](https://github.com/saucer-man)

Previous post
Next post
Back to top
Share post

* [0. 设备准备](#cl-1)
* [1. 配置环境](#cl-2)
* [2. 确定源码分支](#cl-3)
* [3. 下载源码](#cl-4)* [方式1](#cl-5)
  * [方式2](#cl-6)
* [4. 下载驱动](#cl-7)
* [5. 代码编译](#cl-8)
* [6. 刷机](#cl-9)
* [7. 参考](#cl-10)

# pixel 3a编译安装android12

2022-11-21

5921

[安卓](https://saucer-man.com/category/android/)

> 文章最后更新时间为：2023年12月10日 14:08:09

## 0. 设备准备

* pixel 3a
* ubuntu20虚拟机 16g内存 300G存储 6核cpu

对于ubuntu20的建议：内存16G起步，存储不低于250G，cpu不低于4核，不然会速度奇慢，并且会有意想不到的错误，比如编译过程出现内存不够

## 1. 配置环境

参考 <https://source.android.google.cn/docs/setup/build/initializing>

```
sudo apt-get install -y git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 libncurses5 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig git curl vim android-sdk android-tools-adb android-tools-fastboot

# 创建一个软连接，ubuntu20默认没有python环境变量
sudo ln -s /usr/bin/python3 /usr/bin/python

# 填上自己的 Name 和 Email
git config --global user.name Your Name
git config --global user.email [email protected]
```

## 2. 确定源码分支

打开 <https://developers.google.com/android/images> ，找到"sargo" for Pixel 3a，sargo是pixel 3a的代号。

![2022-11-20T16:30:48.png](https:////saucer-man.com/usr/uploads/2022/11/3270413301.png "2022-11-20T16:30:48.png")

这里我要编译的是最新版本android12：12.1.0 (SP2A.220505.008, Sep 2022)。(后面Link链接为官方原始ROM，可以直接下载并刷入手机)

下面要确定安卓源码版本ROM与android源码版本对应的分支，打开<https://source.android.google.cn/docs/setup/about/build-numbers> ，可以看到SP2A.220505.008对应的版本是android-12.1.0\_r27

![2022-11-20T16:32:52.png](https:////saucer-man.com/usr/uploads/2022/11/3379802013.png "2022-11-20T16:32:52.png")

确定需要下载的版本对应的分支为android-12.1.0\_r27，这样就不会下错源码了

## 3. 下载源码

### 方式1

```
# 下载repo工具，repo是一种代码版本管理工具，它是由一系列的Python脚本组成，封装了一系列的Git命令，用来统一管理多个Git仓库。
sudo curl https://mirrors.tuna.tsinghua.edu.cn/git/git-repo -o /usr/local/bin/repo
sudo chmod a+x /usr/local/bin/repo

# 修改一下代码源
export REPO_URL='https://mirrors.tuna.tsinghua.edu.cn/git/git-repo/'
mkdir android12
cd android12

# 下载代码，这里加上--depth=1表示只下载最近一次commit，加快速度
repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b android-12.1.0_r27 --depth=1
repo sync -j4
```

下载代码时的-j参数为线程数，这里设置为4一般够用。挂了一个晚上下载完了，其实网速还算快，大概能跑到6Mb/s，只是数据量比较大，粗略估计大概有80G。

### 方式2

除了上面的方式，也可以通过下载完整包的形式来下载源码：

```
# 下载repo工具，repo是一种代码版本管理工具，它是由一系列的Python脚本组成，封装了一系列的Git命令，用来统一管理多个Git仓库。
sudo curl https://mirrors.tuna.tsinghua.edu.cn/git/git-repo -o /usr/local/bin/repo
sudo chmod a+x /usr/local/bin/repo

curl -OC - https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/aosp-latest.tar # 下载初始化包
tar xf aosp-latest.tar
cd AOSP   # 解压得到的 AOSP 工程目录
# 这时 ls 的话什么也看不到，因为只有一个隐藏的 .repo 目录
repo sync # 正常同步一遍即可得到完整目录，同步完之后得到的是master分支的源码

# 然后切换分支
repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b android-12.1.0_r27

# 同步源码树（以后只需执行这条命令来同步）
repo sync
```

## 4. 下载驱动

参考官方文档：<https://source.android.google.cn/docs/setup/build/downloading#obtaining-proprietary-binaries>

在<https://developers.google.cn/android/drivers> 页面找到SP2A.220505.008对应的驱动，两个都要下：

![2022-11-20T16:41:20.png](https:////saucer-man.com/usr/uploads/2022/11/1128114197.png "2022-11-20T16:41:20.png")

```
wget https://dl.google.com/dl/android/aosp/google_devices-sargo-sp2a.220505.008-772e1993.tgz
wget https://dl.google.com/dl/android/aosp/qcom-sargo-sp2a.220505.008-8c718226.tgz
tar -zxf qcom-sargo-sp2a.220505.008-8c718226.tgz
tar zxvf google_devices-sargo-sp2a.220505.008-772e1993.tgz
```

![2022-11-20T16:41:55.png](https:////saucer-man.com/usr/uploads/2022/11/3944149452.png "2022-11-20T16:41:55.png")

解压出来的两个sh脚本拷贝到android源代码目录执行，执行成功后源代码目录多出以下文件夹，其中在执行时，需要输入键盘ENTER和输入I ACCEPT

```
cp extract-qcom-sargo.sh android12/
cp extract-google_devices-sargo.sh android12/
cd android12/
./extract-google_devices-sargo.sh
./extract-qcom-sargo.sh
```

## 5. 代码编译

```
# 下面这步每次打开新终端都需要执行一次
source build/envsetup.sh
lunch
```

然后选择设备版本，可以参考 <https://source.android.com/docs/setup/build/running#selecting-device-build> ，这里我选了aosp\_sargo-userdebug，序号35

```
Which would you like? [aosp_arm-eng] 25

============================================
PLATFORM_VERSION_CODENAME=REL
PLATFORM_VERSION=12
TARGET_PRODUCT=aosp_sargo
TARGET_BUILD_VARIANT=userdebug
TARGET_BUILD_TYPE=release
TARGET_ARCH=arm64
TARGET_ARCH_VARIANT=armv8-a
TARGET_CPU_VARIANT=generic
TARGET_2ND_ARCH=arm
TARGET_2ND_ARCH_VARIANT=armv8-a
TARGET_2ND_CPU_VARIANT=generic
HOST_ARCH=x86_64
HOST_2ND_ARCH=x86
HOST_OS=linux
HOST_OS_EXTRA=Linux-5.15.0-53-generic-x86_64-Ubuntu-20.04.5-LTS
HOST_CROSS_OS=windows
HOST_CROSS_ARCH=x86
HOST_CROSS_2ND_ARCH=x86_64
HOST_BUILD_TYPE=release
BUILD_ID=SP2A.220505.008
OUT_DIR=out
PRODUCT_SOONG_NAMESPACES=device/google/bonito hardware/google/av hardware/google/camera hardware/google/interfaces hardware/google/pixel hardware/qcom/sdm845 vendor/google/camera vendor/qcom/sdm845 vendor/google/interfaces vendor/google_devices/common/proprietary/confirmatioui_hal vendor/google_nos/host/android vendor/google_nos/test/system-test-harness vendor/qcom/sargo/proprietary
============================================
```

然后进行编译，参考<https://source.android.com/docs/setup/build/building>

```
m
用m构建一切。 m可以使用-jN参数处理并行任务。如果您不提供-j参数，构建系统会自动选择它认为最适合您的系统的并行任务计数。
如上所述，您可以通过在m命令行中列出它们的名称来构建特定模块而不是完整的设备映像。此外， m还提供了一些用于特殊目的的伪目标。一些例子是：

droid - m droid是正常构建。这个目标在这里是因为默认目标需要一个名称。
all - m all构建m droid所做的一切，加上没有droid标签的一切。构建服务器运行它以确保构建树中的所有内容并具有Android.mk文件。
m - 从树的顶部运行构建。这很有用，因为您可以从子目录中运行make 。如果您设置了TOP环境变量，它将使用它。如果不这样做，它会从当前目录查找树，试图找到树的顶部。您可以通过不带参数运行m来构建整个源代码树，也可以通过指定它们的名称来构建特定目标。
mma - 构建当前目录中的所有模块及其依赖项。
mmma - 构建提供的目录中的所有模块及其依赖项。
croot - cd到树的顶部。
clean - m clean删除此配置的所有输出和中间文件。这与rm -rf out/相同。
运行m help查看m提供的其他伪目标。
```

编译时遇到问题

```
[ 96% 124885/129423] soong_build docs out/soong/docs/soong_build.html
FAILED: out/soong/docs/soong_build.html
rm -f out/soong/docs/* && out/soong/.bootstrap/bin/soong_build --soong_docs out/soong/docs/soong_build.html "--top" "/home/yanq/Desktop/android12" "--out" "out/soong" "-n" "out" "-d" "out/soong/build.ninja.d" "-t" "-l" "out/.modu
le_paths/Android.bp.list" "-globFile" "out/soong/.bootstrap/build-globs.ninja" "-o" "out/soong/build.ninja" "--available_env" "out/soong/soong.environment.available" "--used_env" "out/soong/soong.environment.used" "Android.bp"
Killed
09:22:38 ninja failed with: exit status 1
```

这是因为内存不够用了，于是减少编译线程数，继续编译即可:

```
m -j4
```

花了四个多小时，编译完毕。

```
[100% 4454/4454] Target vbmeta image: out/target/product/sargo/vbmeta.img
#### build completed successfully (40:49 (mm:ss)) ####
```

如果内存不够，可以通过下面的方式扩充swap分区

```
# 查看swap大小
ubuntu@ubuntu:~/Desktop$ free -m
              total        used        free      shared  buff/cache   available
Mem:          32058        1197       29622           2        1238       30447
Swap:          2047           0        2047
ubuntu@ubuntu:~/Desktop$ cat /proc/swaps
Filename                Type        Size        Used        Priority
/swapfile                               file        2097148        0        -2

# 停止swap
ubuntu@ubuntu:~/Desktop$ sudo swapoff /swapfile
[sudo] password for ubuntu:

# 删除swap
ubuntu@ubuntu:~/Desktop$ sudo rm /swapfile

# 创建新的swap文件，bs×count=最后生成的swap大小，这里设置8G
ubuntu@ubuntu:~/Desktop$ sudo dd if=/dev/zero of=/swapfile bs=1G count=8
8+0 records in
8+0 records out
8589934592 bytes (8.6 GB, 8.0 GiB) copied, 46.8435 s, 183 MB/s

# 设置权限并启用
ubuntu@ubuntu:~/Desktop$ sudo chmod 0600 /swapfile
ubuntu@ubuntu:~/Desktop$ sudo mkswap /swapfile
Setting up swapspace version 1, size = 8 GiB (8589930496 bytes)
no label, UUID=52662ff3-d23c-44e3-8aef-59c3d7baa11f
ubuntu@ubuntu:~/Desktop$ sudo swapon /swapfile

# 查看设置之后的swap是否是8G
ubuntu@ubuntu:~/Desktop$ free -m
              total        used        free      shared  buff/cache   available
Mem:          32058        3526       18252           2       10278       28075
Swap:          8191   ...