---
title: 老牌 Shiro550 漏洞为何常年高危？ShiroAttack2 新版工具一键爆破密钥、注入内存马，CLI 批量脚本化渗透
url: https://mp.weixin.qq.com/s/UcysNxT_5d0S-npTJa24aA
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:11:13.084609
---

# 老牌 Shiro550 漏洞为何常年高危？ShiroAttack2 新版工具一键爆破密钥、注入内存马，CLI 批量脚本化渗透

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibrevicNauKAWiax5w9HGAXPibI6swcyeotKsMqLciaC7ARRAqUjWa8xTLa0Rtnr6fmZxbPmY2pfo1Pz8YrmMHic5Bf5h1bmibAVrcELicxGsekXyno/0?wx_fmt=jpeg)

# 老牌 Shiro550 漏洞为何常年高危？ShiroAttack2 新版工具一键爆破密钥、注入内存马，CLI 批量脚本化渗透

Dest1ny
Dest1ny

渗透安全HackTwo

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

0x01 工具介绍

**诞生多年的 Shiro550 反序列化漏洞至今依旧高频出现，根源在于项目沿用默认 AES 密钥、配置难以统一修改，且漏洞利用门槛极低。ShiroAttack2 最新版支持 GUI 可视化操作与 CLI 命令行双模式，可自动探测目标框架、批量爆破密钥，适配 CBC 与 GCM 两种加密方式。工具支持直接执行系统命令、注入多类型内存马持久化权限，还能篡改服务端密钥，结构化输出结果便于脚本批量扫描，仅可用于授权范围内的安全测试。**

注意：现在只对常读和星标的公众号才展示大图推送，建议大家把**渗透安全HackTwo**"**设为****星标****⭐️******"**否****则可能就看不到了啦！**

**下载地址在末尾 #渗透安全HackTwo**

0x02 功能介绍

✨核心特点

2016 年的洞，到现在还能用。不是漏洞本身多高级，而是三个很现实的原因叠在一起。

**第一，默认 Key。** Shiro 1.2.4 及之前版本在 `CookieRememberMeManager` 里硬写了一个 AES Key：`kPH+bIxk5D2deZiIxcaaaA==`。十几年来的教程和脚手架代码一直在拷贝这个值。

**第二，Key 换不掉。** rememberMe 要求客户端和服务端用同一个 Key。一旦 Key 写进了配置文件、Docker 镜像、源码仓库，要替换就得所有节点一起改。

**第三，利用成本足够低。** GUI 点几下就能拿 shell，CLI 可以直接嵌进脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXbZeevnfpzcqfnMIGsPComB31NXcm6aEWcFl4VZhqdXm8JvVH0XJfW2e7ztx9vuuWANJXaBtgICQt09x5ia6UZESVicO02iasHcQ/640?wx_fmt=png&from=appmsg)

ShiroAttack2攻击流程

1. 目标探测：向目标发送携带 rememberMe=yes 的请求，通过响应头判断框架类型。Shiro 1.x 版本在接收非法 Cookie 后，会返回 Set-Cookie: rememberMe=deleteMe，以此可精准识别 Shiro 服务端，完成目标确认。

2. 密钥爆破验证：利用 SimplePrincipalCollection 进行序列化处理，搭配字典内的候选 AES 密钥逐一加密测试。若请求响应不再返回 deleteMe 字段，即可判定当前密钥有效，成功获取目标核心密钥。

3. 构造攻击载荷：基于已验证的有效密钥，整合 Gadget 利用链与 TemplatesImpl 回显类，加密生成完整可用的恶意 Payload，为后续攻击执行提供支撑。

4. 远程命令执行：将构造好的恶意 Payload 带入 rememberMe Cookie 中，同时在 Authorization 请求头中携带系统执行命令，发送请求即可触发漏洞，实现远程命令执行。

5. 内存马注入驻留：复用同款 Gadget 利用链，向目标服务注入 Filter、Servlet 等多种类型内存马。攻击脱离 rememberMe 漏洞依赖，实现无文件持久化驻留。

6. 服务密钥篡改：依托内存马的执行权限，动态修改服务端 Shiro 的 AES 加密密钥。篡改后原有旧密钥彻底失效，可彻底断绝原有漏洞利用路径，同时巩固攻击权限。

## CLI 模式 5.0 之后增加了 CLI 模式。核心攻击逻辑 AttackService（1000+ 行）一行没改——通过继承 TextArea 拦截日志输出，利用 ControllersFactory 注册表注入假的 MainController，GUI 和 CLI 共用同一套攻击代码。CLI 不需要 JavaFX 窗口，启动时用一个 JFXPanel 初始化 JavaFX 线程即可。 ``` # 启动 CLIjava -cp shiro_attack-<version>.jar com.summersec.attack.CLI.MainCLI <command> [options] ``` | 命令 | 用途 | | --- | --- | | `detect` | 探测目标是否为 Shiro 框架 | | `crack` | 爆破或验证 Shiro AES Key | | `exec` | 执行系统命令（自动探测 Gadget 链） | | `memshell` | 注入内存马（哥斯拉/冰蝎/蚁剑等） | | `changekey` | 替换目标 Shiro Key | | `gui` | 启动 JavaFX 图形界面 |

## 特点

