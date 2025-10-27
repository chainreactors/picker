---
title: Linux 内核重大安全漏洞曝光！indler 漏洞威胁数亿计算机系统
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458567380&idx=1&sn=18d81c63ed1044e4ad9f30e080f0ac7b&chksm=b18df25e86fa7b48050427a1e197dab73e9921ded984be316f4468ea9170b8d90a2b35e50276&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-08-10
fetch_date: 2025-10-06T18:05:22.477922
---

# Linux 内核重大安全漏洞曝光！indler 漏洞威胁数亿计算机系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxX06t7L6hO0H40PJkrwEcYvj1PKzaJFO79TqcDU9bZLj5lxHwJzQOqg/0?wx_fmt=jpeg)

# Linux 内核重大安全漏洞曝光！indler 漏洞威胁数亿计算机系统

看雪学苑

8月8日，著名系统内核专家、《软件调试》作者张银奎发布了一篇文章《是谁在LINUX内核中开了这个大洞？》，曝光隐藏12年之久的 Linux 内核重大安全漏洞 —— indler 漏洞，并表示该漏洞代码存在于从终端到云的数以亿计的计算机系统上，一旦被黑客利用，后果不堪设想。

一切始于一个“诡异的内核oops”，格蠹内核开发团队在测试幽兰系统镜像的过程中，出现了一个随机的内核oops。一旦这个oops发生，便会产生一系列连锁的不良反应：例如声音无法播放，reboot失败等问题。

