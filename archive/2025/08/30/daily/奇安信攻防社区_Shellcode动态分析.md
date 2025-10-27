---
title: Shellcode动态分析
url: https://forum.butian.net/share/4512
source: 奇安信攻防社区
date: 2025-08-30
fetch_date: 2025-10-07T00:12:38.696230
---

# Shellcode动态分析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Shellcode动态分析

* [CTF](https://forum.butian.net/topic/52)

周末参加了ctf 比赛，第一次接触，花了点时间，找朋友辅助了一下，最终获取题目答案

上周末需要支持 ctf 比赛，没打过呀，记录第一次打 ctf 的经历。
下面为题目
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-88bd65613abf752a276f47da4dbec587d43dd256.png)
解压后是一个二进制文件
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-cb7006a1a2ddc9ef464bc84e345b26b774f43837.png)
• ELF：文件格式为\*\*可执行与可链接格式\*\*（Linux 系统下最常见的二进制文件格式）。
• 64-bit：64 位架构，运行在 x86-64（AMD64）处理器上。
• LSB：采用\*\*小端字节序\*\*（低端字节存储在低地址，x86 架构的典型特征）。
• pie executable：\*\*位置无关可执行文件\*\*（Position-Independent Executable），加载时可随机分配内存地址，增强安全性（对抗缓冲区溢出等漏洞利用）。
使用checksec 查看 文件安全保护机制状态
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-7a56474176a095d153e744c2cc4fa3c2d378f5e7.png)
\*\*RELRO（Relocation Read-Only）\*\*：重定位表只读保护
\*\*栈保护（Stack Canary）\*\*：栈溢出检测机制。
\*\*NX（No-eXecute）\*\*：不可执行内存保护。
\*\*PIE（Position-Independent Executable）\*\*：位置无关可执行文件。
好家伙，都开启了。
然后题目需要找到 恶意 IP 和端口，那 strings 试一下 ，万一有呢
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-ba6e0d17305d612ba042d9378a82415cf5a9a8b1.png)
果真不存在，那么基本信息已经知道了，就先打开 IDA 看一下流程图。
直接拖入到 ida 中，会自动识别架构
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-25cf701a2c90fdb6f6f39252dfb488a1fa016681.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-b93d87e3d715d13d1532690caaa937fc5032f566.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-3cfe69280120973c90e976651a1d41b2abfaa53f.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-f7388c62dfc8db6bafc5945c20eec7581009b0cd.png)
本人也看不懂，找了 ai 总结了一下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-2cf84881afd6684086869c38a345ca5895ba2c43.png)
观察导入表比较少，没有发现和网络相关的单词，猜测 ip 地址应该不是明文写入
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-a06a34ecccc7720cf6a3d6bd4f3fcf4839a33930.png)
回到main 函数中，，把鼠标放到loc\\_14E3 ,空格切换视图
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-45fa9db65b3efdb27d1c3e3a4487e58617379a43.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-408c7ff0d126f1e859b1e12c5cce5e84534af723.png)
addr 就是我们需要获取的 ip 地址
简单看下汇编， rax 为寄存器，他的值在上面是 rbp+dest 给他的，然后是通过call \\_memcpy 进来的，所以我们需要动态调试，静态是不能获取到数据。
动态调试不太会，所以请好盆友来辅导一下。
info files 查看文件入口
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-9829971ee5558ad3db6cbff348cc0619e361ed71.png)
b \\*0x1240 打断点
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-429db744f41c04e04d927f54af30951f3139ec5d.png)
run 运行程序
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-487ff8ff503fa77048e41cffdb644379e1f29155.png)
再次输入 info files 查看文件入口
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-f80704c082cd386142020a0a06807ce915f9ebfb.png)
i b 查看断点信息
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-e6ad3da8505a6def7a4ae99314aa29e30a148b9e.png)
这时，我们删除 1 断点，否则程序无法运行
del 1
run 运行程序
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-89669001d5ae7affce7b1839ae6e26abf634f373.png)
ni 步过 一直步过，直到看到我们的main 函数地址。
输入 ni 后，绿色的小箭头会往下走
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-07e5b2226d3712637cb5e9c74ac500cc09478452.png)
输入第一次 ni 后，后面直接敲回车，一样的意思
一直到这里，就看到程序入口函数了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-6a00f08411cf66db4a16aa5de3697dedda004822.png)
这是输入 si 步入 main 函数中
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-2d478c20ffb7a063f4c6bd1af27c714a649cabfd.png)
上面的框框就是 main 函数的实际内存地址
我们在地址上打断点
b \\*0x55555555540a
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-a571f81e042e6e017d8030cdcb2e1f6029581c42.png)
然后执行 c，可直接进入主函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-e6b2d39f27f65511850947cb04f393e2682ec8b9.png)
n 重复执行一直到能看到 call rax,这里 call rax 就是我们在 ida 分析的汇编，他的值就是从这能寻找到
大概输入了 20 多次回车，就看到了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-5d7577d2ccbbffbabc71c11885693116c167a533.png)
然后我们输入si 进入内存中
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-803540327467bbb6b31e636b62ca64895227b2c7.png)
其实这一步就已经看到数据了，接着回车，直到 syscall 哪一行
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-67a4814769e8921deb9c875cd8da197294795484.png)
然后用syscall去调用connect()，建立连接，就可以看到ip地址，为16进制
转一下数据，就可以看到题目中的答案。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-7008f0e0e10eea1239c9bca339675e12895baff0.png)

* 发表于 2025-08-29 10:00:00
* 阅读 ( 1678 )
* 分类：[应急响应](https://forum.butian.net/community/response)

0 推荐
 收藏

## 1 条评论

[![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b9e534117404dd9e2a3e4641ef974170eed91cf.jpg)](https://forum.butian.net/people/19026)

**[c铃儿响叮当](https://forum.butian.net/people/19026)**
2025-08-29 12:16

大佬写的太好了

* [0 条评论](#comment-2739)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

请先 [登录](https://forum.butian.net/login) 后评论

[![轩公子](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/4118)

[轩公子](https://forum.butian.net/people/4118)

3 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![轩公子](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---