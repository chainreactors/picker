---
title: 如何使用ECharts辅助开展数据可视化分析？
url: https://mp.weixin.qq.com/s?__biz=MzAxNTA4NDAwOQ==&mid=2650736988&idx=1&sn=5e1734a5c81916d6113bf0d3ad513927&chksm=8382d9dab4f550cc2c8fbe9782059486865dfba1150efa8121d5f1347f282775f969fb2935f9&scene=58&subscene=0#rd
source: 信息时代的犯罪侦查
date: 2024-10-05
fetch_date: 2025-10-06T18:52:37.997126
---

# 如何使用ECharts辅助开展数据可视化分析？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gKXsVUZdFwdwofSPIUpwcLvlXaC9NWnOiaSfdXITBz2iamicoo7HuROT1wmWQavZ0zaiaETzChVnnTEeHy6g7OsQmw/0?wx_fmt=jpeg)

# 如何使用ECharts辅助开展数据可视化分析？

原创

嘟嘟的爸爸

信息时代的犯罪侦查

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **知识** | **案例** | **随笔** | **声音** | **其他** |

**编者按**

数据可视化的作用不容小觑，然而很多朋友或许并没有真正操刀体验的经历。

**一、引言**

在当今数据驱动的时代，数据可视化已成为分析的重要工具。ECharts作为一款强大的图表库，可以帮助开发者快速创建丰富的交互式图表，便于直观展示数据。本文将探讨如何在MFC中通过WebView2技术结合ECharts进行数据可视化分析，并详细阐述数据的准备、处理和展示过程。

**二、总体技术结构**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwdwofSPIUpwcLvlXaC9NWnOP6GOIapXfRJEpOBDC8l0qnswCuGS8P3M1vticaooc4sTNmUQK21yl1g/640?wx_fmt=png&from=appmsg)

    在上述架构下，C++桌面端程序通过构造web网页和组织数据，实现借助ECharts展示数据的目的。首先，请大家看一下最终效果，如下图所示。在图示中，左边的两个表格，是我在应用程序中为组织数据提供的用户界面，右边部分是展示的“关联关系”图示。诚然，在这个架构下，如何显示图像，以及如何分析数据之间的关联关系，完全不用开发者费心。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwdwofSPIUpwcLvlXaC9NWnOZQxKKtPzoWTFEv8KhR0o83qprOvmalfVmUQicYvpe3Vn6olQsn6Dyfg/640?wx_fmt=png&from=appmsg)

在这个过程中，需要向大家讲明白四个技术点。我们一一道来。

**三、几个主要的技术要点**

**1、在桌面端应用程序中访问web网页**

在MFC桌面应用程序中，有很多种方法可以实现对web网页的访问和显示。最纷繁复杂的当属使用原始socket，这也是学习网络通信技术的底层基础，在应用层开发中几乎不太可能用到这种技术了。

第二种方法可以使用CHttpFile、CHttpConnectionj等封装好的类，优点是不“挑”浏览器类型，兼容性较好。缺点是无法实现对使用新技术的web网页效果。

本案例中，小编使用了webview2技术。具体实现的细节如下：

（1）包含头文件：

#include <webview2.h>

（2）使用WRL命名空间：

using namespace Microsoft::WRL

（3）定义变量，全局或者局部变量均可以，如果不允许其他方法修改，则可以增加static标识。

// 指向webview2控件的WebViewController

wil::com\_ptr<ICoreWebView2Controller> webviewController = nullptr;

// 指向容纳控件的窗口指针

wil::com\_ptr<ICoreWebView2> webview = nullptr;

（4）初始化控件并实现对某URL网址的访问。下面的代码虽然显得貌似很复杂，不过全文引用即可，您能够修改的部分，可能仅限于目标网址那个地方，也就是小编标红的区域，此处替换为您下载的echarts示例网页的地址即可（本地或者远端均可）。

CoInitialize(NULL);

HWND hWnd = this->m\_hWnd;

