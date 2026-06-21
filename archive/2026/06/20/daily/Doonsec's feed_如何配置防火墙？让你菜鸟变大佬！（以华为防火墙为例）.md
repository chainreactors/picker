---
title: 如何配置防火墙？让你菜鸟变大佬！（以华为防火墙为例）
url: https://mp.weixin.qq.com/s/qng9MxZKH4dJcNBy5tKrjA
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:46:45.047924
---

# 如何配置防火墙？让你菜鸟变大佬！（以华为防火墙为例）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj56EJskjRLhhgW0j8Zq9q7ANZp25uzLcu3wur0DJx2snxfic9tOicx6KzJU50foy3doEu2hibqw0HsRtL4j8RyVcu3YR15FLa6hXzM/0?wx_fmt=jpeg)

# 如何配置防火墙？让你菜鸟变大佬！（以华为防火墙为例）

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNib8S8XGVBsfkW3Mfr0TZbHVtJqqhM7QZ4oGHjZic2DhF6QMZRON0Old9Q/640?wx_fmt=gif&randomid=m98ag9ab#imgIndex=0)

**2026**

**关注我们**

**01**

**了解防火墙基本机制**

配置防火墙之前请了解防火墙基本工作机制。

**1.1  什么是防火墙**

防火墙是一种网络安全设备，通常位于网络边界，用于隔离不同安全级别的网络，保护一个网络免受来自另一个网络的攻击和入侵。这种“隔离”不是一刀切，是有控制地隔离，允许合法流量通过防火墙，禁止非法流量通过防火墙。

如图1-1所示，防火墙位于企业Internet出口保护内网安全。在防火墙上可以指定规则，允许内网10.1.1.0/24网段的PC访问Internet，禁止Internet用户访问IP地址为192.168.1.2的内网主机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibUibMIibgic5Ribcwvh0kkBsiaY4ezI5erDaq3BF2XK0WO8EmhfroawRHwyw/640?wx_fmt=png&randomid=a8myfcew#imgIndex=1)

*图1-1 防火墙控制流量转发*

由上文可见，防火墙与路由器、交换机是有区别的。路由器用来连接不同的网络，通过路由协议保证互联互通，确保将报文转发到目的地；交换机通常用来组建局域网，作为局域网通信的重要枢纽，通过二层/三层交换快速转发报文；而防火墙主要部署在网络边界，对进出网络的访问行为进行控制，安全防护是其核心特性。路由器与交换机的本质是转发，防火墙的本质是控制。

防火墙控制网络流量的实现主要依托于安全区域和安全策略，下文详细介绍。

**1.2 接口与安全区域**

前文提到防火墙用于隔离不同安全级别的网络，那么防火墙如何识别不同网络呢？答案就是安全区域（Security Zone）。通过将防火墙各接口划分到不同的安全区域，从而将接口连接的网络划分为不同的安全级别。**防火墙上的接口必须加入安全区域（部分机型的独立管理口除外）才能处理流量。**

安全区域的设计理念可以减少网络攻击面，一旦划分安全区域，流量就无法在安全区域之间流动，除非管理员指定了合法的访问规则。如果网络被入侵，攻击者也只能访问同一个安全区域内的资源，这就把损失控制在一个比较小的范围内。因此建议通过安全区域为网络精细化分区。

接口加入安全区域代表接口所连接的网络加入安全区域，而不是指接口本身。接口、网络和安全区域的关系如图1-2所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibPZp2fCJt7ibia6UubbeJFuwDibx4TpBAChmKar4S54kkdhXNeOmIjEXsA/640?wx_fmt=png&randomid=u1inhksh#imgIndex=2)

*图1-2 接口、网络和安全区域*

防火墙的安全区域按照安全级别的不同从1到100划分安全级别，数字越大表示安全级别越高。**防火墙缺省存在trust、dmz、untrust和local四个安全区域，管理员还可以自定义安全区域实现更细粒度的控制。**例如，一个企业按图1-3划分防火墙的安全区域，内网接口加入trust安全区域，外网接口加入untrust安全区域，服务器区接口加入dmz安全区域，另外为访客区自定义名称为guest的安全区域。

