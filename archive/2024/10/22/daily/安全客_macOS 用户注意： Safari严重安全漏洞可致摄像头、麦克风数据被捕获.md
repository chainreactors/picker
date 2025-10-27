---
title: macOS 用户注意： Safari严重安全漏洞可致摄像头、麦克风数据被捕获
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787064&idx=1&sn=eb0e5b2ca525fbe78c6e915d6ca10a26&chksm=8893bad7bfe433c1b5181788c6b975e2ad01d9cb21059bb2825cf761e3b2dd2f0b245d4f7812&scene=58&subscene=0#rd
source: 安全客
date: 2024-10-22
fetch_date: 2025-10-06T18:51:32.841995
---

# macOS 用户注意： Safari严重安全漏洞可致摄像头、麦克风数据被捕获

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb4pn3G2XIc1djkYwZeBkzw72FCeURRjtia8dQUW4n5KM6BMcia0lLEg0MTfUmr1RUb7sibSeglj5dxFw/0?wx_fmt=jpeg)

# macOS 用户注意： Safari严重安全漏洞可致摄像头、麦克风数据被捕获

安全客

微软近期曝光了一项严重的安全漏洞，涉及苹果的透明度、同意和控制（TCC）框架。这一漏洞名为 HM Surf（CVE-2024-44133），攻击者可以利用它绕过用户隐私设置，访问敏感数据。苹果在 9 月 16 日对 macOS Sequoia 的更新中发布了 CVE-2024-44133 的修复。

**HM Surf 漏洞****让攻击者能在未获用户同意的情况下，轻松获取浏览器数据、摄像头、麦克风及位置信****息。**微软威胁情报团队的 Jonathan Bar Or 表示，这一漏洞的关键在于某些苹果专有应用（如 Safari）具备特殊权限，能够轻松绕过 TCC 的保护。“HM Surf 涉及移除 Safari 浏览器目录的 TCC 保护，并修改该目录中的配置文件，以获取用户的数据。”他强调，这种隐私风险让用户的安全面临严峻挑战。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb4pn3G2XIc1djkYwZeBkzw7LTWeGzDjmCfM9Hj0RQhxhrtRfRbh4h9AOOzwcAkWGVS0YOy3NGFa2g/640?wx_fmt=other&from=appmsg)

攻击者利用 HM Surf 漏洞的流程如下：

1. 更改主目录：通过 dscl 实用程序改变当前用户的主目录，无需 TCC 访问权限。
2. 修改敏感文件：在用户真实主目录下，编辑“~/Library/Safari”中的重要文件（如 PerSitePreferences.db）。
3. 恢复主目录：将主目录更改回原来的目录，迫使 Safari 使用修改后的文件。
4. 发起攻击：启动 Safari 打开网页，悄悄捕获快照和位置信息。

更可怕的是，微软表示这一攻击可以进一步扩展——攻击者甚至可以保存整个摄像头视频流或悄悄地通过 Mac 的麦克风捕获音频。

微软注意到与知名广告软件 AdLoad 相关的可疑活动，显示该漏洞可能已被恶意软件利用。Bar Or 表示：“我们观察到 AdLoad 的活动与 HM Surf 技术非常相似，但由于无法完全确认其具体步骤，我们不能确定 AdLoad 是否直接利用了这一漏洞。”

这一事件再次提醒我们网络安全的重要性。务必定期更新软件，保持警惕，保护个人隐私。**使用 macOS 系统的用户，请及时更新至最新版本，以防潜在威胁。**Bar Or 最后指出：“攻击者利用类似的方法部署普遍威胁，强调了对抗利用该技术攻击的重要性。”

文章来源：

https://www.darkreading.com/vulnerabilities-threats/macos-safari-exploit-camera-mic-browser-data

**推荐阅读**

|  |
| --- |
| **01**  ｜[关键漏洞可致](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787055&idx=1&sn=5fbaf89659bf338d051cb13fa1bf9923&chksm=8893bac0bfe433d624ae16f6ea2aac5b4e7f989baf93d651e5c5725c4a3df924fd0e735b0fb4&scene=21#wechat_redirect)[AI驱动机器人失控](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787055&idx=1&sn=5fbaf89659bf338d051cb13fa1bf9923&chksm=8893bac0bfe433d624ae16f6ea2aac5b4e7f989baf93d651e5c5725c4a3df924fd0e735b0fb4&scene=21#wechat_redirect) |
| \_ |

|  |
| --- |
| **02**  ｜[新技术绕过“noexec”，Linux执行风险激增](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787042&idx=1&sn=9ff9664f254d1077000edf4df5aeb18b&chksm=8893bacdbfe433dbddfdff5e5b5ff909029b141c9c1b7ddb9543066891e251c28569991008e3&scene=21#wechat_redirect) |
| \_ |

|  |
| --- |
| **03**  ｜[学校遭国家级黑客与勒索团伙的双重网络威胁](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787034&idx=1&sn=601d3128dda5bfa5e68dd68383a041e6&chksm=8893baf5bfe433e3ec3f75a4834085c3e9714c020268cd733fcb4f2de2390a547ffe654f9133&scene=21#wechat_redirect) |
| \_ |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4pn3G2XIc1djkYwZeBkzw7xu83YhJQs0YK3ngm9k2tpU3RqVewH3dzkz0PmX3kfe8xnjL6rXdnKA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4pn3G2XIc1djkYwZeBkzw7WSGrmBKR6ceFgsxJHWPvIIPoBZl4vu1VyJcor2Yxo2iaMGpTAMbz3MA/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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