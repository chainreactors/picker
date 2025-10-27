---
title: 基于证书的TGT请求中的异常检测
url: https://www.4hou.com/posts/qp8p
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-18
fetch_date: 2025-10-04T11:59:11.988700
---

# 基于证书的TGT请求中的异常检测

基于证书的TGT请求中的异常检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 基于证书的TGT请求中的异常检测

lucywang
[技术](https://www.4hou.com/category/technology)
2023-08-17 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)96101

收藏

导语：基于证书的TGT请求中的异常检测

![abstract_threat_actor_attribution-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798786252614.jpg "1690798786252614.jpg")

TGT 是CAS 为用户签发的登录 ticket，也是用于验证用户登录成功的唯一方式。TGT 封装了 Cookie 值以及 Cookie 值对应的用户信息，CAS 通过 Cookie 值（TGC）为 key 查询缓存中有无 TGT（TGC:TGT（key:value）），如果有的话就说明用户已经登录成。

获得对公司网络资源的未经授权访问的最复杂但最有效的方法之一是使用伪造证书进行攻击。攻击者创建这样的证书来欺骗密钥分发中心(KDC)授予对目标公司网络的访问权。此类攻击的一个示例是Shadow Credential(msDS-KeyCredentialLink属性)技术，该技术允许攻击者通过修改受害者的msDS-KeyCredentialLink属性并向其添加授权证书来登录用户帐户。这种攻击很难被检测到，因为攻击者不是窃取凭证，而是使用合法的Active Directory (AD)机制和配置漏洞。

尽管如此，缓解使用伪造证书的攻击是可能的。在分析了托管检测与响应服务MDR的数据后，研究人员确定了网络中此类攻击的几个迹象，并开发了一个能够查找AD中工件的概念验证实用程序，以及可以添加到SIEM中的一些检测逻辑规则。不过，我们有必要首先简单介绍一下基于证书的Kerberos身份验证的特点。

**AD中的Kerberos身份验证和实现过程**

在基于Active Directory的现代企业网络中，资源管理是通过Kerberos协议执行的。只有当用户能够向网络内的任何服务（对象）提供KDC颁发的票证（下图中的Msg E）时，用户才能访问该对象。发送服务票证的KDC组件称为票证授予服务器(TGS)。此外，用户只有在拥有ticket Granting ticket (TGT)(下图中的Msg B)时才会从KDC接收TGS票证。本质上，TGT是成功的用户身份验证的证明，通常虚通过密码验证。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798801920807.png "1690798801920807.png")

**Kerberos身份验证方案**

但是，有一种方法可以在不知道密码的情况下获得TGT，即使用证书。为此，KDC必须信任所提供的证书，并且该证书必须与TGT中请求的主题相关。Kerberos的这一部分称为用于初始身份验证的公钥加密(PKINIT)，如果公司网络中有为域用户颁发证书的证书颁发机构，那么设置身份验证就非常容易。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798816276610.png "1690798816276610.png")

但还有另一种方法，例如，要利用Microsoft Hello For Business功能，如基于PIN的授权或人脸识别，不过前提是登录的设备必须具有自己的AD证书，以便KDC可以基于该证书颁发TGT。但是，并非所有具有活动目录的网络都具有证书颁发机构。这就是创建msDS-KeyCredentialLink属性的原因，可以在其中编写证书。KDC将信任该证书并颁发TGT。这是一个很好的解决方案，扩展了Microsoft Active Directory的功能。

然而，基于上述逻辑，将msDS-KeyCredentialLink属性写入某个对象的主体也将能够获得该对象的票证，这就是问题所在。

**攻击是如何展开的？**

让我们举例说明一种可能的攻击场景:

1.主体logan\_howard对AD域中的任何属性都有写入权限，它使用Whisker将公钥写入域控制器对象(AD -gam$)的msDS-KeyCredentialLink属性。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798831408183.png "1690798831408183.png")

2.主体接收发送给域控制器的TGT(使用Rubeus工具包)。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798843194653.png "1690798843194653.png")

3.在提交此TGT时，主体获得TGS票证，以同步域(MS-DRSR：目录复制服务远程协议)中的密码信息。

4.作为主体，攻击者从域管理员帐户(administrator)“同步”哈希，以冒充管理员，以便获得对数据的访问权限并在公司网络内部横向移动。这种攻击称为DCSync，并使用mimikatz。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798857191611.png "1690798857191611.png")

**工件查找**

我们不关注如何让KDC信任特定的证书，包括被盗的或伪造的证书，而是关注TGT发送时的情况。这会触发域控制器上的事件4768：请求了Kerberos身份验证票证(TGT)。该事件可能包含用于身份验证证书里的工件，包含三个字段：CertIssuerName、CertSerialNumber和CertThumbprint。这些域是我们接下来要重点介绍的。

为方便起见，我们将在ELK集群的Kibana接口中处理所有事件。默认情况下，Logstash实际上知道如何将Event 4768的位字段转换为列表中特定于票证的值数组，这也使得搜索更快更顺畅。我们建议你参考官方的WinLogBeat设置指南，使用一组Docker配置来快速启动和运行你的ELK实验室。

在测试环境中，我们基于使用Whisker生成的伪造证书创建了几个TGT请求事件。下面是这些事件在测试环境中的示例：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798870170759.png "1690798870170759.png")

