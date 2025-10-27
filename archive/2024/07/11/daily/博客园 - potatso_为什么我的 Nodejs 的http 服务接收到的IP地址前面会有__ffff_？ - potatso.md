---
title: 为什么我的 Nodejs 的http 服务接收到的IP地址前面会有::ffff:？ - potatso
url: https://www.cnblogs.com/potatso/p/18293546
source: 博客园 - potatso
date: 2024-07-11
fetch_date: 2025-10-06T17:38:28.048141
---

# 为什么我的 Nodejs 的http 服务接收到的IP地址前面会有::ffff:？ - potatso

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

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

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [为什么我的 Nodejs 的http 服务接收到的IP地址前面会有::ffff:？](https://www.cnblogs.com/potatso/p/18293546 "发布于 2024-07-10 11:15")

# Hello World

今天介绍一个比较绕口的技术。

故事的首先要从测试同学提的一个 BUG 开始

![img](https://img2023.cnblogs.com/blog/1916047/202407/1916047-20240710112133787-47697167.jpg)

为什么一个ipv4 地址前面会有::ffff:呢？是不是你的程序写错了呢。那我们来深究一下这个是什么东西。

这种地址叫 ipv4 mapped ipv6。为什么会有这么奇怪的东西呢，与 ipv6 部署有关。

我们知道，ipb6 的地址空间范围非常大。ipv6 改动不光涉及到网络层，例如配置 ipv6 的路由协议，还有应用层的调整，例如程序从 ipv4 监听改成 ipv6 监听。但是这个改动的成本巨大，又要涉及到代码的调整，又要涉及到地址处理的问题，例如是否监听多协议等等等，于是有人发明了 ipv6 dual stack mode 技术。通俗来讲就是

* 程序只需要监听 ipv6，如果不做特殊设置（IPV6\_ONLY） 那么socket 同时附带同时也监听 ipv4。并且 ipv4 接受到的请求，自动转换为 ipv6 的格式交给应用层处理

下面我们写一个python 的小程序来看一下

```
import socket
import threading

def create_socket():
    # 创建一个可以同时支持 IPv4 和 IPv6 的套接字
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

    # 设置地址重用选项,允许快速重启服务器
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 设置 IPv6 only 选项为 False,允许 IPv4 客户端连接
    if hasattr(socket, 'IPV6_V6ONLY'):
        sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, False)

    return sock

def start_server():
    addr = ("", 8080)  # 监听所有网络接口的 8080 端口

    # 尝试创建支持双栈 IPv6 的套接字
    if socket.has_dualstack_ipv6():
        sock = socket.create_server(addr, family = socket.AF_INET6, dualstack_ipv6 = True)
    else:
        # 如果不支持双栈 IPv6,则创建普通的 IPv6 套接字
        sock = socket.create_server(addr)

    sock.listen(5)
    print("Server listening on 0.0.0.0:8080 (IPv4 and IPv6)")

    while True:
        conn, addr = sock.accept()
        threading.Thread(target = handle_client, args = (conn, addr)).start()

def handle_client(conn, addr):
    print(f"New connection from {addr[0]}:{addr[1]}")

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            conn.sendall(data)  # 回显收到的数据
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        conn.close()
        print(f"Connection closed with {addr[0]}:{addr[1]}")

if __name__ == "__main__":
    start_server()
```

我们通过 nc 使用 ipv4 协议链接 python 的服务端，可以发现正常触发了ffff::

![img](https://img2023.cnblogs.com/blog/1916047/202407/1916047-20240710112216469-1317343181.png)

![img](https://img2023.cnblogs.com/blog/1916047/202407/1916047-20240710112244589-46595096.png)

并且这种监听会被内核socket 标记为 tcp 46。当然，这里还有一个重要区别，我们以 linux 为例，AP\_ENABLE\_V4\_MAPPED 。这个参数决定了双栈模式下，收到的 ipv4 地址是否翻译为 ipv6 地址去展示。

但是这种技术不知为何鲜为人知，导致测试的同学和绝大多数研发都不知道，以为是 BUG。那我们怎么解决呢？

1. 关闭ipv6 双栈
2. 只监听 ipv6
3. 在 Linux 中，默认情况下，AP\_ENABLE\_V4\_MAPPED 是 1，那么 httpd 就会直接监听 ipv6， 因为此时 ipv6 的 socket 能够处理 ipv4 的请求；另外，bind() 系统调用会对用户空间的进程透明处理 ipv6 没有开启的情况，此时会监听到 ipv4。

   而如果我们在编译 httpd 的时候使用 --disable-v4-mapped 参数禁止 ipv4 mapped，那么默认情况下， httpd 会分别监听在 ipv4 和 ipv6，而非只监听 ipv6

回到我们的业务代码，我们的业务是 Nodejs 开发。在 Nodejs 的 Issues 中，很多人都提到了 ipv6 dual stack 很容易误导人，强烈要求社区关闭该功能。

![img](https://img2023.cnblogs.com/blog/1916047/202407/1916047-20240710112312140-796897497.png)

Nodejs 的 socket 监听再没有指定协议的情况下，会使用 Ipv6 dual stack 监听。并且与操作系统有关，Issues 中有人提到，Mac 会默认监听 Tcp46。也就是 ipv4 的请求和 ipv6 的请求不会互相掺杂，但是 ubuntu 却变成了 tcp6.

![img](https://img2023.cnblogs.com/blog/1916047/202407/1916047-20240710112337493-1483496603.png)

所以，大约在 21 年左右，Nodejs 终于支持了单独设置 Ipv6Only 选项，如图

![img](https://img2023.cnblogs.com/blog/1916047/202407/1916047-20240710112456283-1838390545.png)

<https://github.com/nodejs/help/issues/4067#:~:text=https://nodejs.org/api/net.html#serverlisten>

测试由于年少无知，乱提 BUG

posted @
2024-07-10 11:15
[potatso](https://www.cnblogs.com/potatso)
阅读(337)
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