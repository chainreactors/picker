---
title: WebUI:The easiest attack surface in Chromes
url: https://buaq.net/go-138384.html
source: unSafe.sh - 不安全
date: 2022-12-04
fetch_date: 2025-10-04T00:28:28.281988
---

# WebUI:The easiest attack surface in Chromes

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/7d9f5a0927a84f7ebce774c9a3336945.jpg)

WebUI:The easiest attack surface in Chromes

*2022-12-3 13:9:52
Author: [eternalsakura13.com(查看原文)](/jump-138384.htm)
阅读量:32
收藏*

---

发表于

2022-12-03

|

分类于

[浏览器](http://eternalsakura13.com/categories/%E6%B5%8F%E8%A7%88%E5%99%A8/)

|

|

阅读次数:

“WebUI “是一个术语，用于宽泛地描述用网络技术（即HTML、CSS、JavaScript）实现的Chrome浏览器的部分UI。

Chromium中的WebUI的例子。

* Settings (chrome://settings)
* History (chrome://history)
* Downloads (chrome://downloads)

关于webui具体怎么工作在这里将不展开，请参考官方文档详细阅读，本文将重点介绍webui中常见的几类漏洞模式。

[https://chromium.googlesource.com/chromium/src/+/master/docs/webui\_explainer.md](https://chromium.googlesource.com/chromium/src/%2B/master/docs/webui_explainer.md)

我们将以一个简单的漏洞模式来学习webui的数据流传递。

具体的说就是每个WebUI都会注册很多WebUIMessageHandler，而每个Handler上又会注册多个Message Callback，每个Message Callback都有一个对应的Message Name，可以通过这个Message Name来调用到对应的webui函数，并传入参数。

具体来说就是形如以下调用：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` chrome.send("recordNavigation",[1337,0]); ``` |

## case1: issue-1303614

由于该漏洞代码只存在于chromium dev，不存在发行版中，所以没有CVE，只有对应的issue编号。

### Root Cause

* <https://bugs.chromium.org/p/chromium/issues/detail?id=1303614>

让我们看一下代码，这里注册了一个名为recordNavigation的Message Callback，它将对应调用到HandleRecordNavigation函数，并处理传入的参数。

它将对传入的参数列表依次调用ConvertToNavigationView，将其强制转换为NavigationView类型的枚举值，分别得到from\_view和to\_view。

但由于这里并没有检查传入的参数是否小于NavigationView类型能处理的最大值，注意这里仅仅只有一个debug check，这个debug check在release发行版里是不存在的，所以可以试做没有检查。

这将导致在EmitScreenOpenDuration函数处理cast之后得到的from\_view的时候， 触发一个堆溢出。

这里它将对kOpenDurationMetrics列表进行find，但是由于没有检查传入的参数是否小于NavigationView类型能处理的最大值，所以它将find不到。

我们知道在c++里，find如果找不到，迭代器iter将指向end，这其实代表的是指向容器的最后一个元素的**下一个**。

而这里同样也没有检查find找不到的情况，也就是没有检查iter是否指向end，就直接解引用了。它同样也是使用了一个Debug Check，但这其实是无用的。

所以对iter解引用将直接越界，造成buffer overflow。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 ``` | ``` // content::WebUIMessageHandler: void DiagnosticsMetricsMessageHandler::RegisterMessages() {   DCHECK(web_ui());    web_ui()->RegisterMessageCallback(       kRecordNavigation, //----->"recordNavigation"       base::BindRepeating(           &DiagnosticsMetricsMessageHandler::HandleRecordNavigation,           base::Unretained(this))); }  enum class NavigationView {   kSystem = 0,   kConnectivity = 1,   kInput = 2,   kMaxValue = kInput, };  // Converts base::Value<int> to NavigationView based on enum values. NavigationView ConvertToNavigationView(const base::Value& value) { 	DCHECK(value.is_int());   DCHECK_LE(value.GetInt(), static_cast<int>(NavigationView::kMaxValue));   **return static_cast<NavigationView>(value.GetInt());** }  // Message Handlers: void DiagnosticsMetricsMessageHandler::HandleRecordNavigation(     const base::Value::List& args) {   DCHECK_EQ(2u, args.size());   DCHECK_NE(args[0], args[1]);    **const NavigationView from_view = ConvertToNavigationView(args[0]);**   const NavigationView to_view = ConvertToNavigationView(args[1]);   const base::Time updated_start_time = base::Time::Now();    // Recordable navigation event occurred.   **EmitScreenOpenDuration(from_view, updated_start_time - navigation_started_);**    // `current_view_` updated to recorded `to_view` and reset timer.   current_view_ = to_view;   navigation_started_ = updated_start_time; }  void EmitScreenOpenDuration(const NavigationView screen,                             const base::TimeDelta& time_elapsed) {   // Map of screens within Diagnostics app to matching duration metric name.   constexpr auto kOpenDurationMetrics =       base::MakeFixedFlatMap<NavigationView, base::StringPiece>({           {NavigationView::kConnectivity,            "ChromeOS.DiagnosticsUi.Connectivity.OpenDuration"},           {NavigationView::kInput, "ChromeOS.DiagnosticsUi.Input.OpenDuration"},           {NavigationView::kSystem,            "ChromeOS.DiagnosticsUi.System.OpenDuration"},       });    **auto* iter = kOpenDurationMetrics.find(screen);**   DCHECK(iter != kOpenDurationMetrics.end());    base::UmaHistogramLongTimes100(std::string(iter->second), time_elapsed); } ``` |

### poc

browsing `chrome://diagnostics` and open devtools

execute `chrome.send("recordNavigation",[1337,0]);` in console.

### patch

补丁就是加上了我刚刚提到的没有加的检查。

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` auto* iter = kOpenDurationMetrics.find(screen); -  DCHECK(iter != kOpenDurationMetrics.end()); +  if (iter == kOpenDurationMetrics.end()) +    return; ``` |

## other case

<https://bugs.chromium.org/p/chromium/issues/detail?id=1303613>

## case1: CVE-2022-2859

[https://chromium.googlesource.com/chromium/src/+/08b5eaecf33165cda178517fa4ba070d1f598e16](https://chromium.googlesource.com/chromium/src/%2B/08b5eaecf33165cda178517fa4ba070d1f598e16)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 ``` | ```  void MultidevicePhoneHubHandler::RegisterMessages() {   web_ui()->RegisterDeprecatedMessageCallback(       "setFakePhoneHubManagerEnabled",       base::BindRepeating(           **&MultidevicePhoneHubHandler::HandleEnableFakePhoneHubManager**,           base::Unretained(this))); ... ... void MultidevicePhoneHubHandler::HandleEnableFakePhoneHubManager(     const base::ListValue* args) {   AllowJavascript();   const auto& list = args->GetListDeprecated();   CHECK(!list.empty());   **const bool enabled = list[0].GetBool();**   if (enabled) {     **EnableFakePhoneHubManager();**     return;   }   EnableRealPhoneHubManager(); } ... ... void MultidevicePhoneHubHandler::EnableRealPhoneHubManager() {   // If no FakePhoneHubManager is active, return early. This ensures that we   // don't unnecessarily re-initialize the Phone Hub UI.   if (!fake_phone_hub_manager_)     return;    PA_LOG(VERBOSE) << "Setting real Phone Hub Manager";   Profile* profile = Profile::FromWebUI(web_ui());   auto* phone_hub_manager =       phonehub::PhoneHubManagerFactory::GetForProfile(profile);   ash::SystemTray::Get()->SetPhoneHubManager(phone_hub_manager);    RemoveObservers();   fake_phone_hub_manager_.reset(); } ... void MultidevicePhoneHubHandler::EnableFakePhoneHubManager() {   DCHECK(!fake_phone_hub_manager_);   PA_LOG(VERBOSE) << "Setting fake Phone Hub Manager";   **fake_phone_hub_manager_ = std::make_unique<phonehub::FakePhoneHubManager>();** //--->[0]   ash::SystemTray::Get()->SetPhoneHubManager(**fake_phone_hub_manager_.get()**); // ---->[1]   AddObservers(); }  void PhoneHubUiController::SetPhoneHubManager(     phonehub::PhoneHubManager* phone_hub_manager) {   if (phone_hub_manager == phone_hub_manager_)     return;    **CleanUpPhoneHubManager();**  //---->[2]    **phone_hub_manager_ = phone_hub_manager;**  // ---->[1]   if (phone_hub_manager_) {     phone_hub_manager_->GetFeatureStatusProvider()->AddObserver(this);     phone_hub_manager_->GetOnboardingUiTracker()->AddObserver(this);     phone_hub_manager_->GetPhoneModel()->AddObserver(this);   }    UpdateUiState(GetUiStateFromPhoneHubManager()); }  void PhoneHubUiController::CleanUpPhoneHubManager() {   if (!phone_hub_manager_)     return;    **phone_hub_manager_->GetFeatureStatusProvider**()->RemoveObserver(this); //---->[2]   phone_hub_manager_->GetOnboardingUiTracker()->RemoveObserver(this);   phone_hub_manager_->GetPhoneModel()->RemoveObserver(this); } ``` |

[0] 当我们调用两次EnableFakePhoneHubManager, fake\_phone\_hub\_manager\_字段将会被初始化两次, 又由于fake\_phone\_hub\_manager\_是一个unique\_ptr，...