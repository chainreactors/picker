---
title: VulnTarget-P 纯IPv6下的攻防与数据恢复实战
url: https://mp.weixin.qq.com/s/FBQFyPPTj4Q9YjLn6rkJuw
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:32:21.646137
---

# VulnTarget-P 纯IPv6下的攻防与数据恢复实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JQpUg1oh5afia0iaDaUcPFHTZmwBUx4Uj2sgecJ8icLuibNZmD86eRlyUeChyuysfLPFHG5wXSPjS0upTQposK2pwWicYlKabRJhrXyakGvaMO3c/0?wx_fmt=jpeg)

# VulnTarget-P 纯IPv6下的攻防与数据恢复实战

泷羽Sec

![]()

在小说阅读器中沉浸阅读

以下文章来源于乌鸦安全
，作者crow

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4lAxeKZF8nSeG0iamwdwRJdiaNtgAXeVSXXhib5PiavhdBuw/0)

**乌鸦安全**
.

专注于网络安全技术分享，红蓝对抗技术、免杀、反制、内网漫游、安全研究。

（）

`✎ 阅读须知

乌鸦安全的技术文章仅供参考，此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。

乌鸦安全拥有对此文章的修改、删除和解释权限，如转载或传播此文章，需保证文章的完整性，未经允许，禁止转载！

本文所提供的工具仅用于学习，禁止用于其他，请在24小时内删除工具文件！！！

[2026HVV招聘倒计时，未毕业+应届可投！](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247512499&idx=1&sn=612fa28260a1b09dbb72cf61d8e288ef&scene=21#wechat_redirect)

更新时间：`2026年03月28日22:28:22`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JQpUg1oh5af901UK7OM8736GelE5wVM3ZHLKwnSatj74wDJsTIfRHlVKPbmMuUiasZtvLY758fTWTOY8pay7XrIOGIk4722REQEBahr9VDjA/640?wx_fmt=png&from=appmsg)

`vulntarget`靶场系列仅供安全专业人员练习渗透测试技术，此靶场所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用靶场中的技术资料对任何计算机系统进行入侵操作。利用此靶场所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。
`vulntarget`靶场系列拥有对此靶场系列的的修改、删除和解释权限，未经授权，不得用于其他！

`靶场地址：``https://github.com/crow821/vulntarget`

```
下载地址：
百度云
链接: https://pan.baidu.com/s/1sv9qdioNF4PTUliix5HEfg 提取码: 2dwq

夸克网盘：
链接：https://pan.quark.cn/s/e65bf3efbf0b?pwd=GHgE 提取码：GHgE
```

# 1. 靶场概述

`VulnTarget-P` 是专为纯`IPv6`网络环境打造的渗透测试、攻防实战+应急数据恢复靶场，核心聚焦纯`IPv6`场景下的渗透技巧实战与`MySQL`数据库误删数据应急恢复，兼顾漏洞挖掘、内网渗透、权限获取、数据修复等多项实战能力训练，贴合当下`IPv6`网络普及的实战攻防需求。

本靶场共包含两台基于 `Ubuntu Server 22.04` 系统制作的靶机，整体场景适配`VMware`虚拟化平台，已在`Mac`、`Windows`系统环境下完成搭建与测试，运行稳定。

**本环境经过多次搭建、测试而来，中间的ip地址、图片不对应是正常情况，不影响本文阅读和使用。**

# 2. 靶机配置详情

### 2.1 靶机01（`Ubuntu22_tp`）

* **系统版本**：`Ubuntu Server 22.04`
* **网卡配置**：双网卡，适配内外网穿透场景
* **IPv6地址**：`fd00:3333:6666::128`、`fd00:6666:8888::128`
* **特殊机制**：内置模拟`WAF`安全防护，具备定时删除文件的防护规则，提升渗透实战难度。
* 账号密码信息：vuln:vulntarget@123

### 2.2 靶机02（`Ubuntu22_mysql`）

* **系统版本**：`Ubuntu Server 22.04`
* **IPv6地址**：`fd00:6666:8888::130`
* **数据库场景**：内置 `vulntarget` 数据库，模拟攻击者恶意删除操作，已清空 `id=40` 至 `id=60` 的全部用户数据，需完成数据恢复。
* 账号密码信息：root:888888

### 2.3 攻击机配置建议

推荐选用 `Kali Linux` 作为攻击机，为适配纯`IPv6`打靶需求，建议配置双网卡：

* **IPv6地址**：`fd00:3333:6666::100`
* 额外配置`NAT`网络，便于网页访问、工具安装、依赖更新等操作
* 注：上述所有`IPv6`地址仅为推荐配置，可根据个人使用习惯自定义修改

# 3. 打靶核心要求

本靶场内置两个`Flag`，但**不以单纯获取`Flag`为最终目标**，主打无限制实战演练，鼓励尝试多种渗透思路与技术方案，核心训练目标如下：

