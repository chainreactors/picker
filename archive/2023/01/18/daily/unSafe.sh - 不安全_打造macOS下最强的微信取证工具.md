---
title: 打造macOS下最强的微信取证工具
url: https://buaq.net/go-145953.html
source: unSafe.sh - 不安全
date: 2023-01-18
fetch_date: 2025-10-04T04:07:28.853074
---

# 打造macOS下最强的微信取证工具

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/6ecb6f9dc73b33b398c6f25703426615.jpg)

打造macOS下最强的微信取证工具

现有方案WeChat-Data-Analysis[1]LLDB实践1. 打开电脑端微信（不要登陆）2. 在Terminal输入命令lldb -p $(pgrep WeChat)3. br set -n
*2023-1-17 21:6:38
Author: [mp.weixin.qq.com(查看原文)](/jump-145953.htm)
阅读量:739
收藏*

---

## 现有方案

WeChat-Data-Analysis[1]

### LLDB实践

1. 1. 打开电脑端微信（不要登陆）
2. 2. 在Terminal输入命令`lldb -p $(pgrep WeChat)`
3. 3. `br set -n sqlite3_key` 设置断点
4. 4. 输入`c`，回车（继续运行
5. 5. 登陆电脑端微信
6. 6. 输入`memory read --size 1 --format x --count 32 $rsi`，回车

1. 1. arm 上替换为 `memory read --size 1 --format x --count 32 $x1`

   ![](https://mmbiz.qpic.cn/mmbiz_png/mmbXTwYCQ9nAgAZKvgpgw9ymaRxukGQiaUBL5K3SKiarB6ZyaRRqyJDvhicVE4ZpYiaXxEtzDBoDPIgNxyFMENI6Pw/640?wx_fmt=png)

7. 7. 将返回的原始key粘贴到下面的字符串中，用如下代码解析获取密钥：

```
ori_key = """

key = '0x' + ''.join(i.partition(':')[2].replace('0x', '').replace(' ', '') for i in ori_key.split('\n')[1:5])
print(key)
```

本地聊天数据库存储路径：`~/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/[version]/[uuid]/Message/*.db`

App: DB Browser for SQLite

选择如下配置，复制密钥，即可打开浏览：

![](https://mmbiz.qpic.cn/mmbiz_png/mmbXTwYCQ9nAgAZKvgpgw9ymaRxukGQianruLlkOgpphLBYvvmcf0uJDteKUibQyVFdtemlmQVu0dTFHtGa5GUhg/640?wx_fmt=png)

### 原理探究

Tencent的开源项目WCDB[2]是一个高效、完整、易用的移动数据库框架，基于SQLCipher[3]，支持iOS, macOS和Android。

SQLCipher[4] 中使用 sqlite3\_key[5] 函数打开加密的数据库，wcdb 将其封装在setCipherKey[6]方法下：

```
int sqlite3_key(sqlite3 *db, const void *pKey, int nKey)
```

使用 `br set -n sqlite3_key` 设置其断点。再使用`memory read --size 1 --format x --count 32 $rsi` 获取 pKey 传参的值：

```
x86-64 ; 中函数调用时的参数存储如下寄存器中:
%rdi
%rsi
%rdx
%rcx
%r8
%r9
; 六个寄存器用于存储函数调用时的6个参数（如果有6个或6个以上参数）。
%rsi ; 寄存器存储的为第二个参数，即对应 sqlite3_key 函数的 *pKey 传参。
```

---

文章来源: http://mp.weixin.qq.com/s?\_\_biz=MzU0NzczMDg4Mg==&mid=2247483863&idx=1&sn=ae6d1069a517e0176822efad9835dbd3&chksm=fb48a57acc3f2c6c412cf96a1dececc42ec8853931386f0988b404c9df92b0d2f3d9ee8f5491&mpshare=1&scene=1&srcid=0117IZabUGDa7urjFqXCjR0V&sharer\_sharetime=1673960793589&sharer\_shareid=205c037363a9188e37dfb6bb4436f95b#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)