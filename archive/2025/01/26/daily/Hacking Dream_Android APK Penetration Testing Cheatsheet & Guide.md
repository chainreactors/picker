---
title: Android APK Penetration Testing Cheatsheet & Guide
url: https://www.hackingdream.net/2025/01/android-apk-penetration-testing-cheatsheet-guide.html
source: Hacking Dream
date: 2025-01-26
fetch_date: 2025-10-06T20:08:19.403594
---

# Android APK Penetration Testing Cheatsheet & Guide

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Android APK Penetration Testing Cheatsheet & Guide

[January 25, 2025](https://www.hackingdream.net/2025/01/android-apk-penetration-testing-cheatsheet-guide.html "permanent link")

Explore a step-by-step guide to Android APK penetration testing! This blog covers essential techniques such as decompiling APKs, analyzing `AndroidManifest.xml`, detecting exported activities, bypassing SSL pinning, and exploiting vulnerabilities using tools like APKTool, JADX, Burp Suite, and Drozer. Whether you're a beginner or an experienced pentester, this guide provides practical tips for uncovering security flaws in Android applications. Dive into the world of mobile app security and enhance your skills in ethical hacking and penetration testing!

[![Android_Penetration_Testing_Cheatsheet](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-bCzoehp_e-Q_CNZwPqLGbBicgCkf3Qj47y7k-OIMKZmzLHlVvdMjQ6d_Pr_YiC_uc3nCFQGOXj8vcO09Q7EsVhNmleYsrfwWZ2_Y7P3-uLFT9VHbmPC8X9ix1sZ-gboT4jSO2BOUMeqeH1yPoyrZHFM4JKV0ugfQPazJW0mGP6ybbWW4hB6EM9uMqSAD/w640-h640/Android_Penetration_Testing_Cheatsheet.jpg "Android_Penetration_Testing_Cheatsheet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-bCzoehp_e-Q_CNZwPqLGbBicgCkf3Qj47y7k-OIMKZmzLHlVvdMjQ6d_Pr_YiC_uc3nCFQGOXj8vcO09Q7EsVhNmleYsrfwWZ2_Y7P3-uLFT9VHbmPC8X9ix1sZ-gboT4jSO2BOUMeqeH1yPoyrZHFM4JKV0ugfQPazJW0mGP6ybbWW4hB6EM9uMqSAD/s700/Android_Penetration_Testing_Cheatsheet.jpg)

## Android Penetration Testing Basic Checklist

### Step 1: Run the APK in an Emulator

* Use **Android Studio** to set up and run the APK in an emulator. Do not run any unknown apk's on your personal devices.
* Understand the behavior of the application.

---

### Step 2: Decompile the APK

1. Use the following command with **apktool** to decompile the APK:

   ```
   apktool.bat -d applicationName.apk
   ```
2. Explore the contents, such as the `AndroidManifest.xml` file and the `resources` directory.

---

### Step 3: Analyze Decompiled Code with JADX

* Open the APK using `jadx-gui` for easy access to decompiled source code.

---

### Step 4: Review the AndroidManifest.xml File

Focus on the following areas:

1. **API Keys**: Look for exposed API keys.
2. **Content Providers**: Check for exported content providers (`exported="true"`).
3. **SdkVersion**: Analyze the minimum and target SDK versions.
4. **Permissions**: Ensure no unnecessary permissions are declared.
5. **Activities with `exported="true"`**:

   * Test whether such activities can be started using the following command:

     ```
     am start packageName/.activityName
     ```
   * Example:

     ```
     am start b3nac.injuredandroid/.b25lActivity
     ```
   * Verify no sensitive data exists in exported activities.
6. **Backups**: Identify if the app saves backup data during runtime.
7. **Debugging**: Check for debug flags or settings.

---

### Step 5: Exploit Exported Content Providers

Use **Drozer** for further analysis:

1. Run the following command to find accessible content providers:

   ```
   run app.provider.info -a com.app.name
   ```
2. Identify content URIs:

   ```
   run scanner.provider.finduris -a com.app.name
   ```
3. Query the content URI to fetch data:

   ```
   run app.provider.query content://com.app.name.provider.notesprovider/notes/
   ```

---

### Step 6: Review Decompiled Source Code

* In **jadx-gui**, navigate to:
  `Source Code → com → ApplicationName → MainActivity`.
* Analyze the following:
  + Classes and functions (Example: `f.class`).
  + Called functions or classes (double-click to follow references).
* Understand the application's logic and functionality.

---

### Step 7: Check for SSL Pinning

1. Configure a proxy (e.g., **Burp Suite**) on the emulator.
2. Install the Burp certificate on the emulator by downloading it from:

   ```
   http://burp
   ```
3. Start interception in Burp Suite and observe the traffic:
   * If traffic is visible, **SSL Pinning** is disabled.
   * If no traffic is seen, you’ll need to bypass SSL Pinning.

---

### Step 8: Bypassing SSL Pinning

#### Method 1: Using Objection

1. Patch the APK:

   ```
   objection patchapk --source applicationName.apk
   ```
2. Install the generated `patched.apk` on the emulator.
3. Reload the app; a blank screen may appear.
4. Start Objection :

   ```
   objection explore
   ```
5. Disable SSL Pinning:

   ```
   android sslpinning disable
   ```
6. Verify if traffic is now visible in Burp Suite.

#### Method 2: Manual Patching with Frida

* If the above method fails, refer to `Patching Manually using **Frida**` below.

---

### Step 9: Perform Manual Penetration Testing

* Once traffic interception is successful, perform a thorough **Web Penetration Test** to identify vulnerabilities in the application.

---

## Android Penetration Testing Cheatsheet

```
### Static Analysis

#Decompile the application
apktool d appication.apk

#Decompile without resources, use when the app is too huge
apktool d application.apk -r

#Search for strings in all locations
#Even lib directory can contain some useful source code an API key
#Use Strings on .so/ELF files
#smali directory contains the source code - but its not in readable format, need to use dex to jar converter

#### Locations to check for Secrets

- resources/res/values/strings.xml, xmls.xml, integers.xml, attrs.xml - find below strings
 - firebase_database_url
 - google_api_key
 - google_app_id
 - google_crash_reporting_api_key
 - google_storage_bucket
 - client_id
 - API
 - password
 - AWS
 - Secret
 - http:// or https://
 - .db or .sqllite or SQL

or better use jadx-gui from
https://github.com/skylot/jadx/releases/tag/v1.5.0
```

```
### ADB Commands

ADB Cheatsheet is here

#Port forward a port from the Android device to ADB
sudo ssh -p 22 -L 5555:127.0.0.1:5555 bhanu@steins.local

#Connect to a device over wireless
adb tcpip 9090

#connect to the service
adb connect 127.0.0.1:5555

#list connected devices
adb devices

#get a shell from a selected device
#adb -s device_name shell
adb -s 127.0.0.1:5555 shell

#get a shell
adb shell

#get root privs from a shell
su

#install an apk
adb -s "25sdfsfb3801745eg" install "C:\Users\bhanu\Downloads\shell.apk"

#Getting screenshots
adb shell screencap <path to save>

#Recording the screen
adb shell screenrecord <path to save>

#Downloading files
adb pull <source file path> <destination file path>

#Uploading files
adb push <source file path> <d...