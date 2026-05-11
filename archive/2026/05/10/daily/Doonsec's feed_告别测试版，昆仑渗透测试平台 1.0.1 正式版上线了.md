---
title: 告别测试版，昆仑渗透测试平台 1.0.1 正式版上线了
url: https://mp.weixin.qq.com/s/MsIr3O4WRnhBXW-PLgGsVw
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:51:52.823765
---

# 告别测试版，昆仑渗透测试平台 1.0.1 正式版上线了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3oR6eMARh6zekZYD523oaQPLia0rVDN40aWic81KPoSt9RfTDGlVmj5YyiaDsAh9nsThw2kvue8TtoII8yR5JQa0N0pCpiaz9UvSpuort2GibfSI/0?wx_fmt=jpeg)

# 告别测试版，昆仑渗透测试平台 1.0.1 正式版上线了

原创

昆仑AI安全实验室
昆仑AI安全实验室

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**我在甲方内网杀了一圈，靠的是自己攒的一个“缝合怪”**

去年有几个项目比较特殊，目标环境里不能随便引入外部工具，全程只给了我一台干干净净的虚拟机。以前干活，外网打点开Goby，Web测试切Burp，漏洞利用换Metasploit，内网横向用Cobalt Strike，抓密码还得跑impacket——但现在，这些都用不了。

别说商业软件授权的问题，光是来回切换、导入导出数据就够让人头疼了。更麻烦的是，市面上没有一个工具能让我从头到尾都不切换窗口。

所以我把自己关在书房三个月，把过去做红队的经验全写进了一个工具里。我管它叫“昆仑”。下面聊几个我在实战中真正靠它解决问题的情况。

---

### 一、一台被遗忘的交换机

某制造企业的攻防演练，我的任务是从外网打进去，目标是域控。

前期信息收集没发现什么像样的Web漏洞。FOFA搜了目标的IP段，发现一个公网IP开放了443端口，证书信息显示是H3C设备。浏览器访问，一个H3C交换机管理界面。

admin/admin。进去了。

这种事对我来说已经不算惊喜了——边缘设备、临时设备、测试设备，永远是默认密码的重灾区。

翻配置文件，在注释里找到一行：“监控账号/密码monitor/Monitor@123”。运维怕忘密码，直接写在配置里。

用这个账号尝试登录同网段的一台Windows服务器，3389开放，monitor/Monitor@123——直接登录成功，还是本地管理员权限。

这台机器是加域的。net user /domain看了下，域管组有8个账号，域内大概300多台机器。Procdump导出LSASS内存，下载到本地用Mimikatz离线提取，拿到了一个服务账号的NTLM哈希。

从这个点到域控，后面还做了哈希传递、会话劫持、DCSync，全程在昆仑里操作，没开第二个软件。从发现那台交换机到导出krbtgt哈希，总共18个小时。

---

### 二、FID聚类发现的影子资产

某互联网公司SRC挖洞，常规子域名爆破只找到十几个资产。

用昆仑的FID（Web特征聚类）对已知资产的Web页面进行特征提取——HTML结构哈希、响应头顺序、favicon、静态资源列表，每一维单独算哈希。然后对C段全扫，FID自动匹配出了二十多个没有在DNS里出现过的资产。

其中一台是废弃的测试服务器，上面跑着旧版本GitLab，存在已知的RCE漏洞。从发现那台机器到拿到GitLab服务器权限，不到一个小时。

FID的思路其实不复杂：同一个开发团队写代码，同一个运维配置服务器，总会有一些不易察觉的共性。把这些共性变成哈希，就能从茫茫多的IP里把“一家的”资产挑出来。

---

### 三、反连平台检回来的RCE

某云服务商的外网，扫了一圈没找到能用的入口。在某个API的User-Agent头里随手注入JNDI Payload，指向昆仑反连平台的LDAP监听端口。

几分钟后，反连平台收到了一台内网服务器的LDAP回连请求。通过LDAP通道投递恶意Java类，拿到反向Shell。后来定位到这台服务器在第三层内网深处。

如果没有反连平台，这个漏洞大概率被当“无回显”直接忽略了。昆仑的反连平台做了多协议单端口复用——DNS、HTTP、LDAP、RMI共用一个端口，收到回连时根据协议特征自动路由到对应处理逻辑。

---

### 四、FUZZTAG十五分钟跑出一个支付漏洞

某金融客户项目，需要对一个支付接口进行深度测试。这个接口参数比较多——金额、订单号、支付方式、优惠券码、用户ID——各种组合。

昆仑的FUZZTAG引擎可以让我在数据包的任意位置插入标签，自动生成批量请求。当时用`{{int(0-1000)}}`遍历金额参数、用`{{randint(100000,999999)}}`生成订单号、用已知优惠券码列表批量测试，标签之间还可以嵌套。

不到十五分钟，发现一个并发竞争条件：同时发两个相同请求，一个用了优惠券，一个没来得及扣库存，两个订单都成功了。客户安全团队说他们用商业扫描器扫了好几天都没发现。

---

### 五、横向移动的一键化

拿到第一台机器后，最怕的是在横向移动时被检测到。

