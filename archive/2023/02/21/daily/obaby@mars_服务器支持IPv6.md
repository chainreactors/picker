---
title: 服务器支持IPv6
url: https://h4ck.org.cn/2023/02/%e6%9c%8d%e5%8a%a1%e5%99%a8%e6%94%af%e6%8c%81ipv6/
source: obaby@mars
date: 2023-02-21
fetch_date: 2025-10-04T07:35:33.579524
---

# 服务器支持IPv6

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# 服务器支持IPv6

2023年2月20日
[11 条评论](https://h4ck.org.cn/2023/02/11253#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/034f2f38e844df29b76e8e09c3aadffd.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/034f2f38e844df29b76e8e09c3aadffd.jpg)

这几天一直提示服务器即将过期，直到今天上班才又看了下，结果发现真的快过期了。于是就想着续费，结果算了一下一年2000多，这尼码好贵啊。问题是根本不值啊，虽然挂了好几个站。而之所以服务器变得这么贵是因为去年的时候实在受不了服务器越来越卡，直接升级配置，结果升级到现在就成了这个样子了。这就很离谱啊。

这也太离谱啦，降低支配之后还要1600.于是果断的重新开启了一台新的服务器。为了更方便的迁移数据可以直接使用现有的系统盘创建一个自定义镜像，新服务器直接使用创建的镜像启动就ok了，无需做任何的数据迁移。配置完成之后呢，发现实例支持ipv6了，于是顺便开启了一下ipv6。在he.net设置解析之后等了半天没生效，后来发现用的服务器还在阿里云。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230220201322.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230220201322.jpg)

问题是竟然没报错，这就很神奇啊。在阿里云重新添加解析之后就ok了。等了十几分钟生效之后发现AAAA记录有了，但是访问端口80不通。初步怀疑是组策略问题，组策略添加之后依然不通。通过 iptables可以看到端口是开放的。

```
root@hack:/home/wwwroot/h4ck# iptables -L
Chain INPUT (policy ACCEPT)
target prot opt source destination
ACCEPT all -- anywhere anywhere
ACCEPT all -- anywhere anywhere state RELATED,ESTABLISHED
ACCEPT tcp -- anywhere anywhere tcp dpt:ssh
ACCEPT tcp -- anywhere anywhere tcp dpt:http
ACCEPT tcp -- anywhere anywhere tcp dpt:https
DROP tcp -- anywhere anywhere tcp dpt:mysql
ACCEPT icmp -- anywhere anywhere icmp echo-request

Chain FORWARD (policy DROP)
target prot opt source destination
DOCKER-USER all -- anywhere anywhere
DOCKER-ISOLATION-STAGE-1 all -- anywhere anywhere
ACCEPT all -- anywhere anywhere ctstate RELATED,ESTABLISHED
DOCKER all -- anywhere anywhere
ACCEPT all -- anywhere anywhere
ACCEPT all -- anywhere anywhere

Chain OUTPUT (policy ACCEPT)
target prot opt source destination

Chain DOCKER (1 references)
target prot opt source destination
ACCEPT tcp -- anywhere 172.17.0.2 tcp dpt:3001

Chain DOCKER-ISOLATION-STAGE-1 (1 references)
target prot opt source destination
DOCKER-ISOLATION-STAGE-2 all -- anywhere anywhere
RETURN all -- anywhere anywhere

Chain DOCKER-ISOLATION-STAGE-2 (1 references)
target prot opt source destination
DROP all -- anywhere anywhere
RETURN all -- anywhere anywhere

Chain DOCKER-USER (1 references)
target prot opt source destination
RETURN all -- anywhere anywhere
```

但是iptables对应还有v6的半天，组策略添加之后并没有自动添加相关的端口规则：

```
root@hack:/home/wwwroot/h4ck# ip6tables -L
Chain INPUT (policy ACCEPT)
target prot opt source destination

Chain FORWARD (policy ACCEPT)
target prot opt source destination

Chain OUTPUT (policy ACCEPT)
target prot opt source destination
```

通过下面的命令添加策略：

```
ip6tables -A INPUT -p tcp --dport 80 -j ACCEPT
ip6tables -A INPUT -p tcp --dport 443 -j ACCEPT
ip6tables -A INPUT -p tcp --dport 3306 -j ACCEPT
```

再次查看就ok了：

```
root@hack:/home/wwwroot/h4ck# ip6tables -L
Chain INPUT (policy ACCEPT)
target prot opt source destination
ACCEPT tcp anywhere anywhere tcp dpt:http
ACCEPT tcp anywhere anywhere tcp dpt:https
ACCEPT tcp anywhere anywhere tcp dpt:mysql

Chain FORWARD (policy ACCEPT)
target prot opt source destination

Chain OUTPUT (policy ACCEPT)
target prot opt source destination
```

不过此时访问依然不通，这就神奇了，后来想起来可能是nginx监听的问题，修改nginx配置文件，去掉v6前的注释：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230220201945.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230220201945.jpg)

重启nginx，现在就ok啦。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230220-185558.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230220-185558.jpg)

v6地址的80端口已经在坚挺了。家里的联通是支持ipv6的可以看下解析：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230220200616.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230220200616.jpg)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230220200535.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230220200535.jpg)

直接访问也是ok的。

探测效果：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230220202238.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230220202238.jpg)

https://www.boce.com/ipv6/h4ck.org.cn

he.net的认证也升级啦：

![IPv6 Certification Badge for obaby](//ipv6.he.net/certification/create_badge.php?pass_name=obaby&badge=2)

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《服务器支持IPv6》](https://h4ck.org.cn/2023/02/11253)
\* 本文链接：<https://h4ck.org.cn/2023/02/11253>
\* 短链接：<https://oba.by/?p=11253>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[IPv6](https://h4ck.org.cn/tags/ipv6)[WordPress](https://h4ck.org.cn/tags/wordpress)

[Previous Post](https://h4ck.org.cn/2023/02/11269)
[Next Post](https://h4ck.org.cn/2023/02/11240)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2020年9月15日

#### [BuddyPress Theme Remove Sidebar](https://h4ck.org.cn/2020/09/7496)

2021年8月12日

#### [Gravatar 头像无法加载](https://h4ck.org.cn/2021/08/8590)

2022年9月3日

#### [WordPress 自动发布文章](https://h4ck.org.cn/2022/09/10435)

### 11 comments

1. ![](https://gg.lang.bi/avatar/8824e297c4534b8bd95cf3935277fe4f08f4cd576cbecad8166587874e97a036?s=64&d=identicon&r=r) **[叶开](https://qq.md/)**说道：

   [2023年2月20日 20:36](https://h4ck.org.cn/2023/02/11253#comment-92397)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Firefox 110](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/firefox.png "Firefox 110") Firefox 110 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   很可以啊！IPV6认证 哈哈。

   我是简单暴力一点，直接套CF解析，不然IPV6的服务器，不知道怎么用。

   [回复](#comment-92397)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年2月21日 08:48](https://h4ck.org.cn/2023/02/11253#comment-92402)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      比较鸡肋~~~ ![laugh](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/laugh.gif)

      [回复](#comment-92402)
2. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

   [2023年2月21日 00:54](https://h4ck.org.cn/2023/02/11253#comment-92398)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/bad...