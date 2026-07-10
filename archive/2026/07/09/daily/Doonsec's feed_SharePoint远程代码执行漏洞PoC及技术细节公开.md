---
title: SharePoint远程代码执行漏洞PoC及技术细节公开
url: https://mp.weixin.qq.com/s/0W37yYHwlsnqdeK3OD85KA
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:56:31.949384
---

# SharePoint远程代码执行漏洞PoC及技术细节公开

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1IEyeZd3pfHBmMoE9cYNM5muoOlknHWibXc8S6Ra4jO96JLL6I6ZuUNgOdRaZyiayd3GO8TcJI6fWUATfsSUpFia5Wk7icmmKz7gw/0?wx_fmt=jpeg)

# SharePoint远程代码执行漏洞PoC及技术细节公开

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX1icNqSSmqBdRXZnzNEN64Nhc6y0UgB1VLptk8OOwBvO1L2iaxgv8egMRkKObahwwu5eknqrI78P1iaOkA1WdqXZRH1FvKVvEia3g4/640?wx_fmt=gif)

![文章配图](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3ZblicrPEvPABmIvWibo4AK3JzmHXGHTFwdZe0lrPhtDhicKhLIv9Fhic2W8BwLZSHnBLRDHL6n4DvVSh3KkLKJnPgywUn9vE1EUI/640?wx_fmt=png)

针对本地部署版Microsoft SharePoint Server中的高危远程代码执行（RCE）漏洞（CVE-2025-53770），研究人员现已公开概念验证（PoC）利用代码及深度技术细节。该漏洞的披露大幅提高了未打补丁的SharePoint环境遭快速武器化及大规模利用的风险。

Part01

漏洞技术分析

CVE-2025-53770是SharePoint处理特制数据源时存在的不可信数据反序列化缺陷，允许未经身份验证的攻击者通过网络执行任意代码。该漏洞影响本地部署的SharePoint Server 2016、2019及订阅版，但Microsoft 365 SharePoint Online不受影响。

微软在发布初始紧急补丁后，又推送了第二个修复补丁，新增TypeNameParserImpl组件以改变DataSet对象类型名称的解析方式，专门解决泛型类型处理问题。

Part02

PoC利用原理

越南Viettel Cyber的最新研究表明，攻击者仍可通过滥用PerformancePoint BI服务使用的ExcelDataSet控件中的XML模式处理实现RCE。攻击针对/\_vti\_bin/PPS/PPSAuthoringService.asmx终端的BIMonitoringAuthoringService网络服务，该服务暴露了用于验证数据源连接的TestConnection方法。

当传递SourceName="ExcelWorkbook"的DataSource对象至该API时，SharePoint会使用XmlSerializer将dataSource.CustomData字段反序列化为ExcelDataSet实例，随后访问ExcelDataSet.DataTable。Viettel Cyber Security发现该漏洞通过利用XML模式导入处理方式绕过XmlValidator，使非安全类型通过验证。

微软的DataSetSurrogateSelector将输入限制为"XmlSchema"和"XmlDiffGram"并运行XmlValidator以确保仅使用允许的类型。但XmlValidator仅检查主XmlSchema字符串。攻击者通过嵌入引用外部XSD的xs:import和xs:include元素，强制.NET XmlSchema预处理器从攻击者控制的HTTP服务器拉取额外模式。由于XmlValidator不检查导入的模式，外部XSD中的恶意类型定义不会被拦截。

Part03

攻击链实现

PoC利用此缺陷定义指向复杂泛型类型链的msdata:DataType，最终指向System.Web.UI.LosFormatter和System.Windows.Data.ObjectDataProvider——这两个已知的反序列化工具可在输入受控载荷时执行任意代码。攻击者构造匹配的XmlDiffGram载荷填充包含恶意com:pwn元素的行，diffgram实例化ExpandedWrapper对象后调用LosFormatter.Deserialize处理攻击者提供的数据，最终触发RCE。

运行时调用栈流经BinarySerialization.Deserialize()及从压缩base64字符串重建对象的辅助例程，最终抵达SharePoint PerformancePoint堆栈中的ExcelDataSet.get\_DataTable()、ExcelDataSourceProvider.SetDataSource()、DataSourceRegistry.GetDataSource()和ServerHelper.TestDataSourceConnection()。

Part04

实际攻击场景

PoC演示了使用低权限站点成员账户实现完整利用：攻击者首先创建SharePoint列表和项目，随后启动托管外部模式文件（如common.xsd）的HTTP服务器；构造调用TestConnection的SOAP请求，设置SourceName="ExcelWorkbook"并在CustomData字段嵌入恶意ExcelDataSet XML和diffgram；将Location ItemUrl指向以ID和人工后缀（如/sites/zdi/Lists/test/1\_.123）结尾的列表项URL以满足服务正则检查。请求处理完成后，SharePoint服务器上会生成如win32calc.exe的进程，实现可靠的远程代码执行。

Part05

安全建议

安全厂商已确认CVE-2025-53770在野利用，并观察到针对SharePoint的大规模ToolShell攻击活动。此类详细工具链和模式导入技术的公开可能加速模仿攻击。建议运行本地SharePoint的组织立即采取应急措施：应用微软最新补丁、启用AMSI集成、轮换ASP.NET MachineKey值，并对暴露服务器上可疑的PerformancePoint和ViewState活动进行威胁狩猎。

参考来源：

PoC and Technical Details Released for SharePoint Remote Code Execution Vulnerability

https://cybersecuritynews.com/poc-sharepoint-rce-vulnerability/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3y34M5GAibwcktqAsbKu2ibamWeibVrPpa709ynHMljYolGiaw7cPCyW5sCvL9sRS4lJVTOahlPKkMD7YuL5JjW6tibNyibD9QErkrc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1mP5l1EuNKhxEBfV7Pib0NBoPy1gRRFbZoBrlic0HJgw38b2H2OWOIA5oMMDrrl6KqsiaWgnrKF4a6BoqOKcgRmydooUhNqtQDOE/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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