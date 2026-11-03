---
title: 群晖被勒索病毒打穿了，我连夜把我的飞牛 NAS 检查了一遍
url: https://mp.weixin.qq.com/s/UxIWyfVa8w0djSQB9Kyvgg
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:45:09.585225
---

# 群晖被勒索病毒打穿了，我连夜把我的飞牛 NAS 检查了一遍

# 群晖被勒索病毒打穿了，我连夜把我的飞牛 NAS 检查了一遍

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安全预计阅读 11 分钟 · 共 4014 字

群晖被勒索病毒打穿了，我连夜把我的飞牛 NAS 检查了一遍

NAS · 勒索病毒防护

#飞牛NAS#勒索病毒#安全清单#Tailscale

READING PATH

阅读路线

9 个章节

01

先看懂这次攻击，才知道自己该防什么

-

02

第一件事：关掉公网，改走虚拟局域网

-

03

第二件事：把容器一个个过堂

-

04

第三件事：应用中心的套件，别当它不存在

-

05

第四件事：系统里的安全开关，一个个拨上

-

06

第五件事：快照和备份，做物理隔离

-

07

第六件事：学会一套中招后的自救知识

-

08

我的飞牛安全清单

-

09

群晖的今天，是所有 NAS 的预演

10月底那几天，NAS 圈子炸了。[群晖遭到全球性勒索攻击](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457391328&idx=1&sn=be797d62403286e1e1728de73cd05e9f&scene=21#wechat_redirect)。

攻击

C3RB3R 勒索病毒 · Cerber 家族变种

#CVSS 10.0#RCE#0.085 BTC

利用两个 CVSS 满分 10.0 的远程代码执行漏洞，对暴露在公网的设备发起自动化攻击。中招症状：风扇狂转、CPU 拉满、所有文件后缀变成 `.L0CK3D`，每层目录留下一封 `read-me3.txt`，索要 0.085 BTC。加密用 RSA-4096 加 AES，数学上暴力破解不可行，没有通用解密工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxrD3X9McAyGC4U2uSCibIAGiamhKpgKG03IOZiaI8iaAicxrq8KCGPDianDgPsyRuHJY0FmggKQOQXT4mGUudqynndaLjNCSZiav4vX0/640?wx_fmt=png&from=appmsg)

我的主力`NAS`是飞牛。看到这条新闻的时候，我的第一反应不是庆幸。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfzGwT0wZX9RSc74YUS1ZqUzZDvibPQicJvdwuicGMhXCicOzhY366jDb2wxOsb2AwYibC1LgtzS5CPMicZHHf4RhtgC0Rh4UaCbib4kME/640?wx_fmt=png&from=appmsg)

是后背发凉。

因为群晖和飞牛，本质上是同一类东西。一台 24 小时开着的`Linux`机器，跑着一堆套件和容器，被它的主人用端口映射送到公网上。

群晖今天被扫穿，飞牛没有任何理由觉得自己安全。

CHAPTER 01

**01****先看懂这次攻击，才知道自己该防什么**ANALYSIS

这次攻击最值得琢磨的地方，是它的两条路径。

ATTACK PATHS

两条攻击路径

1

路径一 打 Docker 容器

企业在群晖 Container Manager 里自建 GitLab、Confluence，端口映射到外网。GitLab 爆出未授权 RCE 后，自动化脚本攻进未修补容器，再利用高权限容器挂载目录逃逸到宿主机

2

路径二 打套件

群晖官方确认 PHP 核心 RCE 漏洞直接影响 MailStation、Calendar 等原生套件，不需要任何账号密码，从外部直捣未更新套件底层

瘆人

升级到最新版照样中招

#后门#cron.d

不少已经升级到最新版的用户照样中招。因为他们在更新之前就被植入了后门，恶意脚本藏在 `/etc/cron.d/` 这种计划任务目录里。主系统补丁打完了，定时任务依然按时触发加密。

最狠的是，勒索程序会把同机可写入目录下的本机备份一并加密。没启用多版本锁定的备份目录，在它眼里就是普通文件。

看完这几条，你会发现它打的从来都只是群晖。

它打的是：公网暴露的端口、没更新的容器、被忽视的套件、和备份放在一起的快照。这四样东西，我的飞牛一样不少。

CHAPTER 02

**02****第一件事：关掉公网，改走虚拟局域网**ACTION 01

我之前为了在外面看照片，路由器上开着端口映射。看完群晖的案例，我当晚就把映射全删了，顺手把路由器的 UPnP 关掉。

