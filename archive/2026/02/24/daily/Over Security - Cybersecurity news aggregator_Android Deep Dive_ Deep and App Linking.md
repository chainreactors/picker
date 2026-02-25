---
title: Android Deep Dive: Deep and App Linking
url: https://www.hacktivesecurity.com/blog/2025/02/18/android-deep-dive-deep-and-app-linking/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-24
fetch_date: 2026-02-25T04:14:54.829608
---

# Android Deep Dive: Deep and App Linking

* info@hacktivesecurity.com
* Mon - Fri: 9.00 am - 6.00 pm

Advanced Security Solutions to protect the Cyberspace.

[Twitter](https://x.com/hacktivesec)

[Facebook-f](https://www.facebook.com/hacktivesec)

[Linkedin-in](https://www.linkedin.com/company/hacktive-security/)

[Instagram](https://www.instagram.com/hacktivesec/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

Search for:

### Have Any Questions?

+39-06-8773-8747

[free quote](https://www.hacktivesecurity.com/index.php/contacts/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Search for:

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

[![Hacktive Security](http://176.31.202.211/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Over 10 years we help companies reach their financial and branding goals. Engitech is a values-driven technology agency dedicated.

#### Gallery

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1.jpg)

#### Contacts

Via Giosuè Carducci, 21 - Pomigliano d'Arco (Italy)
Paseo Montjuic, número 30 - Barcelona (Spain)

info@hacktivesecurity.com

+39 06 8773 8747

[Twitter](#hacktivesec)

Facebook-f

Pinterest-p

Instagram

# Hacktive Blog

* [Home](https://www.hacktivesecurity.com)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Mobile](https://www.hacktivesecurity.com/blog/category/mobile/)
* Android Deep Dive: Deep and App Linking

[Mobile](https://www.hacktivesecurity.com/blog/category/mobile/)

![](https://www.hacktivesecurity.com/wp-content/uploads/2025/02/hacktivesec_06672_transparent_back_google_pixel_showing_all_e_fdabe135-3221-4ed2-8ff1-da9ea52bd5eb_3.png)

\_ [February 18, 2025](https://www.hacktivesecurity.com/blog/2025/02/18/android-deep-dive-deep-and-app-linking/)\_ [Alessandro Groppo](https://www.hacktivesecurity.com/blog/author/kiks/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2025/02/18/android-deep-dive-deep-and-app-linking/#respond)

### Android Deep Dive: Deep and App Linking

## Introduction

In the [previous blog post](https://www.hacktivesecurity.com/blog/2025/02/12/android-deep-dive-implicit-intents/) we have covered some internal parts of the codebase that are involved in the intent registration and resolution process. In this one we are going to deepen Deep and App Link resolutions in the Android Operating System and its remote Attack Surface. Deep and App Links are data components that permit to associate a specific link to a specific app component. In order to further detail their usage across the Android system, let’s start with a Deep Link introduction.

## Deep Link

Suppose that you are an app developer and you want to make some of your android app components reachable from an external source (e.g. a browser or another application), and you want an “universal” and standard solution: that’s where Deep Links come in place! For example, you can have a link like `privateapp://app/login?username=user` that can be called anywhere (almost) and leads to your application execution logic. Moreover, you have a standard approach that you can use to register an arbitrary schema, host and path and you can also pass and receive parameters like a classic web URL. Deep Links are declared in the `AndroidManifest.xml` application file with an `<intent-filter>` declaration inside the targeted component (that can be an activity, service, receiver or provider). The following declaration can match the previously mentioned example:

```
<activity android:name=".TargetLoginActivity">
	<intent-filter>
		<action android:name="android.intent.action.VIEW">
		<category android:name="android.intent.category.DEFAULT"/>
		<category android:name="android.intent.category.BROWSABLE"/>
		<data android:scheme="privateapp"/>
		<data android:host="app"/>
		<data android:path="login"/>
	</intent-filter>
</activity>
```

As can be seen the `android:scheme`, `android:host` and `android:path` attributes (more attributes can be found in the [documentation](https://developer.android.com/guide/topics/manifest/data-element)) of the `<data>` tag are used to register the specific URI to handle. Another common approach is to use a single `<data>` tag, but seems discouraged from the official documentation:

```
<activity android:name=".TargetLoginActivity">
	<intent-filter>
		<action android:name="android.intent.action.VIEW">
		<category android:name="android.intent.category.DEFAULT"/>
		<category android:name="android.intent.category.BROWSABLE"/>
		<data android:scheme="privateapp"
			android:host="app"
			android:path="login"/>
	</intent-filter>
</activity>
```

The internal classification, as explained in the previous blog post, is of type `Schemes` but can also contains some MIME types and fall inside other categorizations too (that can be enumerated with `dumpsys package`).

### Actions and Categories

An important aspect of a Deep Link reachability is the declared actions and categories. Not all deep links are intended to be reachable from anywhere but an interesting behaviour is that the link can dropped “anywhere” (e.g. in a browser inside the `<a>` element) and a click into it will results into an **implicit intent** sent from the browser to the android system, that will take care of the resolution to the appropriate destination (as explained in the first article). For that reason, actions and categories have a fundamental role:

* [`ACTION_VIEW`](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW): The VIEW action is the default action that is sent if a link is clicked from an `<a>` element or a button from web page. It is useful to be specified inside the `intent-filter` declaration if the intention is to reach the link from a simple click.
* [`CATEGORY_BROWSABL...