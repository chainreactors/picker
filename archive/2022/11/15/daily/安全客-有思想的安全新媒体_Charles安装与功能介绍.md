---
title: Charles安装与功能介绍
url: https://www.anquanke.com/post/id/283124
source: 安全客-有思想的安全新媒体
date: 2022-11-15
fetch_date: 2025-10-03T22:43:58.558177
---

# Charles安装与功能介绍

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Charles安装与功能介绍

阅读量**497930**

发布时间 : 2022-11-14 10:30:41

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 0x01 介绍

Charles是在PC端常用的网络封包截取工具，除了可以在开发中调试端口外，Charles也可以用于分析第三方应用的通讯协议，配合Charles的SSL功能，还可以分析HTTPS协议。

BurpSuite在渗透测试中常用，Charles相比BurpSuite更易上手、简单直观。 Charles是收费软件，可以免费试用30天。试用期过后，未付费仍可继续使用，但是每次使用时间不可超过30分钟，并且启动时将会有10秒的延迟，所以为了以后使用起来不麻烦还是选择付费或者…（你懂的）。

**Charles主要功能：**

1. • 截取http和https网络数据包；
2. • 支持重发网络请求，方便后端调试；
3. • 支持修改网络请求参数；
4. • 支持网络请求的截获并动态修改；
5. • 支持模拟慢速网络等。

## 0x02 下载与安装

官网 https://www.charlesproxy.com/latest-release/download

![]()

找到对应操作系统版本下载，下载成功后根据提示安装即可。

**Charles激活码：**Registered Name: https://zhile.io License Key: 48891cf209c6d32bf4 （转自CSDN：blog.csdn.net/qq\_25821067…） Charles的logo是一个漂亮的瓷花瓶。

![]()

## 0x03 Charles菜单介绍

### 主界面介绍

**主界面如下图**

![]()

**菜单栏中的常用工具：**①：清除捕获到的所有请求； ②：红色代表正在捕获请求，灰色代表目前没有捕获请求； ③：停止SSL的代理； ④：灰色代表未开启网速节流，绿色代表开启； ⑤：灰色代表没有开启断点，红色代表开启； ⑥：编辑修改请求，点击后可以修改请求的内容； ⑦：重复发送请求，点击后选中的请求会被再次发送； ⑧：验证选中的请求响应； ⑨：购买许可证，会跳转至官网； ⑩：常用功能，包含Tools菜单中的常用功能； ⑪：常用设置，包含Proxy菜单中的常用设置。

**查看数据包视图**Charles主要提供Structure和Sequence两种查看数据包的视图。 Structure：将网络请求按访问的域名分类； Sequence：将网络请求按访问的时间排序； 使用时可以来回切换，Charles还提供了Filter功能，可以输入关键字快速筛选网络请求。

### 会话右键支持的功能

![]()

**Repeat、Repeat Advanced**重复执行请求，Repeat Advanced可以指定重复的遍数，这样可以选中多会话，在右侧的chart查看请求的时间等性能。

**Focus**当前选中的域名会被放在顶部，没有Focus的域名统一放到下面的Other Hosts下，也可在View–>Focused Hosts中统一编辑。

**Block List**黑名单中的域名不可联网。

**Export**导出会话Session保存到本地，下次就可通过File–>Open Session打开本地的Session。

**Compare**左侧列表中选择两个Session，右键时会出现该选项，可以对比两个请求的入参和出参。

**Compose**与工具栏中的钢笔图标一样，编辑请求然后执行。

**Map Remote**重定向到另一个请求的返回值当作自己的返回值，可以在Session上右键Map Remote设定规则，或Tools–>Map Remote来管理所有的Map Remote，再勾选Enable Map Remote启用。

**Map Local**使用本地的一个文件的内容作为返回值 可以在Session上右键Map Local设定规则，或Tools–>Map Local管理所有的Map Local，勾选上Enable Map Local启用。

### Proxy菜单

Charles是一个http和socks代理服务器。代理请求和响应使Charles能够在请求从客户端传递到服务器时检查和更改请求，以及从服务器传递到客户端时的响应。

Charles的主菜单有：File、Edit、View、Proxy、Tools、Windows、Help，用的最多的是Proxy和Tools。

![]()

**Proxy 菜单包含以下功能：**Start/Stop Recording：开始/停止记录会话。 Start/Stop Throttling：开始/停止节流。 Enable/Disable Breakpoints：开启/关闭断点模式。 Recording Settings：记录会话设置。 SSL Proxying Settings：SSL 代理设置。 Throttle Settings：节流设置。 Breakpoint Settings：断点设置。 Reverse Proxies Settings：反向代理设置。 Port Forwarding Settings：端口转发。 Proxy Settings：代理设置。 Access Control Settings：访问控制设置。 External Proxy Settings：外部代理设置。 Web Interface Settings：Web 界面设置。

**Recording Settings-记录会话设置**

