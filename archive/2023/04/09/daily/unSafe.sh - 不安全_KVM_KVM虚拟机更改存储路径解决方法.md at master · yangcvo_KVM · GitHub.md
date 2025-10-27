---
title: KVM/KVM虚拟机更改存储路径解决方法.md at master · yangcvo/KVM · GitHub
url: https://buaq.net/go-157709.html
source: unSafe.sh - 不安全
date: 2023-04-09
fetch_date: 2025-10-04T11:29:07.924944
---

# KVM/KVM虚拟机更改存储路径解决方法.md at master · yangcvo/KVM · GitHub

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

KVM/KVM虚拟机更改存储路径解决方法.md at master · yangcvo/KVM · GitHub

KVM虚拟机更改存储路径解决方法玩kvm的2014年开始慢慢接触了，发现功能特别大，比vm好用，vm是基于Windows上面需要安装客户端登陆很麻烦,也有人说也有web管理端其实我觉得运维
*2023-4-8 22:57:40
Author: [github.com(查看原文)](/jump-157709.htm)
阅读量:32
收藏*

---

## KVM虚拟机更改存储路径解决方法

玩kvm的2014年开始慢慢接触了，发现功能特别大，比vm好用，vm是基于Windows上面需要安装客户端登陆很麻烦,也有人说也有web管理端其实我觉得运维在kvm伸缩现在很火的openstack也是底层kvm去生成虚拟机的。

kvm 在之前的搭建环境 一开始安装指定的虚拟机镜像没有放到挂载单独的一块硬盘路径。后果会不堪设想。

kvm服务器：

```
IP：192.168.1.250
镜像存储路径：/opt/vm/
默认的xml文件路径：/etc/libvirt/qemu
```

发现MySQL的服务器已经`挂了`。=\_=

登陆到kvm：

一开始我MySQL跟MySQL主从存储路径都在`/opt/vm/mysql.img` 、`/opt/vm/mysql-2.img`

这里我看了下这两台服务器都已经挂了，因为kvm空间被根目录被吃光了，一开始就没有注意这个配置，后面我在 创建/home/vm/，分了块硬盘空间挂载到这个目录下面。

### 先不要：

把/opt/vm/mysql.img 直接mv到了/home/vm/.

### 这里第一步：

需要先停掉虚拟机。如果虚拟机已经挂了，在kvm用virsh查看下。

如果暂停说明已经卡死了。那么shutdown 也是无效的。

