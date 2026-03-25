---
title: 朝鲜黑客滥用 VS Code 自动运行任务部署 StoatWaffle 恶意软件
url: https://hackernews.cc/archives/63942
source: HackerNews
date: 2026-03-24
fetch_date: 2026-03-25T04:16:14.948365
---

# 朝鲜黑客滥用 VS Code 自动运行任务部署 StoatWaffle 恶意软件

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用-hacker-8033977_1280](https://hackernews.cc/wp-content/uploads/2025/02/hacker-8033977_1280.jpg)

# 朝鲜黑客滥用 VS Code 自动运行任务部署 StoatWaffle 恶意软件

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-03-24](https://hackernews.cc/archives/63942 "10:44")
分类: [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
[暂无评论](https://hackernews.cc/archives/63942#respond)

* 浏览次数 204
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

“Contagious Interview”行动背后的朝鲜黑客组织（又称WaterPlum）被曝利用恶意Visual Studio Code项目传播新型恶意软件家族StoatWaffle。

自2025年12月起，该组织开始采用VS Code “tasks.json”配置分发恶意软件这一新战术。攻击利用”runOn: folderOpen”选项，每当项目文件夹在VS Code中打开时即自动触发执行。

NTT Security在上周发布的报告中指出：”该任务配置会从Vercel上的Web应用下载数据，与操作系统无关。本文虽以Windows环境为例，但核心行为在各系统上基本一致。”

下载的载荷首先检查执行环境是否安装Node.js，若未安装则从官网下载并安装。随后启动下载器，定期轮询外部服务器获取下一阶段下载器，该下载器行为相同——访问同一服务器的另一端点，将接收到的响应作为Node.js代码执行。

**StoatWaffle两大功能模块：**

* **窃密模块**：窃取Chromium内核浏览器和Mozilla Firefox中存储的凭证及扩展数据，并上传至C2服务器。若受感染系统为macOS，还会窃取iCloud钥匙串数据库。
* **远控木马（RAT）**：与C2服务器通信，获取并在受感染主机执行命令。支持切换工作目录、枚举文件目录、执行Node.js代码、上传文件、递归搜索指定目录并列出或上传匹配关键词的文件、运行shell命令及自我终止。

这家日本安全厂商表示：”StoatWaffle是基于Node.js的模块化恶意软件，具备窃密和远控两大模块。WaterPlum持续开发新恶意软件并更新现有工具。”

与此同时，该组织针对开源生态的多次攻击活动也被曝光：

* **恶意npm包**：分发PylangGhost恶意软件，系该 malware 首次通过npm包传播。
* **PolinRider行动**：在数百个公共GitHub仓库中植入混淆的恶意JavaScript载荷，最终部署BeaverTail新版本——这是Contagious Interview关联的知名窃密下载器。其中包括Neutralinojs GitHub组织的四个仓库。攻击者疑似通过恶意VS Code扩展或npm包感染受害者后，篡夺了该组织长期贡献者的GitHub账户（拥有组织级写入权限），强制推送从Tron、Aptos和币安智能链（BSC）交易中获取加密载荷的JavaScript代码，以下载运行BeaverTail。

微软本月对Contagious Interview的分析显示，攻击者通过”精心伪装的招聘流程”实现初始访问——模拟真实技术面试，最终说服受害者在评估环节运行托管于GitHub、GitLab或Bitbucket的恶意命令或包。

部分情况下，攻击者通过LinkedIn接触目标。但被选中的并非初级开发者，而是加密货币或Web3领域的创始人、CTO及高级工程师——这些人很可能拥有公司技术基础设施和加密钱包的高级访问权限。近期一起事件中，攻击者试图通过虚假面试接触AllSecure.io创始人，但未得逞。

这些攻击链部署的主要恶意软件家族包括：OtterCookie（具备广泛数据窃取能力的后门）、InvisibleFerret（Python后门）和FlexibleFerret（Go和Python双版本模块化后门）。InvisibleFerret通常通过BeaverTail投递，但近期入侵中也发现通过OtterCookie获取初始访问后直接作为后续载荷分发。

值得注意的是，FlexibleFerret又称WeaselStore，其Go和Python变体分别被称为GolangGhost和PylangGhost。

攻击者正积极改进战术：新版VS Code项目已弃用Vercel域名，改用GitHub Gist托管脚本下载执行下一阶段载荷，最终部署FlexibleFerret。这些项目同样托管于GitHub。

微软指出：”通过将恶意软件投递嵌入开发者信任的面试工具、编程练习和评估流程，攻击者利用求职者在高动机和时间压力期间对招聘流程的信任，降低其警惕性和抵抗力。”

针对VS Code任务功能的持续滥用，微软在2026年1月更新（1.109版本）中引入缓解措施：新增”task.allowAutomaticTasks”设置，默认关闭，防止打开工作区时自动执行”tasks.json”中定义的任务。

Abstract Security表示：”该更新还禁止在工作区级定义此设置，因此恶意仓库自带的.vscode/settings.json文件无法覆盖用户全局设置。1.109版本及2026年2月更新（1.110版本）还引入二次提示，在新打开的工作区检测到自动运行任务时警告用户，作为用户接受工作区信任提示后的额外防护。”

近月来，朝鲜黑客还通过LinkedIn社交工程、虚假风投公司和欺诈视频会议链接，对加密货币从业者发起协同恶意软件攻击。该活动与GhostCall和UNC1069等集群存在重叠。

MacPaw旗下Moonlock Lab表示：”攻击链最终导向ClickFix式虚假验证码页面，诱骗受害者在终端执行剪贴板注入命令。该行动跨平台设计，针对macOS和Windows分别投递定制载荷。”

美国司法部（DoJ）近日宣布对三名男子判刑——25岁的Audricus Phagnasay、30岁的Jason Salazar和35岁的Alexander Paul Travis，三人因协助朝鲜欺诈性IT工作者计划、违反国际制裁而认罪，此前均于2025年11月认罪。

Phagnasay和Salazar均被判三年缓刑及2000美元罚款，并被没收参与电信诈骗所得非法收益。Travis被判一年监禁，并没收19.3265万美元——这是朝鲜人员冒用其身份所获金额。

佐治亚州南区联邦检察官Margaret Heap在声明中表示：”这些人实际上把网络王国的钥匙交给了疑似朝鲜海外技术工作者——他们试图为朝鲜政府筹集非法资金，而这些人只是为了看似轻松的金钱回报。”

上周，Flare和IBM X-Force详细披露了该IT工作者计划的内部结构，并指出这些工作者在加入计划前需就读朝鲜顶尖大学并通过严格面试。

两家公司指出：”他们被视为朝鲜社会精英成员，已成为朝鲜政府战略目标不可或缺的部分。这些目标包括但不限于：创收、远程就业活动、窃取企业和专有信息、勒索，以及为其他朝鲜组织提供支持。”

---

**消息来源：[thehackernews.com](https://thehackernews.com/2026/03/north-korean-hackers-abuse-vs-code-auto.html)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[朝鲜](https://hackernews.cc/archives/tag/%E6%9C%9D%E9%B2%9C)[黑客](https://hackernews.cc/archives/tag/%E9%BB%91%E5%AE%A2)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用-黑客](https://hackernews.cc/wp-content/uploads/2026/02/生成特定图片-2_压缩版-210x140.png)](https://hackernews.cc/archives/63929 "FBI 警告：俄罗斯黑客在大规模网络钓鱼攻击中盯上 Signal 和 WhatsApp")

##### [FBI 警告：俄罗斯黑客在大规模网络钓鱼攻击中盯上 Signal 和 W...](https://hackernews.cc/archives/63929 "FBI 警告：俄罗斯黑客在大规模网络钓鱼攻击中盯上 Signal 和 WhatsApp")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-23

[![可用 医疗器械](https://hackernews.cc/wp-content/uploads/2026/03/可用-医疗器械-210x140.jpg)](https://hackernews.cc/archives/63734 "医疗科技巨头 Stryker 遭伊朗关联擦除式恶意软件攻击后全球系统下线")

##### [医疗科技巨头 Stryker 遭伊朗关联擦除式恶意软件攻击后全球系...](https://hackernews.cc/archives/63734 "医疗科技巨头 Stryker 遭伊朗关联擦除式恶意软件攻击后全球系统下线")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-12

[![可用-黑客](https://hackernews.cc/wp-content/uploads/2025/08/cybercrime-8878481_640-210x140.png)](https://hackernews.cc/archives/63619 "俄罗斯黑客试图在全球范围内攻破 Signal、WhatsApp 账号")

##### [俄罗斯黑客试图在全球范围内攻破 Signal、WhatsApp 账号](https://hackernews.cc/archives/63619 "俄罗斯黑客试图在全球范围内攻破 Signal、WhatsApp 账号")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-10

[![anonymous-7121611_可用](https://hackernews.cc/wp-content/uploads/2025/02/anonymous-7121611_可用-210x140.jpg)](https://hackernews.cc/archives/63546 "与伊朗相关的 MuddyWater 组织针对美国机构部署 Dindoor 恶意软件")

##### [与伊朗相关的 MuddyWater 组织针对美国机构部署 Dindoor 恶意软件...](https://hackernews.cc/archives/63546 "与伊朗相关的 MuddyWater 组织针对美国机构部署 Dindoor 恶意软件")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-09

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team