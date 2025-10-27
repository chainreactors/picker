---
title: 在WAF中加入AI的一次尝试，附demo程序
url: https://www.secpulse.com/archives/201157.html
source: 安全脉搏
date: 2023-05-31
fetch_date: 2025-10-04T11:37:55.736559
---

# 在WAF中加入AI的一次尝试，附demo程序

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

# 在WAF中加入AI的一次尝试，附demo程序

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[公众号:安全女巫](https://www.secpulse.com/newpage/author?author_id=49672)

2023-05-30

29,461

**********如果你喜欢我的文章，欢迎关注公众号：安全女巫
转载请注明出处：**********https://mp.weixin.qq.com/s/XQYKrlcppPDUAzBSdGC4vw

原文已由作者授权发表，首发于：先知社区

https://xz.aliyun.com/t/12552

## 整体效果和架构图

> 0.1版本

最近想写一个基于 AI 的一个安全攻防项目，想了几个备选的想法，把重点放在了写一个 waf 上，0.1 版本算是完成了，效果图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201157-1685425655.gif)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201157-16854256551.gif)

url 不对劲直接就`forbidden`，否则`hello,{your_url}!`

整体架构可以搭建一个Go服务，当Go服务器接收到用户发送的URL后，它会联系一个用于URL识别的服务器。

这个URL识别服务器使用训练好的模型来自动判断URL是否为恶意请求。一旦Go服务器获得了识别服务器的响应，就可以执行一系列操作。

如果URL没有问题，就会放行；否则，它会向攻击者发送警告、封禁IP地址，或者销毁相关的会话等等，具体的行为取决于业务需求。

这个演示版本只实现了一个简单的Hello World功能，但重点放在了Web应用防火墙（WAF）上。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201157-1685425656.png)

本文从三个方面来介绍：

* 数据集生成并处理
* 神经网络训练过程
* 两个服务器的交互

## 数据集生成并处理

数据集可以从网上找，找到适合自己网络结构的。

还有一种就是自己定制化生成，对于企业来说，就是比如自己企业的测试部门在网页上线之前对网页进行的渗透行为可以把这块流量全部记录下来，或者红蓝对抗、HW的时候要及时复盘流量，自己复现下，按需打一打标签，更新自己的数据集。

比如任何对网站不构成实质性威胁的行为统一打成0，即良性url上。而恶意的url就可以酌情定义了，比如url打过去出现信息泄漏，或者rce这种很严重的都可以打上1，sql注入尝试什么都统统打上1，`<script>alert(1)</script>`这种也是，但凡是正则能识别出来的通通打1！

### badrequest数据集生成

用的xray。靶机用了docker起了个pikachu（因为自己这个helloworld小demo实在没什么可打的，233）。之后把本机的lo0网卡信息全部捕捉下来了，通通标成1就行了。

```
package main

import (
    "bufio"
    "bytes"
    "fmt"
    "log"
    "net/http"
    "os"

    "github.com/google/gopacket"
    "github.com/google/gopacket/pcap"
)

func main() {
    //网卡信息lo0，可以按需修改
    handle, err := pcap.OpenLive("lo0", 65536, true, pcap.BlockForever)
    if err != nil {
        log.Fatal(err)
    }
    defer handle.Close()

    // tcp协议，端口是8000，而且只抓get请求（按需修改按需修改
    filter := "tcp and port 8000 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420"
    if err := handle.SetBPFFilter(filter); err != nil {
        log.Fatal(err)
    }

    // 创建一个文件用于存储URL信息
    file, err := os.Create("url_info.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    // 开始捕获数据包
    packetSource := gopacket.NewPacketSource(handle, handle.LinkType())
    for packet := range packetSource.Packets() {
        // 解析数据包
        if applicationLayer := packet.ApplicationLayer(); applicationLayer != nil {
            // 提取HTTP请求中的URL信息
            if request, err := http.ReadRequest(bufio.NewReader(bytes.NewBuffer(applicationLayer.Payload()))); err == nil {
                url := request.URL.String()

                // 将URL信息写入文件
                if _, err := file.WriteString(url + "n"); err != nil {
                    log.Println(err)
                }

                fmt.Println(url)
            }
        }
    }
}
```

之后把抓包程序跑起来，把pikachu也开开

```
docker run --name piakchu -d -p :80 area39/pikachu
```

之后用xray的爬虫功能就行了

```
./xray_darwin_arm64 webscan --basic-crawler http://127.0.0.1:8000/ --html-output xx.html
```

可以看到能够得到不错的数据，左侧是恶意url数据集

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201157-1685425657.png)

### 良好数据集生成

这块用了两种生成方式，一种就是模拟点击的方式，将所有url按照迭代的方式一代一代的点击一遍，对于本项目，pikachu而言能够点击的url着实不多

```
from requests_html import HTMLSession
import time

def save_links_to_file(links):
    # 追加链接到文件
    with open('urls.txt', 'a') as f:
        for link in links:
            f.write(link + 'n')

def crawl(url, end_time):
    # 创建HTMLSession对象，获取网页内容
    session = HTMLSession()
    r = session.get(url)
    # 获取所有链接
    links = r.html.absolute_links
    urls = []
    for link in links:
        # 如果链接是以http或https开头，则保存链接
        if link.startswith('http'):
            urls.append(link)
    # 保存链接到文件
    save_links_to_file(urls)
    # 递归访问所有链接
    for url in urls:
        # 如果当前时间已经超过了指定时间，则停止递归
        if time.time() > end_time:
            return
        crawl(url, end_time)

# 设置爬取的起始URL和结束时间
start_url = 'http://127.0.0.1:8000/'
end_time = time.time() + 3

# 调用函数，从指定URL开始递归访问所有链接，并追加到文件
crawl(start_url, end_time)
```

最后得到了使用`sort -u urls.txt`看下有多少。发现只有62行有效数据，这和我们使用xray得到的恶意数据集完全不是一个量级（恶意数据集有1万条url

我想了个别的方式（关于如何获取好的url，以构建自己的良性数据集）

实现方式是写了个油猴插件，每次生成数据的人打开一个url的时候插件把url发送给服务器上，服务器端保存所有用户的数据（当然这是访问别的网站时候的数据，但只要数据具有多样性，重点是网络能不能学到恶意url而不是局限于具体的网站架构）。

具体插件架构如图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201157-1685425660.png)

油猴和服务器端代码如下：

```
// ==UserScript==
// @name         Append URL to Local File
// @namespace    http://tampermonkey
// @version      1.0
// @description  Append current URL to local file on page load
// @match        *://*/*
// @grant        GM_xmlhttpRequest
// ==/UserScript==

(function() {
  'use strict';

  // 获取当前页面的URL
  const currentUrl = window.location.href;

  // 发送 HTTP 请求将 URL 发送到服务器
  GM_xmlhttpRequest({
    method: 'POST',
    url: 'http://***:7000',//改成自己的，我用的阿里云，好用，上云就上阿里云！
    data: currentUrl,
    headers: {
      'Content-Type': 'text/plain'
    },
    onload: function(response) {
      console.log('URL sent to server');
    },
    onerror: function(error) {
      console.error('Error sending URL to server:', error);
    }
  });
})();
```

服务器端，用的 nodejs 接收

```
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  if (req.method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      fs.appendFile('urls.txt', body + 'n', err => {
        if (err) {
          console.error('Error appending URL to file:', err);
          res.statusCode = 500;
          res.end('Error appending URL to file');
        } else {
          console.log('URL a...