张银奎提到，这个oops与[719大蓝屏事件](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564526&idx=1&sn=4deed3b6bd00d080b20f3570c0e27abc&chksm=b18d872486fa0e3262df95c425e69c555324b71cda85448884b9aa1528d7e28dcc7cc84cbb39&scene=21#wechat_redirect)原因类似，也是非法访问内存，也就是通常所说的越界。但奇怪的是，越界访问的内存地址不是一般的0指针，也不是明显的小指针（小于4096的地址），而是一个很长的地址：003a72656c646e69。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxebOW3nlQWB7RziaXqdSL6wNribQrvXiaTckA6XgVsiaibQCibwVqYIoEZtNA/640?wx_fmt=png&from=appmsg)

很快，张银奎凭多年经验看出这个地址中包含很多可读的ASCII字符，于是使用windbg的.formats命令转换，得出：

```
0:000> .formats 203a72656c646e69Evaluate expression:  Hex:     203a7265`6c646e69  Decimal: 2322294337798696553  Octal:   0200723446255431067151  Binary:  00100000 00111010 01110010 01100101 01101100 01100100 01101110 01101001  Chars:    :reldni  Time:    Wed Jan 23 00:02:59.869 8960 (UTC + 8:00)  Float:   low 1.10463e+027 high 1.57927e-019  Double:  1.9725e-153
```

错误地址刚好对应的是「 :reldni」这 8 个字符。将这 8 个字符的顺序调整后，就是"indler: "（冒号后面还有一个空格，在栈上找到，有时体现在寄存器里）——为了方便描述，暂且把该漏洞称为 indler 漏洞。

据张银奎介绍，这个oops是随机的，而根据oop提供的函数地址，发生崩溃的内核函数名叫：sysfs\_file\_ops，源代码如下：

```
static const struct sysfs_ops *sysfs_file_ops(struct kernfs_node *kn) 静态常量结构体 sysfs_ops *sysfs_file_ops（结构体 kernfs_node *kn）{  struct kobject *kobj = kn->parent->priv;
  if (kn->flags & KERNFS_LOCKDEP)    lockdep_assert_held(kn);  return kobj->ktype ? kobj->ktype->sysfs_ops : NULL;  返回 kobj->ktype ？kobj->ktype->sysfs_ops ：NULL;}
```

```

```

然而对于这样的内存溢出问题，张银奎笃定这肯定不是“第一现场”，为了找到造成内存溢出的“元凶”，格蠹团队试了很多种方法都没能成功定位。

为了进一步推进，对于越界这样的内存顽症，张银奎使用了最直接的方法：内存检查工具ASAN（Address Sanitizer），但是第一次尝试失败了，因为启用KASAN后，内核无法启动。再次强推KASAN方法，坚定方向，终于，团队成员通过修改u-boot，成功地运行了启用KASAN的内核。很快，KASAN找到了一个内存越界写。

张银奎随即查看内核信息：

* 内核时间戳25秒时，KASAN报告初始化完毕：

```
[   25.146063] kasan: KernelAddressSanitizer initialized (generic)
```

* 33秒时，KASAN抓到越界写：

```
[   33.918201] ==================================================================[   33.918234] BUG: KASAN: slab-out-of-bounds in __memcpy_fromio+0x8c/0x100 [ 33.918234] BUG：KASAN：__memcpy_fromio+0x8c/0x100 中的板块越界[   33.918259] Write of size 8 at addr ffffff8101838afc by task systemd/1 [ 33.918259] 通过任务 systemd/1 在 addr ffffff8101838afc 写入大小为 8
[   33.918283] CPU: 5 PID: 1 Comm: systemd Not tainted 6.1.43-rockchip-rk3588-taiyi #1.0.8 [ 33.918283] CPU：5 PID：1 通信：systemd 未污染 6.1.43-rockchip-rk3588-taiyi #1.0.8[   33.918300] Hardware name: YourLand CodeBook (DT)[   33.918312] Call trace: [ 33.918312] 调用跟踪：[   33.918324]  dump_backtrace+0xd0/0x130[   33.918338]  show_stack+0x20/0x30 [33.918338] show_stack+0x20/0x30[   33.918350]  dump_stack_lvl+0xac/0xe0[   33.918368]  print_report+0x164/0x464[   33.918384]  kasan_report+0xc8/0x1a0[   33.918400]  __asan_store8+0x80/0xa4
```

上面由于涉及到较敏感的安全问题，张银奎省略了代码中很多的调用栈。在关于这次非法方法的详细细节中，也省略了一些具体函数名：

```
[   33.919049] The buggy address belongs to the object at ffffff8101838000                which belongs to the cache kmalloc-4k of size 4096[   33.919061] The buggy address is located 2812 bytes inside of                4096-byte region [ffffff8101838000, ffffff8101839000)
[   33.919082] The buggy address belongs to the physical page:[   33.919094] page:00000000663e5886 refcount:1 mapcount:0 mapping:0000000000000000 index:0x0 pfn:0x101838[   33.919109] head:00000000663e5886 order:3 compound_mapcount:0 compound_pincount:0[   33.919123] flags: 0x8000000000010200(slab|head|zone=2)[   33.919146] raw: 8000000000010200 0000000000000000 dead000000000122 ffffff8100002a80[   33.919159] raw: 0000000000000000 0000000000040004 00000001ffffffff 0000000000000000[   33.919172] page dumped because: kasan: bad access detected
[   33.919192] Memory state around the buggy address:[   33.919205]  ffffff8101838a00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00[   33.919218]  ffffff8101838a80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00[   33.919234] >ffffff8101838b00: 01 fc fc fc fc fc fc fc fc fc fc fc fc fc fc fc[   33.919246]                    ^[   33.919255]  ffffff8101838b80: fc fc fc fc fc fc fc fc fc fc fc fc fc fc fc fc[   33.919270]  ffffff8101838c00: fc fc fc fc fc fc fc fc fc fc fc fc fc fc fc fc[   33.919282] ==================================================================
```

在KASAN的帮助下，张银奎发现了一个内存越界写的错误，通过分析调用栈和错误信息，张银奎逐渐揭开了这个漏洞的秘密。

令人震惊的是，indler漏洞至少在2013年就已经存在，且至今仍在内核主代码树中。这意味着，从2013年到今天的几乎所有Linux内核都有这个漏洞。更令人担忧的是，这个漏洞可以在用户空间通过Linux的虚文件机制触发，黑客可以使用用户空间的应用做跳板，转而攻击内核。

经过初步分析，张银奎及其团队认为这个漏洞可能导致的溢出可以非常大，可以长达数千字节。值得一提的是，他们发现，这个 indler 漏洞代码的来源于 Google。

综合以上特征，indler 漏洞若被黑客利用，势必将引发极其严重的后果。黑客可以使用indler漏洞实施多种攻击，包括向内核空间注入代码实现远程代码执行（RCE）、进行DOS攻击促发溢出，让内核崩溃停止工作。

因此，为了防止这个漏洞被黑客利用，张银奎决定隐藏具体的函数名，并透露目前正在与专业的安全团队合作，商讨下一步的计划。

来源：[《是谁在LINUX内核中开了这个大洞？》](http://mp.weixin.qq.com/s?__biz=MzA3NTk5MDIzNw==&mid=2647670016&idx=1&sn=54cd6e88b7d7b39180591132c79d4fd8&chksm=874c88b2b03b01a4040114b42ef2eaaf4e6e8b833bf35b4935e139c71175d57f75fc30274641&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxQsqcuwwxZLKAHuo4RzmC6n5hXXyVVicTeYopoZOL77aZ8BxTqwzqRiag/640?wx_fmt=png&from=appmsg)

ARM架构作为嵌入式系统领域的瑰宝，一直以来都备受关注。从深度嵌入式，到桌面，再到云，ARM不断攻城略地，正在成为主流。本次培训将带你深入了解ARM架构的三大系列，从M核到A核，从内部调试器到外部调试器，涵盖了丰富的实战内容和动手试验，由《软件调试》作者张银奎亲自主讲，带你揭开ARM的神秘面纱。

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxSO7S2icr5RsWuGibhYCUV7vLTujricWzjaFFnAHZI7MzoHulj8gia5LR5A/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564546&idx=2&sn=6446a19937b02964c69ed7054f6d0161&chksm=b18d874886fa0e5efcf867d5e14ba1e0270e78a8c47b25532152b118fd98db8790bd20ace089&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxqSUqCLLpaYlibTuLGXbRwt79FAZ27q8I0Yp6AzlkAickakCicA6Ly0PJg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxyBtKiaMJNiayqGqiawAElXPpEAtg5l5YTlqgQ9KXDkbnM0JYeziaXMlibqw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxyBtKiaMJNiayqGqiawAElXPpEAtg5l5YTlqgQ9KXDkbnM0JYeziaXMlibqw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxyBtKiaMJNiayqGqiawAElXPpEAtg5l5YTlqgQ9KXDkbnM0JYeziaXMlibqw/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8FkMOZxo9hJgSwj1AM3p2ZxicicMxq3SLLgs2vib6NukicHCUkmzSxB7THNnSmd8xHFpIozqWfwicvAzgw/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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