---
title: 新型ZeroDayRAT间谍软件同时攻击安卓与iOS系统
url: https://mp.weixin.qq.com/s/KRm9Y-ltDoWzXrgCib3gjQ
source: Doonsec's feed
date: 2026-02-17
fetch_date: 2026-02-18T04:13:31.754499
---

# 新型ZeroDayRAT间谍软件同时攻击安卓与iOS系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R9d0DzJpTeJzaiatPZVmiapqduN8nWs7KlC47FbGhKJySvDODpHibnHxAThEPzibm5O2wur0ibxgVWhWMEJCG26pG2AicPF58hZZXungXqIY8SgOk/0?wx_fmt=jpeg)

# 新型ZeroDayRAT间谍软件同时攻击安卓与iOS系统

响应云SRC
响应云SRC

响应云SRC

![]()

在小说阅读器中沉浸阅读

## 响应云SRC

### 文章来源

新型ZeroDayRAT间谍软件同时攻击安卓与iOS系统，实施实时监控和数据窃取

## ZeroDayRAT

**ZeroDayRAT** 是一款通过 Telegram 公开售卖的新型移动端间谍软件平台，其恶意活动最早可追溯至 **2026 年 2 月 2 日**。该恶意软件同时针对 Android 与 iOS 双平台，为攻击者提供轻量化、易操作的跨平台攻击工具。

## 一、全方位监控能力

攻击者可通过基于浏览器的控制面板，对受感染手机实施全维度监控： 实时 GPS 定位追踪 系统通知内容完整捕获 短信访问（含 OTP 验证码） 摄像头 / 麦克风实时调取 屏幕实时录制 结合应用上下文的精准键盘记录 此外，该工具还具备多项高级窃密能力： 枚举设备内已登录账号 加密货币剪贴板地址替换 银行凭证窃取、覆盖攻击 iVerify 研究人员在调研 “即用型” 移动间谍软件市场时发现 ZeroDayRAT，其设计初衷就是降低攻击门槛，无深厚技术背景的攻击者也可轻松使用。

## 二、传播途径分析

ZeroDayRAT 主要依靠社会工程学实现初始感染，核心传播链路： 短信钓鱼（Smishing） 受害者点击短信内恶意链接，跳转至伪造应用下载页面。 其他常见传播渠道 钓鱼邮件 假冒应用商店 WhatsApp / Telegram 聊天中的恶意链接 最终诱导用户下载 Android APK 或 iOS 对应恶意载荷，完成设备植入。![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R9d0DzJpTeLg34ky9G0mdznqcJZVn5wqiaZpj1B21KXib3GRico1fmemuTsiauZ5cW3h5DA62KK2GsgYN3pUYib6RwRtBoK6ibVrpiaiccHjgs7o5Ss/640?wx_fmt=jpeg&from=appmsg)据 iVerify 披露的 ZeroDayRAT 控制面板截图，已出现印度与美国地区的受控设备。

## 三、用户画像构建能力

恶意软件成功植入后，攻击者可从多维度完整构建受害者画像： 设备详细硬件 / 系统信息 SIM 卡及运营商数据 应用安装与使用记录 完整拦截的通话、短信、通知内容 其控制面板可单点集成摄像头、屏幕、麦克风访问权限，大幅提升攻击效率。![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R9d0DzJpTeIHsjORw3P3yKkY05RnkYSaulWOT1gPuczs7QXJFzSP2iczwicxkQ96bLLgf78CGETkBH3yA0hictaBoPp2icgNLonCDibduf1znK5U/640?wx_fmt=jpeg&from=appmsg)

## 四、关键安全风险

攻击者通过短信监控可直接获取： 短信类双因素认证（2FA/OTP）验证码 银行、支付类告警短信 这会显著提升账户接管（ATO）与直接资金损失的风险。

## 五、典型感染链分析

标准攻击流程高度依赖 “制造紧迫感” 的诱导话术： 诱导信息制造焦虑，引导至伪装合法的下载页 用户安装恶意应用 植入程序自动回传数据至攻击者控制面板 攻击者获取： 位置历史轨迹 全量通知内容 含银行告警与 OTP 的短信记录 设备概览界面会展示：设备型号、系统版本、锁屏状态、国家地区、实时活动时间轴，帮助攻击者快速筛选高价值目标。

## 六、防御建议

安全专家建议将手机视为关键终端设备进行防护： 仅通过官方应用商店下载应用 严格限制 / 关闭侧载安装（Android 未知来源安装） 点击短信链接前务必验证真实性 优先使用 \*\* 比短信更安全的多因素认证（MFA）\*\* 方式 怀疑信息泄露后立即修改关键账号密码 警惕异常现象： 突然出现的高危权限请求 设备异常耗电、发热 未知的辅助功能 / 无障碍服务 企业用户： 部署专业移动威胁监测与响应系统 建立间谍软件分类与处置流程 及时上报安全事件，缩小损失范围 参考来源：New ZeroDayRAT Attacking Android and iOS For Real-Time Surveillance and Data Theft

### **师傅们新年快乐 马年大吉**

![image](https://mmbiz.qpic.cn/sz_mmbiz_gif/R9d0DzJpTeIj09LTicDcYY1rCAYOHD5uAkunR1hicia1HJekBPFlySp0VVIm3hl0qNuGqBF4hQtcAw6yCKGLPw6oakksIXKpdIXDyOdVPPNmiaE/640?wx_fmt=gif&from=appmsg)

image

### 抽奖活动

抽奖 给师傅们准备的金牌云电脑

- END -

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/11elNW7ftLN3SQNKn9WfR1KtGpWSIhSSIQzuUvGywS2wgGbaS0UcFricsBibCMsqFWDMicLHVX5YWck3be8AY8Ytg/0?wx_fmt=png)

响应云SRC

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/11elNW7ftLN3SQNKn9WfR1KtGpWSIhSSIQzuUvGywS2wgGbaS0UcFricsBibCMsqFWDMicLHVX5YWck3be8AY8Ytg/0?wx_fmt=png)

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