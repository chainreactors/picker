---
title: Xposed检测绕过
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458496362&idx=2&sn=a59532e93ce90ec59e2310070045c837&chksm=b18e9de086f914f61aa296885f1a9e02c10b36d7e406aa1f56213a58952f50689cbdbf8ff79c&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-03-04
fetch_date: 2025-10-04T08:39:06.749664
---

# Xposed检测绕过

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jlvPLqc00h99N4iaWBmEROXkBSIsTR83nUbHwmvV2Bfic6ic0HkM9M0buTA/0?wx_fmt=jpeg)

# Xposed检测绕过

那年没下雪

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FZfAJlzgym2qq3cobb79jltjPyoBvz4iciccKTNuFnIxxzohG6JiaTyp13tVL60QtKfx4umfK7IibjLA/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：那年没下雪

分享一些Xposed检测绕过的总结，很多加壳软件检测到xposed就会杀死当前软件进程。

1、绕过jar Class检测

```
// 过防止调用loadClass加载 de.robv.android.xposed.        XposedHelpers.findAndHookMethod(ClassLoader.class, "loadClass", String.class, new XC_MethodHook() {            @Override            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {                if(param.args != null && param.args[0] != null && param.args[0].toString().startsWith("de.robv.android.xposed.")){                     // 改成一个不存在的类                    param.args[0] = "de.robv.android.xposed.ThTest";                }                 super.beforeHookedMethod(param);            }        });
```

2、绕过堆栈检测

```
XposedHelpers.findAndHookMethod(StackTraceElement.class, "getClassName", new XC_MethodHook() {            @Override            protected void afterHookedMethod(MethodHookParam param) throws Throwable {                String result = (String) param.getResult();                if (result != null){                    if (result.contains("de.robv.android.xposed.")) {                        param.setResult("");                        // Log.i(tag, "替换了，字符串名称 " + result);                    }else if(result.contains("com.android.internal.os.ZygoteInit")){                        param.setResult("");                    }                }                 super.afterHookedMethod(param);            }        });
```

3、绕过包名检测

```
findAndHookMethod("android.app.ApplicationPackageManager", lpparam.classLoader, "getInstalledApplications", int.class, new XC_MethodHook() {            @SuppressWarnings("unchecked")            @Override            protected void afterHookedMethod(MethodHookParam param) throws Throwable { // Hook after getIntalledApplications is called                if (debugPref) {                    XposedBridge.log("Hooked getInstalledApplications");                }                 List<ApplicationInfo> packages = (List<ApplicationInfo>) param.getResult(); // Get the results from the method call                Iterator<ApplicationInfo> iter = packages.iterator();                ApplicationInfo tempAppInfo;                String tempPackageName;                  // Iterate through the list of ApplicationInfo and remove any mentions that match a keyword in the keywordSet                while (iter.hasNext()) {                    tempAppInfo = iter.next();                    tempPackageName = tempAppInfo.packageName;                    if (tempPackageName != null && tempPackageName.equals("de.robv.android.xposed.installer")) {                        iter.remove();                        if (debugPref) {                            XposedBridge.log("Found and hid package: " + tempPackageName);                        }                    }                }                 param.setResult(packages); // Set the return value to the clean list            }        });
```

4、绕过jar文件检测：

```
Constructor<?> constructLayoutParams = findConstructorExact(java.io.File.class, String.class);        XposedBridge.hookMethod(constructLayoutParams, new XC_MethodHook(XCallback.PRIORITY_HIGHEST) {            @Override            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {                if (param.args[0] != null) {                    if (debugPref) {                        XposedBridge.log("File: Found a File constructor: " + ((String) param.args[0]));                    }                }                 if (isRootCloakLoadingPref) {                    // RootCloak is trying to load it's preferences, we shouldn't block this.                    return;                }                if (((String) param.args[0]).contains("XposedBridge")) {                    if (debugPref) {                        XposedBridge.log("File: Found a File constructor with word super, noshufou, or chainfire");                    }                    param.args[0] = "/system/app/" + FAKE_FILE;                }            }        });
```

5、绕过maps检测

```
XposedHelpers.findAndHookConstructor("java.io.FileReader",lpparam.classLoader ,String.class , new XC_MethodHook() {          @Override          protected void beforeHookedMethod(MethodHookParam param) throws Throwable {              String arg0 = (String) param.args[0];              if(arg0.toLowerCase().contains("/proc/")){                  param.setResult(null);              }          }      });
```

6、绕过vxp检测

```
XposedHelpers.findAndHookMethod("java.lang.System", lpparam.classLoader, "getProperty", String.class, new XC_MethodHook() {           @Override           protected void beforeHookedMethod(MethodHookParam param) throws Throwable {               String arg0 = (String)param.args[0];               if(arg0.equals("vxp")){                   param.setResult(null);               }           }       });
```

7、绕过SO检测

```
findAndHookMethod("java.lang.Runtime", lpparam.classLoader, "exec", String[].class, String[].class, File.class, new XC_MethodHook() {           @Override           protected void beforeHookedMethod(MethodHookParam param) throws Throwable {               if (debugPref) {                   XposedBridge.log("Hooked Runtime.exec");               }                String[] execArray = (String[]) param.args[0]; // Grab the tokenized array of commands               if ((execArray != null) && (execArray.length >= 1)) { // Do some checking so we don't break anything                   String firstParam = execArray[0]; // firstParam is going to be the main command/program being run                   if (debugPref) { // If debugging is on, print out what is being called                       String tempString = "Exec Command:";                       for (String temp : execArray) {                           tempString = tempString + " " + temp;                       }                       XposedBridge.log(tempString);                   }                    if (stringEndsWithFromSet(firstParam, commandSet)) { // Check if the firstParam is one of the keywords we want to filter                       if (debugPref) {                           XposedBridge.log("Found blacklisted command at the end of the string: " + firstParam);                       }                        // A bunch of logic follows since the solution depends on which command is being called                       // TODO: ***Clean up this logic***                       if (commandSet.contains("ls") && execArray.length >= 3 && execArray[1].contains("lib")) {                           param.setThrowable(new IOException());                       } else {                           param.setThrowable(new IOException());                       }                        if (debugPref && param.getThrowable() == null) { // Print out the new command if debugging is on                           String tempString = "New Exec Command:";                           for (String temp : (String[]) param.args[0]) {                               tempString = tempString + " " + temp;                           }                           XposedBridge.log(tempString);                       }                   }               } else {                   if (debugPref) {                       XposedBridge.log("Null or empty array on exec");                   }               }           }       });
```

8、绕过ClassPath检测

```
XposedHelpers.findAndHookMethod("java.lang.System", lpparam.classLoader, "getenv", String.class, new XC_MethodHook() {           @Override           protected void beforeHookedMethod(MethodHookParam param) throws Throwable {               String arg0 = (String)param.args[0];               if(arg0.equals("CLASSPATH")){                   param....