Recording Setting和Start/Stop Recording配合使用，在Start Recording的状态下，可以通过Recording Setting配置Charles的会话记录行为。

Recording Settings 有 Options、Include、Exclude 三个选项卡

1. ![]()• **Options**：通过Recording Size Limits限制记录数据的大小。当Charles记录时，请求、响应头和响应体存储在内存中，或写入磁盘上的临时文件。有时，内存中的数据量突然增多，Charles会提示并停止录制。这时应该清除会话释放内存，再开始录制。在录制设置中，可以限制Charles录制的大小，这样不会影响浏览，Charles指挥停止录制。
2. • **Include**：只有与配置的地址匹配的请求才会被录制；
3. • **Exclude**：只有与配置的地址匹配的请求将不会被录制。

Include和Exclude操作相同，选择Add，填入需要监听的Procotol、Host、Port等信息即可。

![]()

或者右击网址选择Focus，其他的请求就会被放置到Other Host分类中，也可达到过滤的目的。

![]()

**Throttle Settings-节流设置**

Throttle Settings和Start/Stop Throttling配合使用，在Start Throttling的状态下，可以通过Throttle Settings配置Charles的网速模拟配置。

勾选Enable Throttling启用网速模拟配置，在Throttle Preset下选择网络类型即可，具体设置可以根据实际情况自行设置。如果只想模拟指定网站的慢速网络，可以再购选上Only for selected hosts项，再在对话框的下半部分设置中增加指定的hosts项即可。

![]()

**Breakpoint Settings-断点设置**

Breakpoint Settings和Enable/Disable Breakpoints配合使用，在Enable Breakpoints的状态下，可以通过Breakpoint Settings配置Charles的断点模式。

勾选上Enable Breakpoints启用断点模式，选择Add，填入需要监控的Scheme、Procotol、Host和Port等设置断点，再观察或者修改返回的内容，但是要注意请求超时时间问题。或者可以在某个想要设置断点的请求网址上右击选择Breakpoint设置断点。

![]()

### Reverse Proxies Settings-反向代理设置

反向代理在本地端口上创建Web服务器，该端口透明的将请求代理给远程Web服务器。反向代理上所有的请求和响应都可以记录在Charles中。

创建原始目标Web服务器的反向代理，然后将客户端应用程序连接到本地端口，反向代理对客户端应用程序是透明的，可以查看Charles之前可能无法访问的流量。 选中Enable Reverse Proxies进行Add添加即可。

![]()

**Port Forwarding Settings-端口转发**

可以将任何TCP/IP或UDP端口配置为使用Port Forwarding工具从Charles转发到远程主机，这样可以调试Charles中的任何协议。 还可以使用Charles作为Socks代理，所以无需设置端口转发。 配置与Reverse Proxies Settings类似，Add添加即可。

**macOS Proxy-记录计算机上的所有请求**

抓取电脑端的请求，勾选macOS Proxy即可，如果只抓取移动端请求，则取消勾选这个选项。

![]()

**Proxy Settings-代理设置**

默认代理端口为8888（可以自行修改）。填写上端口、勾选上Enable transparent Http proxying，就完成了Charles的代理设置。

![]()

**SSL Proxy Settings- SSL代理设置**

勾选上Enable SSL Proxying就完成了Charles上的SSL代理设置。也可选择Add，填入需要监听的Host和Port信息，就可针对某个域名启用SSL代理。

![]()

**Access Control Settings-访问控制设置**

访问控制列表能控制谁可以使用此Charles实例。通常，在本机运行Charles，并且打算只有自己使用它，无需进行其他设置，因为localhost始终在访问列表中。如果某个IP需要访问Charles，可以选择Add，填入允许访问的IP即可。

![]()

**External Proxy Settings-外部代理设置**

在网络上有个代理服务器，如果想要访问Internet，必须使用该代理服务器，这种情况，需要将Charles配置为访问Internet时使用现有代理。 选中Use external proxy servers，进行配置即可。可以配置单独的代理地址和端口：HTTP、HTTPS、SOCKS。

![]()

**Web Interface Settings-Web界面设置**

Charles也有个Web界面，可以从浏览器访问控制Charles，或者使用Web界面作为Web服务使用外部程序。 在 Web Interface Settings视图中勾选Enable web interface启用Web界面。可以匿名访问也可以通过Add添加Username和Password访问。

![]()

浏览器访问http://control.charles ，输入设定的用户名、密码即可访问。

![]()

**Web界面提供以下功能的访问**Throttling-节流控制：激活或停用任何已配置的限制预设； Recording-录音控制：开始和停止会话录制； Tools-工具：激活和停用工具； Session-会话控制：清除当前会话、以任何支持的格式导出当前会话、以Charles的本机会话格式下载当前会话； Quit-退出。

通过检查Web界面HTML，可以推导出如何将其用作Web服务来自动化Charles。

![]()

### Tools菜单

Tools菜单视图如下图所示：

![]()

