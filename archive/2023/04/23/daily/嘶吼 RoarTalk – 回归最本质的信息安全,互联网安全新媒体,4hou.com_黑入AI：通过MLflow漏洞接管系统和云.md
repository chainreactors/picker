---
title: 黑入AI：通过MLflow漏洞接管系统和云
url: https://www.4hou.com/posts/KEKn
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-23
fetch_date: 2025-10-04T11:31:21.990023
---

# 黑入AI：通过MLflow漏洞接管系统和云

黑入AI：通过MLflow漏洞接管系统和云 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑入AI：通过MLflow漏洞接管系统和云

布加迪
[技术](https://www.4hou.com/category/technology)
2023-04-22 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)142712

收藏

导语：AI测试框架MLFlow曝出的严重漏洞会导致服务器和数据泄密。

**CVE-2023-1177：MLflow中的LFI/RFI**

LFI/RFI导致系统和云帐户被接管

所有CVE在版本2.2.2中已经被修复

已发布了漏洞利用工具和扫描工具

机器学习系统领域最流行的工具之一是MLflow（月下载量超过1300万人次，且这个数字还在增长），它用于管理端到端机器学习生命周期。

Protect AI测试了MLflow的安全性，结果发现了一个混合型的本地文件包含/远程文件包含(LFI/RFI)漏洞，可能导致整个系统或云提供商被人接管。强烈建议运行MLflow服务器的组织立即更新到最新版本，或者至少更新到2.2.2版本。版本2.2.1修复了CVE-2023-1177，版本2.2.2修复了CVE-2023-1176。我们在本博文中探讨了该漏洞的影响、如何检测它，以及我们发现这个严重漏洞的过程。如果你正在运行MLflow，请使用本博文中提供的免费工具，立即开始修补系统。使用传统工具给系统打补丁可能是一个挑战，因为许多自动化补丁管理系统并不枚举或识别MLflow，就算枚举或识别，可能也不会执行版本检查。

立即升级到MLflow的最新版本非常重要，哪怕你的实例不在生产环境中，只在开发环境中使用。

**影响**

如果利用该漏洞，未经身份验证的远程攻击者可以读取启动了MLflow服务器的用户可以访问的这台服务器上的任何文件。

可以通过从MLflow服务器获取私有SSH密钥或云服务提供商凭据来获得远程代码执行的机会。这让攻击者得以远程登录到服务器或云资源，并利用找到的凭据拥有的相应权限执行任意代码。

**漏洞细节**

不需要用户交互。

不需要事先了解环境。

MLflow的所有自定义配置都易受攻击，包括开箱即用的安装环境。

MLflow 2.1.1之前的所有版本都容易受到LFI的攻击。

漏洞利用工具适用于从MLflow v1.12到 v2.1.1的所有版本。

MLflow 2.0之前的所有版本都容易受到LFI的攻击，只需通过更简单地利用：http://

MLflow维护者迅速响应了负责任披露的这个漏洞，在短短几周内交付了修复程序。MLflow 2.1.1之后的版本不再容易受到攻击。

**漏洞检测**

若要检查你的MLflow服务器是否容易受到攻击，请使用我们的免费CVE-2023-117-scanner扫描工具（https://github.com/protectai/Snaike-MLflow）。

**发现过程**

我们先安装了MLflow，启动拦截代理BurpSuite以拦截所有MLflow API调用，运行用数据填充MLflow的实验，然后启动UI服务器作进一步探索。

# Download MLflow source to get access to their example runs

git clone https://github.com/mlflow/mlflow

# Create and enter new directory outside the mlflow/ directory

mkdir mlflowui

cd mlflowui

# Copy the example code from the MLflow source into this new directory

cp -r ../mlflow/examples/sklearn\_elasticnet\_wine .

# Setup a virtual environment for installing requirements

python3 -m venv venv

source venv/bin/activate

# Install mlflow in this virtual environment

pip install mlflow pandas

# Run the example experiment

mlflow run --env-manager=local sklearn\_elasticnet\_wine -P alpha=0.5

# Run the UI to see the experiment details

mlflow ui --host 127.0.0.1:8000

在创建实验时，它给了我们指定存储对象的目录这一选项。这似乎是一个可配置的文件路径，我们可以通过运行的示例实验就可以看到：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863340101980.png "1679863340101980.png")

图1

这立即引起了我们的注意，因为这需要完美地实施过滤机制，以防止本地文件包含或任意文件覆盖。然而，你无法从UI远程运行MLflow实验。由于当你通过UI创建实验时，工件位置实际上没有发生任何变化，因此这里没有任何安全考虑。然后，我们通过点击单趟实验运行继续探索。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863360118165.png "1679863360118165.png")

图2

