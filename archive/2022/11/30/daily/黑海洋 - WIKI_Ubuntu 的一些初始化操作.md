---
title: Ubuntu 的一些初始化操作
url: https://blog.upx8.com/3120
source: 黑海洋 - WIKI
date: 2022-11-30
fetch_date: 2025-10-04T00:05:26.056136
---

# Ubuntu 的一些初始化操作

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Ubuntu和Debian 初始化

发布时间:
2022-11-29

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
25337

最近来来回回折腾了上百次服务器，每次折腾总要做一些重复的操作，挺麻烦，干脆记录一些常用操作，方便日后复制粘贴。

## [一键网络DD脚本](https://blog.upx8.com/go/LzMwMzU)

重装系统组件：`apt-get install -y xz-utils openssl gawk file wget screen && screen -S os`
一键DD脚本：`wget --no-check-certificate -O NewReinstall.sh https://git.io/newbetags && chmod a+x NewReinstall.sh && bash NewReinstall.sh`

## 更新apt包及依赖（新机器必须运行一次，此后无需运行）

`apt update && apt install -y curl wget sudo gnupg2 htop gcc git cmake`

## [安装适用于流媒体的XanMod内核开启BBR2](https://blog.upx8.com/go/LzMwODU)（FQ+PIE）

`echo 'deb http://deb.xanmod.org releases main' | tee /etc/apt/sources.list.d/xanmod-kernel.list`
`wget -qO - https://dl.xanmod.org/gpg.key | apt-key --keyring /etc/apt/trusted.gpg.d/xanmod-kernel.gpg add -`
`apt update && apt install linux-xanmod-rt-edge -y && reboot`

## 修改时区

修改为 UTC 时区：`timedatectl set-timezone UTC`
修改为中国时区：`timedatectl set-timezone Asia/Shanghai`

timedatectl set-timezone Asia/Shanghai # 设置系统时区为上海

timedatectl set-timezone Asia/Tokyo # 设置系统时区为东京

timedatectl set-timezone Asia/Kolkata #【设置印度时区】

timedatectl set-timezone America/New\_York #【设置美国纽约的时区】

## [一键更换国内软件源脚本](https://blog.upx8.com/go/LzMwMTE)

`bash <(curl -sSL https://gitee.com/SuperManito/LinuxMirrors/raw/main/ChangeMirrors.sh)`

## [Debian/Ubuntu 安装卸载和配置 UFW（简单防火墙）](https://blog.upx8.com/go/LzMxODA)

```
#开放所有端口
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -F

Ubuntu镜像默认设置了Iptable规则，防火墙解除（甲骨文云）
apt autoremove netfilter-persistent* -y
reboot
或者强制删除
rm -rf /etc/iptables && reboot
```

## [Linux常用脚本](https://blog.upx8.com/go/LzMwOTU)（测速.bbr等）

```
wget -O jcnfbox.sh https://raw.githubusercontent.com/Netflixxp/jcnf-box/main/jcnfbox.sh && chmod +x jcnfbox.sh && clear && ./jcnfbox.sh
```

## [Toolbox 工具箱（推荐）](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3dkbTE3MzI0MTgzNjUvdnBzdG9vbGJveA)

```
wget -N https://cdn.jsdelivr.net/gh/ednovas/vpstoolbox@main/ednovastool.sh && chmod +x ednovastool.sh && ./ednovastool.sh
```

## 重新安装 vim

`apt update`
`apt remove vim-common -y`
`apt install vim -y`

## 生成 SSH 登录密钥

`ssh-keygen`
`cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`
`chmod 700 ~/.ssh`
`chmod 600 ~/.ssh/authorized_keys`

## 开启root用户登录

`sudo -i
echo root:123123 |sudo chpasswd root
sudo sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin yes/g' /etc/ssh/sshd_config;
sudo sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config;
service sshd restart`

## SSH超时断开时间设置

`vi /etc/ssh/sshd_config`

`ClientAliveInterval 60      # server每隔60秒给客户端发送一次保活信息包给客户端
ClientAliveCountMax 86400   # server端发出的请求客户端没有回应的次数达到86400次的时候就断开连接，正常情况下客户端都会相应`

`service ssh restart         # 重启配置文件`

