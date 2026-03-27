---
title: 这个开源工具能自动检查安全漏洞
url: https://mp.weixin.qq.com/s/ITHExJkViE5C8fLdXn2EHA
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:28:01.757281
---

# 这个开源工具能自动检查安全漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquO2mnJklPBaLPaGicHyvDoOUDDGSibRExVFFTAnewaaI7MpfdEQas0j4unwb2mG6s5dI2icCsBealOAmpqYbwwYjLBOuJib5Nv13Aw/0?wx_fmt=jpeg)

# 这个开源工具能自动检查安全漏洞

Wtttthi
Wtttthi

船山信安

![]()

在小说阅读器中沉浸阅读

#

        做内网安全的兄弟应该都有过这种体验，当拿到一个域控权限或者要做AD安全审计时，面对成百上千的用户和计算机对象，手动一个个去翻密码策略、查委派配置、找Kerberoast目标……步骤是比较麻烦的。

        最近在GitHub上看到个叫**ADPulse**的工具，专门干这事的，一次性给你扫出35类常见AD配置问题和安全风险，是一个比较实用的工具。

简单来说，它通过LDAP连接到域控制器，自动把下面这些高危项给你揪出来：

* **密码策略有没有漏洞**——比如最小长度太短、没开复杂度、锁阈值设太高、甚至可逆加密这种骚操作
* **特权账户里混进了谁**——域管组、企业管组、架构管组这些敏感组里有没有不该在的人，还有那些密码永不过期的账号、描述里写明文密码的骚操作
* **Kerberos攻击面**——哪些账号能打Kerberoast、哪些能打AS-REP Roast，这都是常用来提权的路子
* **委派配置**——无约束委派、约束委派、基于资源的约束委派（RBCD），一个配置不当就可能被人拿去当跳板
* **ADCS证书服务漏洞**——ESC1到ESC15这些经典证书漏洞，工具直接帮你枚举
* **域信任关系**——没开SID过滤的双向信任，外部信任这种容易被横向穿透的点
* **ACL权限滥用**——谁有DCSync权限、AdminSDHolder上有没有不该有的写权限、非特权主体能不能乱改ACL

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquPTBA9MjQMiaiazZmuPgEHScXYM8Rbo83P5VYwfKl8IR15SwWxWZapQ5icCKp74Aj73A3yCqlom3jsaXG0eVjaIAiaVkrFlqTzXNL0/640?wx_fmt=png&from=appmsg)

        主要还有LAPS覆盖率、旧版协议（SMBv1、LLMNR投毒）、GPP密码泄露、影子凭证（Key Credential Link）、SID历史注入……基本上域渗透里常见的坑，它都给你扫一遍。

        这工具是Python写的，安装没啥门槛：

```
git clone https://github.com/dievus/ADPulse.git
cd ADPulse
pip install -r requirements.txt
```

        依赖装完就能跑，不用编译啥的。建议在虚拟环境里装，避免和系统Python包冲突。

## 扫描命令格式如下

最基础的扫描命令长这样：

```
python ADPulse.py --domain corp.local --user jsmith --password 'P@ssw0rd!'
```

如果你在内网里有多个域控，想指定扫哪个，加上`--dc-ip`参数：

```
python ADPulse.py --domain corp.local --user jsmith --password 'P@ssw0rd!' --dc-ip 10.0.0.1
```

        输出支持三种格式：控制台直接看、JSON、HTML。你可以用`--report`参数指定，比如想要全部格式：

```
python ADPulse.py --domain corp.local --user jsmith --password 'P@ssw0rd!' --report all
```

报告默认生成在当前目录，想存到别的地方就用`--output-dir`指定路径。

    有个小细节：如果你在终端里看结果不想看到花花绿绿的颜色，加个`--no-color`就行。

## 实际使用体验

        尝试在测试环境跑了一遍，扫出来不少东西。比如某个测试域里居然有3个用户账号的密码永不过期，还有个计算机账户配置了无约束委派，这些都是高危项。

        工具给出的报告里每个问题都标了风险等级，还会给出简单的修复建议，对于做合规检查和渗透测试前期的信息收集来说，确实省了不少事。

![](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquPAmpDfyfEjFCL9Xic7Zmjr4k9qp1w2zcjlw8sWbxXbw9dSey5UPU6wL9c9jwSAAGQgMial1upngg6iadMSdv4kjfLwT4oJ7nAtNc/640?wx_fmt=jpeg&from=appmsg)

### 注意

**跑这个工具最好用域内普通用户账号**，别直接用域管，毕竟虽然工具本身是只读的，但万一操作失误就不好说了

**建议在非业务高峰期跑**，虽然查询量不大，但LDAP扫描多少会有点负载

**定期跑一跑**，AD配置变动比较频繁，隔段时间扫一次能及时发现新引入的风险点

**配合其他工具一起用**，比如BloodHound做路径分析，ADPulse做配置检查，互补着来更全面

        最后提醒一句：**这玩意儿是拿来审计自己环境的，不是拿来搞破坏的**。在自己授权范围内用，别乱扫别人家的域控。

如果对这个工具感兴趣的兄弟可以去试试

项目地址：https://github.com/dievus/ADPulse

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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