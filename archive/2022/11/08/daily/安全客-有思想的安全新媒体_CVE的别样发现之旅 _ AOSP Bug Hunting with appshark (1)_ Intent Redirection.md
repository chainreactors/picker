---
title: CVE的别样发现之旅 | AOSP Bug Hunting with appshark (1): Intent Redirection
url: https://www.anquanke.com/post/id/282588
source: 安全客-有思想的安全新媒体
date: 2022-11-08
fetch_date: 2025-10-03T21:54:05.595194
---

# CVE的别样发现之旅 | AOSP Bug Hunting with appshark (1): Intent Redirection

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

# CVE的别样发现之旅 | AOSP Bug Hunting with appshark (1): Intent Redirection

阅读量**373329**

发布时间 : 2022-11-07 14:30:09

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 一、背景

LaunchAnywhere是安卓最为经典的漏洞类型之一，现在被Google称为Intent Redirection：[https://support.google.com/faqs/answer/9267555?hl=en。](https://support.google.com/faqs/answer/9267555?hl=en%E3%80%82) 无恒实验室一直对该类型漏洞有研究，我们把这一类问题比作“安卓上的SSRF”，其中Intent就像一个HTTP请求，而未经验证完全转发了这个请求在安卓上会导致严重的安全问题。关于这类漏洞的逻辑与利用，推荐阅读[http://retme.net/index.php/2014/08/20/launchAnyWhere.html这篇文章。](http://retme.net/index.php/2014/08/20/launchAnyWhere.html%E8%BF%99%E7%AF%87%E6%96%87%E7%AB%A0%E3%80%82)

本文将介绍使用appshark引擎挖掘AOSP中Intent Redirection漏洞的一个实际例子，发现的问题被Google评为高危并授予了CVE-2021-39707 & CVE-2022-20223。appshark为无恒实验室自研的自动化漏洞及隐私合规检测工具，当前工具已开源，欢迎感兴趣的朋友试用，开源地址：[http://github.com/bytedance/appshark。](http://github.com/bytedance/appshark%E3%80%82)

## 二、appshark规则编写

为了简化问题，我们使用一个非常基础的规则IntentRedirectionBabyVersion：

```
{
    "IntentRedirectionNoSan": {
      "enable": true,
      "SliceMode": true,
      "traceDepth": 6,
      "desc": {
        "name": "IntentRedirectionBabyVersion",
        "category": "IntentRedirection",
        "detail": "Intent redirection, but a very basic version",
        "wiki": "",
        "possibility": "2",
        "model": "high"
      },
      "entry": {},
      "source": {
        "Return": [
          "<android.content.Intent: android.os.Parcelable getParcelable*(java.lang.String)>",
          "<android.os.Bundle: android.os.Parcelable getParcelable*(java.lang.String)>"
        ]
      },
      "sink": {
        "<*: * startActivit*(*)>": {
          "LibraryOnly": true,
          "TaintParamType": [
            "android.content.Intent",
            "android.content.Intent[]"
          ],
          "TaintCheck": [
            "p*"
          ]
        }
      }
    }
  }
```

可以看到这个规则仅仅考虑从getParcelable到startActivity的数据流，且不考虑sanitizer。这和我们实际使用的规则有一些差别，但足够说明问题。

这里我们扫描的目标是com.android.settings，也就是“Settings”应用。作为一个具有system uid的高权限应用，Settings是AOSP漏洞挖掘的常见目标。

## 三、人工排查与漏洞原理

### 3.1 漏洞原理

扫描出的结果较多，并不是全都可用的，尤其是我们并没有设置任何的sanitizer。经过人工逐个检查，我们发现这一条扫描结果看上去可利用性很高：

```
{
    "details": {
        "position": "<com.android.settings.users.AppRestrictionsFragment$RestrictionsResultReceiver: void onReceive(android.content.Context,android.content.Intent)>",
        "Sink": [
            "<com.android.settings.users.AppRestrictionsFragment$RestrictionsResultReceiver: void onReceive(android.content.Context,android.content.Intent)>->$r2_1"
        ],
        "entryMethod": "<com.android.settings.users.AppRestrictionsFragment$RestrictionsResultReceiver: void onReceive(android.content.Context,android.content.Intent)>",
        "Source": [
            "<com.android.settings.users.AppRestrictionsFragment$RestrictionsResultReceiver: void onReceive(android.content.Context,android.content.Intent)>->$r5"
        ],
        "url": "/Users/admin/submodules/appshark/out/vulnerability/17-IntentRedirectionBabyVersion.html",
        "target": [
            "<com.android.settings.users.AppRestrictionsFragment$RestrictionsResultReceiver: void onReceive(android.content.Context,android.content.Intent)>->$r5",
            "<com.android.settings.users.AppRestrictionsFragment$RestrictionsResultReceiver: void onReceive(android.content.Context,android.content.Intent)>->$r2_1"
        ]
    },
    "hash": "9bfcf0665601df186b025859e4f4c2df4e5f9cb2",
    "possibility": "2"
}
```

其对应的代码在AOSP中的位置为[https://android.googlesource.com/platform/packages/apps/Settings/+/refs/tags/android-12.0.0\_r30/src/com/android/settings/users/AppRestrictionsFragment.java#630：](https://android.googlesource.com/platform/packages/apps/Settings/%2B/refs/tags/android-12.0.0_r30/src/com/android/settings/users/AppRestrictionsFragment.java#630%EF%BC%9A)

```
        public void onReceive(Context context, Intent intent) {
            Bundle results = getResultExtras(true);
            final ArrayList<RestrictionEntry> restrictions = results.getParcelableArrayList(
                    Intent.EXTRA_RESTRICTIONS_LIST);
            Intent restrictionsIntent = results.getParcelable(CUSTOM_RESTRICTIONS_INTENT);
            if (restrictions != null && restrictionsIntent == null) {
                onRestrictionsReceived(preference, restrictions);
                if (mRestrictedProfile) {
                    mUserManager.setApplicationRestrictions(packageName,
                            RestrictionsManager.convertRestrictionsToBundle(restrictions), mUser);
                }
            } else if (restrictionsIntent != null) {
                preference.setRestrictions(restrictions);
                if (invokeIfCustom && AppRestrictionsFragment.this.isResumed()) {
                    assertSafeToStartCustomActivity(restrictionsIntent);
                    int requestCode = generateCustomActivityRequestCode(
                            RestrictionsResultReceiver.this.preference);
                    AppRestrictionsFragment.this.startActivityForResult(
                            restrictionsIntent, requestCode);
                }
            }
        }
```

注意到Google考虑了这个地方有可能存在Intent Redirection导致的越权，因此添加了一个assertSafeToStartCustomActivity作为安全检查：

```
        private void assertSafeToStartCustomActivity(Intent intent) {
            // Activity can be started if it belongs to the same app
            if (intent.getPackage() != null && intent.getPackage().equals(packageName)) {
                return;
            }
            // Activity can be started if intent resolves to multiple activities
            List<ResolveInfo> resolveInfos = AppRestrictionsFragment.this.mPackageManager
                    .queryIntentActivities(intent, 0 /* no flags */);
            if (resolveInfos.size() != 1) {
                return;
            }
            // Prevent potential privilege escalation
            ActivityInfo activityInfo = resolveInfos.get(0).activityInfo;
            if (!packageName.equals(activityInfo.packageName)) {
                throw new SecurityException("Application " + packageName
                        + " is not allowed to start activity " + intent);
            }
        }
    }
```

然而，这个十几行的检查函数远远不够安全，现在我们知道其中实际上隐藏了两个可以被绕过的逻辑。最开始被注意到的是第7-11行的代码，假如有多个Activity符合这个Intent，则这个检查会直接通过：

```
            // Activity can be started if intent resolves to multiple activities
            List<ResolveInfo> resolveInfos = AppRestrictionsFragment.this.mPackageManager
                    .queryIntentActivities(intent, 0 /* no flags */);
            if (resolveInfos.size() != 1) {
                return;
            }
```

Intent假如有多个符合的Activity，会触发用户选择的逻辑。即便我们假设这个选择过程中用户不会因为操作产生安全问题，仅仅依靠`resolveInfos.size() != 1` 也不能保证选择流程会出现，原因是Activity在Manifest中有一个配置叫做`android:priority` ，即优先级。这个配置在AOSP的系统应用中很常见，当Intent可以resolve到多个Activity时，如果其中存在高优先级的Activity则会被直接选择，并不会触发用户选择的流程。因此，假如我们能找到某个存在`priority > 0` 且本身具有利用价值的Activity，则可以直接通过Intent Redirection进行利用。很不巧的是，最常见的可利用Activity正好满足这一条件：

```
        <activity-alias android:name="PrivilegedCallActivity"
             android:targetActivity=".components.UserCallActivity"
             android:permission="android.permission.CALL_PRIVILEGED"
             android:exported="true"
             android:process=":ui">
            <intent-filter android:priority="1000">
                <action android:name="android.intent.action.CALL_PRIVILEGED"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <data android:scheme="tel"/>
            </intent-filter>
```

PrivilegedCallActivity需要CALL\_PRIVILEGED权限才能被调用，这一权限仅仅赋予系统应用，第三方应用无法获得。通过这个Activity我们可以直接让手机拨打任意电话（包括紧急电话），合适的利用可以造成“窃听”的效果。

### 3.2 ...