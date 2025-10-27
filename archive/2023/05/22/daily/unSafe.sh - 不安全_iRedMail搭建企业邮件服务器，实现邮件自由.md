---
title: iRedMail搭建企业邮件服务器，实现邮件自由
url: https://buaq.net/go-165016.html
source: unSafe.sh - 不安全
date: 2023-05-22
fetch_date: 2025-10-04T11:36:57.412158
---

# iRedMail搭建企业邮件服务器，实现邮件自由

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

![]()

iRedMail搭建企业邮件服务器，实现邮件自由

前几天录制了视频《搭建宝塔自带企业邮局》的视频，感觉没什么技术含量，所以今天尝试一下用开源的iRedMail来搭建企业邮箱。iRedMail开源，有网页
*2023-5-21 22:2:14
Author: [blog.upx8.com(查看原文)](/jump-165016.htm)
阅读量:27
收藏*

---

前几天录制了视频《搭建宝塔自带企业邮局》的视频，感觉没什么技术含量，所以今天尝试一下用开源的iRedMail来搭建企业邮箱。

iRedMail开源，有网页端，更适合多用户使用，官网：<https://www.iredmail.org/index-zh_CN.html>

下面开始准备工具：

（CentOS 项目将重点转移到 CentOS Stream，CentOS 8 将在 2021 年底结束）

2、VPS 最好支持 PTR Records

3、域名一个，推荐托管 cloudflare （解析生效快）

4、规划好作为邮件服务器的域名，演示用 mail.jichang.ml，把该域名解析到 VPS IP。

**搭建 iRedMail 邮件服务器**
设置 VPS 以及系统
更新系统、安装组件
yum update -y
yum install wget curl sudo tar socat bind-utils -y
设置 VPS 主机名
我们规划邮局的域名为 mail.jichang.ml ，所以，我们需要对 VPS 的主机名进行设置。

首先，需要编辑 /etc/hosts 文件，找到含有你的 VPS IP 地址的那一行；如果没有，则添加一行。内容如下：

127.0.0.1 mail.jichang.ml mail
其中, 127.0.0.1 可换为你的服务器 IP 地址，后面依次填入长主机名和短主机名，切记不可填反。

然后，我们找到 VPS 的 /etc/hostname 文件，编辑里面的内容为 mail （域名的前缀）

这样，就设置好了主机名。重启 VPS后我们检查一下是否设置正确：

执行：hostname

此时我们应该只能看到短主机名 mail. 如果你看到了长主机名 mail.jichang.ml , 说明之前设置错误，请重新检查上述步骤。

执行：hostname -f

此时，我们应该只能看到长主机名 mail.jichang.ml

这样，我们就全部设置好了主机名（hostname）, 可以进行接下来的其他操作了

**下载并安装 iRedMail**
我写这篇博文的时候，iRedMail 的最新版为 1.5.1，若是版本进行了更新，请大家自行修改下面命令中的版本号。

wget https://github.com/iredmail/iRedMail/archive/1.5.1.tar.gz -O /root/iRedMail.tar.gz
tar -xf iRedMail.tar.gz
cd iRedMail-1.5.1
bash iRedMail.sh

按照以下顺序进行安装

不安装，请按 Ctrl-C

设置安装目录，选择 web服务器，选择数据库类型，设置数据库密码，设置域（不可与 hostname 相同），设置管理员账号、密码，选择需要安装的组件，然后根据系统提示，一路输入 y 回车

重启服务器，让邮件服务器生效！ 至此，邮件服务器搭建完毕，以下开始设置邮件服务器。

可以通过访问（当然，我们目前还没有解析域名，后面一起解析）
https://你的域名/mail ——邮件登录地址
https://你的域名/netdata ——服务器状态监控
https://你的域名/iredadmin ——邮件服务器后台管理