容易忽略

IPv6 入站同样会被扫描

#IPv6#防火墙

IPv6 入站访问同样会被自动化工具扫描。群晖这波攻击里，IPv6 地址一样是入口。我把路由器的 IPv6 防火墙规则收紧了，只允许出站。

远程访问改用 Tailscale。装好登录，手机和笔记本都进虚拟局域网，在外面访问 NAS 和坐在家里没区别。流量点对点加密，公网上根本扫不到我。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyiaOkCe3Uz5vVxxLicYe6ric6d2591V7lyF2ibwj6NibHn7C43KUiagD9Lic4dpbW9zkeiaibyg7FPzr4pxJutNCULibhdHUMX96Bs3EDm8/640?wx_fmt=png&from=appmsg)

这一个动作，直接让我从攻击面上消失了。省下的那点便利，和照片被加密比起来，根本不值一提。

CHAPTER 03

**03****第二件事：把容器一个个过堂**ACTION 02

群晖的案例里，容器是最常被忽视的入口。我逐条检查了自己飞牛上的容器。

3 CHECKS

容器三查

1

① 查端口映射

有没有容器把端口映射到了 0.0.0.0。Docker 端口映射会绕过系统防火墙。不对外服务的容器，改绑 127.0.0.1

2

② 查权限

有没有容器用了 privileged 模式或挂载了 docker.sock。这种容器一旦被打穿，等于把宿主机送出去

3

③ 查镜像来源

GitLab、Confluence 这类企业级软件漏洞一个接一个。跑在 NAS 上的，想清楚有没有必要

我的原则改成了：NAS 上只跑生活和家庭用的服务，开发实验全挪到别的机器。镜像全部重新拉了一遍最新版。旧镜像里的漏洞，你永远不知道什么时候爆。

CHAPTER 04

**04****第三件事：应用中心的套件，别当它不存在**ACTION 03

群晖的教训是套件被当成了盲区。`MailStation`、`Calendar`这些官方套件，很多人装完就忘了，漏洞躺在里面半年。

我把飞牛应用中心里装的每个应用都过了一遍。用不着的直接卸载，用着的确认升到最新版。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfzl1Vgx6MfJ9iaknb1tfUucZYkHQ0ibn50Ificv2hkAbJMndH5xSjBTU5QVRBPgZCFH6xsztKBUln1FGslLXwia1pCKibyfN6VT14wA/640?wx_fmt=png&from=appmsg)

系统本身也一样。飞牛帮助中心的安全披露页，2026 年一年发了十几条高危公告。内核的、应用的，一个月好几条。

我把系统更新设成了每周必看，安全更新当天就打。

CHAPTER 05

**05****第四件事：系统里的安全开关，一个个拨上**ACTION 04

群晖那批中招的机器，大多数连系统自带的安全功能都没开全。飞牛里这些开关也都有，只是默认关着，没人替你拨。

前置

拨之前先做一件事：留一条退路

#手机测试#截图存档

只改一项，改完先在手机连家里 Wi-Fi 的状态下确认还能登录，再用蜂窝网络测外网访问。防火墙和端口这类设置，改错一次就可能把自己锁在门外。路由器上原有的转发规则，先截个图存好。

01

SSH 不常用就关掉

路径是系统设置 → SSH。普通家庭用户没有明确用途，直接关。要维护时临时开，用完关。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfzaQGtG4MVxTLVjZ8NTRajcRWlLibPRryUuNJdk0fG4QZeCuXRzV9pstDJibrKjctKJKtGADnMkbwhRX8etHu9dDAhnXRNxga5DU/640?wx_fmt=png&from=appmsg)

确实需要长期用，把默认的 22 端口改成个没人占的高位端口，路由器转发规则同步改。改端口只是少被常见扫描碰到，不等于安全，密码和密钥认证该有还得有。

02

给网页登录加一道访问码

系统设置 → 安全性 → 访问设置 → 开启访问码。之后从新设备或新浏览器进来，页面会先要访问码，过了才能登录。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfzGLbiaiau7FR7xh06aIukcx4jMUCxz0YOwtQ6nzJhxCF2Lv1iaGibPFC4kagAhBWY7kn7CtTWDNiaPhibqEbjCep0PTgsUJQzHgichHw/640?wx_fmt=png&from=appmsg)