## 安装 Node.js

`curl -sL https://deb.nodesource.com/setup_lts.x -o nodesource_setup.sh`
`bash nodesource_setup.sh`
`apt install nodejs -y`
`npm install npm -g`

## BuyVM 挂载数据盘

查询硬盘：`ls /dev/disk/by-id/`
格式化：`mkfs.ext4 -F /dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-0000`
挂载：`mount -o discard,defaults /dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-0000 /data`
开机挂载：`echo '/dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-0000 /data ext4 defaults,nofail,discard 0 0' | sudo tee -a /etc/fstab`

## 禁止 ping

```
nano /etc/sysctl.conf
```

在文件末尾增加一行

```
net.ipv4.icmp_echo_ignore_all = 1
```

## Ubuntu 一键安装 Maven

Apache Maven是主要用于Java项目的开源项目管理和理解工具。Maven使用项目对象模型POM。

POM对象本质上是一个XML文件，其中包含项目配置详细信息，项目的依赖关系等的信息。

使用`apt`在Ubuntu 20.04安装Maven是一个简单，直接的过程。首先是更新软件包索引运行命令`sudo apt update`。

然后就是运行命令`sudo apt install maven`安装Maven。要验证安装，可以运行命令`mvn -version`，命令将会打印Maven的版本号。

```
sudo apt update
sudo apt install maven
mvn -version
```

Bash

Copy

```
Apache Maven 3.6.3
Maven home: /usr/share/maven
Java version: 11.0.7, vendor: Ubuntu, runtime: /usr/lib/jvm/java-11-openjdk-amd64
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "5.4.0-26-generic", arch: "amd64", family: "unix"
```

现在，Maven已安装在Ubuntu 20.04系统，您可以开始使用它。

## Ubuntu 一键安装 JDK

在Ubuntu系统安装JDK的最简单方法是通过APT包管理器进行安装，执行以下步骤即可：

1.更新系统软件包列表：

```
sudo apt update
```

2.安装JDK 8：

```
sudo apt install openjdk-8-jdk
```

3.验证JDK是否安装成功：

```
java -version
```

如果JDK成功安装，应该能够看到类似如下输出：

```
openjdk version "1.8.0_292"
OpenJDK Runtime Environment (build 1.8.0_292-b10)
OpenJDK 64-Bit Server VM (build 25.292-b10, mixed mode)
```

## 安装docker

```
wget -qO- get.docker.com | bash
```

## 禁止密码登录SSH，只允许密钥登录

```
bash <(curl -fsSL git.io/key.sh) -og AAAAA -p 77777 -d
```

## 证书申请安装

1，安装证书工具

`curl https://get.acme.sh | sh; apt install socat -y || yum install socat -y; ~/.acme.sh/acme.sh --set-default-ca --server letsencrypt`

2、申请证书
`~/.acme.sh/acme.sh --issue -d 你的域名 --standalone -k ec-256 --force --insecure`

3、安装证书
`~/.acme.sh/acme.sh --install-cert -d 你的域名 --ecc --key-file /etc/server.key --fullchain-file /etc/server.crt`

---

## 一键修复脚本

运行所有一键修复脚本前注意看说明，以及保证服务器无重要数据，运行后造成的一切后果作者不负任何责任，自行评判风险！

#### 一键尝试修复apt源

* 支持系统：Ubuntu 12+，Debian 6+
* 修复apt下载包进程意外退出导致的源锁死
* 修复apt源broken损坏
* 修复apt源多进程占用锁死
* 修复apt源公钥缺失
* 修复替换系统可用的apt源列表，国内用阿里源，国外用官方源
* 修复本机的Ubuntu系统是EOL非长期维护的版本(奇数或陈旧的偶数版本)，将替换为Ubuntu官方的old-releases仓库以支持apt的使用
* 修复只保证`apt update`不会报错，其他命令报错未修复
* 如若修复后install还有问题，重启服务器解决问题

```
curl -L https://raw.githubusercontent.com/spiritLHLS/one-click-installation-script/main/repair_scripts/package.sh -o package.sh && chmod +x package.sh && bash package.sh
```

#### 一键尝试修复系统时间

