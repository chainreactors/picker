---
title: 重磅预警！140+AI开源包集体投毒，朝鲜APT组织BlueNoroff利用npm供应链窃取钱包密钥、企业全量凭证
url: https://mp.weixin.qq.com/s/_spAvvhiz7mNUuNA5MVK6g
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:46:27.668653
---

# 重磅预警！140+AI开源包集体投毒，朝鲜APT组织BlueNoroff利用npm供应链窃取钱包密钥、企业全量凭证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/E3ZvvAXyiaibkaVLByYN8rSwg98DrGeQg38qoXFgTcoEyLSsbiajfZEbiaCou3MaYoP6ia80HRHvNTCt7XDo1QlYyXcDOx7yPVGN2J69S4C0ELdc/0?wx_fmt=jpeg)

# 重磅预警！140+AI开源包集体投毒，朝鲜APT组织BlueNoroff利用npm供应链窃取钱包密钥、企业全量凭证

原创

AI紫队安全研究
AI紫队安全研究

AI紫队安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**大家好，我是AI紫队安全研究。建议大家把公众号“AI紫队安全研究”设为星标，否则可能就无法及时看到啦！因为公众号只对常读和星标的公众号才能大图推送。操作方法：先点击上面的“AI**紫队安全研究**”，然后点击右上角的【...】,然后点击【设为星标】即可。**

**关注视频号 “**AI紫队安全研究**” 不定期周五晚上10点直播。**

![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibm5ST4jPia8NgU4pyGZrVs1laQPXCQ706kggJFR37t0sAJbVnP4B0K75bwicEic7FmZIoSNaefEII7RUu9d747zFdolPgpGcMnKvs/640?wx_fmt=png&from=appmsg)

导语

不用漏洞、不用钓鱼邮件，只要你执行一句`npm install`，后台静默触发多层远控木马。微软6月最新安全报告曝光重大供应链灾难：朝鲜APT组织Sapphire Sleet攻陷Mastra AI全套npm账号，批量污染140+官方开源包，搭配仿冒热门库easy-day-js实施跨平台窃密，Windows/macOS/Linux全沦陷，开发密钥、云Token、加密钱包一键打包外传，大量AI公司、Web3团队中招。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaiblAic1Z4szs2w9uiaTurX4FGmVFHzpWeH7RQ3vMzfRJTAlxBSu0ianJnXZvNXaZiafH3dMXpziawGKiahBBnRVrr6Xl6tqGSmZ8CJiac0/640?wx_fmt=png&from=appmsg)

一、攻击者背景：国家级APT，专攻金融与Web3赛道

本次幕后团伙Sapphire Sleet（又称BlueNoroff、CryptoCore），长期由境外国家力量支撑，核心目标：加密货币私钥、金融机构内部数据、科技企业开发凭证。

过往作案记录：

1. 2026年4月篡改Axios主流HTTP库，实施大规模供应链投毒；

2. 常年针对交易所、VC、AI初创公司、Web3项目定向渗透；

3. 入侵后不仅窃取数据，还长期潜伏留后门，反复搜刮资产。

本次攻击是其标准化供应链猎杀流程，成熟度远超普通黑产。

二、完整攻击流程：五步无声入侵，开发者毫无察觉

第一步：劫持官方维护账号，掌握发包权限

黑客窃取Mastra项目核心发布账号`ehindero`，该账号拥有全系列`@mastra`包发布权限。此前所有版本均通过GitHub Actions自动化发布，攻击者改用匿名邮箱手动发包，留下异常痕迹。

第二步：制作仿冒恶意包 easy-day-js（拼写劫持Typosquat）

瞄准全球周下载5700万+的dayjs日期库，注册近似包名easy-day-js：

封面文档、作者信息、Github地址完全复制原版，肉眼无法区分；

分两阶段投放：v1.21纯干净诱饵无恶意代码，降低平台风控；

v1.22新增`postinstall`自动执行脚本setup.cjs，安装即运行木马。

第三步：140+官方AI包批量植入恶意依赖

攻击者篡改全部Mastra套件package.json，强制写入`easy-day-js^1.11.21`模糊版本号。

只要开发者更新、拉新项目依赖，npm会自动解析到带毒1.22版本，不需要你手动引入恶意包，间接依赖自动投毒。

第四步：安装瞬间触发多层解密载荷

执行npm install时自动运行混淆脚本，动作包括：

1. 关闭Node证书校验，所有HTTPS通信不验证证书，方便连接黑客C2；

2. 写入隐藏追踪文件到系统临时目录，记录本机所有项目路径；

3. 远程拉取41KB跨平台远控核心程序，内存加载、不落地文件规避杀毒。

第五步：全系统搜刮+永久驻留，长期监控

远控木马落地后两大核心危害：

1. 全域数据窃取

遍历浏览器Chrome/Edge/Brave所有加密钱包（MetaMask、Coinbase等）、历史记录、系统环境变量、Git Token、SSH私钥、数据库密码、云API密钥；

2. 多渠道持久化，重启也逃不掉

Windows：注册表Run项伪装Nvm工具开机启动；