一个接口只能加入到一个安全区域，一个安全区域下可以加入多个接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibarxGmergiaP7LicKSAFuNYepSicDbwr5phcvCdPicQtmDiapd8XyTeZtF8g/640?wx_fmt=png&randomid=0z00hdgc#imgIndex=3)

*图1-3 划分安全区域*

上图中有一个特殊的安全区域local，安全级别最高为100。local代表防火墙本身，local区域中不能添加任何接口，但防火墙上所有接口本身都隐含属于local区域。凡是由防火墙主动发出的报文均可认为是从local安全区域发出，凡是接收方是防火墙的报文（非转发报文）均可认为是由local安全区域接收。

另外除了物理接口，防火墙还支持逻辑接口，如子接口、VLANIF、Tunnel接口等，这些逻辑接口在使用时也需要加入安全区域。

**1.3  安全策略**

前文提到防火墙通过规则控制流量，这个规则在防火墙上被称为“安全策略”。安全策略是防火墙产品的一个基本概念和核心功能，防火墙通过安全策略来提供安全管控能力。

如图1-4所示，安全策略由匹配条件、动作和内容安全配置文件组成，针对允许通过的流量可以进一步做反病毒、入侵防御等内容安全检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibIVsJ4WImMxawL0V6rpgQ2Yacy1kPOHvNZaFgdYflVIoXatYe8YRoHg/640?wx_fmt=png&randomid=9ki9w7mo#imgIndex=4)

*图1-4 安全策略的组成及Web界面*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibkPpB0FYGnGQqbFMhKAAjoHqnJXGuPgYke4FQ2oAThkZxjkibZsRW4Cg/640?wx_fmt=png&randomid=7prap4ii#imgIndex=5)

所有匹配条件在一条安全策略中都是可选配置；但是一旦配置了，就必须全部符合才认为匹配，即这些匹配条件之间是“与”的关系。一个匹配条件中如果配置了多个值，多个值之间是“或”的关系，只要流量匹配了其中任意一个值，就认为匹配了这个条件。

一条安全策略中的匹配条件越具体，其所描述的流量越精确。你可以只使用五元组（源/目的IP地址、端口、协议）作为匹配条件，也可以利用防火墙的应用识别、用户识别能力，更精确、更方便地配置安全策略。

**穿墙安全策略与本地安全策略**

穿过防火墙的流量、防火墙发出的流量、防火墙接收的流量均受安全策略控制。如图1-5所示，内网PC既需要Telnet登录防火墙管理设备，又要通过防火墙访问Internet。此时需要为这两种流量分别配置安全策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibsdSf8GZNDPvVuhNCVckYHH1ELibiar0wyzjMm4gP0oLwDuW5yqNibU88w/640?wx_fmt=png&randomid=84j4gjz2#imgIndex=6)

*图1-5 穿墙安全策略与本地安全策略*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibH8xhz05ezZlCNNyAbXEJSAiafgRN02arhVu3dLib2mk8Y85LicckATTrQ/640?wx_fmt=png&randomid=hzmmcf4r#imgIndex=7)

*表1-1 穿墙安全策略和本地安全策略配置*

尤其讲下本地安全策略，也就是与local域相关相关的安全策略。以上例子中，位于trust域的PC登录防火墙，配置trust访问local的安全策略；反之如果防火墙主动访问其他安全区域的对象，例如防火墙向日志服务器上报日志、防火墙连接安全中心升级特征库等，需要配置local到其他安全区域的安全策略。记住一点防火墙本身是local安全区域，接口加入的安全区域代表接口连接的网络属于此安全区域，这样就可以分清防火墙本身和外界网络的域间关系了。

**缺省安全策略与安全策略列表**

