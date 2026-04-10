---
title: 2025平航杯服务器取证部分
url: https://mp.weixin.qq.com/s/KRDsD1c32zuXe3JHL4P26Q
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:41:25.090397
---

# 2025平航杯服务器取证部分

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rlbOU0KufJOEibIzh9fv8lib2vnF9lQ7PBy8UngG9HqUpiaUlVEz5HkfKcDxS1GmicO14gADuWfZl8GnSE8Gs3T2uTHibud69kicT58U/0?wx_fmt=jpeg)

# 2025平航杯服务器取证部分

原创

正在思考ing
正在思考ing

正在思考ing

![]()

在小说阅读器中沉浸阅读

本来想在一周之内把前一年平航杯的真题都练一遍，备战本周末的比赛，结果拼尽全力就只完成了服务器取证部分，看来这一块还有很多要学习的地方

---

**案件背景：**
2025年4月，杭州滨江警方接到辖区内市民刘晓倩(简称：倩倩)报案称：其个人电子设备疑似遭人监控。经初步调查，警方发现倩倩的手机存在可疑后台活动，手机可能存在被木马控制情况；对倩倩计算机进行流量监控，捕获可疑流量包。遂启动电子数据取证程序。

警方通过对倩倩手机和恶意流量包的分析，锁定一名化名“起早王”的本地男子。经搜查其住所，警方查扣一台个人电脑和服务器。技术分析显示，该服务器中存有与倩倩设备内同源的特制远控木马，可实时窃取手机摄像头、手机通信记录等相关敏感文件。进一步对服务器溯源，发现“起早王”曾渗透其任职的科技公司购物网站，获得公司服务器权限，非法窃取商业数据并使用公司的服务器搭建Trojan服务并作为跳板机实施远控。

请你结合以上案例并根据相关检材，完成下面的勘验工作。

**检材：**
window.e01
20250415\_181118.zip
export-disk0-000002.vmdk
BLE
USBPcap

**容器密码：**
早起王的爱恋日记❤

服务器镜像是export-disk0-000002.vmdk，是个VMware虚拟磁盘文件

**49. 该电脑最早的开机时间是什么(格式：2025/1/1 01:01:01)**

2022/02/23 12:23:49

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmdyDCddsfGv0FziamOHkgAZnSib1kEJJnEib0OXTz71ck1bU6CxzFia5FKLmLVPM7wXXF2zxy4kFPhkfQ5T2UzEp846Coxm84P0qM/640?wx_fmt=png&from=appmsg)

**50. 服务器操作系统内核版本(格式：1.1.1-123)**

3.10.0-1160.119.1.el7.x86\_64

注意区分操作系统版本和内核版本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmNYeprnv09coXUgxvjbtqGjGZjpRBdwqSMPSOjUucJj5JNbcibibaialqbZLkIkj1v9e2WR8MKZLqeYxYIDLT6hqOeV1TibNsCFsI/640?wx_fmt=png&from=appmsg)

**51. 除系统用户外，总共有多少个用户(格式：1)**

3

除系统用户以外有3个用户（常规用户）

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rniafQBNqjyrFTTibBqUxtsgJBBAQSduEPzNuiaWkLibTjE2l4fNl6lRTZIWC0rHvjvJjRXAI4KTNvtLTeT8niagq0uU0xNzsTGktbY/640?wx_fmt=png&from=appmsg)

**52. 分析起早王的服务器检材，Trojan服务器混淆流量所使用的域名是什么(格式：xxx.xxx)**

wyzshop1.com

Trojan服务器的概念：

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkDcv2Z65t12Tn49RY0MZKp8tGRmgpL6u1joChrzTU8hfZxV4p320Kq984iavvqic0yHSogF046xTQbP2DicyXw7eMMZG83nLqdl4/640?wx_fmt=png&from=appmsg)

查看Trojan服务器混淆流量所使用的域名需要仿真起来，因此顺便ssh连接一下

调整虚拟机网络适配器为VMnet8（NAT 模式），再修改一下网卡配置文件 /etc/sysconfig/network-scripts/ifcfg-ens33

将虚拟机与本机调整至同一网段就能ssh连接了

要看Trojan服务器混淆流量所使用的域名，需要查看Trojan服务的配置文件

在/root目录下找到了trojan目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlqsTibXswXXrWS6j7H6PrzPj8mGYwMia33HleCy8opfiauQYfHKVLsZyocco8mSZfgmpGsjZyFXqXtgcDOgeVeibqgrnLd0phXVIo/640?wx_fmt=png&from=appmsg)

进而确定配置文件的路径为/root/trojan/config.json，查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rl7m7c4sDAib1INiaT6xiakCsNSS9IW7ZLk0vANBklVIUpn37bw41dbjdg35p4fRu8UOmVSgxDmelHtWfcBtI3j1Iiak9CHN0CxXms/640?wx_fmt=png&from=appmsg)

