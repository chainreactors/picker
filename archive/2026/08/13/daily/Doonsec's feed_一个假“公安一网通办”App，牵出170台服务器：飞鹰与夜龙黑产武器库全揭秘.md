---
title: 一个假“公安一网通办”App，牵出170台服务器：飞鹰与夜龙黑产武器库全揭秘
url: https://mp.weixin.qq.com/s/oHxJcfwyKtG3L99SrOigZw
source: Doonsec's feed
date: 2026-08-13
fetch_date: 2026-08-14T03:58:29.330883
---

# 一个假“公安一网通办”App，牵出170台服务器：飞鹰与夜龙黑产武器库全揭秘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GEVYW8ofHic1wK1ULI7jpGJiaia83aCHkCz2VTzx1lSib46AbdypYH3ickgHfZtNRSCujf9ncp9ViaJ6b61rtwDlPibTq0ic5ccrwzEQOZ7J0j5TOIA/0?wx_fmt=jpeg)

# 一个假“公安一网通办”App，牵出170台服务器：飞鹰与夜龙黑产武器库全揭秘

老鑫安全
老鑫安全

老鑫安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#

> 源码泄露后，黑产从“卖工具”进化到“开平台”，安卓安全正面临工业化挑战。

## 一、从一款假App挖出工业化产业链

2026年6月18日，国家网络安全通报中心发布紧急提醒：一款伪装成“公安一网通办”的恶意App正在传播，点名域名 `110GongAn.com` 与IP `207.56.30.188`。

顺着这条线索深挖，安全研究人员发现这远不止一个孤立的恶意App，而是一整套**开箱即用的安卓远控黑产生态链**。这套系统名为“飞鹰”，背后至少活跃着**170台在线服务器**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic2F43WLsHicXLN6pEJRicKYFuiclx5YvzibTGK1QngvXF6VickqIskojGCibH2voPSfVO7JWkBGxWo8ybvF9Ps6Bg3f7nwoQgO2bDBn8/640?wx_fmt=png&from=appmsg)

被点名的服务器托管在香港，几乎每月轮换证书与域名，却始终指向同一后台。通过指纹扩线，研究人员在30天内找到了158台特征一致的服务器，加上使用同一份默认证书的12台，总数达到170台。这些服务器集中在香港少数托管商，零星散落于美国、中国大陆及欧亚地区。

> **需要说明的是：** 170是服务器数量，而非受害者数量——每一台服务器背后，都可能控制着成百上千台被感染的手机。

## 二、“飞鹰”：开箱即用的作案作坊

飞鹰远控平台的核心是一套**网页控制台**，将木马生成、APK打包、C2设备管理全部集成在一起。

![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic031Rnia8Y7P6XkkTw8X5WUrfD4bklre2Eybjsv83SYhficSa4tsNm2NOj6LJ39uhlRAfVJjP5qreFK4ia6iaQuUk2Rsu6iakdH14J0/640?wx_fmt=png&from=appmsg)

### 技术细节：一键生成背后的“免杀”机制

飞鹰的APK构建脚本（`ApkBuilder.php`）展示了工业化恶意软件生成的精细程度：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic3KOpbyxsb5RrJ6z5gV6quMxqQCyTyUNgueBpkS7C89m7elEB8Z7Vicibs0ibqDia9561Ckz6g5BXb6ribkciaWKw55Ihiadjia0YiaW8Tw/640?wx_fmt=png&from=appmsg)

* • **包名随机化**：将硬编码的默认包名 `com.icontrol.protector` 替换为听起来合法的随机名称，如 `com.cloud.manager.core`。
* • **类名混淆**：核心功能类名被重命名为8-14位随机字符串。原始的类名暴露了其真实能力：`RecordPayPassword`（支付密码捕获）、`LiveKeysStrok`（键盘记录）、`ScreenCaps`（屏幕截图）、`Webjector`（钓鱼覆盖层）、`AccessibilityActivity`（无障碍服务滥用）、`CameraCap`（摄像头访问）。
* • **C2地址加密**：使用AES-128-CBC加密硬编码进样本，密钥通过PBKDF2-SHA1经过65,536次迭代派生。
* • **熵值填充**：向APK的assets目录注入2.8-3.5MB的结构化JSON填充数据（伪装成SDK配置缓存），降低文件熵值以规避杀毒软件的启发式检测。开发者甚至在注释中写明：“降低熵值避免触发AV警报”。

生成的样本在沙箱中被检测为**SpyNote安卓木马**变种。其核心能力包括：记录支付密码、键盘输入、截屏、叠加钓鱼弹窗、调取摄像头，最关键的是**滥用安卓无障碍服务**——无需系统漏洞，只需诱骗用户在设置里打开开关，即可实现读屏+模拟点击。

## 三、通报三周后“夜龙”上线：攻击能力的代际升级