这里可以查看我写的篇：[kvm-hellp帮助篇](http://blog.yangcvo.me/2015/06/18/KVM%E8%99%9A%E6%8B%9F%E5%8C%96%E5%AE%9E%E7%94%A8%E7%AF%87-%E7%AC%AC%E4%BA%8C%E7%AF%87-help%E5%B8%AE%E5%8A%A9%E6%96%87%E6%A1%A3%E5%A4%A7%E5%85%A8/)-只对kvm入门人员帮助

```
virsh undefine $1   删除虚拟机取消定义   删除虚拟机先执行这个 取消定义。
```

强制关闭虚拟机：

```
virsh undefine mysql
virsh undefine mysql-2
```

### 这里第二步移动镜像存储目录：

然后： 把/opt/vm/mysql.img 直接mv到了/home/vm/.
移动指定的目录。

### 第三步需要修改xml文件

这里一开始遇到很多头大的问题：

* 第一我直接vim /etc/libvirt/qemu/mysql.xml
* 第一我直接vim /etc/libvirt/qemu/mysql-2.xml

这样修改了以后是不能生效的。而且一错在错，因为如果改完了以后直接去启动MySQL

提示：`/opt/vm/ 下没有 mysql-2.img`

[![](https://camo.githubusercontent.com/65ed5d27bcd05bfd5e452a5f2ae23042ab7502664d2c64ca522ae553fbc46b43/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d332e706e67)](https://camo.githubusercontent.com/65ed5d27bcd05bfd5e452a5f2ae23042ab7502664d2c64ca522ae553fbc46b43/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d332e706e67)

这里我知道是没有生效，就取消了定义mysql-2 取消定义需要删除快照才能取消定义。

这里又做错了一步：

### 如何取消定义虚拟机

[![](https://camo.githubusercontent.com/c4c62d596885213701813ca45d87840ac42a5c74a417d941d8737cf90ab68ded/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d322e706e67)](https://camo.githubusercontent.com/c4c62d596885213701813ca45d87840ac42a5c74a417d941d8737cf90ab68ded/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d322e706e67)

我把自己辛辛苦苦的快照都删除了，然后取消了定义。

### 注意：

发现取消了定义以后，我的/etc/libvirt/qemu/mysql-2.xml 已经被删除了，取消定义是会删除xml文件的。所以这个时候发现自己大错特错，之前忘记了一个重要的操作。
这里我发现我MySQL已经被删除了。可是镜像文件还是在/home/vm/mysql-2.img
还好我做了主从，删除了只是其中一台。这个时候求助了之前搞虚拟化的朋友--`甜橙大神`。

### 紧急修复

这里我在他的指导帮助下搞定了。

### 修复第一步：

我这里先拷贝了一份其他虚拟机的xml文件,做相应修改.

然后打开文件：

name uuid img 之类的都要修改

* 先删除:uuid- uuid 可以不填-删除这行就行了

```
<uuid>876f7ff7-a0e7-f64d-fc3c-bc48fee28635</uuid>
```

* 改成自己恢复的镜像。

```
 <source file='/home/vm/mysql-2.img'/>
```

* 修改网卡信息：

```
  <mac address='52:54:00:e9:cb:c4'/>
```

这里的是拷贝过来的，所以你稍微做下修改，我这里把F1改成了c4.

* 修改VNC链接的端口

```
<graphics type='vnc' port='5950' autoport='no' listen='0.0.0.0'>
      <listen type='address' address='0.0.0.0'/>
```

这里是我拷贝过来的，所以5950我改成了我之前MySQL的5941的。

改好后保存退出。。

### 启动虚拟机-加载xml文件。

重新定义xml文件

```
virsh # define /etc/libvirt/qemu/mysql-2.xml
定义域 mysql-2（从 /etc/libvirt/qemu/mysql-2.xml）
virsh # start mysql
域 mysql 已开始
```

这里显示已经启动成功了。所以取消定义是最危险的。因为没有备份xml文件。

### VNC连接修改网卡信息。

这里需要用VNC连接到这台服务器，然后修改网卡信息。

这里查看网卡信息，没有IP，在查看if-eth0
[![](https://camo.githubusercontent.com/fe147ac7f328f117972e78e5d9d9fce96114bff15f258a5f19e65ca97b159384/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d342e706e67)](https://camo.githubusercontent.com/fe147ac7f328f117972e78e5d9d9fce96114bff15f258a5f19e65ca97b159384/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d342e706e67)

需要修改mac地址：

[![](https://camo.githubusercontent.com/4b4cd6af12f83061ec12ddc691d63b6d12d2e6585c41dc6414a9f4641e96516f/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f6b766d352e706e67)](https://camo.githubusercontent.com/4b4cd6af12f83061ec12ddc691d63b6d12d2e6585c41dc6414a9f4641e96516f/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f6b766d352e706e67)

改完保存退出。这个时候重启网卡。会发现报错。

[![](https://camo.githubusercontent.com/e40edc1d715b7a61fcf865a5df46bcec742ba69f86dcb66f9572ad079d526674/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d362e706e67)](https://camo.githubusercontent.com/e40edc1d715b7a61fcf865a5df46bcec742ba69f86dcb66f9572ad079d526674/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d362e706e67)

centos6.5，查看 `/etc/udev/rules.d/70-net*` 文件，确保里面`eth0` 的mac 跟xml里 的一样

[![](https://camo.githubusercontent.com/4fa94e5e88cb5551420d476237408587d59d711a93fc2b33ae63c348cf311e4f/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d372e706e67)](https://camo.githubusercontent.com/4fa94e5e88cb5551420d476237408587d59d711a93fc2b33ae63c348cf311e4f/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d372e706e67)

这里修改eth0 的mac 到xml里的，删了eth1
重启就可以了。

[![](https://camo.githubusercontent.com/3f71cb2c1d310c59e889f470b0adba7d1ad57707c12c100b2196cc9d6a8e0311/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d382e706e67)](https://camo.githubusercontent.com/3f71cb2c1d310c59e889f470b0adba7d1ad57707c12c100b2196cc9d6a8e0311/687474703a2f2f3778727468772e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f4b564d382e706e67)

现在已经恢复回来了。

### 切记

xml文件修修改改就行了，还是不要随便删了 。

### 这里的最简单解决方法：

---

文章来源: https://github.com/yangcvo/KVM/blob/master/KVM%E8%99%9A%E6%8B%9F%E6%9C%BA%E6%9B%B4%E6%94%B9%E5%AD%98%E5%82%A8%E8%B7%AF%E5%BE%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95.md
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)