---
title: 【高级持续性威胁追踪】解析APT攻击事件之软件供应链攻击
url: https://www.secpulse.com/archives/197240.html
source: 安全脉搏
date: 2023-03-10
fetch_date: 2025-10-04T09:06:09.501372
---

# 【高级持续性威胁追踪】解析APT攻击事件之软件供应链攻击

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 【高级持续性威胁追踪】解析APT攻击事件之软件供应链攻击

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-09

14,322

**概述**

供应链攻击技术是APT攻击组织常用的攻击技术之一，也是最近一些年APT攻击组织使用最多的攻击方式之一，主要针对特定的企业和用户进行定向攻击活动，供应链攻击方式多种多样，软件供应链攻击是供应链攻击当中比较主流的一种攻击方式，基于软件源代码、开源软件第三方包和软件开发工具相关等攻击都是软件供应链攻击。

基于软件源代码的攻击方式，APT攻击组织攻陷软件供应商之后，然后将恶意代码直接嵌入到软件供应商的软件代码当中，然后通过软件供应商将包含有恶意代码的软件分发给该软件供应商的企业客户，导致所有使用该软件的企业客户全部中招，这种供应链攻击方式非常隐蔽，也是危害最大的一种攻击方式，此前SolarWinds供应链攻击事件就是一种基于软件源代码的攻击方式。

基于开源软件第三方包的攻击方式，APT攻击组织利用PyPI、NPM等第三方包进行供应链攻击，这种攻击方式可以定向攻击一些大型企业的开发人员，再通过窃取这些开发人员的登录凭证等信息之后，进行后续的渗透攻击活动，渗透到企业内网，进行更隐蔽的APT攻击活动。

基于软件开发工具相关的攻击方式，APT攻击组织利用伪造的包含恶意软件的软件开发工具或者被感染了恶意代码的软件开发工具的工程项目文件，诱骗企业开发人员安装或使用这些软件开发工具和工程项目文件，安装木马后门进行下一步的攻击活动，Lazarus APT攻击组织就曾利用这种攻击方式，通过感染了恶意代码的软件开发工具的工程项目文件，定向攻击安全研究人员，此前XCodeGhost供应链攻击事件也是这种基于软件开发工具的攻击方式。

三种攻击方式中，基于软件源代码的攻击方式是最隐蔽，最难发现，也是技术难度最高的一种攻击方式，因为它需要先通过其他攻击方式对相应的软件供应商企业进行定向攻击之后，再进行后面的基于软件源代码的供应链攻击活动，同时需要确保在攻陷软件供应商之后长时间不被该供应商企业发现，这是非常难的，同时还需要向供应商相应的软件植入恶意代码，整个过程也需要做的非常隐蔽，所以这种攻击方式是很难实现的,基于开源软件第三方包和基于软件开发工具相关的软件攻应链攻击方式是相对容易实现的供应链攻击方式。

深信服蓝军APT研究团队一直致力于研究各种APT组织攻击手法TTPs等，基于一些真实的攻击事件对软件供应链攻击活动进行了深入的研究，分析了基于开源软件第三方向的攻击方式和基于软件开发工具相关的攻击方式。

**分析**

2023年1月，安全研究人员披露了某攻击者针对一款领先的流行机器学习框架PyTorch进行供应链攻击活动，PyTorch是一个流行的Python开源机器学习库，总下载量约1.8亿次，提供了广泛的工具来训练和部署机器学习模型，特别适合深度学习。

第三方包解压之后，在runtime目录下包含恶意脚本和恶意程序，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197240-1678344710.png)

通过\_\_init\_\_.py初始化脚本，启动目录下的triton恶意程序，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197240-16783447101.png)

利用PyPI第三方包进行软件供应链攻击，主要通过在PyPI第三方包程序setup.py和\_\_init\_\_.py脚本里面加入经过编码混淆过的恶意代码，相关POC工具代码，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197240-1678344711.png)

2021年1月，深信服蓝军APT研究团队披露了Lazarus APT组织通过在VS项目中设置预构建事件命令，进行基于软件开发工具相关的供应链攻击，当运行受感染的VS软件开发工具的工程项目文件之后，恶意代码会调用rundll32执行VS项目中附带的恶意64位的DLL文件，感染后的VS软件开发工具的工程项目文件，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197240-1678344713.png)

