---
title: CNFaster 大盘鸡 VNC 重装：实现系统盘与数据盘合并教程
url: https://blog.upx8.com/4692
source: 黑海洋 - IT技术知识库
date: 2025-02-17
fetch_date: 2025-10-06T20:34:28.127086
---

# CNFaster 大盘鸡 VNC 重装：实现系统盘与数据盘合并教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# CNFaster 大盘鸡 VNC 重装：实现系统盘与数据盘合并教程

发布时间:
2025-02-16

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
49571

最近入手了非常火热的：

```
CNFaster HK 240HKD年付，硬盘80HKD一次性付费，内存流量翻倍
```

的大盘鸡，奈何后来不给重新搓盘只能挂载数据盘。所以这篇教程旨在通过重装**将系统盘转换成lvm管理，并且将数据盘和系统盘合二为一**，直接搓成一个完整的大盘。

* 使用一键重装脚本，并重启到 netboot.xyz（可使用商家后台 VNC 手动安装）

```
curl -O https://raw.githubusercontent.com/bin456789/reinstall/main/reinstall.sh || wget -O reinstall.sh $_
bash reinstall.sh netboot.xyz
reboot
```

* 重启后，从CNFaster后台进入vnc
  ![image](https://tu-minio.39.al/lsky/2025/02/15/4501b0d4549429a2e1ad852e192de8ab.png)
* 进入 netboot.xyz
  ![image](https://tu-minio.39.al/lsky/2025/02/15/c78dcf30beacb66b8f6de130d9b4fa34.png)
* 输入后台提供的网络IP 子网掩码 网关
  ![image](https://tu-minio.39.al/lsky/2025/02/15/d6f13d898dfbc7664fc5da739ff04ccc.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/5ecbcae2e6d0d725cd6eca7598b35d58.png)
* 选择网络安装
  ![image](https://tu-minio.39.al/lsky/2025/02/15/121a45cca0617a46c71633b8b75fddd3.png)
* 选择系统和版本（debian12）
  ![image](https://tu-minio.39.al/lsky/2025/02/15/798bac83aa5a064be0b56cd99f87d498.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/221cb35bc2c2a0f9272915df16c5c5e2.png)
* 进入图形化安装界面
  ![image](https://tu-minio.39.al/lsky/2025/02/15/7eff5614ae89916ff28d52fc7cc5a622.png)
* 设置语言，一路默认
  ![image](https://tu-minio.39.al/lsky/2025/02/15/c192317b8028b5d0264511f1f9564d7f.png)
* 手动设置网络，填入后台提供的IP地址掩码网关，DNS我用了8.8.8.8
  ![image](https://tu-minio.39.al/lsky/2025/02/15/45c735cceb83e2e54ebb7a76b68a8930.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/993a7e18def9fab6027babe843f7c830.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/fa9c585dccdb8fe5c96d8da45a41e91f.png)
* 设置root和新建账户密码
  ![image](https://tu-minio.39.al/lsky/2025/02/15/95a83ca637b39fa581f5b9b1310376ee.png)
* **选择设置lvm管理硬盘** **(重要)**
  ![image](https://tu-minio.39.al/lsky/2025/02/15/fc3d3ff6bca6e6003a3ecd9fa51cdcc5.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/1ed7450e2e373f2fdd0d06f46eea5d82.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/9131dc0907b938873e181ed02b65680a.png)
* 写入更改
  ![image](https://tu-minio.39.al/lsky/2025/02/15/573a5ef6ef9d3b12f5c27adf62c0ee73.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/c1f4a6fe10938932fcd1668285ed69b0.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/7fd5408b95d8dc845448bf3ab5d18040.png)
* 开始安装系统
  ![image](https://tu-minio.39.al/lsky/2025/02/15/3d85e0452bc6335fac3a719e2e4c1109.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/529fc53e6991ed63cfd9979df1d05583.png)
* 仅安装系统必要和ssh server
  ![image](https://tu-minio.39.al/lsky/2025/02/15/cd1d82c3155028238f2492cdd1ac2f17.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/ea86dfe523dbd30f5ef3be224c67803e.png)
* **设置grub**（**重要**）
  ![image](https://tu-minio.39.al/lsky/2025/02/15/db9ed2e2723793f19192b7bb50580bde.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/e6d0088d4c8f5068be6b600d688687dc.png)
* 引导安装完成，重启
  ![image](https://tu-minio.39.al/lsky/2025/02/15/27f6b8bfb0f2b139e994ab81e8ba23c8.png)
  ![image](https://tu-minio.39.al/lsky/2025/02/15/3f692e8279201285b8f3463b7e27d3f8.png)
* **注意**：默认只支持用户账户登陆，所以用用户账户登陆后开启root ssh登陆

```
su root
```

![image](https://tu-minio.39.al/lsky/2025/02/15/ee023d2086705572e3ec522591a39864.png)

```
echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
systemctl restart ssh
```

![image](https://tu-minio.39.al/lsky/2025/02/15/12dbf08a3fd5e18bbcbe00dce3b860e2.png)

* 下一步开始拓展lvm空间

```
lsblk
vgs
lvs
```

![image](https://tu-minio.39.al/lsky/2025/02/15/591d12f46ba0324294c450b4b4f37353.png)

* 创建物理卷

```
pvcreate /dev/vdb1
```

![image](https://tu-minio.39.al/lsky/2025/02/15/20c1091abd9c84b18d8662c2bcc6850b.png)

* 扩展volume

```
pvcreate /dev/vdb1
```

![image](https://tu-minio.39.al/lsky/2025/02/15/b09e94be5152f1a7195574409d267ca6.png)

* 拓展所有剩余空间至逻辑卷

```
lvextend -l +100%FREE /dev/debian12-vg/root
```

![image](https://tu-minio.39.al/lsky/2025/02/15/8ac8dc203794abb8d951e2739b83ec78.png)

* resize卷，并查看是否添加成功

```
resize2fs /dev/debian12-vg/root
df -h
```

![image](https://tu-minio.39.al/lsky/2025/02/15/928bf63e0d1c331aa38abb0b4c935500.png)

**至此，扩容完成！**

[取消回复](https://blog.upx8.com/4692#respond-post-4692)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")