在MDR服务的框架内，研究人员每周观察到数十万个基于证书的票证请求事件。研究人员可以依据这些样本，分析出一些攻击模式：

攻击的很大一部分是由Microsoft Azure Active Directory的基于证书的票证请求组成的（下图中聚合的“Azure”行）。不过这些都不重要，可以使用Kibana接口中具有CertIssuerName字段值的正则表达式轻松地过滤它们。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798891443918.png "1690798891443918.png")

还有许多事件用于Microsoft Hello For Business证书(“Hello4B self gen”行)使用的证书。在这种情况下，将证书数据写入msDS-KeyCredentialLink属性，并以编程方式生成密钥(NCRYPT\_IMPL\_SOFTWARE\_FLAG)。它们通常有一个以“CN=”开头的名称和一个两位数的序列号，通常是01。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798902936342.png "1690798902936342.png")

如果计算机有一个存储在受信任的平台模块中的密钥（“TPM注册”行），那么使用该密钥的证书也可以用正则表达式来描述，因此我们对此不感兴趣。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798915771654.png "1690798915771654.png")

但最常见的情况可能是使用Microsoft证书颁发机构颁发的证书（“Windows服务器CS角色颁发”行）。可以在运行Microsoft Windows服务器版本的计算机上启用此服务。值得注意的是，如果你自己监控本地基础设施，并且不是MSSP，你会发现通过CertIssuerName值过滤掉这种情况要容易得多——您的CA服务器的名称(很可能是林中每个域的唯一名称)。实际上，即使是大型公司网络也只有相当少的CA能够颁发证书。但是，即使你是一个MSSP，为了过滤掉所有客户端PKI服务器的名称仍然不会有太大麻烦。现在来看其他领域的一些模式。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798928123202.png "1690798928123202.png")

此时，也可能存在第三方PKI实现，其证书在颁发票证时受到Kerberos服务器的信任。例如，监控时遇到了Lanaco公司开发的专业软件。

使用真实数据，让我们看看可以过滤掉哪些查询。为此，我们可以使用上述正则表达式构建以下聚合：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798941184959.png "1690798941184959.png")

卡巴斯基MDR服务中基于证书的票证请求事件的聚合

查看“Rest”行，其中包含剩余的未过滤事件(其中13个)，注意CertIssuerName字段。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798954820273.png "1690798954820273.png")

未过滤的基于证书的票证请求事件的扩展列表

**Whisker代码分析**

在如上示例中，证书是在带有默认参数的Whisker实用程序中生成的。有关生成自签名证书的过程的描述，请参阅此处。

Whisker试图将其证书作为Microsoft Hello For Business证书（在程序生成的情况下，是一对密钥）。但是，原始证书(当Windows PC独立生成证书以使用此功能时)包含一个错误：CertIssuerName字段中的可分辨名称（DA）表示法使用格式“CN=…”。攻击者的工具包没有此错误，这是可疑的。

第二和第三行可以与测试台的数据进行比较，但要在MDR产品系统中进行。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798969146470.png "1690798969146470.png")

我们可以直接向Kibana添加一个Painless脚本，该脚本可以查找CertIssuerName和TargetAccountName之间不区分大小写的匹配所导致的所有4768个事件。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798982117526.png "1690798982117526.png")

有10个这样的事件，它们都与Whisker实用程序的使用有关。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690798995288201.png "1690798995288201.png")

**使用票证标志搜索字段**

现在，让我们考虑在任意时间间隔内测试台上的事件中的winlog.event\_data.TicketOptionsDescription字段，在此期间，伪造和合法的TGT请求都会发生。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690799009379447.png "1690799009379447.png")

引人注目的是没有名称规范化标志，这在Kerberos基础设施中起着重要作用。问题是服务或帐户可以有多个主名称。例如，如果一台主机有多个名称，那么基于它的服务可能有多个服务主体名称(Service Principal names, spn)。为了使客户机不必为每个名称请求票证，KDC可以在凭据检索过程中向它提供映射信息。启用名称规范化标志时请求此功能。理论上讲，如果设置了“canonicalize”选项，KDC可以在响应和TGT中修改客户端和服务器的名称和SPN。但在发现的示例中，却没有类似标识，这很可疑。让我们找到所有使用PKINIT(基于证书)请求但却没有此标识的票证。以下是研究人员根据卡巴斯基MDR产品数据创建的请求。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690799024119794.png "1690799024119794.png")

以上是Whisker + Rubeus在测试台(AD-Gam主机)上的活动(过去30天)以及在测试ADCS设置中的一组漏洞时所做的工作，我们将其合并为ADCS ESC或Certified Pre-Owned。此外，还有一个通过证书名称过滤的误报和一个发送到客户端的事件。

让我们看看Rubeus的例子，看看为什么在票证请求中没有设置名称规范化标志。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230731/1690799037135178.png "1690799037135178.png")

事实证明，Rubeus并不是故意进行这个操作的。同样地，对于使用Kerberos的安全分析人员来说，Impacket是事实上的标准工具包。这就解释了为什么会出现上述可以现象。由于代码的简单性和流行性，这样的实用程序非常多。

**msDS-KeyCredentialLink属性**

我们可以比较两个属性：一个是在Hello for Business配置期间合法设置的，另一个是由Whisker设置的。他们之间是有区别的。在比较这些属性时，研究人员编写了一个工具，可以让你从非法属性设置中找到...