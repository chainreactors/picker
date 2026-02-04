---
title: 红队武器化(二):frp静态特征消除以及流量改造
url: https://forum.butian.net/share/4759
source: 奇安信攻防社区
date: 2026-02-03
fetch_date: 2026-02-04T04:06:21.687046
---

# 红队武器化(二):frp静态特征消除以及流量改造

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 红队武器化(二):frp静态特征消除以及流量改造

* [渗透测试](https://forum.butian.net/topic/47)

本文将简单介绍frp这款隧道代理工具的项目结构和代码运行流程以及如何通过对frp二次开发(后面简称"二开")来消除其静态特征和流量特征从而规避杀软以及EDR的检测。

前言
==
大家好，我是拖更博主r0leG3n7。本文将简单介绍frp这款隧道代理工具的项目结构和代码运行流程以及如何通过对frp二次开发(后面简称"二开")来消除其静态特征和流量特征从而规避杀软以及EDR的检测。如有任何错误和不足欢迎各位师傅指正，转载请注明文章出处。
frp项目分析过程
=========
致敬伟大的原项目:<https://github.com/fatedier/frp>，我选择的是较新版本0.65.0的frp。(我写这篇文章的时候frp刚刚更新到0.66.0，但应该不影响我当时二开的就是最新版的frp\[狗头\])。
先问大家一个问题，如果我需要对某个开源项目进行二开，我有必要把这个开源项目里所有的代码结构都分析得明明白白的嘛？那当然是没那个必要，对于这种大型的开源项目，我们需要很明确自己想要把这个项目改成什么样子，确定自己的需求，确定项目有哪些对于你来说是"缺陷"的地方，这样就不会在庞大的代码海洋里迷失自己。
需求分析
----
1、首先来到我们软件生命周期最重要的需求分析阶段，我的大致的需求就是要改frp的静态特征和流量特征来绕过EDR检测达到免杀的效果，确定大致的需求以后我需要知道frp有哪些特征。
原版的frp有如下几个典型特征:
1）frp的服务端和客户端启动时都会默认读取同目录名为frpc.ini或者frps.ini的配置文件。
2）frp的客户端与服务端发起TCP连接时会发送诸如版本号、架构、token、run id等信息进行登录认证。
3）frp的客户端与服务端在连接成功或者失败时都会在控制台输出一些debug信息或者提示信息。
4）frp的客户端与服务端在TCP连接建立后的第一个应用层数据包会发送一个自定义的字节，这个字节的值为0x17。
5）frp的客户端与服务端在TCP连接建立成功后，服务端可以通过对某些API接口发起get请求、post请求或者put请求去控制客户端，比如/api/reload、/api/stop等。
2、确定大致的需求并且定位"缺陷"以后，我要明确我的需求，明确我要把它改成什么样子。
我明确的需求:
1）对于frp的服务端和客户端在本地读取配置文件的行为，我可以把配置文件信息想象成shellcode，按照loader加载shellcode那样处理。我想到的是将配置文件硬编码在程序里面；或者将配置文件加密后通过命令行传入frp，frp客户端与服务端尝试建立连接时再进行解密；或者通过远程URL加载；还有最重要的是去除通过文件路径读取配置文件的功能。
2)对于frp的服务端和客户端建立连接失败时的输出的错误信息，我要进行删除或者修改；对于建立连接成功时发送的登录信息或者代理信息，我要进行TLS加密或者将默认变量名、键值对修改；对于TLS建立连接的默认自定义字节以及服务端控制客户端的api默认接口名也是一样地做修改处理。
项目分析
----
1、程序所需的依赖写在了项目的go.mod文件中,在GoLand的IDEA可以按"Alt键+回车键"自动下载对应的依赖。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1766233990906-c1c734dc-efc6-449f-9420-bae651ba7f15.png)
2、项目的Makefile是编译命令文件，在这里可以找到服务端代码入口/cmd/frps以及客户端的代码入口/cmd/frpc。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1766233631711-3ab47dbd-dcd8-49ae-8ad1-da4d74b6343a.png)
3、我们可以直接定位到客户端/cmd/frpc/mian.go，编译时会自动搜索该目录下的mian.go文件作为编译的入口，重点关注sub.Execute()。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1766996744837-7d9ffe1f-1829-4cd5-97dc-3dbd9f476f5b.png?x-oss-process=image%2Fformat%2Cwebp)
4、按alt跟进sub.Execute()，它的主要功能是rootCmd.Execute()这行 。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1767000918507-926139ac-d195-4e25-a4bf-990784c295dd.png?x-oss-process=image%2Fformat%2Cwebp)
5、按alt跟进rootCmd.Execute()，rootCmd.Execute()会执行rootCmd中的RunE，RunE中包含两个关键的函数runMultipleClients()和runClient()，这两个函数主要的功能就是加载配置文件然后建立与服务端的链接。我们主要看runClient()函数，一般情况下一个frpc客户端只加载一个配置文件，所以不用怎么去考虑改runMultipleClients()，我二开的时候索性直接删掉了命令行配置文件路径的输入。runClient()传入一个名为cfgFile的全局变量，它是frp客户加载配置文件的路径。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1767063586066-7c4cba45-68ff-4f21-9dfd-bc3532118b16.png)
6、纵观整个rootCmd.Execute()过程，我们都没有看到给cfgFile全局变量赋值的地方。但是我们知道原版的frpc客户端是从命令行输入配置文件路径的，我们可以从包的init()函数看到程序是怎么从命令行中获取用户输入的配置文件路径赋值cfgFile变量的。init()函数是 Go 语言中的一个特殊函数，通常用于资源、包和变量的初始化。它的特点是每个包的 init() 在程序运行期间只执行一次；init()无需手动调用，会在main()之前自动执行，导入包的 init() 先于当前包的 init() 执行。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1767065104680-a98708c4-4e5d-494e-badf-e729e4be2857.png?x-oss-process=image%2Fformat%2Cwebp)
7、回到rootCmd.Execute()，按alt跟进runClient()函数，我们来到了这次二开中最重要的函数config.LoadClientConfig(),它是我们修改配置文件传参关键。从返回值我们可以知道，它会返回配置文件的基本配置信息、代理配置信息、配置文件格式等。config.LoadClientConfig()的传入参数是配置文件路径，这个函数是需要完全改写的，我上面的需求已经说的很明确了，我会从硬编码、远程URL输入或者命令行输入去读取配置文件，不会有从文件路径读取配置文件的行为，减少文件落地。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1767148943721-6d0f62f4-da73-43e8-9041-caa84afe58d7.png?x-oss-process=image%2Fformat%2Cwebp)
8、虽然说要完全改写config.LoadClientConfig()，但是我们还是要按alt跟进看一下它的内部逻辑以便我们更精确无误地对它进行修改，config.LoadClientConfig()存在读取并转换配置文件的legacy.ParseClientConfig()方法。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1767148975042-ec671e11-e852-43e4-a1c1-9a0fa817a3ef.png?x-oss-process=image%2Fformat%2Cwebp)
9、按alt跟进legacy.ParseClientConfig()，legacy.ParseClientConfig()函数通过文件读取函数GetRenderedConfFromFile()以及传入的文件路径来读取配置文件信息并将其赋值content变量，然后将content的类型转化为字节数组后将其作为参数传给UnmarshalClientConfFromIni()方法，UnmarshalClientConfFromIni()将转换后的基础配置文件信息赋值给cfg。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1767148897746-5382de13-f409-4638-84c6-e265ab00a6ca.png)
10、同样地，legacy.ParseClientConfig()通过legacy.LoadAllProxyConfsFromIni(),将转换后的代理配置文件信息等赋值给变量proxyCfgs和visitorCfgs。这时候我们知道配置文件信息主要是靠UnmarshalClientConfFromIni()和LoadAllProxyConfsFromIni()两个函数进行转换的，到时候我们二开的时候就照着这两个函数简单修改一下就行了。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1767149469597-aed30c72-86a5-4a39-97f1-466cd92f786d.png)
11、了解完它是怎么读取并转化配置文件信息后，我们再回到上面的runClient()函数，再大致了解一下它是怎么通过startService方法以及转化后的配置文件信息启动服务的，这里注意startService方法第五个参数cfgFile为配置文件路径，到时候服务端调用/api/reload接口重新加载配置文件时候会用到。因为我二开时将通过文件路径读取配置文件信息这个行为删除了，这个参数到时候会变成空值，这个参数置空以后服务端调用该接口可能会报错。
![](https://cdn.nlark.com/yuque/0/2026/png/27682735/1768118083819-72db35b3-9f3d-42f8-88cd-ced71513b636.png)
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1766313711825-f01774fc-ac76-4f2c-bc83-290c45ced936.png)
12、service.go的NewService创建服务对象方法。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1766315152285-55a66a33-8515-4092-8989-70af6434a154.png)
13、service.go的Run运行服务对象方法。
![](https://cdn.nlark.com/yuque/0/2025/png/27682735/1766315520399-74b57634-5c59-4a0e-9e11-f98a43df48cb.png)
frp项目二开过程
=========
本节我将介绍如何对frp原项目进行二开改造隐藏其静态特征和流量特征，包括修改传参方式，修改frp默认输出，修改frp静态字符串，修改frp的TLS流量特征等。相信看过四大名著《三国演义》的都知道赵云在长坂坡七进七出，单骑救主的故事，我第一次了解到这个故事的时候我就觉得不可思议，真的有人能从这么多的魏军人马中带着个婴儿死里逃生吗？在二开了frp之后，我就悟到了。frp客户端就是赵云，配置文件就是阿斗，单骑救主护送阿斗回蜀就是frp客户端与服务端建立连接的通信过程。赵云之所以会被在茫茫人海中被魏军检测到，并不只是因为他喊了那句"我乃常山赵子龙"，更多的是因为他有对阿斗进行明目张胆地"取餐"这个行为，不过好在他能及时调整，将阿斗硬编码到自己的怀里，才做到了七进七出。我觉得单骑救主这个故事可以有更多opsec的改进方案让他变得更加合理更加地叫人信服，至于怎么改，请看下面听我娓娓道来。
传参方式
----
传参方式的修改在上面需求的第一条已经提出来了，我的最终方案是去除通过文件路径读取配置文件的部分；如果frp收到命令行传入的加密配置文件，就解密该配置文件进行连接；如果读取不到命令行传入的加密配置文件，就读取硬编码的配置文件进行连接。
1、首先去除init()函数中接收对配置文件路径的输入,新增一个全局变量eStr,用于接收用户控制台输入的加密后的配置文件信息，使用示例"-e &lt;加密的配置文件信息&gt;"。
rootCmd.PersistentFlags().StringVarP()方法参数说明:
第一个参数为接收控制台输入的指针
第二个参数为参数名称
第三个参数为传入参数的简写，比如"-c ./frpc.ini"
第四个参数为参数的默认值(StringVarP就必须为字符串类型，BoolVarP就必须为布尔类型，以此类推)
第五个参数为参数介绍说明
![](https://cdn.nlark.com/yuque/0/2026/png/27682735/1768129127559-0bf5a4fa-ff66-4e2f-8978-f7b6b5ef2638.png)
2、修改rootCmd.Execute()逻辑，当eStr变量不为空(也就说收到来自用户在命令行输入的加密配置文件内容），就对传入的加密配置文件内容进行解密，将它解密后的明文传给一个自定义的cfgContent变量；如果eStr变量为空，就将硬编码的配置文件信息传给cfgContent变量。cfgContent变量最终会作为参数传给修改后的runClient()函数。
![](https://cdn.nlark.com/yuque/0/2026/png/27682735/1768274803631-719cb2f7-1011-40c0-9058-60a0e45a572b.png)
3、修改runClient()函数运行逻辑，之前runClient传入第一个参数是配置文件路径，我现在将这个参数改成配置文件内容，到时候硬编码的配置文件或者解密后的配置文件可以直接作为参数调用这个函数，修改的地方主要是config.LoadClientConfig()这个部分，将其修改为了一个新的函数config.LoadClientConfigFromContent()，用于接收传入的配置文件内容并将其转换。
![](https://cdn.nlark.com/yuque/0/2026/png/27682735/1768356008225-54c9acb4-7a5a-4b24-b47b-32bdaa7f6af1.png)
4、config.LoadClientConfigFromContent()第一个传入参数为配置文件内容的字符串，返回值与之前一致。
```php
func LoadClientConfigFromContent(content string, strict bool) (
\*v1.ClientCommonConfig,
[]v1.ProxyConfigurer,
[]v1.VisitorConfigurer,
bool, error,
) {
var (
cliCfg \*v1.ClientCommonConfig
proxyCfgs = make([]v1.ProxyConfigurer, 0)
visitorCfgs = make([]v1.VisitorConfigurer, 0)
isLegacyFormat bool
)
contentBytes := []byte(content)
// Render template with values
renderedContent, err := RenderWithTemplate(contentBytes, GetValues())
if err != nil {
return nil, nil, nil, false, fmt.Errorf("render template error: %v", err)
}
if DetectLegacyINIFormat(renderedContent) {
// Parse legacy INI format
legacyCommon, err := legacy.UnmarshalClientConfFromIni(renderedContent)
if err != nil {
return nil, nil, nil, true, err
}
// Parse ...