**Tools菜单包含以下功能：**No Caching Settings：禁用缓存设置； Block Cookies Settings：禁用Cookie设置； Map Remote Settings：远程映射设置； Map Local Settings：本地映射设置； Rewrite Settings：重写设置； Black List Settings：黑名单设置； White List Settings：白名单设置； DNS Spoofing Settings：DNS欺骗设置； Mirror Settings：镜像设置； Auto Save Settings：自动保存设置； Client Process Settings：客户端进程设置； Compose：编辑修改； Repeat：重复发包； Repeat Advanced：高级重复发包； Validate：验证； Publish Gist：发布要点； Import/Export Settings：导入/导出设置； Profiles：配置文件； Publish Gist Settings：发布要点设置。

**No Caching Settings-禁用缓存**

此工具可以防止客户端应用程序缓存任何资源，所以，始终向远程网站发出请求，始终都可看见最新的版本。

**适用范围**该工具可以作用于每个请求中，只要选中Enable No Caching即可。也可以仅对已经配置的请求启用，同时选中Only for selected locations即可。当用于选定的请求时，可以使用简单但功能强大的模式匹配将工具的效果限制为指定的主机和路径。

![]()

**Block Cookies Settings-禁用Cookie**

此工具阻止了Cookie的发送和接收。它可用于测试网站，就像在浏览器中禁用了Cookie一样。网络爬虫通常不支持Cookie，因此该工具还可用于模拟网络爬虫网站的视图。

**适用范围**该工具可以作用于每个请求，选中 Enable Block Cookies 即可。也可以仅对已配置的请求启用，启用 Block Cookies 的同时，选中 Only for selected locations即可。当用于选定的请求时，可以使用简单但功能强大的模式匹配将工具的效果限制为指定的主机和路径。

**工作原理**此 工具通过操纵控制响应 Cookies 的 HTTP 请求头来禁用 Cookies。从请求中移除 Cookie 请求头，防止 Cookie 值从客户端应用程序发送到远程服务器。从响应中删除 Set-Cookie 请求头，防止请求设置客户端应用程序从远程服务器接收的 Cookie。

![]()

**Map Remote Settings-远程映射**

此工具根据配置的映射更改请求站点，以便从新站点透明地提供响应，就好像这是原始请求一样。

通过此映射，可以从另一个站点提供全部或部分站点，比如：

1. • 可以把 tide.com/charles/ 映射到 localhost/charlesdev/ 来为 tide.com 提供一个子目录；
2. • 可以把 tide.com/\*.php 这种指定后缀的所有文件映射到 localhost/charlesdev/。

**映射类型**

1. • 可以将目录映射到目录，如tide.com/charles映射到localhost/charlesdev/；
2. • 可以将文件映射到文件，如tide.com/charles/download.php映射到test.com/test/test.htm；
3. • 可以将带有文件模式的目录映射到目录，如tide.com/charles/\*.php映射到localhost/charlesdev/；
4. • 如果在目标映射中未指定路径，则URL的路径部分将不会更改。如果要映射到根目录，需要在目标路径字段中以/结尾。

**HTTPS**此工具可以将HTTP请求映射到HTTPS目标，也可以将HTTPS请求映射到HTTP目标。

![]()

**Map Local Settings-本地映射**

此可以使用本地文件，本地文件的内容将返回给客户端，就像是正常的远程响应一样。 Map Local可以加快开发和测试的速度，可实现在开发环境中也能安全的进行测试。 工作原理 当请求与Map Local映射匹配时，它会检查与路径匹配的本地文件。如果在本地找到所请求的文件，就将其作为响应返回，就好像它是从远程站点加载的一样，因此它对客户端是透明的。如果在本地找不到所请求的文件，那么该请求会像平常一样由网站提供，返回由真正的服务器提供的数据。

**Rewrite Settings-重写**

Rewrite工具允许创建请求和响应在通过Charles时修改它们的规则，比如添加或修改头信息、搜索和替换响应内容中的某些文本等。 重写集 重写集可以单独激活和停用。每个集合包含站点和规则的列表。这些站点选择规则将要运行的请求和响应。 重写规则 每个规则都买哦熟了一次重写操作。规则可能会影响请求URL的Header，正文或部分内容；它可以根据请求或响应来操作；它可以定义搜索、替换或者仅替换样式重写。

**Black List Settings-黑名单**

Black List工具将阻止被列入黑名单的域名的所有请求。当Web浏览器尝试从被列入黑名单的域名请求任何页面时，该请求将被Charles阻止。也可以输入通配符阻止其子域名。

**White List Setting-白名单**

White List工具将阻止除了被列入白名单的域名之外的所有请求。 如果一个请求与黑名单和白名单都不匹配，则该请求会被阻止。

**DNS Spoofing Settings- DNS欺骗**

此工具允许通过将自己的主机名指定给远程地址映射来欺骗DNS查找。当请求通过Charles时，DNS映射将优先。 Charles包...