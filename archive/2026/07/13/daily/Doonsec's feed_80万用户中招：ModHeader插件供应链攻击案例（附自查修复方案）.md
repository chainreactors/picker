---
title: 80万用户中招：ModHeader插件供应链攻击案例（附自查修复方案）
url: https://mp.weixin.qq.com/s/fHC71Gh4J0hvhnzwt4NTQQ
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:45:52.767439
---

# 80万用户中招：ModHeader插件供应链攻击案例（附自查修复方案）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tNyBeBKReNJOWPdBAkeAvBfGtAOWv0JAl5jBRuVCibI6QmwFqTAd8dal313GjhUKxrvJcXiaHO22fDPBV6aAa0lWXQo2IvtCLd4HLibAVibJMjs/0?wx_fmt=jpeg)

# 80万用户中招：ModHeader插件供应链攻击案例（附自查修复方案）

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于潇湘信安
，作者3had0w

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM6fpNgxJic72iaxuNHwNA0BooiblUaaQuiavCyr7GWWPulUHw/0)

**潇湘信安**
.

一个不会编程、挖SRC、代码审计的安全爱好者，主要分享一些安全经验、渗透思路、奇淫技巧与知识总结。

最近看到Hackindex曝出ModHeader这个Chrome扩展程序包含恶意软件，前段时间我还安装分享过这个插件...，圈内有不少师傅也在用这插件，有安装过的师傅还请及时清理...。

这里主要是提醒下大家，详细技术分析请看原文：

https://hackindex.io/research/modheader-malware-chrome-spyware

**前言**

近日安全研究团队曝光重大浏览器插件供应链风险：**Chrome 应用商店官方上架的 ModHeader v7.0.18 版本内置完整窃密 SDK**，谷歌已主动下架该版本并自动禁用用户设备内插件，超 80 万安装用户面临浏览记录泄露风险。

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNLib7uw5JKGZunicYfBJpzibrkhywjb4OnZj4uib1F89IUqC7pk2qg7mDJT8JRx7Jfjlqzs9RUtJEeOxwUWT58ks7ibLltjbickPibSvU/640?wx_fmt=png&from=appmsg)

ModHeader 是前端、测试、安全、运维人群高频使用的工具，核心功能是全局修改网站 HTTP 请求 / 响应头，为实现功能，插件默认申请**全网站访问、网络请求监听、页面脚本注入**等高风险权限，一旦植入恶意代码，可完整监控全部上网行为。

**一、恶意代码藏在哪？用伪装完美绕过商店审核**

本次恶意载荷采用极具欺骗性的隐藏手段，普通开发者浏览代码完全无法分辨：

**1、伪装成通用日期库 dayjs.min-\*.js**

恶意窃取逻辑全部封装在名为`dayjs.min-6a736ee8.js`的文件中，对外导出看似工具函数，实际全部为窃密配套逻辑：提取访问域名、判断浏览器类型、定时休眠、生成追踪指纹。审核人员扫一眼文件名会默认是第三方开源依赖，直接忽略内部恶意代码。

**2、官方正版签名，无盗版篡改**

涉事插件 ID：`idgpnmonknjnojddfkpgkljpfnnfcklj`，是商店原版 ModHeader 标识，文件携带谷歌商店官方签名，并非第三方修改盗版，属于典型**供应链投毒**。

二、完整窃密流程：加密收集访问域名，定时回传境外伪装服务器

恶意代码内置一套完整、成熟的数据窃取链路，全程做 AES-GCM 加密混淆规避网络抓包检测：

### 1. 采集用户浏览域名

用户打开任意网站时，插件自动提取网站域名，加密后存入本地数据库，统计每个站点访问频次；**仅采集域名，不会抓取完整 URL、Cookie 与账号密码**。

### 2. 生成永久设备追踪指纹

基于时间哈希生成唯一设备标识，代码内置中文盐值`mod盐header`，用于长期标记同一台设备，持续追踪用户上网习惯。

### 3. 错峰定时上传，规避流量监测

插件会根据设备指纹计算专属上传时段（早 7 点至 15 点随机时间），每日仅上传一次加密数据，批量受害者上传时间分散，很难通过流量审计批量发现异常。

### 4. 假学术站点做数据接收服务器