其中remote\_addr字段就是Trojan服务器混淆流量所使用的域名

**53. 分析起早王的服务器检材，Trojan服务运行的模式为：**
**A、foward B、nat
C、server D、client**

B

在上一题的配置文件中，运行模式的run\_type字段为you guess，去其他地方看看

在/root/trojan/examples目录下，有选项几种模式的配置样例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlj6w7lkasz7InnHz9icA7n1JpuW3iawzoxOyIILAmU6l1ItMFnibPD4mtdwo5ZHk1rcdqe2vLNeBJquv60YwISTXx74kXvkXRCwo/640?wx_fmt=png&from=appmsg)

将几种模式的样例与上一题的配置文件对比一下，可以确定是nat模式

**54. 关于 Trojan服务器配置文件中配置的remote\_addr 和 remote\_port 的作用，正确的是：**
**A. 代理流量转发到外部互联网服务器**
**B. 将流量转发到本地的 HTTP 服务（如Nginx）**
**C. 用于数据库连接**
**D. 加密流量解密后的目标地址**

A

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkqElTXYkClibetFljw55hZkHdTXDeIPObRQibgcBDW6zJBkO18LpiaMBlTOibMnJRCLEEPicXAv5jckS5cHPBjsoiaO9lf3nicBMn86I/640?wx_fmt=png&from=appmsg)

**55. 分析网站后台登录密码的加密逻辑，给出密码sbwyz1加密后存在数据库中的值(格式：1a2b3c4d)**

f8537858eb0eabada34e7021d19974ea

在取证工具的分析页面发现了宝塔面板，有两个网站

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmdMehIOKS1aJd36AU4SVJ5k07SbVaJwiaIGiagTuDicn8Jhvm510tA8cc3ZaXX6NkSIxsOBNx3KK6Kn3fhZW9qyCCaucmcw38nMk/640?wx_fmt=png&from=appmsg)

但不知道是哪个

先重置一下宝塔面板的密码然后登录

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmpRE1upJiaAQiaeF294Bb3ScWkcANuUKZkqMcE413VlibrwSwvs9PQ2cELL7I81o1RgHdTUSD2uO9LrsIsaODdIbQ05eJyL2xfIc/640?wx_fmt=png&from=appmsg)

在宝塔面板的数据库页面发现了phpMyAdmin，直接登录不知道密码，在/etc/my.cnf中增加skip-grant-tables字段，随后使用systemctl restart mysql命令重启数据库即可免密登录phpMyAdmin

* 用户名：root
* 密码：toor

在phpMyAdmin中发现数据库tpshop2.0被删除了，猜测网站就是之前在取证工具中看到的www.tpshop.com

进入www.tpshop.com的目录/www/wwwroot/www.tpshop.com，分析网站代码，找到下面几个文件

./application/admin/controller/Admin.php

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkpthysibu447yHtsd7R9ia2HXk5Vb7ibxicyFmAyUL9Xd2SKPtrFQueeUd02WAVSoicQQa9MiaSJVapdt9dVG7wBJ8TbrurBr54WvAs/640?wx_fmt=png&from=appmsg)

我们需要找到encrypt()函数的定义

./application/function.php

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlnmFEp0OVVS2bCdhbGmQd9NlLcyE1nxQ0JwgcNJjWzoias1DkVIkiapWtJ1bl0l45qVkskXEjw0oloEQg9FASxXAS2v3Sf6qMrU/640?wx_fmt=png&from=appmsg)

显然网站的密码加密逻辑就是在明文密码前面加上AUTH\_CODE后计算md5哈希

查找AUTH\_CODE值

./application/config.php

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlfWD4uPCxKicXyiaaUUoym6MEhcJRribeibgujfTZo7s0eCwERzCsY5OmAF2ekkQFMKWLVMMn5JhnImhFGnIoB5XQACtLWyjwr1Oo/640?wx_fmt=png&from=appmsg)

AUTH\_CODE为TPSHOP，那么本题的答案就是md5('TPSHOPsbwyz1')

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmcibC9pAmexrps5u6cqETeiaq7OdADLz5Nh9jU2zG9wZ1kmHyuVMHgFUrz96icl1Y2PJvHeksg30yYU7ssiaS0vM7ibGiaaYeibQdt6A/640?wx_fmt=png&from=appmsg)

**56. 网站后台显示的服务器GD版本是多少(格式：1.1.1 abc)**

2.1.0 compatible

需要查看网站后台，因此需要先进行网站重构

上一题中我们在phpMyAdmin中已经发现了数据库tpshop2.0已被删除，尝试恢复一下

在网站根目录的backuo文件夹下找到了数据库的备份文件

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkCmrX0n0IUADJA0K63Ddib5cC7a6zDR2ueGIoj0StMfZk8XADvwuOMqH0KaZrbQy5CPY4KSnia9u0lXpwH4w5EzVm1NyQlibf8zQ/640?wx_fmt=png&from=appmsg)

