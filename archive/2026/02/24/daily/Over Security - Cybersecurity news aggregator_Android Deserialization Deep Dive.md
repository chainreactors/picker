---
title: Android Deserialization Deep Dive
url: https://www.hacktivesecurity.com/blog/2025/03/13/android-deserialization-deep-dive/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-24
fetch_date: 2026-02-25T04:14:55.705617
---

# Android Deserialization Deep Dive

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
* Android Deserialization Deep Dive

[Mobile](https://www.hacktivesecurity.com/blog/category/mobile/)

![](https://www.hacktivesecurity.com/wp-content/uploads/2025/03/hacktivesec_06672_transparent_back_google_pixel_showing_all_e_462e110a-049c-44ae-ac57-7818732623bc_1.png)

\_ [March 13, 2025](https://www.hacktivesecurity.com/blog/2025/03/13/android-deserialization-deep-dive/)\_ [Alessandro Groppo](https://www.hacktivesecurity.com/blog/author/kiks/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2025/03/13/android-deserialization-deep-dive/#respond)

### Android Deserialization Deep Dive

## Introduction

Serialization and deserialization mechanisms are always risky operations from a security point of view. In most languages and frameworks, if an attacker is able to deserialize arbitrary input (or just corrupt it as we have demonstrated years ago with the Rusty Joomla RCE) the impact is usually the most critical: Remote Code Execution. Without re-explaining the wheel, since there are already multiple good resources online that explains the basic concepts of insecure deserialization issues, we would like to put our attention into an interesting android API and class: `getSerializableExtra` and `Serializable`.

## getSerializableExtra introduction

The [`getSerializableExtra`](https://developer.android.com/reference/android/content/Intent#getSerializableExtra(java.lang.String)) API, from the [`Intent`](https://developer.android.com/reference/android/content/Intent#getSerializableExtra(java.lang.String,%20java.lang.Class%3CT%3E)) class, permits to retrieve a [`Serializable`](https://developer.android.com/reference/java/io/Serializable) object through an extra parameter of a receiving Intent and, if the component is exported and enabled, it can represents an interesting attack surface from an attacker point of view. The `getSerializableExtra(String name)` has been deprecated in Android API level 33 (Android 13) in favor of the type safer `getSerializableExtra(String name, Class<T> clazz)`. The [`Serializable`](https://developer.android.com/reference/java/io/Serializable) class documentation, that enables object deserialization, contains the following bold text:

> **Warning: Deserialization of untrusted data is inherently dangerous and should be avoided. Untrusted data should be carefully validated.**

Since we already know the generic risks of deserializing an arbitrary input object, the objective of this deep dive is to understand the real consequences of calling `getSerializableExtra` on arbitrary input with and without the type safer parameter.

## getSerializableExtra internal code overview

### First steps

What’s better than actually begin by reading the source code of the API in our interest? We think nothing, so this is the summary of the `getSerializableExtra` flow using AOSP on Android 15: `Intent::getSerializableExtra` => `Bundle::getSerializable` => `BaseBundle::getSerializable` => `BaseBundle::getValue` => `..`.

```
// Intent::getSerializableExtra
public @Nullable Serializable getSerializableExtra(String name) {
    return mExtras == null ? null : mExtras.getSerializable(name);
}

// Bundle::getSerializable
public Serializable getSerializable(@Nullable String key) {
    return super.getSerializable(key);
}

// BaseBundle::getSerializable
Serializable getSerializable(@Nullable String key) {
    unparcel();
    Object o = getValue(key);
    if (o == null) {
        return null;
    }
    try {
        return (Serializable) o;
    } catch (ClassCastException e) {
        typeWarning(key, o, "Serializable", e);
        return null;
    }
}

// BaseBundle::getValue
final Object getValue(String key) {
	return getValue(key, /* clazz */ null);
}

// BaseBundle::getValue
final <T> T getValue(String key, @Nullable Class<T> clazz) {
	// Avoids allocating Class[0] array
	return getValue(key, clazz, (Class<?>[]) null);
}
// BaseBundle::getValue
final <T> T getValue(String key, @Nullable Class<T> clazz, @Nullable Class<?>... itemTypes) {
	int i = mMap.indexOfKey(key);
	return (i >= 0) ? getValueAt(i, clazz, itemTypes) : null;
}

// BaseBundle::getValueAt
final <T> T getValueAt(int i, @Nullable Class<T> clazz, @Nullable Class<?>... itemTypes) {
	Object object = mMap.valueAt(i);
	if (object instanceof BiFunction<?, ?, ?>) {
		synchronized (this) {
			object = unwrapLazyValueFromMapLocked(i, clazz, ...