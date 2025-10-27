---
title: 安全竞赛中的IoT类题目环境部署方法研究
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247499316&idx=1&sn=19e6c5c7e90a89f32416cd5b4714c7c9&chksm=fa522b8acd25a29cda9cbfcda489a2f471a7cfe3f5b1b6eb2b7b18cc409f46525eb93defc22e&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-12-29
fetch_date: 2025-10-04T02:40:37.181018
---

# 安全竞赛中的IoT类题目环境部署方法研究

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQ9Z8x94lCh0fTFXtT8oNxOic6BbMCwQE3DLKuVAxezBzzag7UOeyB7Asf5ezZNgI0qmC2FJ3lNiaiaw/0?wx_fmt=jpeg)

# 安全竞赛中的IoT类题目环境部署方法研究

原创

智能安全实验室

山石网科安全技术研究院

‍

**‍1**

**前言**

CTF Pwn 静态/动态靶机模版互联网上已经有较为完善的教程文章，单个异构程序的 IoT 题目只需要在互联网已有模版基础上嵌套 qemu-user 即可解决，需要完整异架构系统的 IoT 题目环境部署方案尚存在空缺。本文针对这个问题，给出一套解决方案。

---

**2‍**

**整体架构**

宿主机运行 docker Ubuntu 等基础镜像，docker 内安装 qemu-system 运行完整异构系统，qemu 内运行题目相关服务程序。通过配置 qemu-system 实现动态靶机。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQ9Z8x94lCh0fTFXtT8oNxOweiaysfRhXAg4ZC9c9xavUGTYUxViarskltar98EM4XbwcOZfJhrWBCA/640?wx_fmt=png)

## 准备资源

**所需要文件下载地址：https://people.debian.org/~aurel32/qemu/**。

部署不同环境所需要文件数量不一致，具体看后文，或下载站点 README 。

### arm

* vmlinuz ：系统内核
* initrd ：启动镜像，启动相关的驱动模块
* hda ：磁盘镜像

三者固定搭配，挑选一种下载即可：

```
-kernel vmlinuz-2.6.32-5-versatile -initrd initrd.img-2.6.32-5-versatile -hda debian_squeeze_armel_standard.qcow2
-kernel vmlinuz-2.6.32-5-versatile -initrd initrd.img-2.6.32-5-versatile -hda debian_squeeze_armel_desktop.qcow2
-kernel vmlinuz-3.2.0-4-versatile -initrd initrd.img-3.2.0-4-versatile -hda debian_wheezy_armel_standard.qcow2
-kernel vmlinuz-3.2.0-4-versatile -initrd initrd.img-3.2.0-4-versatile -hda debian_wheezy_armel_desktop.qcow2
```

### mips

* vmlinuz ：系统内核
* hda ：磁盘镜像

两者固定搭配，挑选一种下载即可：

```
-kernel vmlinux-2.6.32-5-4kc-malta -hda debian_squeeze_mips_standard.qcow2
-kernel vmlinux-3.2.0-4-4kc-malta -hda debian_wheezy_mips_standard.qcow2
```

### powerpc

hda ：磁盘镜像

固定搭配，挑选一种下载即可：

```
-hda debian_squeeze_powerpc_standard.qcow2
-hda debian_squeeze_powerpc_desktop.qcow2
-hda debian_wheezy_powerpc_standard.qcow2
-hda debian_wheezy_powerpc_desktop.qcow2
```

**为了方便下面以 arm 为例子记录。**

---

**3‍**

**出题环境 & 流程**

以下为参考出题环境：

* 本地 Ubuntu 虚拟机

+ Qemu-system
+ docker/docker-compose ：用于提供异构环境
+ scp : 用于向 qemu 虚拟机传输文件
+ arm-linux-gnueabi-gcc ：用于异架构程序编译（qemu 内默认没有编译环境）

* 远程 VPS （可选）：用于部署验证

以下为参考顺序，自行根据实际调整：

1. 搭建一个能自启动 qemu 虚拟机，能转发 qemu 虚拟机的 ssh、gdbserver、challenge 等服务，自动挂载 flag 的 docker 镜像
2. 不断重复的出题调试过程

1. 编写源码
2. 编译程序并用 scp 传输到 qemu 虚拟机
3. gdbserver 调试分析并编写 exp