可以在宝塔面板中修复

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmQjKEkO5zJ2Y9kxZw4vicZScQ9zhWxF5iavQPsEMJsA738nLqxZVQ5u0pzwB0HpiaUGxk3yoJNxicYgpUSQZYLnRxic6FwbcO251ibY/640?wx_fmt=png&from=appmsg)

这里我们已知服务器的ip，又实现了免密登录，可以先用navicat连接数据库再修复

navicat连接前需要先关闭服务器的防火墙

```
systemctl stop firewalld
```

密码可以空着

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkNNCRdbqjaibrLyqzJibgnQwVkOTpmGHHpwZibkNaetVtfAGFaF4PDLP1kVebm0yicVSLHbldfKxr2wOtibibhmnO98tR2WnA5nqINY/640?wx_fmt=png&from=appmsg)

将我们在服务器中找到的备份导出到本地，随后在navicat中右击tpshop2.0-运行SQL文件，选择我们刚刚导出到本地的.sql文件即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rnqEtFL6AssdxkAC773DC99icozpkOWWVK18GgA1j6bvJLvmWicSAe1fUNDFlrP3edx1EMibjfC8sxtvSDAapZjUr5hE35ic4ztF4U/640?wx_fmt=png&from=appmsg)

数据库恢复成功

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rn16wDp4UtJQshP3m3w4iayzmGNLnGHVDl57icMVy9nicv8JSWnwR8ZTibqON06ARUSic4jTBxmXKUYIPT36iarIed2DrZIVYzkIYJeE/640?wx_fmt=png&from=appmsg)

phpMyAdmin中的数据库也成功更新

在宝塔面板中我们已经确定网站url为www.tpshop.com

接下来修改本机的hosts文件，手动指定www.tpshop.com映射到服务器的ip（192.168.50.5）

1. 以管理员身份运行记事本
2. 打开C:\Windows\System32\drivers\etc\hosts
3. 添加字段192.168.50.5 www.tpshop.com
4. 执行命令ipconfig /flushdns刷新DNS缓存

访问www.tpshop.com

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmHqD3h12ss1bSDicFxge923jfwWyEmje8hFnwLefGLZDgew6CjmuO2ordSdDVte50S37qN7rYyNED3SHumVFkNLRvFbUDGeYQk/640?wx_fmt=png&from=appmsg)

网站重构成功

> 其实不修改hosts文件，直接访问192.168.50.5也可以
>
> 这里遇到个奇怪的问题，访问网站的时候要把梯子关掉，否则就会被定位到这个网站
>
> ![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rkAAc2rib4bpPd6DKRyJ3PDLlJZwx2tjyJah2JwSibU3vFsC361hSEurD0qEw1A0LvFO4GMXyVD6ZAJicuWiaQibOpfkEbWnOd2dUFU/640?wx_fmt=jpeg&from=appmsg)

接下来需要找到网站后台的路径

分析网站日志文件/www/wwwlogs/www.tpshop.com.log

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmJqH7y7MRX0VKPqgODmRGG8mFB8J3Nqz1YzAsdD0jXSWENDWy1bRpzI2Iq0uictLpYPM8FfMI3kQhfT3JQwFp1jmLibcIlFczzc/640?wx_fmt=png&from=appmsg)

找到网站后台路径为/index.php/Admin/Admin/login.html

访问http://www.tpshop.com/index.php/Admin/Admin/login.html

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkQoYKA4A85icWTjNX8ykOWsMHkMVic34BNYGvMTqgJuw6MPzS8nD2ppyfOrPzPZekLuPPhicdHOX1619zwuZorwEwYZSibaXVSzlk/640?wx_fmt=png&from=appmsg)

我们需要admin的账号和密码才能登录

数据库中的tp\_admin表存储了admin的账号和密码哈希

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlPpPoY309AMrOwAljmqhycBVkXAsyzReSicM80RLPO4SgjibB9g0ArdaFVujmCJXTx3V7DVZwVKjyJm95zfS8cmNia87YwCEqefE/640?wx_fmt=png&from=appmsg)

我们只需要将原密码哈希修改为在第55题中求得的sbwyz1的哈希即可

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkjVoDDyvaw0FIJmWMRXWibkjL0yBQYiaqpwJicShE9PoRsS9SXW77cb1LxngC68IK2NYxSwRJZVgxrQfbDlgS9Lhc76DfqU9ax2w/640?wx_fmt=png&from=appmsg)

保存一下，回到后台登录页面输入

* 账号：admin
* 密码：sbwyz1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rk0iaZG3GhT1z5bcEIebkh69SW7OkJNDBxIXlGpAy19UZ31XSGtN963NfpdsZWBOck7T3icx7yEJLbHC3IU59KpmGA52i...