访问码是登录之前的门槛，不能替代密码和双重验证。单独设一个，别跟登录密码重复。要命的是很多人把访问码写进公众号教程里，等于公开贴告示。

03

管理员开双重验证，自己的设备才勾信任

先在个人设置 → 双重验证，绑定支持 TOTP 的身份验证器。手机扫码，输应用生成的一次性验证码，绑完。再去系统设置 → 安全性 → 账号安全，开启强制双重验证，指定用户或用户组范围。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfz2KnQwOtOsxjCduN0pACmSdicMG4okorSguAsTdMtQI2F7KlXUTPFTrQQlI83tB6weda5ianK1S6B8rn8xDanE8ibSmtQVM3vmAs/640?wx_fmt=png&from=appmsg)

顺序坑

先绑管理员，再扩大强制范围

#家人#锁死

先确认管理员账号已经绑好、安全邮箱能收到邮件，再扩大强制范围。不然家人还没绑定，一强制就全登不上。

前置条件两条：系统时间改成自动同步（TOTP 基于时间，时间不对验证永远失败）；绑定安全邮箱并开启邮件通知服务（手机丢了靠它拿紧急验证码）。信任设备只在自己的私人电脑上勾。

04

开启异常 IP 封禁

系统设置 → 安全性 → 防护 → 开启封禁异常 IP，按需调整自动封禁规则。异常登录行为会被限制，官方说明这条规则对 SSH 登录同样生效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxV9f077b4KldffqEB7Hb5d1lTh3HibmkDwDD2TMHxE6pyibMI7R4YoicV37wnuDfJo0lXoDBoCCYCdWsYtzibLCwsm42LwNMsHL4E/640?wx_fmt=png&from=appmsg)

提醒一句，你自己连错几次密码，也可能被短暂封禁。操作前先确认局域网访问方式、管理员邮箱和其他恢复入口都可用。也别图方便把常用来源全塞进永久白名单，那等于把封禁废了。

05

防火墙：入站管死，出站别乱动

系统设置 → 安全性 → 防火墙。默认关闭，开启后看到一堆预设规则，先理清楚再动。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyp82ESEPBMrUvwyCshtpsRNuxTfpJXToibjUicFiaXC6Moh7Vu5IhGKy741skFPgef38MxBTBTgdJBiaDVXiaJWre4zZoNwCibQoiaqc/640?wx_fmt=png&from=appmsg)

入站规则控制谁能连你 NAS 上的端口。只放真正需要的服务，能限定来源 IP 或局域网网段的，别选全部来源。我自己的情况是只保留一个对外端口。

出站规则控制 NAS 主动往外连。新手千万别一上来就设成全部禁止。系统更新、通知、DDNS、云同步、FN Connect 全靠出站。

前车之鉴

出站卡太死会把自己锁在门外

#邮件#双重验证

社区里有人把出站卡太死，直接把自己锁在门外，连双重验证的邮件都发不出去，最后靠命令行救回来的。

入站从严，出站默认允许。这是我踩过弯路之后的做法。

还有两条：别照抄别人截图里的端口号，服务端口因人而异。端口转发要和防火墙规则对得上，路由器开着你没放行的端口，等于白开。

06

不用的共享协议，平时关掉

系统设置 → 文件共享协议。逐项检查：

SMBWebDAVFTPNFSDLNA

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyRJ7IuKxTFBtrn5ogEwqVkbojd3miallA98DFwkH4mpDwxY6E8eTFwfIPWrdUWrSRibKicBfXJOia7FKfdbpMOCyOZ76sE4hqicu7s/640?wx_fmt=png&from=appmsg)

电脑局域网访问共享文件要用 SMB，部分播放器走 WebDAV，媒体设备用 DLNA。不需要的那项就关，需要时再开。

最容易犯的错是想着以后可能用到，全打开。这些协议一旦映射到公网，就是明晃晃的入口。群晖这次被打穿的路径里，就有一条是这类对外服务。

07

先申请免费证书，再开强制 HTTPS

系统设置 → 安全性 → 证书 → 新增证书，按页面提示申请 Let's Encrypt 免费证书。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyO31WgM9j1Ee7n0ycVHF8T8Nn78WgH74pnn2Bhiavjtm5r28uf9ZicSSHfR88704TVXBCuf29sTKH1mibCM6Yq2bcVTibcafs2mag/640?wx_fmt=png&from=appmsg)

顺序

顺序别搞反

#证书#HTTPS

