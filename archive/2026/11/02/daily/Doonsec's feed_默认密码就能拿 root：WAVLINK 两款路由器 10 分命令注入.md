---
title: 默认密码就能拿 root：WAVLINK 两款路由器 10 分命令注入
url: https://mp.weixin.qq.com/s/HnNSI2YEISYQISGSUIvhxg
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:45:50.747108
---

# 默认密码就能拿 root：WAVLINK 两款路由器 10 分命令注入

# 默认密码就能拿 root：WAVLINK 两款路由器 10 分命令注入

红队安全圈
红队安全圈

红队安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

30 秒看懂

影响范围 · WAVLINK WN536AX6-A（V260507）、WN553X1-B（V260403\_2.0.0），OpenWrt 21.02 定制固件

利用状态 · 公开 PoC 与复现文章已放出，远程可打，暂未见在野扫描

补丁状态 · 未知，厂商未发修复固件，先改密码、关掉公网管理

一个没做过滤的 file\_id 参数，被拼进 shell 命令交给 popen 执行，而执行这条命令的进程是 root。WAVLINK 两款路由器、三个 CVE，都是同一个毛病。

## 01  事情是什么

三个漏洞同一批披露，根因一模一样：Web 后端 /bin/ioos 处理 OpenVPN 客户端相关请求时，把用户传的 file\_id 直接塞进了一条 shell 命令。

CVE-2026-120279，WN536AX6-A，CVSS 3.1 打满 10.0，不需要任何账号。另外两个都在 WN553X1-B 上：CVE-2026-120231 走 openvpn\_cli 分支，CVE-2026-120238 走 ovpn\_file 分支，都是 9.9。

三个都标了 CWE-78，都写明 exploit 已公开。也就是说，现在拿到固件的人，照着公开文档就能把命令打进去。

## 02  为什么危险

问题出在 /bin/ioos 里的两个函数，sub\_416568 和 sub\_4162A8。file\_id 被 snprintf 拼成一条 uci 查询语句，然后直接交给 popen：

snprintf(buf, 0x200,

  "uci show ovpnclient | grep "

  "\"file\_id='%s'\"",

  file\_id);

popen(buf, "r");

// ioos 以 root 身份运行

file\_id 被放进双引号里，输入 a";命令;" 就能闭合引号，把后面的内容当成命令跑掉。因为 ioos 是 root，注入的 curl、nc、rm 全部按 root 执行，直接拿到设备完整控制权。同一函数里还写了另一处，把 uci 里存的路径拼成 rm -rf "%s" 交给 system，能删任意文件。

真正让 10.0 站得住的是认证那一环。WN536AX6-A 出厂配置里 FirstLogin=1，也就是默认允许免密登录，不发密码、只发一个空的登录请求，就能换到合法 token：

GET /protocol.csp

  ?fname=system&opt=login

  &function=set&usrid=

拿到 token 之后套上注入参数，一条 GET 就落命令：

GET /protocol.csp

  ?token=<TOKEN>

  &fname=net&opt=openvpn\_cli

  &function=set

  &ovpn\_enable=1

  &sel\_pwd\_val=0&usr\_name=x

  &usr\_passwd=x&file\_id=

    aa%22%20%7C%20id%20%23

WN553X1-B 稍微麻烦一点，默认口令是 admin，硬编码在 /etc/config/winstar 里，登录时 usrid 传 SHA256(admin) 即可。也就是说，只有改过管理员密码的设备才算真挡住了第一关，出厂状态等于没有认证。

顺带记一个坑：WN553X1-B 打成功时接口可能返回 error 10001，那是后续 uci 操作失败，注入的命令其实已经执行完了。判断成没成要看命令的副作用，不要看返回码。

## 03  谁受影响

无线型号WN536AX6-A · WN553X1-B（WN553X3B）

固件版本V260507 · V260403\_2.0.0

平台OpenWrt 21.02 / MT7986、MT7981

前置条件能访问管理页（默认口令或免密）

开了 WAN 侧 Web 管理、或管理口直接暴露在公网的设备风险最高。只在纯内网当 AP 用、管理页不对外的，攻击面小很多，但默认口令这一关仍然不成立。复现环境是把固件用 qemu-aarch64 加 chroot 跑起来，lighttpd 在前、ioos 在后，说明这些路径不是静态分析猜的，是打通过一遍。

## 04  怎么修

1. 改密码、关免密。 管理员密码别用 admin，后台的 FirstLogin / 快速登录选项一并关掉。

2. 关公网管理。 WAN 侧远程管理关掉，管理页只允许内网访问；用不到就整个关掉。

3. 边界封端口。 在家用或办公网络出口封掉设备管理端口，只留必要的转发规则。

4. 查有没有被动过。 看 /tmp 下有没有陌生文件、管理日志有没有异常登录。命令注入的典型落地就是写 /tmp 或者起一个 nc 回连。

5. 固件没出之前撤下公网。 厂商未发修复版本，这一点没法靠打补丁解决。

一条自查命令，判断是不是免密登录状态：

curl -s "http://<IP>

  /protocol.csp?fname=system

  &opt=login&function=set

  &usrid="

// 返回带 token 即为免密可登录

## 05  一句判断

公网暴露的家用路由器，今晚就该处理；纯内网当 AP 的，明天改密码也来得及，但别拖过这个月。这类设备的实际价值不在漏洞本身，而在于它常年在边界上、固件常年不更新、默认口令常年不改。一个能拿 root 的命令注入，配上免密登录，等于把内网入口的钥匙挂在门上。

## 06  POC 链接

https://github.com/pipiyyb/cve/blob/main/WAVLINK%20WN536AX6-A/WN536AX6-A\_file\_id.md

https://github.com/senxitoyshuyi-ui/HACKALL/blob/main/WAVLINK%20WN553X1-B%20Router/WAVLINK\_WN553X1-B\_openvpn\_cli\_command\_injection.md

https://github.com/senxitoyshuyi-ui/HACKALL/blob/main/WAVLINK%20WN553X1-B%20Router/WAVLINK\_WN553X1-B\_ovpn\_file\_command\_injection.md

说明：三份文档都带完整请求样本与复现结果，作者在 qemu 模拟的固件上验证过。只贴地址，不展开利用全文。

下期继续蹲厂商补丁和 PoC 动静，**关注**后漏洞先知道，修复不踩坑。

— END —

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5HsgFkdwV2JyJtbCAnjqN7qIvk8GZkoD7I5eY36IQQvribiauFhgInT7GIPm2O5D9d2ynIcbnPicbGnox7PL4Hh4g/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过