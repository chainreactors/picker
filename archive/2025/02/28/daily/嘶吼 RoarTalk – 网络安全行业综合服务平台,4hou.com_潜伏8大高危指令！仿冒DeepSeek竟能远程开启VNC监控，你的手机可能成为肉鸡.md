---
title: 潜伏8大高危指令！仿冒DeepSeek竟能远程开启VNC监控，你的手机可能成为肉鸡
url: https://www.4hou.com/posts/W1vE
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-28
fetch_date: 2025-10-06T20:35:29.883994
---

# 潜伏8大高危指令！仿冒DeepSeek竟能远程开启VNC监控，你的手机可能成为肉鸡

潜伏8大高危指令！仿冒DeepSeek竟能远程开启VNC监控，你的手机可能成为肉鸡 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 潜伏8大高危指令！仿冒DeepSeek竟能远程开启VNC监控，你的手机可能成为肉鸡

安天
[技术](https://www.4hou.com/category/technology)
2025-02-27 16:23:53

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)267393

收藏

导语：安天移动安全团队通过国家计算机病毒应急处理中心的协同分析平台，发现了一批假冒DeepSeek的恶意应用程序。针对这一情况。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642382144902.jpg "1740642239428017.jpg")

近日，国产AI大模型DeepSeek（深度求索）一经推出，凭借其卓越的性能在全球范围内引发了广泛关注，与此同时也成为了不法分子聚焦的目标。安天移动安全团队通过国家计算机病毒应急处理中心的协同分析平台，发现了一批假冒DeepSeek的恶意应用程序。针对这一情况，安天移动安全团队迅速展开了深入分析和关联拓展，揭示了这些恶意应用的潜在威胁，并采取了相应的防护措施，为用户安全使用国产AI产品保驾护航。

**1．样本基本特征对比**

仿冒应用程序名、图标与正版应用别无二致，普通用户难以分辨真假。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642383511957.png "1740642205548545.png")

**2．样本详细分析**

**1# 动态分析**

恶意应用运行后直接提示更新，点击后会直接弹出安装同名恶意子包弹框请求。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642384214038.png "1740642192160273.png")

诱导用户请求启用无障碍服务。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642385494404.png "1740642181813646.png")

程序名、图标和正版基本一致，且可以同时安装于同一设备中。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642385795393.png "1740642169205585.png")

与官方正版应用比较，恶意样本运行后的界面如下，直接访问的DeepSeek的官网。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642387109363.png "1740642155170517.png")

正版DeepSeek应用如下，可以看到需要登录后才能正常使用，运行界面也不一致。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642387157045.png "1740642142187941.png")

**2# 静态分析**

该恶意应用使用了一些对抗手段来对抗逆向分析工具，增加分析难度，逃避安全检测，具体如下：

样本通过工具创建同名文件夹，对抗分析工具。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642388110781.png "1740642127245085.png")

使用伪加密修改zip文件数据的方式让工具误认为存在密码。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642389906393.png "1740642112206023.png")

使用整体自定义壳进行加固处理。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642390213146.png "1740642091107248.png")

使用类名、变量名混淆来增加分析难度。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642390492969.png "1740642075179859.png")

使用动态加载的方式加载恶意子包。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642391330617.png "1740642055153598.png")

**子包功能详细分析：**

**其关键指令解析如下：**

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642392790145.png "1740642044931076.png")

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642393680074.png "1740642034479491.png")

**主要信息获取行为如下：**
1、获取短信信息。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642394106538.png "1740641970143336.png")

2、获取通讯录。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642394342316.png "1740641958184437.png")

3、发送短信。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642395226513.png "1740641948187450.png")

4、获取应用安装列表。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642396157933.png "1740641936102364.png")

5、获取cookie。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642397169911.png "1740641926191511.png")

6、通过无障碍服务监控用户的点击、输入等行为。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642398199491.png "1740641776179563.png")

7、窃取google验证码。

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642399180413.png "1740641765687412.png")

8、VNC屏幕监控。

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642400129168.png "1740641754120391.png")

9、通过激活设备管理器和无障碍服务防卸载。

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642401152764.png "1740641721836141.png")

**3# 网址信息服务器网址如下：**

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642401209559.png "1740641711303495.png")

**3．历史溯源**

根据分析恶意木马的服务器指令特征，发现该木马与历史家族Trojan/Android.Coper的指令基本一致，如下图所示（左图为该木马，右图为Trojan/Android.Coper家族样本）。

![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642402294095.png "1740641694554325.png")

该木马家族作为长期活跃的恶意攻击威胁，于2021年7月被首次披露，安天病毒百科已经收录了该家族样本，见https://www.virusview.net/malware/Trojan/Android/Coper。该木马初期以伪装成哥伦比亚官方金融应用“Bancolombia Personas”进行传播，后续逐步扩展伪装对象至Chrome浏览器、Google Play应用商店、McAfee安全软件及DHL Mobile等全球知名应用。其攻击链通过仿冒合法程序诱导用户下载并执行恶意代码，进而实现敏感数据窃取，包括但不限于短信内容、通讯录信息及主流社交/金融应用的账户凭据，最终对受害者构成隐私泄露与资金安全的双重威胁。

**4．分析总结**

经综合分析，该恶意样本采用多层伪装机制，其主程序仿冒为DeepSeek官方应用，通过诱导性展示目标官网界面降低用户警惕性。在运行阶段，样本通过动态代码加载技术隐蔽加载恶意子包，并建立与C&C服务器的加密通信信道。恶意模块具备多维度数据窃取能力，包括：1、隐私窃取模块（短信/联系人/应用列表等）；2、界面监控模块（滥用无障碍服务权限实施屏幕内容抓取）；3、指令执行模块（支持远程指令解析，实现功能动态扩展）。攻击链中特别采用界面伪装与恶意行为分离机制，有效规避基础安全检测，最终导致用户敏感信息泄露及设备控制权限沦陷。

安天威胁情报中心已通过实时威胁狩猎系统完成覆盖该家族全量样本的检测规则部署，并联动移动终端防护体系实现安装阻断，为防范AI技术滥用场景下的新型网络威胁提供主动防御支撑。

![25.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642403103458.png "1740641643151982.png")

（相关链接：

https://virus.cverc.org.cn/#/entirety/file/searchResult?hash=E1FF086B629CE744A7C8DBE6F3DB0F68）

**5．防护建议**

1、建议从官方网站、各大手机厂商应用平台下载正版应用。

2、对与请求无障碍服务和激活设备管理器的行为提高警惕，不轻易授予相关权限。

3、在手机设置中关闭"允许安装未知来源应用"的选项。

4、定期在设置-应用管理中查看近期安装的陌生程序。

5、对设备电量异常消耗的情况予以关注。

6、养成定期使用手机管家等具有杀毒功能应用的使用习惯，及时查杀病毒。

6．关联样本

银行间谍木马：

![26.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642404147339.png "1740641611910243.png")

除此之外，通过内部大数据关联分析发现，近期除了上面提到的银行木马外，还存在其他冒用DeepSeek名义从事诈骗活动的情况，如下为部分关联样本信息：

![27.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740642404218253.png "1740641598206177.png")

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GhYVoaTs)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/10/a4d310d551660a09a8f6.jpg)

# [安天](https://www.4hou.com/member/e3QQ)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意...