Lazarus APT组织通过上述的供应链攻击方式，目的是为了定向盗取安全研究人员的0day漏洞等，近日该攻击方式的POC被公开，深信服蓝军APT研究团队第一时间进行了跟踪分析，主要分为两步，第一步搜索vcxproj程序源文件，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197240-16783447131.png)

然后对该源文件进行感染，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197240-1678344715.png)

针对上面基于开源软件第三方包和基于软件开发工具相关的两种攻击活动，安全厂商可以针对开源软件的第三方包和软件开发工具的相关工程文件进行安全扫描，检测里面是否包含相关恶意代码特征等，同时可以检测第三方包的版本信息、描述字段等包信息特征。

**总结**

供应链攻击技术是最近几年APT组织攻击使用的最常用的攻击技术，未来随着全球云计算虚拟化等平台的高速发展，基于软件供应链攻击的活动可能会越来越多，要检测这种类型的攻击活动，不仅需要安全厂商各种安全产品，包含云(情报层面)+端(样本层面)+网(流量层面)联动，同时还需要专业的安全人员基于自己丰富安全经验才有可能发现这种高端隐蔽的APT攻击活动，事实证明，目前披露的一些高端的APT攻击组织往往在供应链攻击方面做的非常隐蔽，例如像SolarWinds这种APT攻击活动确实很难发现。

深信服蓝军APT研究团队专注全球高级威胁事件的跟踪与分析，拥有一套完善的自动化分析溯源系统以及外部威胁监控系统，能够快速精准的对 APT 组织使用的攻击样本进行自动化分析和关联，同时积累并完善了几十个 APT 以及网络犯罪威胁组织的详细画像，并成功帮助客户应急响应处置过多个 APT 及网络犯罪威胁组织攻击事件，未来随着安全对抗的不断升级，威胁组织会研究和使用更多新型的 TTP，深信服蓝军APT研究团队会持续监控，并对全球发现的新型安全事件进行深入分析与研究。

**参考链接**

`https://mp.weixin.qq.com/s/n8vqqHdzj1j_Cf_HgBTsnQ`

`https://medium.com/checkmarx-security/py-torch-a-leading-ml-framework-was-poisoned-with-malicious-dependency-e30f88242964`

`https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi`

`https://checkmarx.com/blog/how-npm-packages-were-used-to-spread-phishing-links/`

`https://blog.phylum.io/phylum-discovers-another-attack-on-pypi`

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197240.html**](https://www.secpulse.com/archives/197240.html)

Tags: [apt](https://www.secpulse.com/archives/tag/apt)、[Lazarus](https://www.secpulse.com/archives/tag/lazarus)、[供应链](https://www.secpulse.com/archives/tag/%E4%BE%9B%E5%BA%94%E9%93%BE)、[供应链攻击技术](https://www.secpulse.com/archives/tag/%E4%BE%9B%E5%BA%94%E9%93%BE%E6%94%BB%E5%87%BB%E6%8A%80%E6%9C%AF)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![6月-7月红蓝对抗实战训练营](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1688103742245-300x195.png)

  6月-7月红蓝对抗实战训练营](https://www.secpulse.com/archives/202625.html "详细阅读 6月-7月红蓝对抗实战训练营")
* [![6月-7月红蓝对抗实战训练营](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1688103742245-300x195.png)

  6月-7月红蓝对抗实战训练营](https://www.secpulse.com/archives/202471.html "详细阅读 6月-7月红蓝对抗实战训练营")
* [![6月-7月红蓝对抗实战训练营](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686118560670-300x197.png)

  6月-7月红蓝对抗实战训练营](https://www.secpulse.com/archives/201510.html "详细阅读 6月-7月红蓝对抗实战训练营")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/08/16/9f4b1a0a8978eebf651bfe827b4d307a-300x255.jpeg)](https://www.secpulse.com/newpage/author?author_id=9241aaa) | [Further\_eye ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=9241) | |
| 文章数：319 | 积分： 2105 |
| 深信服科技旗下安全实验室，致力于网络安全攻防技术的研究和积累，深度洞察未知网络安全威胁，解读前沿安全技术。 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/...