macOS：LaunchAgent伪装Node服务；

Linux：system后台常驻单元；

3. 二次植入PowerShell深层后门，获取系统最高SYSTEM权限，可远程执行任意命令、植入服务级木马，清除杀毒日志。

三、本次攻击3个恐怖关键点，所有开发务必警惕

1. 间接依赖藏毒，自查极难

你项目里没直接写easy-day-js，但Mastra全套AI工具自带该依赖，大量AI大模型开发、本地知识库项目全部中招，很多团队几周后才发现异常外联。

2. 跨平台无差别渗透，Windows/mMac/服务器全中

不管本地开发机、CI/CD流水线、线上服务器，只要执行npm安装就触发后门，企业自动化构建环境风险最高，流水线密钥极易泄露。

3 无痕内存执行，主流EDR很难拦截

载荷大量使用字符串混淆、Base64置换、XOR加密，全程内存反射注入，不落地恶意exe，传统文件查杀失效，只能监控异常Node外联行为。

四、高危人群自查清单（中一条立刻排查）

1. 项目使用任何`@mastra`系列AI工具，版本>=1.13.1；

2. 本地/服务器近期更新过Mastra依赖；

3 开发环境存有加密钱包、云服务器密钥、数据库凭证；

4 企业CI/CD流水线自动拉取npm第三方开源包；

5 前端、AI、Web3开发团队，长期批量更新依赖。

五、立刻执行！4套分级处置方案

【紧急止损：已经使用Mastra 1.13.1及以上】

1. 删除全局&项目node\_modules、lock锁文件，彻底清理npm缓存；

2. 降级Mastra至1.13.0安全版本，package.json锁定固定版本，禁用^模糊符号；

3. 全网检索项目中easy-day-js依赖，全部删除；

4. 全量轮换所有密钥：Git、云厂商、数据库、钱包私钥优先转移资产。

【开发环境长期防护】

1. 安装脚本强制禁用：全局配置`npm config set ignore-scripts true`，杜绝postinstall自动执行；

2 生产/CI统一使用`npm ci`而非npm install，严格按照lock文件安装，禁止自动升级；

3 引入依赖安全扫描工具（Snyk/Lockfile-lint），每次提交检测恶意第三方包。

七、总结：供应链攻击不再是小事

过去大家觉得供应链投毒离自己很远，只会挖矿、弹窗广告。但Sapphire Sleet这类国家级APT的出现，彻底改写风险等级：

攻击者有充足人力、情报资源，长期埋伏开源项目，利用开发者“信任官方包”的心理，悄无声息掏空企业核心资产与个人加密财富。

AI、Web3、前端团队作为npm重度使用者，必须把依赖安全纳入日常流程，不要等密钥、钱包被盗后再补救。

转发给身边前端、AI开发同事，自查项目依赖，守住开发环境第一道防线！

**加入知识星球，可获取权益**

一、"全球高级持续威胁：网络世界的隐形战争"，总共26章，为你带来体系化认识APT，欢迎感兴趣的朋友入圈交流。

![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibnCqpgXqJOeTYYNKJPrdb9IibicQrF8SfJJOPkxn9NqBXGBtnZzdwicBfxUibFa0gsq2k0jReSITKceuu0NtEtQeCy0QkVDxWuVeL8/640?wx_fmt=png&from=appmsg)

二、为什么加入？

职场瓶颈期找不到突破方向？安全项目落地缺成熟方案？面对APT攻击、勒索病毒不知如何构建防御体系？

三、在这里，你能获得的不只是资料包，而是直接对接行业专家的「私人顾问服务」

✅ 职业发展「精准导航」

 1v1简历优化：针对安全岗（渗透测试/安全运营/合规等）拆解JD，突出核心竞争力；

 晋升避坑指南：从工程师到安全负责人，分享晋升路径，避开「技术强但管理弱」的晋升陷阱；

 技能栈规划：根据你的基础（应届生/3年经验/资深专家）定制学习路线，比如从0到1学SOC安全建设、APT威胁狩猎。

✅ 安全方案「对症开方」

 实战方案库：含医疗/制造业/等行业的勒索防御、数据安全合规、供应链安全加固方案（附落地工具清单+成本测算）；

 架构设计咨询：小到EDR选型，大到零信任体系搭建，提供「预算效果」平衡的最优解（已帮10+企业节省40%防护成本）。

✅ 圈子资源「直接对接」

 大厂安全负责人拆解真实案例（如某支付公司攻防对抗的实战复盘）；

四、适合谁？

 想突破职业天花板的安全工程师/架构师；

 需快速落地安全项目的企业负责人；

 关注行业动态的安全爱好者或IT从业人员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibkJsTBMez9zJVBx2GkJZX37f7O4FrIibRh5t4A452yETKicDN4YVqlC8IFp7j3rb1FtERwaHNkNFWq93j1mMPnGemzXIv4NGaUSU/640?wx_fmt=png&from=appmsg)

**喜欢文章的朋友动动发财手点赞、转发、赞赏，你的每一次认可，都是我继续前进的动力。**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

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