* JavaFX GUI + CLI 双模式，同一套攻击逻辑
* 多版本 CommonsBeanutils gadget（1.8.3 / 1.9.2 / AttrCompare / ObjectToStringComparator）
* 自动 AES 模式切换：CBC 和 GCM 各走一遍，哪个命中锁哪个
* 内存马注入（Filter / Servlet / Interceptor / HandlerMethod / TomcatValve）
* 回显类型：TomcatEcho / SpringEcho / DFS-AllEcho / ReverseEcho / NoEcho
* 回显生成器（jEG）和内存马生成器（jMG）第三方集成，失败自动回退 Legacy
* Shiro Key 替换（6 条注入路径，自动验证新旧 Key）
* 自定义请求头、Cookie 合并、POST 型探测
* `--json`

  结构化输出，适合脚本化和 AI 调用
* HTTP/HTTPS 代理（支持认证）
* Key 生成器

###

0x03 更新介绍

```
GUI 全新界面：现代 CSS 主题（app.css）、Header/POST Body 并排布局、对齐网格重排JMG 内存马生成 Tab：新增 pass/path/key 输入字段，支持 MemshellGenerateRequest 参数化CLI --jeg 标志：exec 命令支持第三方 jEG 回显生成器CLI --dynamic-memshell 标志：运行时 Javassist 编译内存马源码（替代硬编码 Base64）jEG 回显增强：MODE_CMD 设置 GADGET_JDK_TRANSLET + shiroKey + Authorization 头（明文），支持明文/Base64 双格式响应解析Gadgets.createTemplatesImpl(byte[])：支持直接传入字节码构造 TemplatesImpl，Javassist superclass 修复
```

0x04 使用介绍

📦安装与使用指南

```
单文件可执行版本shiro_attack-<version>-<jdk>.jar包含 data/ 和 lib/ 的完整压缩包shiro_attack-<version>-<jdk>-bundle.zip
```

运行目录结构：

```
./├── shiro_attack-{version}-{jdk}.jar├── data/│   └── shiro_keys.txt   # Key 字典，每行一个 Base64 Key└── lib/                 # CommonsBeanutils 各版本 JAR
```

**0x05 内部VIP星球介绍-V1.5（福利）**

如果你想学习更多**渗透测试技术/应急溯源/免杀工具/挖洞SRC赚取漏洞赏金/红队打点等**欢迎加入我们**内部星球**可获得内部工具字典和享受内部资源和内部交流群，****每天更新1day/0day漏洞刷分上分******([2026POC更新至10922+](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect))****，**包含全网一些**付费扫描****工具及内部原创的Burp自动化漏****洞探测插件/漏扫工具等，AI代审工具，最新挖洞技巧等**。shadon/Hunter/0zone/Zoomeye/Quake/Fofa高级会员/AI账号/CTFShow等各种账号会员共享。详情点击下方链接了解，觉得价格高的师傅后台回复" **星球** "有优惠券名额有限先到先得**❗️**啥都有**❗️**全网资源最新最丰富**❗️****（🤙截止目前已有2900+多位师傅选择加入❗️早加入早享受）**

最新漏洞情报分享：https://t.zsxq.com/DSAvv

**👉****[点击了解加入-->>内部VIP知识星球福利介绍V1.5版本-1day/0day漏洞库及内部资源更新](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect)**

结尾

# 免责声明

# 获取方法

**公众号回复**20260711**获取下载、回复 加群 获取交流群**

# 最后必看-免责声明

文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！

---

# 往期推荐

**1.[内部VIP知识星球福利介绍V1.5（AI自动化）](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect)**

**2.[CS4.8-CobaltStrike4.8汉化+插件版](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247483949&idx=1&sn=cae68096be06be4f0ea746ee5908dc79&scene=21#wechat_redirect)**

**3.[全新升级BurpSuite2026.4专业(稳定版)](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247498687&idx=1&sn=61c2f88f87221eb2b9316bdedf6c0b33&scene=21#wechat_redirect)**

**4.[最新xray1.9.11高级版下载Windows/Linux](http://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247483882&idx=1&sn=e1bf597eb73ee7881ae132cc99ac0c8e&chksm=cf16a75af8612e4c73eda9f52218ccfc6de72725eb37aff59e181435de095b71e653b446c521&scene=21#wechat_redirect)**

**5.[最新HCL AppScan Standard](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497507&idx=1&sn=5b6961225d8adb6ba8d5e43d4943ef9e&scene=21#wechat_redirect)**

渗透安全HackTwo

微信号：关注公众号获取

后台回复星球加入：知识星球

扫码关注 了解更多

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qFFAxdkV2tgPPqL76yNTw38UJ9vr5QJQE48ff1I4Gichw7adAcHQx8ePBPmwvouAhs4ArJFVdKkw/640?wx_fmt=png "二维码")

上一篇文章：[Nacos配置文件攻防思路总结|揭秘Nacos被低估的攻击面](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247492839&idx=1&sn=b6f091114fbd8e8922153a996c8f4f1c&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RjOvISzUFq7Xn8hrO8IErNMnOukYmCdtMhJibzK67Lzz9AJA3XPKvDxfPc8KEgT42O89Dh0UScq9g2GsjbF6Enw/0?wx_fmt=png)

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