窃取数据统一 POST 上传至 `https://api.stanfordstudies.com/app/log`：

* 前端页面伪装成 “斯坦福学术研究项目”，和斯坦福大学无任何关联；
* 域名托管 AWS 美国服务器，使用飞书 Lark 企业邮箱，代码内嵌中文字符，多处线索指向中文运营者；
* 仅单向接收数据，无远程指令下发通道，无法远程控制浏览器。

## 三、关键细节：当前版本窃取功能处于休眠，但风险极高

本次被下架的 v7.0.18 版本中，窃取代码内置**空浏览器白名单开关`$w = []`**，默认拦截上传逻辑，在逆向测试环境中并未产生数据外发记录。

但风险不能忽视：

1. 攻击者只需推送新版更新、修改白名单，即可一键激活全网 80 万设备的窃密功能；
2. 插件自带本地存储，会缓存所有页面完整请求/响应头，本次测试环境缓存数据高达 178MB，头部信息包含**登录 Token、会话 Cookie、内网地址**等敏感数据，长期留存本地存在泄露隐患。

## 四、该插件不会执行的高危操作

1. 无远程代码执行逻辑，不存在 eval、动态加载外部脚本；
2. 不会窃取账号密码、完整页面内容，上传仅包含域名、浏览器类型、设备指纹；
3. Cookie 仅读取长度用于本地统计，不会上传 Cookie 明文。

## 五、个人用户完整清理步骤

1. 打开 Chrome 扩展管理，确认 ModHeader 已被浏览器自动禁用，直接卸载插件；

2. 删除本地残留存储目录（Mac、Windows路径）：

```
Mac路径：~/Library/Application Support/Google/Chrome/Profile 1/Extensions/idgpnmonknjnojddfkpgkljpfnnfcklj
Windows路径：C:\Users\username\AppData\Local\Google\Chrome\User Data\Default\Extensions\idgpnmonknjnojddfkpgkljpfnnfckljC:\Users\username\AppData\Local\Google\Chrome\User Data\Default\Sync Extension Settings\idgpnmonknjnojddfkpgkljpfnnfckljC:\Users\username\AppData\Local\Google\Chrome\User Data\Default\Managed Extension Settings\idgpnmonknjnojddfkpgkljpfnnfckljC:\Users\username\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\idgpnmonknjnojddfkpgkljpfnnfckljC:\Users\username\AppData\Local\Google\Chrome\User Data\Default\IndexedDB\chrome-extension_idgpnmonknjnojddfkpgkljpfnnfcklj_0.indexeddb.leveldb
```

同步清理 IndexedDB、本地扩展设置、同步缓存文件夹；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNI3QjVGYEUrY5zvaxCQjkzLBvFt2deDTR7kYesJsmIXcHMxnnl7IkUafZcLrAKbQu2Hra0WkEcIdjhUMqthyxbvhb61nMS9iaIc/640?wx_fmt=png&from=appmsg)

3. 本地 DNS 屏蔽恶意域名：`api.stanfordstudies.com`；

4. 如需修改 HTTP 请求头，更换其他无风险同类工具，切勿重新安装 ModHeader。

六、企业运维/安全团队检测狩猎规则

批量排查终端 Chrome 扩展，命中以下 IOC 即可判定风险：

### 网络 IOC

```
api.stanfordstudies.com 对外POST请求/app/log
```

扩展特征

```
插件ID：idgpnmonknjnojddfkpgkljpfnnfcklj版本号：7.0.18恶意文件：dayjs.min-6a736ee8.js、background-94ad634d.js
```

静态特征字符串

```
硬编码AES密钥：aWfU3yG_wksZaQdSnxPJBOId0cAN8KK/UIlZbli7-bE指纹盐值：mod盐header
```

## 七、安全总结与长期防护建议

1. 开发调试类插件权限极高（全网站、网络监听），非必要不安装；
2. 定期清理长期不用的浏览器扩展，定期查看商店插件评分与最新评论；
3. 企业环境限制员工私自安装第三方扩展，开启浏览器扩展管控；
4. 警惕使用名校、官方机构名称伪装的陌生域名，此类多为恶意数据接收站点；
5. 关注插件更新动态，商店突然下架、强制禁用的扩展第一时间卸载清理缓存。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

学习网安实战技术，戳“阅读原文”

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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