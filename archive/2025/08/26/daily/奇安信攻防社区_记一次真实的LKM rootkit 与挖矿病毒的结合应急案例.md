---
title: 记一次真实的LKM rootkit 与挖矿病毒的结合应急案例
url: https://forum.butian.net/share/4491
source: 奇安信攻防社区
date: 2025-08-26
fetch_date: 2025-10-07T00:12:44.632621
---

# 记一次真实的LKM rootkit 与挖矿病毒的结合应急案例

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

### 记一次真实的LKM rootkit 与挖矿病毒的结合应急案例

* [安全管理](https://forum.butian.net/topic/54)

本次文章主要展示挖矿病毒与LKM rootkit的排查发现

故事背景来源于群友的一次应急响应，客户数十台服务器均中招挖矿木马，服务器占用异常但是排查的时候却没有办法直接查到是什么原因，最后发现是rootkit，当然了有人可能会说这不算，仁者见仁吧
简单复盘：
-----
首先当然是上图，在服务器执行top指令，未发现系统资源占用异常
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753429690782-73e9a274-f708-4fa8-9c05-b0100409127e.png)
细心的基友应该已经看见cup最上面是99了，但是看不见是哪个进程，在执行下述指令之后，重新执行top指令，就又看到了占用异常的进程
```php
kill -63 0
lsmod
rmmod x11
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753430066212-a1310c55-3abb-4554-b96a-871fb01e5e56.png)
此时可以看到，python3进程存在异常，此进程很明显是被挂东西了，放到vt里一查，挖矿的无疑了
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753430442563-b19abaef-2d49-4cf3-b861-db90a4874635.png)
好胸弟对此有个疑问，就是为什么是kill -63 0，这个东西是从什么地方来的？于是好胸弟把样本拷贝后进行分析
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753430904530-8408ce96-cd24-4969-9d7e-01cf8ff879c2.png)
主要关注x11.ko这个文件
从第一张图就发现了，挖矿的大哥直接用的github上开源的东西
<https://github.com/m0nad/Diamorphine>
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753430577804-ddd78284-eaaf-4855-9753-7d624902136b.png)
从第二张图就看到了实现功能，可以看到，多个分支语句用来实现不同功能，kill -63 实现自身隐藏与显现；kill -31 pid 用来隐藏或显示用户启动的进程；kill -64 是用来提权的
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753430817562-ad47257b-84ae-49a6-a7c6-32a99d157490.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753430678958-aa2cbe6a-35f0-46ed-b083-736a5c04a022.png)
本地试验了一下，根据github的说明，Linux Kernels 2.6.x/3.x/4.x/5.x/6.x (x86/x86\\_64 and ARM64) 版本均可以使用，根据实验发现，该rootkit小工具需要根据目标设备内核去生成(实验部分使用的是github上面的)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753435716999-bbcdaca7-c53c-4bf6-bb5f-637d1bf24c20.png)
可以看见，安装成功后，rootkit是自动隐藏的，接下来尝试一下隐藏用户进程
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753435832711-8452789e-5578-450b-b328-6889732acccf.png)
执行kill -31 1919后，再次执行ps -aux，已经看不到进程了
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753435857771-504af197-1943-44d3-a1aa-d158712b5e3d.png)
再次执行kill -31 1919后，又看到了进程
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753435889237-c3c4f76f-ea65-411d-8400-0e98987ab42c.png)
而后执行kill -63 0发现，恶意的文件可以看见了
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753435940700-7b11091f-14a1-4339-b775-fe07c5851b86.png)
由于恶意进程python3本身是没有隐藏能力的，是基于rootkit工具实现隐藏，所以一般直接将他去除掉，隐藏也就直接失效了，这样即使不知道被隐藏的进程pid是什么，也能去掉隐藏效果
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753436155101-d220839e-98d0-494e-aa43-239d3c495933.png)
并且在本地还发现了攻击者用来日志清除的工具
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753432407404-5eb3cd9e-f7cc-4dbc-a3a1-a1c287370f26.png)
功能非常多
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753432424590-dd981e4f-64a1-4564-91ce-7df91ab8dcdd.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1753432451559-07065523-e017-456b-92cc-43c4a9a38fb4.png)
github项目如下，大家感兴趣自己看看就行
[https://github.com/infinite-horizon219/mig-logcleaner-resurrecte](https://github.com/infinite-horizon219/mig-logcleaner-resurrected)
\*\*后续python3挖矿木马分析：\*\*
--------------------
为了保证客户环境的稳定性，在将python3 挖矿样本迁移后，在本地进行测试，尝试执行后结果如下：
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755213115063-1eadd35c-c1a6-4ee9-80a3-101b58a6321a.png)
翻译过来就是：
2025年8月14日 07:31:10:配置文件中不包含任何钱包或它们无效!
2025年8月14日07:31:10:以太坊挖矿的最小配置文件是“wallet=&lt;你的以太坊钱包&gt;
2025年8月14日 07:31:10:以太坊挖矿的最小命令行选项是“-wallet&lt;你的以太坊钱包&gt;”
2025年8月14日 07:31:10:请参阅ReadMe文档以获取详细信息。
而后在客户服务器发现config.ini文件
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755213031591-7bec3abf-ff9c-44a6-9c37-f746567e3779.png)
### 配置文件解析
- `\*\*wallet\*\*`
- \*\*作用\*\*：矿工的钱包地址
- \*\*值\*\*：`ZEPHYR2smB5JfBY2WKW8GF3eMvCHE5QeLQBKj77jmJtPhSfJWg9L4PPAiv7kpqQXu29NXKD7iK76CZBXDtpf95rWcAxeE1L81GG44`
- \*\*说明\*\*：该地址疑似属于 \*\*Zephyr/XMR 区块链\*\*
- `\*\*rigName\*\*`
- \*\*作用\*\*：矿机的标识名称，用于在矿池中区分不同设备
- \*\*值\*\*：`node17`
- \*\*说明\*\*：矿池后台可据此监控每台设备的算力、在线状态等
- `\*\*email\*\*`
- \*\*作用\*\*：可选字段，通常用于接收矿池通知
- \*\*示例值\*\*：空值
- `\*\*pool1\*\*`
- \*\*作用\*\*：主矿池地址及端口
- \*\*功能开关参数\*\*
| | | |
|---|---|---|
| 参数 | 值 | 作用 |
| `noLog` | `true` | 禁用日志输出（减少磁盘占用，但不利排查问题）。 |
| `autoUpdate` | `false` | 禁用软件自动更新（保持版本稳定）。 |
| `sortPools` | `false` | 不自动切换矿池（仅使用 `pool1`）。 |
| `useSSL` | `true` | 启用 SSL/TLS 加密通信（防止算力提交被窃听） |
| `protocol` | `JSON-RPC` | 使用 \*\*JSON-RPC 协议\*\*（主流挖矿通信协议，如以太坊、Zephyr） |
### 配置文件用途总结
- \*\*所属软件\*\*：基于 \*\*RandomX 算法\*\*的挖矿软件（如 XMRig、Zephyr 官方矿工），用于挖掘 Monero（XMR）或 Zephyr（ZEPH）等虚拟币
- \*\*核心目标\*\*：
1. 将矿机算力定向提交至指定矿池（`pool1`）。
2. 挖矿收益自动发放至配置的钱包地址（`wallet`）。
3. 通过加密通信（`useSSL=true`）保障数据传输安全。
而后在用户机器上收集到下述文件
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755213598017-91350d67-a223-4c30-94c5-1b71b4160fba.png)
### 样本局部特征
继续分析python3样本，发现矿池地址 xmr-eu1.nanopool.orgxmr-eu2.nanopool.orgxmr-jp1.nanopool.org
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755215500610-26119124-ed02-4712-bdb7-3cbcd27fcc5d.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755213715740-33299fe4-50ae-484a-b73d-b9a1c9bd77db.png)
该地址具备以太坊门罗币标准特征xmr-euxxx，也从侧面应征，该样本目标为以太坊门罗币
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755213892998-93a3443c-924e-4638-9e6d-88b60793235b.png)
继续分析python3样本，发现该样本存在MinerClient ，并且实际上该工具采用Golang编写
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755214115143-a3ede797-6019-4b31-9f44-f1ebc2578471.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755569305829-52202e34-a33f-4192-ab51-441350770c6b.png)
而后在后续发现程序利用golang语言的高并发优势，初始化挖矿配置 → 绑定矿工参数 → 通过Goroutine启动挖矿任务，实现了挖矿的全部流程
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755214228137-235c11ca-6c13-414e-8563-31de70c07f48.png)
而后发现了疑似解析动态矿池地址的域名解析函数
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755215675857-7db5935e-8c46-4bd4-840b-51b831010a2a.png)
使用`github.com/miekg/dns.IsFqdn`检查域名是否为完全限定域名
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755215713596-f39d2f39-dd82-4e00-bc3b-0861b009daaf.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755215769593-970326aa-23b8-40f1-ba92-f67fbf746dd1.png)
下述模块为矿池连接器（Pool Connector）模块中的连接建立函数，该模块主要作用疑似为： 调用 `net\_ParseIP`直接解析输入地址 、 通过 `main\_poolconnector\_ResolveIP`解析域名 、 循环遍历所有解析到的IP地址 、 对每个地址调用 `main\_poolconnector\_doConnect`尝试连接
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755216118571-533f4a1c-93d8-44d3-b3aa-fa923e2ac949.png)
而后在测试python3样本的时候，也能证明此处的应用
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1755216203879-ca28cb81-8fd5-4f93-94e9-f0601e873274.png)
暂时就到这吧，样本134mb，分析起来实在是成本高

* 发表于 2025-08-25 10:07:46
* 阅读 ( 2249 )
* 分类：[应急响应](https://forum.butian.net/community/response)

3 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![vlan911](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/43077)

[vlan911](https://forum.butian.net/people/43077)

5 篇文章

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

#### ![vlan911](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/qrcode-36d63cc744264cc47f3999f6c981ac7ba2f986bf.jpg)

---