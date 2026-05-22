---
title: 三个 CVE 与 2026 年 5 月那条被无视的利用链
url: https://mp.weixin.qq.com/s/PBSxXmTFJUv6zCx4u9oC0g
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:03:09.341837
---

# 三个 CVE 与 2026 年 5 月那条被无视的利用链

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSgwRr8DIicxrfvebcicJouA4q06EichRiaccJkOReADr1KB6nfTR66kd9Iqibo4iaNNMsnPCcZHxs28TLvVNuUT1pSs7E1ug4fOrZajM/0?wx_fmt=jpeg)

# 三个 CVE 与 2026 年 5 月那条被无视的利用链

Bob Rudis
Bob Rudis

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://rud.is/b/2026/05/14/three-cves-and-the-may-2026-exploit-chain-nobodys-taking-seriously/ | Bob Rudis |

2026 年 5 月以接近每周一次的节奏甩出了三个严重的 Linux 漏洞，而安全圈大多把它们当成三起互不相干的倒霉事件来谈。它们不是。把三个拼在一起，就得到一条稳定、无竞争条件、取证上几乎无声的杀伤链，从公网一路打穿到 root。如果你在任何关键业务前面跑着 nginx，请停下手里的活，把这篇看完。

CVE-2026-42945，代号 "NGINX Rift"，5 月 13 日由 depthfirst 公开。这是 `ngx_http_rewrite_module`里的一个堆缓冲区溢出，自 2008 年以来潜伏在每一个 nginx 构建中。未经身份验证的攻击者只要发出一个精心构造的 HTTP 请求，就能覆写堆内存，在 worker 进程中拿到远程代码执行 —— 不需要认证、不需要先有会话，除了一条通往 80 或 443 端口的网络路径，没有任何其他前置条件。根因出在 rewrite 指令的两次遍历不一致上：长度计算阶段按 `is_args=0`( 原始字节数 ) 跑，而拷贝阶段按 `is_args=1`( URI 转义后 ) 跑，于是写入直接越过了分配的边界。触发条件是一种随处可见的配置写法：一条 `rewrite`指令里带未命名的 PCRE 捕获 ( `$1`、`$2`) 且替换字符串中含问号，紧跟着同一个块中再来一条 `rewrite`、`if`或 `set`。CVSS 9.2，名副其实。

CVE-2026-31431，"Copy Fail"，由 Theori 于 4 月 29 日公开。这是 `authencesn`加密模板中的一个逻辑漏洞，允许无特权的本地用户向任意可读文件的页缓存里写入 4 个可控字节，并借此提权到 root。利用代码只有 732 字节的 Python ( 没有竞争条件，没有磁盘写入，没有取证残留 —— 页缓存被污染意味着文件完整性检查依然能过，因为磁盘上的底层文件压根没被动过 )。它在 2017 年以来发布的每一个发行版上都能跑。CISA 已经把它列入了"已知被利用漏洞"目录，修复截止日期为 5 月 15 日。

接下来是 CVE-2026-43284 和 CVE-2026-43500，"Dirty Frag"，由 Hyunwoo Kim 于 5 月 7 日披露。这是一条双漏洞利用链，落点与 Copy Fail 一样 —— 页缓存到 root 的 LPE —— 但完全绕开了 Copy Fail 的缓解措施。要是你以为把 `algif_aead`拉黑就万事大吉，那 Dirty Frag 就改走 `xfrm-ESP`或 `rxrpc`这条道。Microsoft 已经在野观测到相关活动：SSH 拿到落脚点，投放一个 ELF 二进制，再通过 `su`提权。完全可确定性复现。没有竞争条件。同一类漏洞，不同的落点。

为什么这套组合拳比其中任何一个单独的漏洞都更值得警惕？利用链通常是学术练习，发出来证明可行，然后就躺在某个 CTF 题解里慢慢烂掉。这次不是。CVE-2026-42945 从互联网替你递上立足点，CVE-2026-31431 或 CVE-2026-43284 在你登上机器后再把 root 塞到你手里。两步都不需要竞争条件、用户交互或认证。两步都不会在磁盘上留下明显的取证痕迹。截至本文写作时，两者都已经有公开可用的概念验证代码。

这里的攻击面真的让人坐立难安。NGINX 是地球上部署最广的 Web 服务器。WordPress —— 加上一堆海量部署的插件，其官方推荐的 NGINX 配置里就包含那个有漏洞的 rewrite 写法 ( 我查过了，白纸黑字写在文档里 ) —— 撑起了全网 40% 以上的份额。这意味着 whitehouse.gov、NASA、英国政府、澳大利亚政府、加州州政府，以及基本上每一所美国主要大学，都可能在影响范围内。每一个被《21st Century IDEA Act》要求维持公开 Web 存在的联邦机构。每一个在 LEMP 技术栈上跑 WordPress 的市政府。每一个躲在 NGINX ingress controller 后面的 SaaS 应用。攻击者根本不需要什么 0day 链来打这些目标，他们只需要一份公网扫描器的数据访问权、一条用来 grep 出脆弱版本字符串的命令，以及发出一个 HTTP 请求的能力。

我针对 NGINX Rift 模式发布了一个静态配置扫描器。单个 bash 脚本，除了 bash 4+ 和 grep 之外没有任何依赖，离线运行在配置文件上，不会触碰正在运行的 nginx 进程：

```
git clone https://git.sr.ht/~hrbrmstr/cve-2026-42945-scanner
cd cve-2026-42945-scanner
./scan-nginx-rift.sh /etc/nginx
```

在每一台跑 nginx 的机器上都跑一遍。在 CI 里加上 `--json`。把它指向 ingress controller 的 configmaps。输出会告诉你文件、行号、有问题的指令，以及紧随其后的哪条指令构成了可利用条件：

```
[VULN] sites-enabled/wordpress.conf:8 - rewrite ^/([^/]+?)-sitemap([0-9]+)?.xml$
          followed by "if" at line 12
```

如果扫到了命中项，你按优先级有两个选择：

1. 把 nginx 升级到 1.30.1 ( stable ) 或 1.31.0 ( mainline )。
2. 在每一条受影响的 `rewrite`里，把未命名捕获替换成命名捕获：

```
# Before (vulnerable)
rewrite ^/([^/]+?)-sitemap([0-9]+)?.xml$ /index.php?sitemap=$1&sitemap_n=$2 last;

# After (safe)
rewrite ^/(?<term>[^/]+?)-sitemap(?<num>[0-9]+)?.xml$ /index.php?sitemap=$term&sitemap_n=$num last;
```

至于内核侧，现在就去查你发行版的补丁状态，别信什么 "我们回头会搞定" 的鬼话。如果没法立刻打补丁，把 `algif_aead`加进黑名单可以挡住 Copy Fail，但对 Dirty Frag 完全没用。对付 Dirty Frag，如果你的业务用不到，就卸载 `xfrm_algo.ko`和 `rxrpc.ko`，并确保 AppArmor 或 SELinux 策略已经封掉了非特权用户命名空间。

三周三个 Linux 关键 CVE，全都有公开的利用代码，全都藏在已经跑了好多年的代码里。从披露到能用的 exploit 之间的间隔，现在是用小时算，不是用月算。上面那个扫描器把 nginx 这一侧的口子堵上了一块。剩下的，就看你是今天就去检查自己的配置，还是等到日志里冒出什么不对劲的东西才动手 —— 而到了那一步，这种不留取证残留的 LPE 意味着 "看着不对劲" 可能就是你能看到的全部。

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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