先确认证书签发成功、访问域名和证书域名一致、浏览器显示连接安全，再开强制 HTTPS。强制 HTTPS 本身只是把 HTTP 重定向到 HTTPS，没有有效证书就开，你会得到一个满屏报错的后台。证书有有效期，留意自动续签状态，到期没续上，外网访问直接断。

08

账号分级，别全家人共用一个管理员

管理员账号只干维护的活，装应用、改系统设置。日常看照片、存文件、播放影音，用普通账号。

每个用户单独设密码，够强，别跟其他网站重复。文件夹权限按需给，不要让每个家庭账号都有管理员权限。不用了的账号及时停用或删除。

我之前的做法很糟。全家共用一个管理员账号，图省事。真出事的时候，你连是谁操作的都查不出来。

关完这套，大概二三十分钟。群晖事件里那些机器要是做过这一步，结局会改写很多。

CHAPTER 06

**06****第五件事：快照和备份，做物理隔离**ACTION 05

这次事件里最惨的用户，是备份和正本放在同一台机器上的。勒索程序遍历所有挂载目录，备份被当普通文件一起加密。

我把备份策略重新做了三件事。

3 THINGS

备份三件事

1

① 开启快照并设置防篡改

快照锁住之后，勒索软件改不动历史版本

2

② 备份放离线

关键数据每周备份到移动硬盘，备完就断开连接。离线备份不挂在网上，勒索软件够不着

3

③ 3-2-1 原则

三份数据，两种介质，一份异地。云端那份用带版本历史的服务，防止同步的也是加密后的文件

备份只有能恢复才算数。我挑了个周末做了次恢复演练，从离线盘还原了一个目录，验证了文件能打开。

CHAPTER 07

**07****第六件事：学会一套中招后的自救知识**ACTION 06

这次事件里有一个救命知识点，我第一次知道，觉得应该让更多人知道。

救命

千万别拔电源，别重启

#内存#主密钥#48字节

如果你有一天亲眼看着文件后缀在变化，记住，千万别拔电源，别重启。因为解密所需的 48 字节主密钥，在加密运行期间就存在内存里。保持通电，切断外网，从内网 SSH 进去导出内存镜像，有机会免费无损恢复全部数据。一断电，就只剩交赎金一条路。

RESCUE

正确自救顺序

1

① 拔网线断外网

切断攻击者连接

2

② 保持通电

保住内存里的主密钥

3

③ SSH 登录导出内存镜像

有机会免费无损恢复

4

④ 隔离排查后门

检查 /etc/cron.d/ 等计划任务残留

5

⑤ 轮换所有密码

防止二次入侵

6

⑥ 再谈恢复

确认安全后开始恢复数据

平时把这条记下，关键时刻值 0.085 个比特币。

CHAPTER 08

**08****我的飞牛安全清单**CHECKLIST

| 项目 | 我做了什么 |
| --- | --- |
| **公网暴露** | 删除端口映射，关 UPnP，收紧 IPv6 入站 |
| **远程访问** | 改用 Tailscale 虚拟局域网 |
| **SSH** | 默认关闭，需要时临时开，长期用改高位端口 |
| **访问码** | 已开启，独立设置，不与登录密码重复 |
| **双重验证** | 管理员已绑定 TOTP，强制全员开启，仅私人设备信任 |
| **异常 IP 封禁** | 已开启，规则覆盖 SSH，白名单没乱加 |
| **防火墙** | 入站只放必要端口，出站默认允许，端口转发与规则对应 |
| **共享协议** | SMB、WebDAV、FTP、NFS、DLNA 只开当前需要的 |
| **HTTPS** | 先申请 Let's Encrypt 证书，再开强制 HTTPS |
| **账号分级** | 管理员只做维护，家人用普通账号+各自密码 |
| **容器** | 端口不绑 0.0.0.0，不用 privileged，镜像更新 |
| **套件** | 卸载不用的，更新在用的 |
| **系统** | 安全更新当天打，每周查看披露页 |
| **快照** | 开启防篡改快照 |
| **备份** | 离线硬盘加云端异地，做过恢复演练 |
| **自救知识** | 记住中招时别断电 |

CHAPTER 09

**09****群晖的今天，是所有 NAS 的预演**CONCLUSION

有人觉得，我用的是飞牛，这次是群晖的事，与我无关。

这个想法最危险。攻击者写自动化脚本的时候，盯上的从来都是一类暴露面。

公网端口、过期容器、被遗忘的套件、没有隔离的备份。换个牌子，这些套路一样好使...