防火墙存在一条缺省安全策略default，默认禁止所有的域间流量。缺省策略永远位于策略列表的最底端，且不可删除。

用户创建的安全策略，按照创建顺序从上往下排列，新创建的安全策略默认位于策略列表底部，缺省策略之前。防火墙接收到流量之后，按照安全策略列表从上向下依次匹配。一旦某一条安全策略匹配成功，则停止匹配，并按照该安全策略指定的动作处理流量。如果所有手工创建的安全策略都未匹配，则按照缺省策略处理。

由此可见，安全策略列表的顺序是影响策略是否按预期匹配的关键，新建安全策略后往往需要手动调整顺序。

企业的一台服务器地址为10.1.1.1，允许IP网段为10.2.1.0/24的办公区访问此服务器，配置了安全策略policy1。运行一段时间后，又要求禁止两台临时办公PC（10.2.1.1、10.2.1.2）访问服务器。

此时新配置的安全区策略policy2位于policy1的下方。因为policy1的地址范围覆盖了policy2的地址范围，policy2永远无法被匹配。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibvzG7KBIBu5gjHjHahhyK7IvfyQqCx1DzA2BlUfW8FusyeiadBQtn5xw/640?wx_fmt=png&randomid=hx3xmalv#imgIndex=8)

需要手动调整policy2到policy1的上方，调整后的安全策略如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibFqRdXoR4kVYFWWic6Qia4I52VXcWtnIjxPR8w7l76ZicibNYJ7mWJ7xltw/640?wx_fmt=png&randomid=tfenq9dq#imgIndex=9)

因此，配置安全策略时，注意先精确后宽泛。如果新增安全策略，注意和已有安全策略的顺序，如果不符合预期需要调整。

**02**

**完成初始配置**

首次使用设备，完成防火墙接入互联网的基础配置。

**2.1  设备出厂配置**

防火墙设备出厂配置如下表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibCOcdiaiaaicYlJFWI0jaDqmLLaZ0o8Pu0kDZWDvWgBfuKKrZGOQeZRU8Q/640?wx_fmt=png&randomid=bie7xl2c#imgIndex=10)

*表 2-1 防火墙出厂配置*

**2.2  连线**

按下图连接管理网口、内网口GE0/0/2和外网口GE0/0/3。图中管理PC与设备管理网口连接，用于登录Web界面。如果使用命令行配置，首次登录请使用Console配置线连接管理PC的串口与设备的Console口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNib9diaCh5mdQjAknDOsCjqMJQca6ob4GwXndDHR3urQuzn25Pl5KrxkHA/640?wx_fmt=png&randomid=ebc4gm6k#imgIndex=11)

*图1-6 防火墙线缆连接*

**2.3  登录Web界面**

**背景信息**

推荐使用以下浏览器登录设备Web界面：

* Internet Explorer浏览器：10-11
* Firefox浏览器：62及以上版本
* Chrome浏览器：64及以上版本

**操作步骤**

1.  将管理员PC网口与设备的管理口（MEth 0/0/0或GigabitEthernet 0/0/0）通过网线直连或者通过二层交换机相连。

2.  将管理员PC的IP地址设置为192.168.0.2～192.168.0.254范围内的IP地址。

3.  在管理员PC的浏览器中输入地址：https://192.168.0.1:8443。

输入地址登录后，浏览器会给出证书不安全的告警提示，选择继续浏览。

4.  如果是首次登录设备，弹出创建管理员帐号界面。输入用户名、密码、确认密码，然后单击“创建”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNib25scbTP4KL0hm2S02tV3zjQGYJEKHBHMrhUsttlcBicYdlIBrwOnDEQ/640?wx_fmt=png&randomid=8fhc0ptu#imgIndex=12)

首次登录创建的管理员，拥有系统管理员权限和Web服务类型。

5.  帐号创建成功，在弹出的提示框中单击“确定”。