点击上图所示的运行名称，将我们带到实验运行细节，在这里我们可以看到实验涉及的文件，并下载文件，如下图所示。

在这里，我们在工件文件中看到了一个很大的“Register Model”（注册模型）按钮。我们很好奇。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863376167263.png "1679863376167263.png")

图3

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863386103536.png "1679863386103536.png")

图4

它似乎不是什么特别值得关注的对象，因为它只是弹出一个模式，让你选择模型，然后将该模型的详细信息保存为“Version 1”（版本1）。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863395382755.png "1679863395382755.png")

图5

但是底层到底发生了什么？为此我们检查了BurpSuite。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863405427393.png "1679863405427393.png")

图6

我们发现了在UI中并没有显示的另一个协议和文件路径输入。这似乎很可疑。我们将它手动更改为用户的私有SSH密钥：file: /// Users/danmcinerney/. ssh/id\_rsa。访问该文件将允许你以启动了MLflow服务器的用户的身份远程登录到MLflow主机。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863419132234.png "1679863419132234.png")

图7

新的source在响应中有所体现，这通常表明服务器端出现了变化。我们很想知道这实现了什么操作，于是回过头去查看已注册的模型细节。实验中没有什么运行工件，模型细节或模型版本细节中也没有值得关注的对象。这似乎是另一条死胡同，类似我们发现你可以将实验工件路径指向任意位置，但UI随后不让你任何操作。然而在检查BurpSuite请求和响应日志后，我们发现了一些值得关注的异常。

攻击者现在拥有访问权

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863440626248.png "1679863440626248.png")

图8

get-artifact API调用中的“500内部服务器错误”让我们感到可疑。在安全测试的早期，get-artifact API调用值得注意，因为它是从工件存储库返回文件数据的调用。这是你从实验运行下载模型的方法，我们发现它受到了一个防止本地文件包含漏洞的函数的保护，如下所示。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863460175346.png "1679863460175346.png")

图9

我们花了一些时间试图绕过这个，但没有成功。这个特殊的get-artifact调用的不同之处在于，它不是试图从子文件夹获取文件，而是直接访问文件名。此外，它实际上不是同一个API调用。下面是记入文档的get-artifact REST API调用：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863470138666.png "1679863470138666.png")

图10

下面是类似的model-version/get-artifact调用：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863481635819.png "1679863481635819.png")

图11

区别包括URL路径、参数和值。这显然不是同一个API调用。

我们注意到这个API调用不在说明文档中。关键区别在于，它通过path URL参数直接查找文件名，而不是通过合法的get-artifact API调用中的相对文件路径来查找。

这就意味着LFI防护机制并不存在，因为不需要执行目录遍历。只需要控制源文件夹的位置。在上面的几个步骤中，当我们创建一个新的模型版本时，尝试将API请求的source路径位置修改为：file:///Users/danmcinerney/.ssh/id\_rsa：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863492179191.png "1679863492179191.png")

图12

我们应该做的是将source位置更改为文件夹而不是更改为文件。我们纠正了这一点。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863510106659.png "1679863510106659.png")

图13

随后我们重新发送了发现的这个未记入文档的REST API调用，并将其指向id\_rsa，这是新模型版本source位置中的文件以及提供远程登录服务器功能的私有SSH密钥。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230327/1679863522116363.png "1679863522116363.png")

图14

使用检索到的SSH密钥，我们就可以通过终端访问运行MLflow服务器的主机。MLflow最常被配置为使用S3存储桶作为工件存储区。如果是这种情况，那么机器上另一个价值非常高的目标将是~/.aws/credentials文件，可想而知该文件存储的是AWS凭据。

其他高价值目标可能包括包含明文密码的Web服务器SQL配置文件或包含所有用户密码散列的/etc/shadow，这些用户密码散列可以通过hashcat之类的工具来破解。

**漏洞利用工具**

为了帮助保护你的系统，我们创建了一个简单的工具来发现潜在漏洞，这个工具名为MLFIflow.py（https://github.com/protectai/Snaike-MLflow）。

**安装**

git clone https://github.com/protectai/Snaike-MLflow

cd Snaike-MLflow/MLFIflow

python3 -m venv mlfiflow

source mlfiflow/bin/activate

pip install -r requirements.txt

**使用**

默认情况下，MLFIflow将尝试从MLflow服务器读取/etc/passwd，并使用找到的用户名搜索SSH密钥和云凭据文件：

python MLFIflow.py -s http://1.2.3.4:5000

若要指定待下载的文件的自定义单词列表，使用-f标志：

python MLFIflow.py -s http://1.2.3.4:5000 -f /path/to/wordlist.txt

本文翻译自：https://protectai.com/blog/hacking-ai-system-takeover-exploit-in-mlflow如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?e9zz8wBM)

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

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://ww...