管理员账号：[[email protected]](https://blog.upx8.com/cdn-cgi/l/email-protection)你的域 例如 [[email protected]](https://blog.upx8.com/cdn-cgi/l/email-protection)
管理员密码：安装时候设置的密码
以上信息，可以在 /root/iRedMail-1.5.1/iRedMail.tips 文件中查看

**配置 iRedMail 邮件服务器**

在申请证书之前，请完成 邮件服务器域名 的相关解析，我们规划的邮件服务器地址为 mail.jichang.ml ，所以，申请证书之前，需要对把该域名指向 VPS IP。

申请证书
以下是 ACME 脚本申请证书，比较方便哈。

为我们计划的邮件服务器域名 mail.jichang.ml 申请证书，请自行替换命令行中的域名

curl [https://get.acme.sh](https://iweec.com/go/aHR0cHM6Ly9nZXQuYWNtZS5zaA%3D%3D) | sh
~/.acme.sh/acme.sh --register-account -m [[email protected]](https://blog.upx8.com/cdn-cgi/l/email-protection)
~/.acme.sh/acme.sh --issue -d mail.jichang.ml --webroot /var/www/html
~/.acme.sh/acme.sh --installcert -d mail.jichang.ml --key-file /etc/pki/tls/private/iRedMail.key --fullchain-file /etc/pki/tls/certs/iRedMail.crt
重载服务
service postfix reload;service dovecot reload;service nginx reload

禁用 iRedMail 灰名单
找到 VPS 文件，/opt/iredapd/settings.py

plugins = ["reject\_null\_sender", "wblist\_rdns", "reject\_sender\_login\_mismatch", "greylisting", "throttle", "amavisd\_wblist", "sql\_alias\_access\_policy"]
将其中的 ”greylisting ” 这项删去即可

然后，重启 iredapd

service iredapd restart

配置域名 DNS 及解析
以下内容，推荐观看 演示视频，然后根据需要，替换以下命令行中的相关命令。

设置 PTR 反向解析（这里我省略了）

检测方式：nslookup 8.8.8.8（服务器IP）

设置 A 记录
将 mail.jichang.ml 的 A 记录指向你的 VPS 服务器（邮件服务器）

检测方式：nslookup mail.jichang.ml

设置 MX 记录
MX 记录就是邮件的解析记录，非常重要的一条记录，配置根域名的 MX 记录为自己的邮件域名地址，优先级为 10

检测方式：nslookup -type=mx jichang.ml

设置 SPF 记录
SPF 记录是为了防止垃圾邮件而设定的，告知收件方，从设置的允许列表中发出的邮件都是合法的，设置方式为添加一条根域名的 TXT 解析记录

内容为 v=spf1 mx ~all（此处修改成：v=spf1 mx ip4:198.74.113.143 ~all）

检测方式：nslookup -type=txt jichang.ml

设置 DKIM记录
DKIM 可说是避免被判定为垃圾邮件的一大利器，DKIM 属于一种类似加密签名的解析记录，只有包含此加密数据，且公钥与密钥相匹配才属于合法邮件，要设置 DKIM 记录，首先要查询 DKIM 信息。

查询DKIM 信息有两种方式：

第一种：在系统中执行命令查看：amavisd showkeys

若是出现报错：Config file "/etc/amavisd.conf" does not exist, at /usr/sbin/amavisd line

修改 /usr/sbin/amavisd 文件

搜索 config\_files = ( '

把括号里面的路径改为 ‘/etc/amavisd/amavisd.conf’

第二种：直接查看 /root/iRedMail-1.5.1/iRedMail.tips 文件，里面有相应的 DKIM（视频中我使用的是这种方法）

将括号内的文本 去除引号以及空格并相连 就是咱们的 DKIM 数据，在解析中添加一条 dkim.\_domainkey 的 TXT 解析，内容就是咱们组合出的文本

测试方式：nslookup -type=txt dkim.\_domainkey.jichang.ml

设置 DMARC 记录
DMARC 记录是当收件方检测到伪造邮件等行为时，将根据您的配置进行操作的一个记录，比如拒绝邮件或放入垃圾邮件以及不做处理等，同时会反馈一份检测报告到配置的邮箱地址内。

添加方法就是增加一条 \_dmarc 的 TXT 解析，内容为配置选项，v=DMARC1; p=none; pct=100; rua=mailto:[[email protected]](https://blog.upx8.com/cdn-cgi/l/email-protection)

检测方式：nslookup -type=txt \_dmarc.jichang.ml

添加 iRedMail 用户
当然，你可以直接使用刚才系统创建的系统管理员邮箱，我们另外也可以增加邮箱用户

登录前，选择你的网页语言，其他就很简单了。

测试 iRedMail 邮件服务器
登录你的邮件服务器，里面的三封邮件是系统发过来的。

尝试用该邮件发送以及接收其他邮件的邮件，若是严格按照上面来配置，应该是一点问题都没有。

最后，我们访问 https://www.mail-tester.com/

按照网页上面给出的邮箱地址，我们用刚才搭建好的邮件服务器给这个地址发送一封邮件，然后点击测试。

按照提示做适当的修改！

用刚才创建的用户，给 GMAIL 发一封邮件试试。

如果你是需要用其他客户端软件来收取或是发送邮件，端口列表在这里：

协议 地址 端口&加密端口
IAMP 邮箱域名 143,993
POP3 邮箱域名 110,995
SMTP 邮箱域名 25,587

使用客户端收发邮件也非常完美！

文章来源: https://blog.upx8.com/3567
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)