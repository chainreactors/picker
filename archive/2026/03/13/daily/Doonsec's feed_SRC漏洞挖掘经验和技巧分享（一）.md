---
title: SRC漏洞挖掘经验和技巧分享（一）
url: https://mp.weixin.qq.com/s/TvZoFPQRVgt63E2nvOE9AA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:08:13.372393
---

# SRC漏洞挖掘经验和技巧分享（一）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquMaowUTHGrz2cowazEADLcp10mYjsicmNoHaMKsBpHsYLVqAjFKwCLELlRuhDwVLLOutDULvvFmdq76mqLiafthDSlaoIicgVvKMM/0?wx_fmt=jpeg)

# SRC漏洞挖掘经验和技巧分享（一）

船山团队
船山团队

船山信安

![]()

在小说阅读器中沉浸阅读

# SRC漏洞挖掘经验和技巧分享

深挖一些实战中的细节和技巧。很多朋友觉得SRC漏洞挖掘就是拿着扫描器咔咔一顿扫，其实不然，真正能挖到高危、拿到高奖金的人，往往在细节上做得更足。下面将自己这几年积累的一些经验分享给大家，希望能对各位有所帮助。

---

## 一、子域名收集：别小看SSL证书

子域名收集是老生常谈，但方法不同，效果天差地别。我以前挖网易SRC挖了两年，自以为把他们的域名摸透了，直到我用上了基于SSL证书的查询方法，才发现自己之前漏掉了多少东西。

常用的证书查询网站：

* **censys.io**
* **crt.sh**

这两个网站通过扫描全网SSL证书，能帮你找到某个主域名下的所有子域名，甚至是一些你根本想不到的二级、三级域名。原理很简单：很多站点为了HTTPS，会申请证书，而证书里通常会包含域名信息。这些数据被Censys和crt.sh收集后，就成了我们免费的子域名字典。

除了证书查询，还有一些第三方接口也很好用：

* riskiq
* shodan
* findsubdomains
* dnsdb.io

这几个网站各有侧重，建议组合使用。

**实战案例**
有一次，我在crt.sh上查到一个二级域名 nss.a.com（域名脱敏），用常规的子域名枚举工具扫了一圈，啥也没发现。但我不死心，把这个二级域名丢到GitHub上搜索，结果在一个公开的代码仓库里找到了一个三级域名的接口地址，类似 http://nss.a.com/api/v1/test。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquOPux4QCOLjXqLBKbHy1InAebLXjfS6nibpNpictF1xVjuJhFPqeAlgDC2Y6tsQ8icPVrfJeAmHPR6mE7Zwc5ZSGfWiaqXcBBlRhFE/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquPZAkzwPM4pXeQDculibVZOu7SwvFuXEgB4EC6Pq7VdEicZzIibY6TSjnHFOESOfjJfIw9nWT4YlVbg6AicdS1e9thjWuGxicPs8aA8/640?wx_fmt=jpeg&from=appmsg)

直接访问这个接口，提示缺少参数，而且参数名直接在报错信息里暴露了。我根据代码里的提示，构造了正确的JSON请求头，成功调通了接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquNjOrqc5IF3dFbnb4mzg56Au9AxRnhoqXibHkB0sfVMvzwhpNt3GiaVII7uNibaZOFFz5NgByy7z5c1oFGRPvvic2DDmI4ucgkaCI4/640?wx_fmt=jpeg&from=appmsg)

这时候我灵机一动：这个接口用的是fastjson，会不会有反序列化漏洞？一试，果然中招，直接进了内网。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquOX40vJibXIVzQ8KJeYDQ2BeF3cxictLSypH8j4SWvWw96J1cZAYGKSVoLdzrXm6NfljSmyEECnhnHWtQQX0Uzutwp0gHSKwdGJ4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquMiaqic8ot9RqkGyIDXmefdBmbLZ37xicvfibcracsObcBwQ9dK22aTsG5r5EhKYUHcStkmfgrSzJAu7dkbxDdkyrNjgzGJ2hVY2Pw/640?wx_fmt=jpeg&from=appmsg)

这个案例告诉我们：子域名收集只是第一步，后续结合GitHub代码审计、接口测试，往往能挖出意想不到的洞。

---

## 二、IP段收集：巧用CNNIC Whois

有了域名，还得知道厂商的IP段，这样才能进行端口扫描。很多人直接拿域名去查IP，然后扫那几个IP，但大厂的IP段可能很广，而且分散。

我常用的方法是去 **CNNIC IP地址查询系统**（http://ipwhois.cnnic.net.cn/）。随便拿一个已知的IP查一下，比如 123.58.191.1，会看到这个IP属于“Netease-Network”。然后我就可以用这个网络名称继续查询，把整个“Netease-Network”名下的所有IP段都拉出来。

![](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquOB6WCoVicPjTe3grADESictLwExJc3EZhibDaUbwMwPHQIzJxmygZwZvickMZaaVdzM5NqUN9PI4c7yAGypFN0Dd64ytzbKvUGhJs/640?wx_fmt=jpeg&from=appmsg)

像网易这样的大厂，网络名称不止一个，比如直接用“netease”模糊查询也能查到一堆IP。虽然CNNIC不支持模糊查询，但我们可以多试几个关键词，比如公司英文名、缩写等，把能查到的IP段全收集起来，端口扫描的目标就丰富多了。

---

## 三、端口扫描：masscan + nmap 的进阶玩法

面对大批量IP，我的套路是：**masscan全端口扫描 + nmap服务识别**。宜人贷安全应急响应中心的公众号有篇文章《宜人贷安全建设之端口监控服务篇》讲得很好，大家可以去看看。

但在实际扫描中，我遇到一个烦人的问题：有些IP开了WAF，masscan一扫就返回几百个开放端口，全是假的。等它扫完再判断，太浪费时间了。

我的解决办法：**动态监控masscan输出**。设定一个阈值（比如80），用Python的subprocess实时抓取masscan打印的“found=xx”信息，一旦发现当前IP开放的端口数超过阈值，立马kill掉这个进程，跳过该IP，进入下一个。这样就能快速过滤掉WAF干扰。

代码大概长这样：

```
import re, subprocess, os

limitNumber = 80
command = 'masscan 59.111.14.159 -p1-65535 --rate 2000'
child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

while child.poll() isNone:
    output = child.stdout.readline()
    line = str(output, encoding='utf-8').strip()
    if'found='in line:
        print(line)
        foundNumber = re.findall(r'found=(\d{1,5})', line)
        if int(foundNumber[-1]) > limitNumber:
            os.kill(child.pid, 9)
            print('疑似有WAF！存活端口' + foundNumber[-1] + '个')
            break
```

注意：如果用 -oX 或-oJ 输出结果，就抓不到实时打印了，所以这里直接保存标准输出，最后再用正则提取端口。

masscan跑完后，就该nmap上场了。我的常用命令：

```
nmap -sV -sT -Pn --version-all --open <target>
```

* -sV：识别服务版本
* -sT：全连接扫描（不用root也能跑，虽然慢点，但普通用户权限就可以）
* -Pn：跳过主机发现（反正masscan已经确认主机存活了）
* --open：只显示开放端口
* --version-all：每个端口都尝试所有探针，提高识别准确率

服务识别出来后，就是常规的安全测试了，大家各有各的招，我就不赘述了。

---

## 结语

SRC漏洞挖掘是一场持久战，信息收集、字典积累、技巧优化都需要日积月累。希望我的这些经验能给你带来一些启发。

---

以上内容根据个人经验整理，如有疏漏，欢迎指正。如果你有更好的技巧，也欢迎在评论区分享交流。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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