6月23日，就在国家通报发出三周后，新平台 **“夜龙”** 上线。7月中旬，第二代版本已在开发中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic2U200OQUm3n2zKmytEiap3flKBPVxbdezrJnokqVb1CuiaC5ofsaQ5rketCrC1z00cD4RQZf8YlWVbL7mgUbFzdTyYXVXWN6JaM/640?wx_fmt=png&from=appmsg)

夜龙在飞鹰的基础上进一步升级，其能力对比清晰地揭示了黑产武器的进化方向：

|  |
| --- |
|  |

| 能力维度 | “飞鹰”平台 | “夜龙”平台（第二版） |
| --- | --- | --- |
| **核心监控** | 键盘记录、截屏、摄像头抓拍 | **实时屏幕共享** 、读短信/相册、录音、文件管理 |
| **钓鱼目标** | 通用应用模板 | 精准针对**支付宝、微信、工农建等银行App**，以及 **TokenPocket、imToken** 加密钱包 |
| **隐蔽手段** | 应用图标正常显示 | **安装后自动隐藏图标** ，更难被发现和卸载 |
| **远程操控** | 模拟点击 | **“黑屏模式”** ：远程操控时屏幕显示假“系统更新”界面，受害者看着黑屏，账户正被清空 |

无障碍服务使短信验证码基本失效，但活体人脸验证与转账限额仍有实际防护作用。

## 四、技术核心：为何难以防御？

### 1. 攻击入口不在技术漏洞，而在“用户授权”

木马的能力来自于**安卓无障碍服务**。攻击者只需诱骗用户在设置中为其开启该权限，便可获得几乎等同于系统级的控制能力。**手机被控制的入口不在高深漏洞，而在那个随手点下的授权确认框。**

### 2. 基础设施高度集中且有迹可循

虽然攻击者频繁更换域名和证书，但其登录面板的**指纹特征**暴露了其规模：

* • 页面在加载自定义品牌前会短暂显示 **“AdminPro”** 标题；
* • 访问时固定返回**302跳转到HTTPS**，并带有严格的 `Strict-Transport-Security` 头。

利用这些特征组合查询，30天内即发现约158台服务器，加上默认证书关联的12台，共约170台。

## 五、防护建议

### 对普通用户：

* • **拒绝非官方渠道的应用**，尤其警惕通过短信、社交软件传播的APK安装包；
* • 如遇App要求开启**无障碍服务**权限，务必核实其必要性；
* • 对伪装成公安、银行、政府的App保持高度警惕。如发现手机出现异常“系统更新”黑屏、应用莫名消失等情况，应立即检查无障碍服务列表。

### 对企业与安全团队：

* • 监控Telegram等渠道的源码泄露与工具售卖情报；
* • 利用飞鹰面板的指纹特征（AdminPro标题、302跳转、HSTS头）进行资产测绘，主动发现内部或上下游关联的恶意服务器；
* • **转变防守思路**：源码泄露导致的变种层出不穷，封禁单个样本或域名已无法解决问题，需建立基于行为特征的检测能力，尤其要监控内网设备对可疑C2地址的连接行为。

## 附录：学术研究与IOC参考

### 源码及技术分析参考

本文涉及的飞鹰（Flying Eagle）源码及SpyNote木马逆向分析资料，因资源较为敏感，不便直接公开链接。

**关注本公众号，在后台发送关键词「飞鹰源码」** ，即可获取以下学术研究参考资源：

* • 飞鹰Docker部署包（中国龙.zip）相关分析资料
* • SpyNote逆向分析案例与技术文档
* • APK构建工具与C2面板源码参考

> **郑重声明：** 上述资源仅供网络安全学术研究、威胁分析及防御技术学习使用，严禁用于任何非法用途。请务必遵守相关法律法规，合理使用。

---

### 关键IOC（指标）

|  |
| --- |
|  |

| 类型 | 指标 |
| --- | --- |
| 恶意域名 | 110gongan[.]com, fusu.us[.]ci, alcs.xyttkx[.]cc |
| 恶意IP | 207.56.30[.]188, 207.56.30[.]194 |
| APK SHA-256 | c692ad120cc90548d48dbe57d006f2403c49833b8993af3c38fe031eb39999bd |
| 源码脚本 | ApkBuilder.php (0376db397807c1f1e32a99a9db622f35f4fe5597bd05b4fd5e93117062e0131f) |

---

> 从伪装公安App到170台服务器，从飞鹰到夜龙，安卓远控黑产已进入工业化时代。而这一切的起点，可能只是一个用户随手点下的“允许”按钮。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bkcWdoIicx2ceUKiaEJfG0L5ZJtpCjuISeOmHuvZZbpibNciacvzGib2W6jibSJPwQnuibB9SIic18Eiafy2LZicYLiarnFtA/0?wx_fmt=png)

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