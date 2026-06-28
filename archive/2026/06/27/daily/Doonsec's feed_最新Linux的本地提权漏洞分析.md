---
title: 最新Linux的本地提权漏洞分析
url: https://mp.weixin.qq.com/s/Q-Vxgm4rlcbUMSQcuMV9lw
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:10:57.862965
---

# 最新Linux的本地提权漏洞分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Sq4BUsrXeTicvar7HXvHicePpYZ4HgnQBUG1yFofDc763OQo0mXKqGmLD4mocxj2KbVK8usEkelGbvPm1WrTmBHBRmYiaBYxKce8XCsZdVrLP8/0?wx_fmt=jpeg)

# 最新Linux的本地提权漏洞分析

原创

非虫
非虫

软件安全与逆向分析

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年6月25日，JFrog Security Research公开了DirtyClone（CVE-2026-43503）。它不是一个全新的内核原语，而是DirtyFrag修复链上的回归绕过：`__pskb_copy_fclone()`在克隆`skb`时丢掉了`SKBFL_SHARED_FRAG`，于是`esp_input()`把一张仍然挂着文件页缓存的页误判成普通网络缓冲区，最后在原地解密时把数据写回了页缓存。

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT9BsAlcic3F292p9sQQshL0daUMliaRh4eIaj8lEyFMdga1WicrxNicrdMg3IOhbNhP77BO9xSRpkbouLRo05ok9AXSLMq8uJRtDnE/640?wx_fmt=png&from=appmsg)

从NVD的变更记录看，这也不是单点失误，而是一组frag-transfer helper在转移frag描述符时都可能把共享标记弄丢；DirtyClone公开利用的是其中最直接的`__pskb_copy_fclone()`克隆路径。

```
文件页缓存
  -> TEE/dup to local克隆
  -> `__pskb_copy_fclone()`
  -> `SKBFL_SHARED_FRAG`丢失
  -> `esp_input()`
  -> 原地decrypt
  -> 页缓存被改写
```

## 1 漏洞成因

DirtyFrag原本已经补过一次：只要`skb`带着外部共享页，`esp_input()`就应该先走`skb_cow_data()`，再做解密。DirtyClone的问题在于，`__pskb_copy_fclone()`先复制frag描述符，再把剩余的`shinfo`交给`skb_copy_header()`，但后者只处理gso相关字段，不会把`skb_shinfo()->flags`里的`SKBFL_SHARED_FRAG`带过去。结果是，页还在，标记没了，`skb_has_shared_frag()`就会返回false。

再往下看，问题就变成了典型的“看起来不共享，实际上还共享”。`esp_input()`依据错误的标记跳过COW，后续的IPsec原地解密直接落在页缓存页上。磁盘文件本身没有被改，改动只停在内存里的page cache里，所以文件完整性监控和重启后的磁盘校验都看不见这个状态。

## 2 利用链

DirtyClone的PoC没有重新发明写原语，而是把DirtyFrag里已经验证过的`seq_hi`控字节技巧接了回来。大致流程是：

```
只读打开`/usr/bin/su`
  -> 把目标页塞进ESP包
  -> 用`TEE`或等价的`nft dup to local`在内核里复制该包
  -> 复制后的`skb`丢标记
  -> `esp_input()`原地写回
  -> 反复48次，覆盖`su`前192字节
  -> 执行被污染的`su`得到root
```

这里真正可控的是每个4字节word。PoC通过XFRM状态里的`seq_hi`携带目标word，再配合AES-CBC的IV和封装方式，让解密结果写成想要的字节。目标文件通常选`/usr/bin/su`，因为只要把它的前192字节换成一个极小的`setuid(0)+execve("/bin/sh")`ELF，下一次执行时就能拿到root。

PoC里用的是`TEE`，本质上只要能走到`nf_dup_ipv4()`并触发`__pskb_copy_fclone()`，思路就成立。

## 3 Ubuntu24.04上的现实约束

Ubuntu24.04和更高版本默认启用了AppArmor对非特权user namespace的限制。也就是说，标准的`unshare(CLONE_NEWUSER|CLONE_NEWNET)`起手式不再像Debian、Fedora那样顺手，PoC想拿到`CAP_NET_ADMIN`会被默认策略卡住。JFrog公开的代码也明确提到，在Ubuntu上需要放开`kernel.apparmor_restrict_unprivileged_userns`，或者让目标进程落在允许`userns`的AppArmor配置里。

所以，Ubuntu24.04不是“没有这个洞”，而是默认把最常见的利用起点收紧了。对普通本地用户来说，它更像是把标准打法从“开箱即用”变成了“还得先过一层系统策略”。

## 4 补丁与缓解

主线修复在2026年5月21日合入，首个修复标签是`v7.1-rc5`。真正稳妥的处理只有升级内核，并确认发行版回补链路完整。临时缓解只能缩小面：保留Ubuntu的userns限制，尽量别让普通用户获得`CAP_NET_ADMIN`，同时避免`xt_TEE`、`esp4`、`esp6`这类触发面自动加载。

## 参考资料

* JFrog Security Research：https://research.jfrog.com/post/dissecting-and-exploiting-linux-lpe-variant-dirtyclone-cve-2026-43503/
* DirtyClone PoC仓库：https://github.com/rafaeldtinoco/security/tree/main/exploits/dirtyclone
* TheHackerNews报道：https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html
* Ubuntu24.04发行说明：https://documentation.ubuntu.com/release-notes/24.04/
* Ubuntu AppArmor user namespace说明：https://discourse.ubuntu.com/t/understanding-apparmor-user-namespace-restriction/58007
* NVD变更记录：https://nvd.nist.gov/vuln/detail/CVE-2026-43503/change-record?changeRecordedOn=05%2F23%2F2026T10%3A16%3A43.350-0400

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

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