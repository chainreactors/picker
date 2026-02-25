---
title: Android Deep Dive: Implicit Intents
url: https://www.hacktivesecurity.com/blog/2025/02/12/android-deep-dive-implicit-intents/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-24
fetch_date: 2026-02-25T04:14:54.032005
---

# Android Deep Dive: Implicit Intents

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
* Android Deep Dive: Implicit Intents

[Mobile](https://www.hacktivesecurity.com/blog/category/mobile/)

![](https://www.hacktivesecurity.com/wp-content/uploads/2025/02/hacktivesec_06672_transparent_back_google_pixel_showing_all_e_e1617f16-cac6-4a8e-a7fe-2eed53781b6e_3.png)

\_ [February 12, 2025](https://www.hacktivesecurity.com/blog/2025/02/12/android-deep-dive-implicit-intents/)\_ [Alessandro Groppo](https://www.hacktivesecurity.com/blog/author/kiks/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2025/02/12/android-deep-dive-implicit-intents/#respond)

### Android Deep Dive: Implicit Intents

## Introduction

From the official Android documentation, the `Intent` is described as “an abstract description of an operation to be performed”. Conceptually, it can be simplified as an “intention to do something with another application” across Inter-Process Communication (IPC). One of the most interesting facility that intents offer is the implicit resolution. An application can explicitly declare to handle specific intents (through the `<intent-filter>` declaration) and these intents are ***magically*** delivered to it from other applications, without the knowledge of the final destination package. Since magic can be hypothetically just defined as a form of ignorance (*at least* in computer science?), let’s see where the “magic” happens in the Android source code!

## Intent registration

### Starting from the beginning

Let’s start from an application point of view that needs to handle specific actions: an `<intent-filter>` is declared inside the `AndroidManifest.xml`:

```
<component android:name>
	<intent-filter>
		<action android:name="android.intent.action.VIEW">
		<category android:name="android.intent.category.DEFAULT"/>
		<data android:scheme="scheme"/>
	</intent-filter>
</component>
```

In this example, the `component` can be of any type: an `activity`, `receiver`, `service` or `provider`. Some filters are also specified in order to discriminate matching events that the component is interested into: `action`, `category` and `data` (with the `android:scheme` attribute) are specifically used in this case (check out the [<intent-filter> documentation](https://developer.android.com/guide/topics/manifest/intent-filter-element) for more filters and options). At install time, the [`PackageInstaller`](https://developer.android.com/reference/android/content/pm/PackageInstaller) service is responsible to install the application and all its components, including intent filters. More specifically, diving into the AOSP (Android Open Source Project) codebase, it is possible to identify some key functions that parse all declared components. More specifically, the [`ComponentResolver::addAllComponents`](https://cs.android.com/android/platform/superproject/%2B/android-14.0.0_r37%3Aframeworks/base/services/core/java/com/android/server/pm/resolution/ComponentResolver.java;drc=4bf59a583eefeb8b27a79fbd1fc5093ddb79d747;l=191) method calls four methods that parse all components’ details.

```
    public void addAllComponents(/*..*/){
        /*..*/
        synchronized (mLock) {
            addActivitiesLocked(computer, pkg, newIntents, chatty);
            addReceiversLocked(computer, pkg, chatty);
            addProvidersLocked(computer, pkg, chatty);
            addServicesLocked(computer, pkg, chatty);
            onChanged();
        }
        /*..*/
```

Following the `Add[Component]Locked` logic, components are registered based on their type on specific variables (e.g. `mActivities`, `mProviders`, `mReceivers` and `mServices`) and then intent filters are parsed. Let’s take the activity parsing as an example to reference some code, but the concept is the same across all different components. `addActivitiesLocked` calls [`mActivities.addActivity`](https://cs.android.com/android/platform/superproject/%2B/android-14.0.0_r37%3Aframeworks/base/services/core/java/com/android/server/pm/resolution/ComponentResolver.java;l=282) (part of the `ComponentResolver` class) that calls `addFilter` for each declared intent filter.

```
	// code cutted for demonstration purposes
	protected void addActivity(@NonNull Computer computer, ParsedActivity a, String type,
			List<Pair<ParsedActivity, ParsedIntentInfo>> newIntents) {
		final int intentsSize = a.getIntents().size();
		for (int j = 0; j < intentsSize; j++) {
			Pars...