6.  进入登录界面，输入已经创建的用户名、密码登录设备，单击“登录”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibb5C62SOLTdcul1SQkPX6NEZiclP99snJQWZ4SNtTHQRCktZWiaSjjLvw/640?wx_fmt=png&randomid=whdn242j#imgIndex=13)

访问Web界面登录地址时，浏览器无法验证设备提供的默认证书，会有安全告警提示。可以在此界面上单击“下载根证书”下载证书，然后双击证书文件进安装，下次登录就没有安全告警提示了。

7.  新帐号首次登录，系统弹出修改初始化密码界面。输入当前密码、新密码、确认密码，单击“确定”。

8.  重新进入登录界面，输入帐号和新密码，单击“登录”。

**2.4  防火墙Web界面**

防火墙Web界面采用横向板块+竖向菜单的导航方式，界面布局如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibyAib6o3mbwzzmdw0TgKnoAJgfib1qU7L6v1Xd4pGv8h0dhhicdWG5cIkQ/640?wx_fmt=png&randomid=eyc8g726#imgIndex=14)

*图1-7 Web界面布局*

**后续处理**

* 选择“网络 > 接口”，可以修改管理口的IP地址，修改后需要重新登录。
* 选择“系统 > 管理员 > 管理员”，可以新建其他管理员。防火墙支持管理员绑定不同的权限角色。

**2.5  配置三层接入**

防火墙缺省工作在三层，通常作为企业Internet出口网关，实现内外网通信的同时进行安全防护。此种模式设备通过路由协议转发各个网段之间的报文。因此，这种接入方式也被称为“路由模式”。

防火墙三层接入部署在内外网之间时，通常还需要负责内网的私网地址与外网的公网地址之间的转换，也就是NAT功能，因此这种接入方式又常被称为“NAT模式”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNibnylVLmFcR28W4PA9VYAzIBAqebN5pSMv1h36Zo572ibyzc7cv3k725A/640?wx_fmt=png&randomid=cybsenov#imgIndex=15)

*图1-8 防火墙三层接入组网图*

初始接入时，请使用Web界面提供的快速向导，根据企业的Internet接入方式将防火墙快速接入Internet。然后在此基础上进行高级配置。

* **静态IP：**如果从网络服务商处获得固定的IP地址，请选择此接入方式。
* **PPPoE：**如果从网络服务商处获得用户名和密码进行拨号，请选择此接入方式。
* **DHCP：**如果从网络服务商自动获取IP地址，请选择此接入方式。

**执行快速向导后，防火墙具备的基本配置如下：**

* **上网接口：**加入untrust区域，并通过管理员选择的接入方式获取到公网IP地址。
* **局域网接口：**加入trust区域，私网IP地址配置完毕；如果管理员在向导中启用了局域网DHCP服务，则局域网接口开启DHCP服务器功能为局域网PC分配IP地址及DNS服务器地址。
* **源NAT：**存在一条Easy IP方式的源NAT策略，出接口是上网接口的所有流量的源IP地址被转换为上网接口IP地址。
* **路由：**存在一条缺省路由，出接口是上网接口，将流量转发至Internet。
* **安全策略：**未配置，需要自行手工配置安全策略，允许局域网用户访问Internet。

**使用三层Internet接入向导：静态IP**

**数据准备**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaHEoHjs2BuD14ibhOVdveGjqfNDjSaeNib92rnHjJJribSiauicNDfKOLDyky54xia6icmE4EUAJ8gGRyqR8QWdk3Mmzw/640?wx_fmt=png&randomid=yuvpn9nz#imgIndex=16)

**操作步骤**

1.  选择“系统 > 快速向导”。

2.  单击“下一步”。

3.  根据需要修改主机名、管理员密码，然后单击“下一步”。如果无需修改，单击“跳过”。

4.  根据设备的所在地配置系统时间，然后单击“下一步”。

5.  选择接入互联网方式为“静态IP”，然后单击“下一步”。

6.  配置接入互联网参数，然后单击“下一步”。...