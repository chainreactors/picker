---
title: PyPI恶意存储库fshec2攻击分析
url: https://www.secpulse.com/archives/201724.html
source: 安全脉搏
date: 2023-06-13
fetch_date: 2025-10-04T11:44:13.435101
---

# PyPI恶意存储库fshec2攻击分析

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

# PyPI恶意存储库fshec2攻击分析

[漏洞](https://www.secpulse.com/archives/category/vul)

[洞源实验室](https://www.secpulse.com/newpage/author?author_id=49765)

2023-06-12

17,334

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-1686550904.gif)

**0x00 事件背景**

PyPI（Python Package Index）**是Python官方的包索引和分发平台**。它是一个公共的、全球性的存储库，用于存储、发布和安装Python包和模块。

PyPI允许开发者将他们编写的Python代码打包为可重用的模块或库，并将其发布到PyPI上供其他开发者使用。开发者可以通过使用pip工具（Python的包管理工具）从PyPI上安装所需的模块或库。PyPI提供了一个广泛的Python包，涵盖了各种用途和领域的功能。

**0x01 事件过程**

2023年4月17日ReversingLabs公司的安全团队向PyPI团队报告了名为fshec2的恶意包。同一天该包从PyPI存储库中删除。

**0x02 技术分析**

该包安装后，会产生\_\_init\_\_.py，full.pyc，main.py三个文件。

\_\_init\_\_.py从main模块中导入load\_path函数。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-1686550905.png)

main.py中的load\_path函数通过importlib库加载full.pyc文件并将其作为模块对象，最后调用该对象的get\_path函数。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-16865509051.png)

从full.pyc的文件头中可知，该文件是3.10b版本Python编写的，部分工具如pycdc，uncompyle6无法完整的反编译出py源码。手动反编译结果如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-1686550906.png)

get\_path函数首先会根据宿主的系统决定相关的行为，**在Windows下**，该函数会向C2服务器发送自己的hostname和user信息，并且将C盘用户根目录下的目录结构发送给C2服务器。同时还会将从C2服务器上获取的commands写入本地。

随后会通过create\_windows\_task函数获取Python路径和恶意脚本路径，再使用命令：

schtasks /create /tn "{task\_name}" /tr "{python\_path} {script\_path}" /sc minute /mo {trigger\_interval} /F /RL HIGHEST /NP

添加Windows计划任务。这个命令将创建一个计划任务，定期以最高权限运行指定的 Python 脚本。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-1686550908.png)

**在Linux下**，同样会向C2服务器发送自己的hostname和user信息，随后将当前的计划任务写入到了\_\_crontabl\_default.txt文件下。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-1686550910.png)

最后会用subprocess.call添加计划任务，任务为：

\*/10 \* \* \* \* /usr/bin/python3 {file\_path\_user} >> {dir\_path}/{file\_path\_all}run.log 2>&1

含义是每隔 10 分钟执行一次 /usr/bin/python3 {file\_path\_user} 命令，并将输出结果追加到 {dir\_path}/{file\_path\_all}run.log 文件中。

send\_file函数会向C2服务器的uploads目录上传文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-1686550914.png)

通过以上的函数结合，该恶意库的攻击行为可以进化。

第一阶段会从C2下载的新的Python文件，通过其中的execute\_commands\_as\_per\_url函数进行第二阶段的payload下载。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-16865509141.png)

随后的攻击行为是多变而且可控的，由于在本文章编写的2023年6月5日，C2服务器的相关目录已删除，无法获取后续的payload，分析结束。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-1686550915.png)

**0x03 相关反应**

**2023年4月17日，**该恶意包从PyPI存储库中删除。

**2023年6月5日，**仍能从国内镜像网站上下载到该恶意包。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-1686550916.png)

**至2023年6月6日，**微步未对该IP进行标记，VirusTotal上ADMINUSLabs，CRDF，CyRadar，ESET，ESTsecurity，Kaspersky共6家安全公司对该IP进行了标记。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-16865509161.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-1686550919.png)

**0x04 事件启示**

如今，**基于第三方库的攻击事件变得非常普遍**，对于Python来说，即使PyPI对发布的软件包进行了源码检测，仍然会有一些恶意软件包能够逃脱检测并被上传。例如pyrologin、easytimestamp、discorder、discord-dev等恶意Python库，它们采用了与通用库相似的名称，导致程序员在使用pip install命令时意外安装这些恶意库，最后在调用恶意库的导出函数时进行了恶意操作。

本次的fshec2攻击示例，尽管没有采用先进的攻击技术，但它却成功地利用了pyc文件绕过了PyPI对源代码的检测以及杀毒软件的检测。这种可以简单复现的攻击手法需要引起安全相关人员和互联网公司的重视。

这种攻击手法提醒我们，**尽管PyPI等开源库平台已经采取了一系列安全措施，但我们仍然需要保持高度警惕。**作为开发者和用户，我们应该对第三方库的使用持谨慎态度，并采取一些预防措施来减少潜在的风险。具体措施如下：

* **仔细验证和核实要安装的库的来源及可信度。**确保库的作者是可信赖的，并检查库的下载来源是否是官方渠道；
* **避免在生产环境中直接安装不受信任的库。**使用库时，可以先在开发环境中进行测试和评估，确保库的功能和安全性符合预期；
* **及时更新已安装的库。**随着安全漏洞的不断发现和修复，开源库的更新版本通常会修复已知的漏洞和安全问题；
* 在使用任何第三方库之前，应仔细阅读其文档、查看其社区反馈和评价，了解库的使用方式、功能和潜在风险。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201724-1686550922.gif)

**本文作者：[洞源实验室](newpage/author?author_id=49765)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/201724.html**](https://www.secpulse.com/archives/201724.html)

Tags: [fshec2](https://www.secpulse.com/archives/tag/fshec2)、[PyPi](https://www.secpulse.com/archives/tag/pypi)、[Python](https://www.secpulse.com/archives/tag/python)、[恶意包](https://www.secpulse.com/archives/tag/%E6%81%B6%E6%84%8F%E5%8C%85)、[恶意存储库](https://www.secpulse.com/archives/tag/%E6%81%B6%E6%84%8F%E5%AD%98%E5%82%A8%E5%BA%93)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![【Python+Java】Burpsuite插件开发](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1683612811183-300x164.png)

  【Python+Java】Burpsui…](https://www.secpulse.com/archives/200103.html "详细阅读 【Python+Java】Burpsuite插件开发")
* [![WECHAT二维码闪退分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1683184162259-300x201.png)

  WECHAT二维码闪退分析](https://www.secpulse.com/archives/199777.html "详细阅读 WECHAT二维码闪退分析")
* [![CTF中RSA常见攻击方法](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678785929506-300x205.png)

  CTF中RSA常见攻击方法](https://www.secpulse.com/archives/197505.html "详细阅读 CTF中RSA常见攻击方法")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/26/494834f404f48769dcb680f30320c212-300x276.png)](https://www.secpulse.com/newpage/author?author_id=49765aaa) | [洞源实验室](https://www.secpulse.com/newpage/author?author_id=49765) | |
| 文章数：8 | 积分： 0 |
| 供应链检测中心旗下实验室，专注供应链安全、产品测评、漏洞研究、代码审计 | |

* [![阿波罗主机安全管理](/wp-cont...