3. 编译并上传最终版程序（去除符号表等操作），并删除 qemu 虚拟机内调试所产生（遗留）与解题无关文件
4. 编写守护进程脚本，守护进程脚本自启动项
5. 重启 qemu 虚拟机验证 flag、服务是否正常。**在 docker kill qemu-system 进程，再运行 run.sh 启动 qemu 虚拟机，不能重启、重编译 docker，否则 qemu 虚拟机将被还原**
6. **最重要一步：在 docker 将 qemu 虚拟机磁盘文件（qcow2）拷贝出来并保存，以后靶机启动的就是这个磁盘文件，就能恢复好搭建完毕的环境**

## qemu网络配置

使用 qemu-system 的 user 网络模式（类似 vmware nat 模式），qemu 启动命令：

```
#!/bin/bash
qemu-system-arm -M versatilepb \
-kernel vmlinuz-3.2.0-4-versatile \
-initrd initrd.img-3.2.0-4-versatile \
-hda debian_wheezy_armel_standard.qcow2 \
-append "root=/dev/sda1 console=tty0" \
-net user,hostfwd=tcp::8888-:22,hostfwd=tcp::8080-:8080,hostfwd=tcp::1234-:1234,restrict=no \
-net nic \
-nographic
```

* `-net nic`：让 qemu 自动配置一张满足最基础需求的虚拟网卡 eth0 ，ip 位置默认为 10.0.2.15
* `-net user,hostfwd=tcp::8888-:22,hostfwd=tcp::8080-:8080,hostfwd=tcp::1234-:1234`：

+ `user` 指定使用 user 模式
+ `hostfwd=tcp::8888-:22,hostfwd=tcp::8080-:8080,hostfwd=tcp::1234-:1234` 映射宿 docker 端口到 qemu 虚拟机中，多端口则按需添加

然后在 Dockerfile 开放对应端口：

```
# challenge
EXPOSE 8080
# ssh
EXPOSE 8888
# gdbserver
EXPOSE 1234
```

docker-compose.yml 配置宿主机到 docker 的映射端口：

```
version: "2"
services:
  game:
    build: .
    restart: unless-stopped
    ports:
      - "12000:8080"
      - "8877:8888"
      - "1234:1234"
```

至此，启动服务后，可以通过 `<宿主机IP:12000>` 等端口访问 qemu 内对应服务。

---

**4‍**

**动态 flag 实现**

**qemu-system 挂载目标需要是文件夹**。各个竞赛平台实现动态 flag 传入方法不尽相同，但通常出题模版会给出 run.sh 文件（供作者在靶机开启后进行自定义操作），解决思路是：

1. 在 Dockerfile 创建固定 flag 文件夹并做好权限管理：/home/ctf/flag

   ```
   COPY ./flag /home/ctf/flag/flag
   ```
2. 在 run.sh 将竞赛平台 flag 写入 /home/ctf/flag/flag

Qemu 启动命令：

```
#!/bin/bash
qemu-system-arm -M versatilepb \
-kernel vmlinuz-3.2.0-4-versatile \
-initrd initrd.img-3.2.0-4-versatile \
-hda debian_wheezy_armel_standard.qcow2 \
-hdb fat:/home/ctf/flag \
-append "root=/dev/sda1 console=tty0" \
-net user,hostfwd=tcp::8888-:22,hostfwd=tcp::8080-:8080,hostfwd=tcp::1234-:1234,restrict=no \
-net nic \
-nographic
```

* `-hdb fat:/home/ctf/flag` ：将 `/home/ctf/flag` 文件挂载，默认权限是只读

Qemu 开机后需要再虚拟机内挂载文件夹：

```
# 创建对应的挂载点
mkdir -p /home/ctf/flag
# 挂载
mount /dev/sdb1 /home/ctf/flag
```

#### 创建开机事件自动挂载

因为 qemu 虚拟机会随靶机开关而开关，需要配置开机自动挂载 flag 。

在 `/etc/init.d` 创建文件 `mount-flag.sh` 写入以下内容：

```
#! /bin/sh
### BEGIN INIT INFO
# Provides:          SkYe231_mount-flag
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Desc ription: mount service
# Desc ription:       mount docker flag
### END INIT INFO
mkdir -p /home/ctf/flag
mount /dev/sdb1 /home/ctf/flag
```

* Provides ：提供者，需要唯一不重复
* 剩余配置项是启动时间等，有需要自己客制化

加上权限：

```
chmod +x mount-flag.sh
```

添加启动事件：

```
insserv -d mount-flag.sh
```

---

**5‍**

**配置自启动 qemu**

测试网络连通转发、flag 挂载正常后，将 qemu 启动命令写入 run.sh ，配置 docker 开机自启动 qemu 方便后续出题工作。

将初步配置的 qemu 虚拟机磁盘镜像提取出来，替换下载的，后续启动的都是这个已配置的镜像