昆仑的横向移动模块集成了哈希传递、票据传递、WMI、SMB、WinRM、计划任务持久化，全部图形化操作。不需要手敲impacket命令，也不用记WMI的语法——选中目标机器，选择方法，点击执行。

有次护网，从一台普通域用户出发，通过Kerberoasting拿到一个服务账号，这个服务账号恰好是Server Operators组成员。BloodHound显示Server Operators可以登录某台成员服务器，而那台服务器上正好有域管在活动。

整条链——发现SPN→请求TGS→破解→登录跳板机→抓域管哈希——全程在昆仑的界面里完成。后来复盘，防守方的SIEM没有触发任何告警，因为每一步都是正常的Windows操作。

---

### 六、纯Python的意义

最后说点技术上的。昆仑纯Python实现，打包成一个exe，双击即用。所有功能模块——资产发现、MITM代理、漏洞扫描、PoC引擎、C2框架、横向移动、反连平台——都在一个进程里。

模块之间通过事件总线通信，资产发现扫到新目标自动通知漏洞扫描，漏洞验证通过反连平台拿到回连自动更新状态，不需要人工把数据从一个工具搬到另一个工具。

Python版本用了3.10+，网络IO全部异步处理，并发扫描几千个IP不会卡界面。数据库用SQLite，单文件存储，不需要装MySQL不用配环境。

---

目前昆仑支持的功能都在下面的清单里了。如果你也受够了在无数工具之间来回切换的痛苦，不妨试试。有问题直接提Issue，看到就修。

**资产发现与指纹识别**（端口扫描、多协议Banner、JA3/JA3S、favicon、FID特征聚类）

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zgANyLTYjDvmCvpyOgAsG1Cu4xh6Psjz6GnO7usN0Ax4Vq83riaLwDnhOaXZGzacI5bnKJttJY2GnlbEiaFeMXhYnJ30P7q11qA/640?wx_fmt=png&from=appmsg)

**MITM代理**（HTTP/HTTPS/HTTP2/WebSocket拦截修改、证书动态签发、断点改包）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6yD4LQ4pg1Olx5N8au1MvpIZmCSaUjPibugCzHJnSyTSRvsWgI1uEZyEWr9ccN8pzQu7danVmeAOmfdIM5HW4hrTKHLahJmjuRo/640?wx_fmt=png&from=appmsg)

**Web Fuzzer + FUZZTAG**（标签化模糊测试，`{{int}}`、`{{xss}}`、`{{payload}}`批量生成）
**漏洞扫描引擎**（Nuclei模板兼容、沙箱执行、DNSLog/HTTPLog/LDAPLog多信道OOB）
**反连平台**（DNS/HTTP/LDAP/RMI多协议端口复用）
**C2框架**（HTTP/HTTPS/DNS/WebSocket Beacon、心跳抖动、流量混淆）

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6y6nRDEVsP06sgODNU82dXvfDkf2B2mDqxs4zaQUDn40Iq7dZ4sZorhN0piaTUeLaDZpoZCQaEq1HVw65f4ZUnoHKwF7oZL0AA0/640?wx_fmt=png&from=appmsg)

**横向移动**（哈希传递、票据传递、WMI、SMB、WinRM、计划任务持久化）
**提权辅助**（Windows系统信息收集、补丁对比、风险高亮、利用建议生成）
**域控攻击**（DCSync、Shadow Credentials、Skeleton Key、AdminSDHolder、跨域信任利用）

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6yCEDcnUH8cbcqmZiaNhuNyGmc5bEBMdiagRMNiag8zjCfPiak1LvlLrV2Ymqlh7Uxia0M2XM7Gq81wibKeHbMLHAvKRmQK0a2aeRbac/640?wx_fmt=png&from=appmsg)

**JWT/OAuth专项**（可视化解码、算法篡改、OAuth流程分析）

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6wwRiayjPgyaRricSng2jhuFQ8FLL5OyO8whUR1SXVTYjTT66pvcssCGULapSPuDVTcSSIlmPN1HKX1wiana15fuD2ncuHVOTyUOo/640?wx_fmt=png&from=appmsg)

**Java反序列化利用**（30+链、图形化Payload生成、内存马注入）
**被动扫描引擎**（流量自动分析、信息泄露/安全配置缺陷实时发现）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6zjPyVR7Ttc6lj10XAw3BBJMqxZJFC2XdXa95QmHPJ3HIM0ATksZMcOgrweWeEq7FL8wyRkVqWuxKiaFHLTVicxfFRETLkvTCbibA/640?wx_fmt=png&from=appmsg)

**插件市场**（热加载、社区分享、沙箱隔离）
**报告生成**（HTML/PDF/Markdown、MITRE ATT&CK自动映射）

**新增修复系统**（WIN10-11全版本 Linux macOS）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zxPsSBiaTT0QiaBjibScxViciathof2tlahJCticqia6DncZNe4Fiatd1zWxPQKdTAqnyRPFWmxviaJJm5R8JLbEAURJnZRMiaKa1quLS8k/0?wx_fmt=png)

昆仑AI安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zxPsSBiaTT0QiaBjibScxViciathof2tlahJCticqia6DncZNe4Fiatd1zWxPQKdTAqnyRPFWmxviaJJm5R8JLbEAURJnZRMiaKa1quLS8k/0?wx_fmt=png)

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