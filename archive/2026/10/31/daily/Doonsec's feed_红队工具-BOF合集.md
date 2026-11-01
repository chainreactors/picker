---
title: 红队工具-BOF合集
url: https://mp.weixin.qq.com/s/j9UGBgEXa2QrHRjC7vLCCg
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:19:12.603728
---

# 红队工具-BOF合集

# 红队工具-BOF合集

安全天书

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本文所涉及的技术、思路和工具仅用于本地靶场安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，请务必在获得明确书面授权的环境下使用，并遵守相关法律法规，一切后果由使用者自行承担！！

项目介绍

    一组用于开发后操作的信标对象文件（BOF）。包括凭证查找、系统枚举、事件日志分析和权限管理工具。

| BOF | 描述 | 用途 |
| --- | --- | --- |
| **adduser-domaingroup** | 通过 将用户添加到域组，回退到域本地/内置组（目标为 DC）`NetGroupAddUser``NetLocalGroupAddMembers` | 用途 |
| **adduser-localgroup** | 在Windows电脑上将用户添加到本地组 | 用途 |
| **bkread** | 读取带有备份语义的文件，无需更改ACL`SeBackupPrivilege` | 用途 |
| **查验通道** | 探测读取目录路径和子文件夹（深度-1或递归） | 用途 |
| **Credguard-Check** | 检查凭证保护、HVCI、轻微保护、VBS状态 | 用途 |
| **卷曲** | 带有TLS指纹识别的HTTP/HTTPS请求 | 用途 |
| **decrypt-credmanager** | 使用 DPAPI 解密 Windows 凭证管理器的条目 | 用途 |
| **DPAPI-unprotect** | 在当前用户的上下文中解密任意的DPAPI大块（可选择熵） | 用途 |
| **DSREG状态** | 报告设备、租户、用户和代理状态的文档`dsregcmd /status` | 用途 |
| **边缘传递转储** | 从进程内存中转储存储在 Microsoft Edge 中的明文密码 | 用途 |
| **enum-credmanager** | 列出Windows凭证管理器条目（无解密） | 用途 |
| **列举信用** | 以凭证为中心的文件枚举，支持可选的应用数据发现和内联内容转储 | 用途 |
| **enum-logon-events** | 登录事件（4624）查询安全事件日志 | 用途 |
| **枚举注册** | 提取所有已加载用户蜂箱的RDP历史、已安装软件、环境变量、WSL/Docker信息 | 用途 |
| **enum-stored-accounts** | 列出服务账户、带密码的任务，以及每个配置文件的DPAPI材料（哪些令牌值得窃取） | 用途 |
| **枚举用户权利** | 列出被赋予有效LSA用户权的账户;默认为`SeMachineAccountPrivilege` | 用途 |
| **假窗口弹出异步** （BOF-PE，x64） | 显示原生Windows凭证界面，桌面调暗;运行为异步 BOF 作业，以确保信标保持响应 | 用途 |
| **Enumshares（登记份额）** | 枚举远程共享并测试文件系统访问（单主机） | 用途 |
| **enumshares-file** | 从上传的主机名文件中枚举远程共享 | 用途 |
| **列表管道** | IPC侦察用的命名管道列表 | 用途 |
| **LSFILES** | 递归文件/目录列表，包含万用符、日期/大小过滤器 | 用途 |
| **nslookup-file** | 通过并行 DNS 查询解析主机名文件 | 用途 |
| **RemoveUser-DomainGroup** | 通过 从 中移除用户，退回到域本地/内置组（目标 DC）`NetGroupDelUser``NetLocalGroupDelMembers` | 用途 |
| **removeuser-localgroup** | 从Windows计算机的本地组中移除用户（或针对DC时的域本地组） | 用途 |
| **SCCM-WMI** | 从实时WMI策略中恢复SCCM网络访问账户凭证，作为（CRED-3）`SYSTEM` | 用途 |
| **SCCM盘** | 从磁盘上恢复SCCM网络访问账户凭证，格式为（CRED-4）`OBJECTS.DATA``SYSTEM` | 用途 |
| **SCCM-本地侦察** | 本地SCCM客户端recon：路径、缓存权限、管理点、日志UNC/URL抓取（RECON-7） | 用途 |
| **TCPSCAN** | 单主机的TCP连接扫描 | 用途 |
| **TCP扫描文件** | TCP 连接扫描上传文件中的主机（接受输出）`nslookup-file` | 用途 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQXKUPLHEKticgWt0HJnjhP8GWgYGXQgaQUVOwVuMmOibYpEIPWKEPuia2BFuQPjhz7CNvxQsNCEE3fTK60jjiaTjfZUA1HAGOJeMfk/640?wx_fmt=png&from=appmsg)

GitHub地址：

```
https://github.com/chryzsh/redteam-bofs
```

注意：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测。

**红蓝偶像练习生小圈子**

**更多工具思路文章请加入纷传，圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结以及自研工具与插件，目前圈子已满400人，欢迎各位进圈子交流学习！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQXm0N3QQT1byMjhzMvPx3RqYswWyvlOTqPbxMWYiawjx8h7EJwTTDrE5Wp4CytmjG2dYtIGjAJMCSicXoY1N8nOcFE2a0oqNwWnE/640?wx_fmt=jpeg&from=appmsg)

****圈子目前更新相关技术文章：****

************* HeavenlyBypassAV内部版工具-轻松免杀各大杀软
* HeBypassAV内部版Patch免杀工具-轻松绕过杀软EDR
* Heavenly自动化红队后渗透工具免杀生成器
* Heavenly白加黑自动化生成免杀工具
* HeavenlyProtectionCS内部CS插件
* Heavenly专版Linux免杀工具
* 冰蝎webshell免杀工具

* 哥斯拉webshell免杀工具
* 红队场景下lnk钓鱼Bypass免杀AV
* Frp免杀隧道工具
* 1day和0dayPOC
* lnk钓鱼思路视频讲解
* lnk钓鱼Bypass天擎
* msi钓鱼
* chm钓鱼
* Kill360核晶
* AV对抗-致盲AV（核晶）
* 捆绑免杀360
* Kill火绒
* 火绒6.0内存免杀
* kill-windows Defender

* Defender分离免杀
* Defender知识点
* EDR对抗思路
* 进程注入知识点

* 自启动思路
* **多种维权手法**

* Fscan免杀核晶
* QVM解决思路
* 红队思路-钓鱼环境下小窗口截屏窃取
* 免杀Todesk/向日葵读取工具

* 渗透测试文章思路
* 内网对抗文章思路
* **还有更多红队工具文章！期待您的加入！！！**********

**往期推荐**

**********[安全天书免杀课来袭｜助力实战免杀钓鱼(文末送福利)](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485167&idx=1&sn=7ab4393e75cf94d13cb79e22b92fb8d0&scene=21#wechat_redirect)**

**[【红队工具】攻防后渗透工具自动化免杀！！！](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485305&idx=1&sn=3b4c50d0f88a753089767db5304b6626&scene=21#wechat_redirect)**

**[【红队工具】红队内网后渗透CobaltStrike插件更新](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485006&idx=1&sn=e3bcf2070226fcfc93b565ae2c9d85ad&scene=21#wechat_redirect)**

**[免杀更新--Heavenly自动化生成白加黑3.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485679&idx=1&sn=991c111e2627ec8835dc13b8bc919eb3&scene=21#wechat_redirect)**

**[绕过360安全卫士实现维权](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485280&idx=1&sn=467194cdf681646597a84e7f08b638bf&scene=21#wechat_redirect)**************

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

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