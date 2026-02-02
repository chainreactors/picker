---
title: 如何给 Linux 内核提交补丁：一次真实的踩坑记录
url: https://bestwing.me/How-to-patch-a-linux-kernel-bug-zh.html
source: Swing'Blog 浮生若梦
date: 2026-02-01
fetch_date: 2026-02-02T04:15:41.686612
---

# 如何给 Linux 内核提交补丁：一次真实的踩坑记录

[![Swing'Blog 浮生若梦](/images/logo.png)](/)
[Swing'Blog 浮生若梦](/)

* [Home](/)
* |
* [About](/about/)
* |
* [Articles](/archives/)
* |
* [RSS](/atom.xml)
* |
* [Categories](/categories/)
* |
* [Links](/link)

# 如何给 Linux 内核提交补丁：一次真实的踩坑记录

2026-02-01

[内核开发](/categories/%E5%86%85%E6%A0%B8%E5%BC%80%E5%8F%91/),
[安全研究](/categories/%E5%86%85%E6%A0%B8%E5%BC%80%E5%8F%91/%E5%AE%89%E5%85%A8%E7%A0%94%E7%A9%B6/)

### Table of Contents

1. [背景](#%E8%83%8C%E6%99%AF)
   1. [分析一下崩溃](#%E5%88%86%E6%9E%90%E4%B8%80%E4%B8%8B%E5%B4%A9%E6%BA%83)
2. [第一步：环境准备](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87)
   1. [克隆正确的仓库](#%E5%85%8B%E9%9A%86%E6%AD%A3%E7%A1%AE%E7%9A%84%E4%BB%93%E5%BA%93)
   2. [配置 Git 邮件](#%E9%85%8D%E7%BD%AE-Git-%E9%82%AE%E4%BB%B6)
   3. [为什么用 Mutt？](#%E4%B8%BA%E4%BB%80%E4%B9%88%E7%94%A8-Mutt%EF%BC%9F)
3. [第二步：写修复代码](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%86%99%E4%BF%AE%E5%A4%8D%E4%BB%A3%E7%A0%81)
4. [第三步：测试](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%B5%8B%E8%AF%95)
5. [第四步：自测清单](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E8%87%AA%E6%B5%8B%E6%B8%85%E5%8D%95)
   1. [代码风格](#%E4%BB%A3%E7%A0%81%E9%A3%8E%E6%A0%BC)
   2. [多配置编译](#%E5%A4%9A%E9%85%8D%E7%BD%AE%E7%BC%96%E8%AF%91)
   3. [启动测试](#%E5%90%AF%E5%8A%A8%E6%B5%8B%E8%AF%95)
   4. [验证修复](#%E9%AA%8C%E8%AF%81%E4%BF%AE%E5%A4%8D)
   5. [跑 selftests](#%E8%B7%91-selftests)
   6. [拼写检查](#%E6%8B%BC%E5%86%99%E6%A3%80%E6%9F%A5)
6. [第五步：写提交信息](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E5%86%99%E6%8F%90%E4%BA%A4%E4%BF%A1%E6%81%AF)
   1. [几个要点](#%E5%87%A0%E4%B8%AA%E8%A6%81%E7%82%B9)
   2. [调用栈怎么写](#%E8%B0%83%E7%94%A8%E6%A0%88%E6%80%8E%E4%B9%88%E5%86%99)
7. [第六步：生成和发送补丁](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E7%94%9F%E6%88%90%E5%92%8C%E5%8F%91%E9%80%81%E8%A1%A5%E4%B8%81)
   1. [一个坑：&#115;&#101;&#x63;&#117;&#114;&#x69;&#116;&#121;&#64;&#x6b;&#x65;&#114;&#110;&#101;&#108;&#x2e;&#x6f;&#114;&#103;](#%E4%B8%80%E4%B8%AA%E5%9D%91%EF%BC%9A-115-101-x63-117-114-x69-116-121-64-x6b-x65-114-110-101-108-x2e-x6f-114-103)
8. [第七步：处理反馈](#%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E5%A4%84%E7%90%86%E5%8F%8D%E9%A6%88)
9. [第八步：申请 CVE](#%E7%AC%AC%E5%85%AB%E6%AD%A5%EF%BC%9A%E7%94%B3%E8%AF%B7-CVE)
10. [和维护者的邮件沟通](#%E5%92%8C%E7%BB%B4%E6%8A%A4%E8%80%85%E7%9A%84%E9%82%AE%E4%BB%B6%E6%B2%9F%E9%80%9A)
11. [我踩过的坑](#%E6%88%91%E8%B8%A9%E8%BF%87%E7%9A%84%E5%9D%91)
12. [时间线](#%E6%97%B6%E9%97%B4%E7%BA%BF)
13. [小结](#%E5%B0%8F%E7%BB%93)
14. [参考资料](#%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99)

最近给 Linux 内核提交了一个补丁，修复 `skbuff_fclone_cache` 的 usercopy 问题，过程中踩了不少坑。这篇文章记录一下整个流程，希望能帮到想给内核提补丁的朋友。

## 背景

事情是这样的，n132和我发现了一个内核 panic，在启用 `CONFIG_HARDENED_USERCOPY` 的时候会触发。

问题出在 `skbuff_fclone_cache` 这个 slab 缓存创建的时候没有定义 usercopy 区域，但是 `skbuff_head_cache` 是有的。这就导致内核在尝试把 `sk_buff.cb` 的数据拷贝到用户空间的时候会 BUG()。

崩溃的调用链大概是这样：

1. TCP 用 `alloc_skb_fclone()` 分配 skb
2. `skb_clone()` 克隆这个 skb
3. 克隆的 skb 被放到 `sk_error_queue`
4. 用户空间调用 `recvmsg(MSG_ERRQUEUE)` 读错误队列
5. `sock_recv_errqueue()` 调用 `put_cmsg()` 拷贝数据
6. 然后就炸了，`__check_heap_object()` 检查失败

崩溃日志长这样：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``` | ``` [    5.379589] usercopy: Kernel memory exposure attempt detected from SLUB object 'skbuff_fclone_cache' (offset 296, size 16)! [    5.382796] kernel BUG at mm/usercopy.c:102! [    5.383923] Oops: invalid opcode: 0000 [#1] SMP KASAN NOPTI [    5.384903] CPU: 1 UID: 0 PID: 138 Comm: poc_put_cmsg Not tainted 6.12.57 #7 [    5.384903] Hardware name: QEMU Standard PC (i440FX + PIIX, 1996), BIOS rel-1.16.3-0-ga6ed6b701f0a-prebuilt.qemu.org 04/01/2014 [    5.384903] RIP: 0010:usercopy_abort+0x6c/0x80 [    5.384903] Code: 1a 86 51 48 c7 c2 40 15 1a 86 41 52 48 c7 c7 c0 15 1a 86 48 0f 45 d6 48 c7 c6 80 15 1a 86 48 89 c1 49 0f 45 f3 e8 84 27 88 ff <0f> 0b 490 [    5.384903] RSP: 0018:ffffc900006f77a8 EFLAGS: 00010246 [    5.384903] RAX: 000000000000006f RBX: ffff88800f0ad2a8 RCX: 1ffffffff0f72e74 [    5.384903] RDX: 0000000000000000 RSI: 0000000000000004 RDI: ffffffff87b973a0 [    5.384903] RBP: 0000000000000010 R08: 0000000000000000 R09: fffffbfff0f72e74 [    5.384903] R10: 0000000000000003 R11: 79706f6372657375 R12: 0000000000000001 [    5.384903] R13: ffff88800f0ad2b8 R14: ffffea00003c2b40 R15: ffffea00003c2b00 [    5.384903] FS:  0000000011bc4380(0000) GS:ffff8880bf100000(0000) knlGS:0000000000000000 [    5.384903] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033 [    5.384903] CR2: 000056aa3b8e5fe4 CR3: 000000000ea26004 CR4: 0000000000770ef0 [    5.384903] PKRU: 55555554 [    5.384903] Call Trace: [    5.384903]  <TASK> [    5.384903]  __check_heap_object+0x9a/0xd0 [    5.384903]  __check_object_size+0x46c/0x690 [    5.384903]  put_cmsg+0x129/0x5e0 [    5.384903]  sock_recv_errqueue+0x22f/0x380 [    5.384903]  tls_sw_recvmsg+0x7ed/0x1960 [    5.384903]  ? srso_alias_return_thunk+0x5/0xfbef5 [    5.384903]  ? schedule+0x6d/0x270 [    5.384903]  ? srso_alias_return_thunk+0x5/0xfbef5 [    5.384903]  ? mutex_unlock+0x81/0xd0 [    5.384903]  ? __pfx_mutex_unlock+0x10/0x10 [    5.384903]  ? __pfx_tls_sw_recvmsg+0x10/0x10 [    5.384903]  ? _raw_spin_lock_irqsave+0x8f/0xf0 [    5.384903]  ? _raw_read_unlock_irqrestore+0x20/0x40 [    5.384903]  ? srso_alias_return_thunk+0x5/0xfbef5 ``` |

这个 bug 后来被分配了 [CVE-2026-22977](https://vulert.com/vuln-db/net--sock--fix-hardened-usercopy-panic-in-sock-recv-errqueue)。

### 分析一下崩溃

崩溃信息里说 `offset 296, size 16`，我们来算一下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` sizeof(struct sk_buff) = 232 offsetof(struct sk_buff, cb) = 40  sk_buff_fclones 里面： - skb1 从 0 开始 - skb2 从 232 开始  所以 skb2.cb 的偏移 = 232 + 40 = 272 崩溃偏移 296 = 272 + 24，刚好在 sock_exterr_skb.ee 里面 ``` |

这就确认了问题确实出在克隆 skb 的 `cb` 字段。

## 第一步：环境准备

### 克隆正确的仓库

这里点，我们**不要直接克隆 Linus 的主仓库**！要根据你的补丁类型选择对应的子系统仓库：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` # 网络相关的 bug 修复，用这个： git clone https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git cd net  # 网络相关的新功能，用这个： git clone https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net-next.git  # 其他通用的： git clone https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git ``` |

| 仓库 | 用途 |
| --- | --- |
| `net.git` | 当前版本的 bug 修复 |
| `net-next.git` | 下一版本的新功能 |
| `linux.git` | 通用开发 |

我这个是 net模块里的代码，所以应该用 `net.git`。

### 配置 Git 邮件

编辑 `~/.gitconfig`：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` [user]     name = Weiming Shi     email = bestswngs@gmail.com  [sendemail]     smtpserver = smtp.gmail.com     smtpserverport = 587     smtpencryption = tls     smtpuser = bestswngs@gmail.com ``` |

用 Gmail 的话需要去 Google 账户安全设置里生成一个应用专用密码。

### 为什么用 Mutt？

这里要特别说一下，**千万不要用 Gmail 网页版发补丁**！

Gmail 网页版会：

* 把纯文本转成 HTML
* 自动换行，直接把补丁搞坏
* 把 Tab 换成空格
* 各种编码问题

内核要求纯文本邮件，补丁要内联在邮件里（不是附件）。推荐的组合是：

* **`git send-email`** 发补丁
* **`mutt`** 看维护者回复

Mutt 配置 `~/.muttrc`：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` set realname = "Weiming Shi" set from = "bestswngs@gmail.com" set use_from = yes set envelope_from = yes  set my_user = "bestswngs@gmail.com" set my_pass = "xxxx xxxx xxxx xxxx"  # 应用专用密码  set imap_user = $my_user set imap_pass = $my_pass set folder = "imaps://imap.gmail.com:993" set spoolfile = "+INBOX"  set smtp_url = "smtps://$my_user:$my_pass@smtp.gmail.com:465/" set ssl_force_tls = yes  set postponed = "+[Gmail]/Drafts" set record = "+[Gmail]/Sent Mail"  set header_cache = ~/.mutt/cache/headers set message_cachedir = ~/.mutt/cache/bodies set certificate_file = ~/.mutt/certificates ``` |

## 第二步：写修复代码

创建工作分支：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` git checkout -b fix-skbuff-fclone-usercopy ``` |

修复其实很简单，把 `kmem_cache_create()` 换成 `kmem_cache_create_usercopy()`：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` -	net_hotdata.skbuff_fclone_cache = kmem_cache_create("skbuff_fclone_cache", +	net_hotdata.skbuff_fclone_cache = kmem_cache_create_usercopy("skbuff_fclone_cache",  						sizeof(struct sk_buff_fclones),  						0,  						SLAB_HWCACHE_ALIGN|SLAB_PANIC, +						offsetof(struct sk_...