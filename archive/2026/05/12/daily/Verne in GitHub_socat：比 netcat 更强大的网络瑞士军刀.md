---
title: socat：比 netcat 更强大的网络瑞士军刀
url: https://blog.einverne.info/post/2026/05/socat-command-usage.html
source: Verne in GitHub
date: 2026-05-12
fetch_date: 2026-05-13T05:45:52.928149
---

# socat：比 netcat 更强大的网络瑞士军刀

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# socat：比 netcat 更强大的网络瑞士军刀 一条命令连接万物，端口转发、隧道、调试一网打尽

Posted on 05/12/2026
, Last modified on 05/12/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-05-12-socat-command-usage.md)

![socat 网络数据流示意图](https://pic.einverne.info/images/2026-05-12-10-00-00-socat-network-streams.png)

在 Linux 网络工具箱里，大多数人都知道 [[netcat]]（nc），遇到要临时监听端口、传文件、测连通性，第一反应就是 `nc`。但用了一段时间之后我发现，[[socat]] 才是那个被严重低估的工具——它不仅能做 netcat 的一切，还能做很多 netcat 根本做不到的事，比如 SSL 加密通信、Unix socket 代理、串口转 TCP，以及真正灵活的双向数据流转发。

这篇文章我想把自己用 socat 的经验好好梳理一遍，从基础概念到实战场景，争取让你看完之后不再只会用 netcat 了。

## socat 是什么

socat 的全称是 **SO**cket **CAT**，名字直接说明了它的设计思路——把各种类型的数据流（socket）像 cat 一样连接起来。官方的描述是”建立两个双向字节流并在它们之间传输数据”，听起来有点抽象，但换个说法就清楚了：socat 可以把任意两个”地址”连接起来，数据在两端之间双向流动。

这里的”地址”可以是 TCP 端口、UDP 端口、Unix socket、文件、管道、设备（比如串口 /dev/ttyS0）、甚至标准输入输出。这种设计让 socat 的应用场景非常广泛，而不像 netcat 那样主要局限在 TCP/UDP 的范畴内。

安装也很简单：

```
# Debian/Ubuntu
sudo apt install socat

# macOS
brew install socat

# CentOS/RHEL
sudo yum install socat
```

## 核心语法与基本概念

socat 的命令格式很固定：

```
socat [options] <address1> <address2>
```

两个地址之间会建立双向数据流。地址的格式通常是 `TYPE:parameters`，比如 `TCP:127.0.0.1:8080`、`UDP-LISTEN:9000`、`STDIN`、`FILE:/tmp/data.txt` 等。

几个最常用的地址类型：

* `TCP:<host>:<port>` — 连接到某个 TCP 地址
* `TCP-LISTEN:<port>` — 监听某个 TCP 端口
* `UDP:<host>:<port>` / `UDP-LISTEN:<port>` — UDP 版本
* `STDIN` / `STDOUT` — 标准输入输出
* `FILE:<path>` — 读写文件
* `UNIX-CONNECT:<path>` / `UNIX-LISTEN:<path>` — Unix domain socket
* `OPENSSL:<host>:<port>` — SSL/TLS 连接
* `EXEC:<command>` — 执行命令并连接其 stdin/stdout

## 端口转发：最高频的使用场景

端口转发大概是我用 socat 最多的场景。比如你在内网有一台机器，只有 22 端口对外开放，但你想在本地直接访问那台机器上的 Web 服务（假设跑在 8080）。用 socat 一行搞定：

```
# 在跳板机上运行：将本地 8888 转发到目标机器的 8080
socat TCP-LISTEN:8888,fork TCP:target-host:8080
```

这里的 `fork` 参数很重要，它让 socat 在接受一个连接后继续监听，而不是只处理一次就退出。没有 `fork` 的话，socat 接受第一个连接处理完就会停止，这显然不是我们想要的行为。

如果要把本地的 UDP 端口转发出去：

```
socat UDP-LISTEN:5353,fork UDP:8.8.8.8:53
```

还有一个我经常用到的场景：把 IPv6 地址桥接给只支持 IPv4 的程序访问。比如本地服务只绑定在 IPv4，但你想从 IPv6 客户端访问：

```
socat TCP6-LISTEN:8080,fork TCP4:127.0.0.1:8080
```

## 替代 netcat 做简单通信

用 socat 做简单的 TCP 监听和连接，和 netcat 几乎一样直观。

在服务端监听：

```
socat TCP-LISTEN:12345 STDOUT
```

在客户端连接发送数据：

```
echo "hello from socat" | socat - TCP:server-ip:12345
```

传文件也很方便，接收端先开好监听：

```
socat TCP-LISTEN:12345 > received_file.tar.gz
```

发送端：

```
socat - TCP:server-ip:12345 < local_file.tar.gz
```

比起 netcat，socat 的好处是行为更可预测，不同平台的 netcat 实现差异很大（BSD 版和 GNU 版语法有不少差异），而 socat 的行为跨平台高度一致。

## Unix Socket 代理：解决权限问题的妙用

这个场景在容器和 CI/CD 环境里特别实用。Docker daemon 的 socket 默认在 `/var/run/docker.sock`，只有 root 或 docker 组的用户才能访问。如果你在某个受限环境里需要让普通用户或某个进程访问 Docker API，可以用 socat 在 TCP 端口上暴露一个代理：

```
socat TCP-LISTEN:2375,fork UNIX-CONNECT:/var/run/docker.sock
```

之后就可以通过 `DOCKER_HOST=tcp://127.0.0.1:2375` 来使用 Docker 客户端，不再受 socket 权限限制。当然，这样做要注意安全问题，仅在受控环境中使用。

反过来，如果某个工具只支持 Unix socket，但你的服务暴露的是 TCP 端口，也可以反向代理：

```
socat UNIX-LISTEN:/tmp/myapp.sock,fork TCP:127.0.0.1:3000
```

## SSL/TLS 加密通道

这是 socat 相对于 netcat 最大的优势之一。你可以用 socat 快速建立一个加密通道，不需要额外配置 nginx 或 stunnel。

先生成自签证书：

```
openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt
cat server.key server.crt > server.pem
```

服务端启动加密监听：

```
socat OPENSSL-LISTEN:443,cert=server.pem,verify=0 TCP:127.0.0.1:8080
```

客户端连接：

```
socat TCP-LISTEN:8080,fork OPENSSL:server-host:443,verify=0
```

`verify=0` 表示不验证证书（适合自签证书的测试场景），生产环境应该正确配置 CA 证书验证。

## 串口通信转 TCP

这个功能是 socat 独有的，netcat 完全做不到。在嵌入式开发或者工业设备调试中，经常需要把串口数据转发到网络上，让远程的机器能够访问本地的串口设备：

```
# 把本地串口 /dev/ttyUSB0 转发到 TCP 9600 端口
socat TCP-LISTEN:9600,fork /dev/ttyUSB0,raw,echo=0,b115200
```

`b115200` 是波特率设置，`raw` 表示原始模式，`echo=0` 关闭回显。另一端可以用 socat 连接这个 TCP 端口，就像直接操作本地串口一样。

## 在脚本里动态测试端口连通性

socat 可以用来替代 telnet 做端口连通性测试，而且更适合在脚本里使用：

```
# 测试 TCP 端口是否可达，超时 5 秒
socat /dev/null TCP:target-host:8080,connect-timeout=5
echo $?  # 0 表示成功，非0 表示失败
```

比 telnet 好的地方在于 socat 的退出码很规范，适合脚本判断，而 telnet 在不同系统上行为不一致。

## 几个实用的小技巧

在使用 socat 的过程中，我积累了一些提升体验的习惯：

加上 `-d -d` 可以开启详细日志，排查问题时非常有用：

```
socat -d -d TCP-LISTEN:8080,fork TCP:backend:8080
```

对于需要长期稳定运行的转发，可以配合 systemd 或者 supervisor 来管理进程，而不是直接跑在 shell 会话里，避免断开 SSH 后转发失效。

`reuseaddr` 选项可以避免”地址已在使用”的错误，在频繁重启的开发场景下很实用：

```
socat TCP-LISTEN:8080,reuseaddr,fork TCP:backend:8080
```

对于需要多个并发连接的场景，默认的 fork 模式已经够用；但如果担心 fork 带来的开销，可以用 `TCP-LISTEN:port,fork,max-children=50` 限制最大子进程数。

## 最后

socat 是那种乍看文档有点发怵、但真正上手之后会让你爱不释手的工具。它的地址格式设计非常正交——理解了”两个地址之间建立双向流”这个核心模型，几乎所有用法都能举一反三。端口转发、协议转换、加密隧道、串口桥接，这些场景在日常运维和开发调试中比你想象的出现得更频繁。

我现在遇到网络调试的需求，第一反应已经从 `nc` 变成了 `socat`，主要因为它的行为更一致、功能更全面，而且在 SSL 和 Unix socket 这些场景上完全没有替代品。如果你还没把它放进自己的工具箱，值得花半个小时好好熟悉一下。

## Related Posts

* [socat：比 netcat 更强大的网络瑞士军刀](/post/2026/05/socat-command-usage.html) - 05/12/2026
* [自行搭建 ZeroTier Network Controller 组件虚拟局域网](/post/2021/11/zerotier-self-hosted-network-controller.html) - 11/04/2021
* [独服 Proxmox VE 配置 NAT 使虚拟机共用一个公网 IP](/post/2021/10/proxmox-ve-config-nat-vm-use-same-public-ip.html) - 10/15/2021
* [简单高效跨平台的备份程序 Restic](/post/2021/09/restic-backup-tool.html) - 09/12/2021
* [『译』我最喜欢的命令行工具](/post/2020/10/my-favorite-cli-tools.html) - 10/30/2020
* [rTorrent 和 ruTorrent 使用](/post/2020/03/rtorrent-and-rutorrent.html) - 03/16/2020
* [命令行的艺术](/post/2020/03/the-art-of-command-line.html) - 03/04/2020
* [Syncthing 又一款同步工具](/post/2019/10/syncthing.html) - 10/11/2019
* [同步工具整理总结](/post/2019/10/sync-tools.html) - 10/10/2019
* [每天学习一个命令：xargs 连接输出和输入](/post/2019/06/xargs.html) - 06/19/2019

---

* [← Previous（前一篇）](/post/2026/05/codex-lb-chatgpt-account-load-balancer.html "codex-lb：用负载均衡的思路管理多个 ChatGPT 账号")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2026/05/switch-claude-code-codex-accounts.html "本地快速切换 Claude Code 和 Codex CLI 账号的几种方案")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/05/socat-command-usage.html)评论。

* [学习笔记 510](/categories.html#学习笔记)

* [linux 437](/tags.html#linux)
* [networking 6](/tags.html#networking)
* [socat 1](/tags.html#socat)
* [command-line 4](/tags.html#command-line)
* [tools 13](/tags.html#tools)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").