* 攻克靶机01，获取命令执行权限（核心）
* 获取靶机01内置`Flag`
* 获取靶机02内置`Flag`
* 完成靶机02的数据库数据恢复，还原全部`200`条完整数据（核心）
* 全程严格遵循纯`IPv6`网络打靶规则，禁止使用`IPv4`网络开展渗透操作

# 4. 核心考察知识点

本靶场全面覆盖纯`IPv6`网络环境下的各类实战攻防技能，重点考察以下技术点：

* `IPv6`端口扫描技术
* `IPv6`目录遍历与目录扫描技术
* `IPv6`场景漏洞挖掘与漏洞利用技术
* `IPv6`内网探测与横向移动技术
* Ipv6下的内网代理搭建与流量转发技术
* `Ipv6`下的`Webshell`使用
* `IPv6`场景服务暴力破解技术
* `MySQL`数据库误删数据应急恢复技术

# 5. Hint

* 靶机01内置模拟`WAF`防护，会定时清理可疑文件，渗透时需灵活规避防护机制
* 场景搭建贴合实战，单漏洞难度较低，但综合之后难度偏高。

# 6. 网络配置

### 6.1网络拓扑结构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JQpUg1oh5acF7URt2VjCnMJiciclrbczaKk8J1SfcrbAph3rUrE8VDBasDDsl3JMopLAIwlm0ic0CsI9r21lfOric2lzbuT2Naj9VxLKB49XMSg/640?wx_fmt=png&from=appmsg)

### 6.2 VMware ip地址配置

#### 6.2.1 Windows下环境配置

在`Windows`下的`VMware`中，除了`NAT`模式可以直接在网卡里面配置外，其他的模式不支持直接配置`ipv6`的地址：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/JQpUg1oh5ac6VrMqpMtA3gYK6QSk7xTCPTskflNencnUib8GJV2n1AegsicyDJX74HWHPQefttmka0vMupMafoohXVSzXmx7ckDkibXE0yYWvs/640?wx_fmt=png&from=appmsg)

但只要是虚拟机本身支持`ipv6`，就可以进行内网的`ipv6`通信。

新建`vmnet4`网络（当然名字可以随便写）

![image.png](https://mmbiz.qpic.cn/mmbiz_png/JQpUg1oh5aeQaYWUXan5aLJpycOsSfVFpWP3cbiar02H2epEKmJsMTiaZuO6qs9jICYGgqNgzzybTdgGRN7fk11DshDkTc5goGSfJFNBzdU58/640?wx_fmt=png&from=appmsg)

`ipv4`子网有无并不重要，因为在整个网络中是不使用`ipv4`网络的（`kali linux`除外，需要加载首页的`js`文件以及安装其它必要工具）

同样新建`vmnet5`网络：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/JQpUg1oh5aeY95lIIs2WLjeZYjmVdN2zKwU4g3JTkazib74ATQo7j3rwiawGicwicKuNHqh4VvCNzwXicQqZp5vxsCe4nrFHAFP2g6a5sJBVKfek/640?wx_fmt=png&from=appmsg)

#### 6.2.2 mac下地址配置（intel）

`mac`上使用的是`vmware fusion`软件，版本：`13.5.1`

`![image.png](https://mmbiz.qpic.cn/mmbiz_png/JQpUg1oh5afuicCCmlLEdJwwoL7nvOibEBjR8XkgCrCjiaHDtKj3963m68lLqzclResCxF6VUzYjyvypYMq4kB3Rf7fJE89nmoWgUrfzibqLozY/640?wx_fmt=png&from=appmsg)`

`mac`上和`Windows`上不同，它可以指定`ipv6`的地址，不过因为靶机本身是写死`ipv6`地址的，所以在这里仅供参考：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/JQpUg1oh5ae5j1OhCNxHZxEm4GOT2pic0I7AeGkdLj145puicp8YqE1D4dejL2jibicZCI9qPUgssg7ZRRvBztcMudhlOI59fDotOqXxCz0CXQY/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/JQpUg1oh5acaGLVqk7bIY6pspG0ZfhcKUKx0mQkW9ZpsmYL4tFvic0q4LmJlNmDPqsuvTq6ApEt4b7rfTBYAVaBAdmCOHgGWJ2xczSd1siaHY/640?wx_fmt=png&from=appmsg)

### 6.2.3 kali地址配置

在`kali`上可以配置临时的`ipv6`地址：

```
ip addr add fd00:3333:6666::100/64 dev eth0 nodad
```

而且建议`kali`配置双网卡，其中一个网卡为`nat`模式，可以连接互联网就更好了。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/JQpUg1oh5acAa1gFz35ibgdpDNItRibkkXGEZhS86pVwcHNdrsqLA1JhNSE5Zw1eZTzVFT5iabibnt6usOB3NvhJlCNmsgrbN8Ws7pprWmVicbGI/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_png/JQpUg1oh5afuKWnibJnlbexNDPPMaeDoiaWGfatEEj4oGVdcP9RURpFibf38nmXU37eicsJb5AC4E7gBJ7q52K9LCYtrH0krgpNy02xmEqF1wJg/640?wx_fmt=png&from=appmsg)

