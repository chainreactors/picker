---
title: ROADtools：微软云环境渗透与审计的实用框架
url: https://mp.weixin.qq.com/s/CYa6nIUZmiZIYciGeLUCYg
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:05:29.266258
---

# ROADtools：微软云环境渗透与审计的实用框架

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibeqk2pxwNEz8r6FvUIK8YIxIKCU9cnZtAK2JVH3gSTEMb2ylicesOYICQg2DgnWgYBibWwCmPabOia3Z4xJubHibZ1aFj4XiaaYj0Yk/0?wx_fmt=jpeg)

# ROADtools：微软云环境渗透与审计的实用框架

原创

工具党
工具党

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> ROADtools是一套用于探测和分析微软Azure AD (Entra ID)环境的工具集，包含信息收集工具ROADrecon和令牌操作工具roadtx。它能帮助红队蓝队从离线数据库中深度挖掘用户、权限和策略。无论你是想模拟攻击路径，还是审计自家云环境，这套工具都值得一试。

## 01 它到底是什么？

说简单点，ROADtools是你的Azure AD探索工具箱。这个名字很有意思，“Rogue Office 365 and Azure (active) Directory tools”直译过来就是“流氓版Office 365和Azure AD工具”，暗示了它在红蓝对抗中的特殊定位。

整个框架基于Python 3.7+，分为三个核心部分：

* **ROADlib**

  ：基础库。处理与Azure AD的认证，负责操作包含ROADrecon数据的数据库。它的数据库模型直接根据Azure AD内部API的元数据定义自动生成，跟官方保持同步。
* **ROADrecon**

  ：侦察尖兵。主打信息收集，能把目标Azure AD里的几乎所有数据都扒下来，存到本地数据库里慢慢分析，还带一个图形界面。
* **roadtx**

  ：令牌大师。专门玩转Azure AD颁发的各种令牌，支持多种认证流程、设备注册和主刷新令牌相关操作。

## 02 ROADrecon：你的离线情报数据库

这是整个套件里最出名的工具，能干这么几件事：

* 自动生成数据库模型：利用官方的元数据，在本地创建一个SQLAlchemy支持的数据库。
* 异步爬取数据：用Python批量发起请求，把Azure AD图(Graph)里能找到的东西一股脑儿全存到本地。
* 多种分析方式：既可以通过插件查询数据库输出报告，也能在一个功能全面的网页界面里直接挖掘数据。

它的新版界面（ROADrecon UI NG）基于Vite+VueJS+PrimeVue重写了，性能更好，还加了策略详情页这样的实用功能。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibc5H4p1iadcjWbPIfRKFWVtPibHJpuenEM2icI6oLWgyZOTiaYKQDNicDTaSLYuAnjnZuOjI96iba6liaYVgSWzaAsbmIC5zkXdLUvPO8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdpcZgYxaRpg0hV90Jr1sxQNYUjiaERbhwjaMwiblyxvYdzqgnktwwHUSqNFzricFkv0JyUN7y9WElcfAqQYNS62geUnnusfGDhIg/640?wx_fmt=png&from=appmsg)

▲ ROADrecon新版界面与策略详情页

## 03 如何把它装起来

安装方法有好几种，挑你顺手的来。

### Docker方式（最省心）

如果你想快速体验新版图形界面，直接上Docker。

cd roadrecon
# 把roadrecon.db文件也复制到roadrecon/目录下
sudo docker-compose up -d

完事之后，浏览器打开`http://localhost:5173`就能看到界面了。注意，新版后端端口是5000，不直接提供旧版UI了。

### Pip安装（传统方式）

如果你喜欢自己掌控一切，可以克隆代码后用pip安装。

cd roadrecon
pip install .
# 或者用pipx
pipx install git+https://github.com/synacktiv/ROADtools --include-deps

装好后，运行`roadrecon gui`命令启动服务。这个方式启动的服务默认在5000端口，用的是旧版界面构建。

### 从GitHub直接装“最新构建”

项目每次提交到master分支，都会通过Azure Pipelines自动打包。你可以去构建产出页面（见）下载打包好的`.whl`或`.tar.gz`文件，直接pip安装就行。

pip install roadlib/
pip install roadrecon/

如果打算二次开发，可以用`pip install -e`进行可编辑模式安装。

## 04 roadtx：专治各种令牌难题

如果说ROADrecon是看的，那roadtx就是干的。它能在不同类型的Azure AD令牌之间进行交换，并模拟使用它们。

比如，你手头有一个某种方式获取到的访问令牌，想看看它能不能换成其他资源服务的令牌，或者你想研究主刷新令牌(PRT)在各种场景下的行为，roadtx就能派上用场。它支持的流程挺全，具体怎么用，项目Wiki里写得很详细。

安装方法和ROADrecon类似，确保Python版本≥3.7。

# 从源码安装
pip install roadlib/
pip install roadtx/

## 05 优点和需要注意的地方

先说好的方面。

ROADrecon最厉害的是它的“离线分析”能力。把整个环境数据拖下来，慢慢翻，不用担心触发告警或者请求限制。图形界面做得很直观，比纯命令行友好得多。新版前端性能提升明显，处理大型数据库时后端分页很实用。

roadtx则填补了一个工具空白，把Azure AD令牌那些复杂的操作封装成了命令行，对研究认证流程帮助很大。

再讲讲用的时候要留神几点。

权限是首要问题。要收集数据，你用的账号得有相应的Azure AD API读取权限。在真实对抗或红队评估中，怎么拿到一个有足够权限的初始立足点，本身就是个挑战。

数据量可能很大。全面收集一个大型企业的Azure AD数据，会生成庞大的数据库，对本地存储和分析能力有一定要求。

此外，这只是个信息收集和令牌操作框架。它帮你看到风险和路径，但具体的攻击利用需要结合其他知识和工具。而且，在正式生产环境里瞎跑之前，最好在测试环境里先折腾明白。

## 06 适合谁用？

红队成员肯定喜欢它。用来进行Azure AD环境内部侦察，摸清用户关系、应用程序、服务主体和权限分配，规划横向移动路径。

蓝队和安全运维用它来做云端配置的日常审计和基准检查。定期拉取一份数据下来，看看和上次相比有什么变化，有没有多出什么可疑的应用或过高权限。

渗透测试人员在面对微软云环境时，它能极大提升信息收集效率。

说实话，这套工具的学习曲线不算特别陡峭，尤其有了图形界面之后。如果你是微软云安全方向的新手，跟着Wiki一步步操作，是理解Azure AD复杂内部结构的一个非常直观的方法。

项目作者是Dirk-jan Mollema，在Azure AD安全领域研究很深。工具本身也在持续更新，由Synacktiv的开发者维护着新的前端界面，用起来比较踏实。

---

获取方式：回复“ROADtools”获取

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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