* 支持系统：Ubuntu 18+，Debian 8+，centos 7+，Fedora，Almalinux 8.5+
* 由于系统时间不准确都是未进行时区时间同步造成的，使用chronyd进行时区时间同步后应当解决了问题

```
curl -L https://raw.githubusercontent.com/spiritLHLS/one-click-installation-script/main/repair_scripts/modify_time.sh -o modify_time.sh && chmod +x modify_time.sh && bash modify_time.sh
```

#### 一键尝试修复sudo警告

* 一键尝试修复`sudo: unable to resolve host xxx: Name or service not known`警告(爆错)

不要在生产环境上使用该脚本，否则容易造成网络hosts配置错误，配置的host名字不在外网IP上反而在内网IP(127.0.0.1)上

```
curl -L https://raw.githubusercontent.com/spiritLHLS/one-click-installation-script/main/repair_scripts/check_sudo.sh -o check_sudo.sh && chmod +x check_sudo.sh && bash check_sudo.sh
```

#### 一键修改系统自带的journal日志记录大小释放系统盘空间

* 支持系统：Ubuntu 18+，Debian 8+，centos 7+，Fedora，Almalinux 8.5+
* 1.自定义修改大小，单位为MB，一般500或者1000即可，有的系统日志默认给了5000甚至更多，不是做站啥的没必要
  + 请注意，修改journal目录大小会影响系统日志的记录，因此，在修改journal目录大小之前如果需要之前的日志，建议先备份系统日志到本地
* 2.自定义修改设置系统日志保留日期时长，超过日期时长的日志将被清除
* 3.默认修改日志只记录warning等级(无法自定义)
* 4.以后日志的产生将受到日志文件大小，日志保留时间，日志保留等级的限制

```
curl -L https://raw.githubusercontent.com/spiritLHLS/one-click-installation-script/main/repair_scripts/resize_journal.sh -o resize_journal.sh && chmod +x resize_journal.sh && bash resize_journal.sh
```

#### 一键尝试修复网络

**该脚本轻易勿要使用，请确保运行时服务器无重要文件或程序，出现运行bug后续可能需要重装系统**

**一定要在screen中执行该脚本，否则可能导致修改过程中ssh断链接而修改失败卡住最终SSH无法连接！不在screen中执行后果自负！**

* 支持系统：Ubuntu 18+，Debian 8+，centos 7+，Fedora，Almalinux 8.5+
* 尝试修复nameserver为google源或cloudflare源
* 尝试修复为IP类型对应的网络优先级(默认IPV4类型，纯V6类型再替换为IPV6类型)

```
curl -L https://cdn.spiritlhl.workers.dev/https://raw.githubusercontent.com/spiritLHLS/one-click-installation-script/main/repair_scripts/network.sh -o network.sh && chmod +x network.sh && bash network.sh
```

如果是纯V6的也可以不使用上面脚本的nat64，使用warp添加V4网络

比如：[https://gitlab.com/fscarmen/warp](https://blog.upx8.com/go/aHR0cHM6Ly9naXRsYWIuY29tL2ZzY2FybWVuL3dhcnA)

```
wget -N https://gitlab.com/fscarmen/warp/-/raw/main/menu.sh && bash menu.sh [option] [lisence/url/token]
```

非纯V6的，带V4切换优先级到IPV4可用以下命令

```
sudo sed -i 's/.*precedence ::ffff:0:0\/96.*/precedence ::ffff:0:0\/96  100/g' /etc/gai.conf && sudo systemctl restart networking
```

#### 一键解除进程数限制

```
curl -L https://raw.githubusercontent.com/spiritLHLS/one-click-installation-script/main/repair_scripts/unlimit.sh -o unlimit.sh && chmod +x unlimit.sh && bash unlimit.sh
```

## 一键环境安装脚本

只推荐在新服务器上安装，环境不纯净不保证不出bug

运行所有一键环境安装脚本前注意看说明，以及保证服务器无重要数据，运行后造成的一切后果作者不负任何责任，自行评判风险！

#### 一键安装jupyter环境

* **本脚本尝试使用Miniconda3安装虚拟环境jupyter-env再进行jupyter和jupyterlab的安装，如若安装机器不纯净勿要轻易使用本脚本！**
* **本脚...