### 6.3 Ubuntu\_tp-01网络配置

直接使用网络适配器`4`和`5`，看下`ip`地址：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/JQpUg1oh5aejuf6tCjxbVyDyibKfgQq10EKR9h8dm6m6mO2zPEtSCcyFZy6KmOgic1DjZJvBS1ibpCtVd5iagkiblk1xTnHrEUvJMcBKQDFQTt0s/640?wx_fmt=png&from=appmsg)

#### 6.3.1 Ubuntu\_mysql\_02网络配置

连接网络适配器`05`就行了：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/JQpUg1oh5acGvcCKMSLFzicPSCEtpiae0krJSJPqkpBFbCZUhw7OgyibZemV3I8c61csVvTwX5WxOJqaMnyJP72tLicKn90FILhicrOMVlSlM3u8/640?wx_fmt=png&from=appmsg)

#### 6.3.2 网络检查

`kali`攻击机`ping` 第一台设备：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/JQpUg1oh5ad5kY7BKXiacnic7cBT9MaZlLmFKuDl9k5rriczjibfZcFwMqhTyJJvx80f7icgpiax70E8vCTBL5AtoKPPvt01OyaQibo9S3KONmxJNY/640?wx_fmt=png&from=appmsg)

访问首页：

```
http://[fd00:3333:6666::128]:32180/index.html
```

`![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/JQpUg1oh5adwXaULUOEF8J6HHt2icibWZaWib3sroZaEFQojBnXeBGWzZmypqnydNSCCvfa3VkOX40rhcwTtzibyOK90v9XeUIAyBh2xJQzOZKU/640?wx_fmt=png&from=appmsg)`

`Ubuntu01`这台设备去`ping``Ubuntu02`这台设备：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/JQpUg1oh5adU5uLmEIjBJXD0C3XZdIIpl48AGS6Py8kIopK5Q0owCxmlmvQa0gWT1K5LJsUBhr5OpDBHFRPue85azk8ubLxGNS3fUgRIqBI/640?wx_fmt=png&from=appmsg)

同样使用`Ubuntu02`这台机器去访问`Ubuntu01`这台虚拟机的网站试试：

```
curl [fd00:6666:8888::128]:32180
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/JQpUg1oh5adZhBDCZBXPmzcjn7u0icy4aLHvqLiccq0aiaE4IbWibvTJwwHOGNia2Urwol32DkiccibBZNo8VYJtAm70Gef47GcXsaT4fGY99w5Mc0/640?wx_fmt=png&from=appmsg)

至此，环境配置完成，准备打靶。

### 6.4 靶机网络配置说明-仅供参考（备用）

本文中的靶机`ip`地址并不是固定死的，你也可以按照你个人的理解来写`ipv6`的地址，我的地址仅供参考，请注意在`mac`下考虑`ipv6`的`DAD`问题：

建议关闭`ipv6`的`DAD`检测，在`01`和`02`的机器上都执行：

```
关闭 IPv6 DAD 检测（内核级，真正生效）
echo "net.ipv6.conf.all.dad_transmits = 0" >> /etc/sysctl.conf
echo "net.ipv6.conf.default.dad_transmits = 0" >> /etc/sysctl.conf
sysctl -p
```

`Ubuntu01`的地址：

```
cp /etc/netplan/50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml.bak
vim /etc/netplan/50-cloud-init.yaml
```

```
network:
  version: 2
renderer: networkd
ethernets:
    ens33:
      match:
        macaddress: 00:0c:29:dd:5c:66
      addresses:
        - fd00:3333:6666::128/64
      accept-ra: no
      optional: true

    ens37:
      match:
        macaddress: 00:0c:29:dd:5c:70
      addresses:
        - fd00:6666:8888::128/64
      accept-ra: no
      optional: true
```

注意：这个地址仅供参考，如果你真的不会的话，可以问问`ai`。

应用网络：

```
netplan apply
```

`Ubuntu02`：

```
cp /etc/netplan/50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml.bak
vim /etc/netplan/50-cloud-init.yaml
vim /etc/netplan/50-cloud-init.yaml
```

```
network:
  version: 2
  renderer: networkd
  ethernets:
    ens33:
      dhcp4: no
      dhcp6: no
      addresses:
        - fd00:6666:8888::130/64
      accept-ra: no
      optional: true
```

同样应用网络：

```
netplan apply
```

准备打靶！

tips：加我wx，拉你入群，一起学习

![](https://mmbiz.qpic.cn/mmbiz_jpg/HficxWTTwt1ACBHDE9o8KA6icOCZVKdLBJOca699BJK50FDxBNnhRZrS1hyXb2K4AkLTYfJwt...