```
docker cp xxx:/home/ctf/xxx.vmdk .
```

run.sh 写入 qemu 启动命令：

```
#!/bin/bash
qemu-system-arm -M versatilepb \
-kernel vmlinuz-3.2.0-4-versatile \
-initrd initrd.img-3.2.0-4-versatile \
-hda debian_wheezy_armel_standard.qcow2 \
-hdb fat:/home/ctf/flag \
-append "root=/dev/sda1 console=tty0" \
-net user,hostfwd=tcp::8888-:22,hostfwd=tcp::8080-:8080,hostfwd=tcp::1234-:1234,restrict=no \
-net nic \
-nographic
```

Dockerfile 配置启动、暴露端口等：

```
COPY ./run.sh /home/ctf
COPY debian_wheezy_armel_standard.qcow2 /home/ctf
COPY initrd.img-3.2.0-4-versatile /home/ctf
COPY vmlinuz-3.2.0-4-versatile /home/ctf
COPY ./flag /home/ctf/flag/flag

# 禁用QEMU音频配置
ENV QEMU_AUDIO_DRV=none

CMD exec /bin/bash -c "./run.sh; trap : TERM INT; sleep infinity & wait"

# challenge
EXPOSE 8080
# ssh
EXPOSE 8888
# gdbserver
EXPOSE 8080
```

docker-compose.yml 配置宿主机映射端口：

```
version: "2"
services:
game:
  build: .
  restart: unless-stopped
  ports:
    - "12000:8080"
    - "8888:8888"
    - "1234:1234"
```

---

**6‍**

**守护进程‍‍‍‍**

确保靶机开启后，重复访问、重复攻击等原因导致服务进程崩溃退出后能自启动。

按照实际需要选择以下两种守护进程方法：

* 每次访问启动全新环境：docker xintd 守护 qemu 虚拟机
* 进程崩溃后恢复沿用此前环境：qemu 虚拟机内守护进程

### xinted 守护 qemu

将 qemu 启动命令写入 run.sh 或者 start.sh 存储。**每次建立链接会启动一个新的 qemu 虚拟机，断开连接则对应 qemu 虚拟机（进程）关闭**，确保 qemu 虚拟机开机速度快，否则链接超时了还没有开启完毕。

```
#!/bin/bash
#ulimit -t 55 #max cpu using
#ulimit -m 524288 #max memory
#ulimit -u 1500 #max process
qemu-system-arm -M versatilepb \
-kernel vmlinuz-3.2.0-4-versatile \
-initrd initrd.img-3.2.0-4-versatile \
-hda debian_wheezy_armel_standard.qcow2 \
-hdb fat:/home/ctf/flag \
-append "root=/dev/sda1 console=tty0" \
-net user,hostfwd=tcp::8888-:22,hostfwd=tcp::8080-:8080,hostfwd=tcp::1234-:1234,restrict=no \
-net nic \
-nographic
```

将 xinted 守护程序替换为 run.sh 或者 start.sh ：

```
service ctf
{
  disable = no
  socket_type = stream
  protocol   = tcp
  wait       = no
  user       = root
  type       = UNLISTED
  port       = 8080
  bind       = 0.0.0.0
  server     = /usr/sbin/chroot
   # replace helloworld to your program
  server_args = --userspec=1000:1000 /home/ctf timeout 50 ./run.sh
  banner_fail = /etc/banner_fail
   # safety options
  per_source= 10 # the maximum instances of this service per source IP address
  rlimit_cpu= 60 # the maximum number of CPU seconds that the service may use
  rlimit_as = 1024M # the Address Space resource limit for the service
   #access_times = 2:00-9:00 12:00-24:00

   #Instances=20 #process limit
   #per_source=5 #link ip limit

   #log warning die
  log_on_success = PID HOST EXIT DURATION
  log_on_failure =HOST ATTEMPT
  log_type =FILE /var/log/myservice.log 8388608 15728640

}
```

* `server_args` ：修改调整为 run.sh
* 其他配置可以参考，根据需要客制化

### qemu 内守护进程

> 使用 shell 脚本实现守护进程，配置为开机自启动项

`/etc/init.d` 创建守护进程 shell 脚本 `challenage-start-agent.sh`，写入内容：

```
#!/bin/bash
PROGRAM=httpd

while true; do
       RESULT=`ps aux | grep -w ${PROGRAM} | grep -v grep | wc -l`

       if [ ${RESULT} = 0 ];then
               # echo "${PROGRAM} was killed"
               cd /var/www/html
              ./httpd 2>/dev/null 1>&2 &...