CreateCoreWebView2EnvironmentWithOptions(nullptr, nullptr, nullptr,

Callback<ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler>(

[hWnd](HRESULT result, ICoreWebView2Environment\* env) -> HRESULT{

env->CreateCoreWebView2Controller(hWnd, Callback<ICoreWebView2CreateCoreWebView2ControllerCompletedHandler>(

[hWnd](HRESULT result, ICoreWebView2Controller\* controller) -> HRESULT {

if (controller != nullptr) {

webviewController = controller;

webviewController->get\_CoreWebView2(&webview);

}

wil::com\_ptr<ICoreWebView2Settings> settings;

webview->get\_Settings(&settings);

settings->put\_IsScriptEnabled(TRUE);

settings->put\_AreDefaultScriptDialogsEnabled(TRUE);

settings->put\_IsWebMessageEnabled(TRUE);

RECT bounds;

::GetClientRect(hWnd, &bounds);

webviewController->put\_Bounds(bounds);

Microsoft::WRL::ComPtr<ICoreWebView2Settings> settings2;

webview->get\_Settings(&settings2);

settings2->put\_IsScriptEnabled(TRUE);

CString strHtmlFilePath = \_T("");

strHtmlFilePath = GetProgramFolder();

strHtmlFilePath += \_T("//flsdmap.html");

int len = MultiByteToWideChar(CP\_ACP, 0, strHtmlFilePath, -1, NULL, 0); // 计算所需长度

std::wstring wstr(len, 0);

MultiByteToWideChar(CP\_ACP, 0, strHtmlFilePath, -1, &wstr[0], len); // 转换

LPCWSTR lpwstr = wstr.c\_str(); // 获取 LPCWSTR

webview->Navigate(lpwstr);

EventRegistrationToken token;

webview->add\_NavigationStarting(Callback<ICoreWebView2NavigationStartingEventHandler>(

[](ICoreWebView2\* webview, ICoreWebView2NavigationStartingEventArgs\* args) -> HRESULT {

wil::unique\_cotaskmem\_string uri;

args->get\_Uri(&uri);

std::wstring source(uri.get());

return S\_OK;

}).Get(), &token);

webview->AddScriptToExecuteOnDocumentCreated(L"Object.freeze(Object);", nullptr);

webview->ExecuteScript(L"window.document.URL;", Callback<ICoreWebView2ExecuteScriptCompletedHandler>(

[](HRESULT errorCode, LPCWSTR resultObjectAsJson) -> HRESULT {

LPCWSTR URL = resultObjectAsJson;

//doSomethingWithURL(URL);

return S\_OK;

}).Get());

webview->add\_WebMessageReceived(Callback<ICoreWebView2WebMessageReceivedEventHandler>(

[](ICoreWebView2\* webview, ICoreWebView2WebMessageReceivedEventArgs\* args) -> HRESULT {

wil::unique\_cotaskmem\_string message;

args->TryGetWebMessageAsString(&message);

webview->PostWebMessageAsString(message.get());

return S\_OK;

}).Get(), &token);

return S\_OK;

}).Get());

return S\_OK;

}).Get());

**2、如何使用ECharts图表？**

ECharts为大家提供了非常丰富的图表类型。大家可以在ECharts示例网站上点击您感兴趣的图表类型，将该图表对应的网页下载到本地。当然，同时下载到本地的还会有几个系统支撑文件，如：echarts.min.js等。

在下载的html文件中，您会很明显地看到支撑文件以及数据文件的描述，如下图所示。显示雷达图，需要echarts.min.js提供技术支撑，具体的数据保存在radar.js中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwdwofSPIUpwcLvlXaC9NWnONcVQFlTlxiaOkbv6syljQdiceW3BbEdB3SRicXODbvsicicphKwEQql0pjQ/640?wx_fmt=png&from=appmsg)

**3、如何构造数据文件？**

ECharts图表所依托的数据文件，既可以单独保存在一个文件之中，也可以与html文件融合到一起。具体采用哪种方案，小编认为与数据文件的大小相关，如果数据节点太多（如超过100万）……，建议使用单独的数据文件；如果节点只有几十个、几百个，与网页融合到一起也是不错的选择。

在实现上述雷达图中，小编就使用了单独的数据文件，通常是json格式。如何构造json格式的数据节点，取决于您在应用程序中的处理逻辑。比如，小编要构造12个内设机构在5个维度上的数据，以便形成雷达图。很明显，json数据不可能手工实现，一定要在应用程序中动态生成，这一点并不难，不过一定要细心，动态生成的过程中，有时候多了一个中括号、大括号，可能都无法正确显示图表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwdwofSPIUpwcLvlXaC9NWnO5zhhTYmxthicqjyMGP3qib1qRbswzoAT1KKPCfFLYP27qvefic47v5XgQ/640?wx_fmt=png&from=appmsg)

**4、如何动态选择图表类型？**

事实上，在ECharts实例网站下载的html文件中，设置有相应的图表类型标识，可以在应用程序中访问该本地文件实现标识符替换，然后刷新就可以显示新的图表类型了。如下图所示，将force替换为circular，就可以变更关联关系图的样式，如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwdwofSPIUpwcLvlXaC9NWnO2aJrSo7BgS8aRWeTEuRab27VklsOq6qZujkCUyntde9k6eqeicVBHag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwdwofSPIUpwcLvlXaC9NWnOLWT6Fia3UA7bJ3PMibGLeJe5iaEPG8mQBw0gvBY9Tia63fYVuB9cicn3bfQ/640?wx_fmt=png&from=appmsg)

**四、有点感慨**

7年前，小编协助办理一起网络传销案件，该案涉及的用户数据信息高达43万条。我记得当时也想借助echarts进行数据层级的展示，以便在法庭上展现一个犯罪组织的架构。但是，当数据节点达到1万以上时，展示每一个节点显示标题、数值等细节信息已经完全没有必要了。虽然我能够在程序中生成具有43万个节点、关系的json数据文件，但却达不到设想中的震撼效果。 说到这里，当时那个案件的成功办理还要感谢一个叫做**智qi云**的研发团队提供的支持。

小编认为，当数据量达到海量时，很多处理逻辑都变了，而这应该成为我们“取证人”面对海量数据时必要的心理准备。

**以上与诸君共勉。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/gKXsVUZdFwfseXriaDM44eHD16k06y9No7u6PHvUNFyS6MNdc6tgbvbxRexliaaQpu5F1XpyC4Wh6SzNCD5LDXNQ/0?wx_fmt=png)

信息时代的犯罪侦查

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gKXsVUZdFwfseXriaDM44eHD16k06y9No7u6PHvUNFyS6MNdc6tgbvbxRexliaaQpu5F1XpyC4Wh6SzNCD5LDXNQ/0?wx_fmt=png)

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