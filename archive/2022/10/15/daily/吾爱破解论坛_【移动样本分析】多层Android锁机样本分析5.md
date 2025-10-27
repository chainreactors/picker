---
title: 【移动样本分析】多层Android锁机样本分析5
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651138526&idx=1&sn=3a711c3e2cbaa17ca6576987b12a91a6&chksm=bd50b98a8a27309ccaf2fb527954a57f8af1eae7bda3740416a63e2424e89dbfb02fbee9403b&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2022-10-15
fetch_date: 2025-10-03T19:57:05.231256
---

# 【移动样本分析】多层Android锁机样本分析5

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJbRMLH9riaaSnUX2qtTvJhYicwYlsxicEKERdAOjZOFtfAia3BeypsDNznhWicuYI2ibfqosW2vicW6wS0g/0?wx_fmt=jpeg)

# 【移动样本分析】多层Android锁机样本分析5

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：小骚**

# Contacts联系人

```
 复制代码 隐藏代码
包名:com.fock.lock
MD5值:0c298c0f5a8847753dd6d352d7a30be8
文件大小:936.80 KB
来源:某三楼
```

## 用到的工具

* 模拟器+Xposed
* android studio(看日志和运算结果)
* jeb或者任何可以反编译apk工具

## 入口分析

* 从 AndroidManifest.xml 分析入口以及服务 主启动页面是 MainActivity 进去看看

```
 复制代码 隐藏代码

<application
android:allowBackup="true"
android:debuggable="true"
android:icon="@drawable/MT_Bin"
android:label="@string/MT_Bin"
android:theme="@style/MT_Bin">

    <activity android:name=".MainActivity">
      <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
      </intent-filter>
    </activity>

    <service android:enabled="true" android:exported="true" android:name=".MyService"/>

    <receiver android:exported="true" android:name=".AutoBroadcast">
    <intent-filter android:priority="2147483647">
        <action android:name="com.fock.lock.js"/>
        <action android:name="android.intent.action.BATTERY_CHANGED"/>
        <action android:name="android.intent.action.DATA_ACTIVITY"/>
        <action android:name="android.intent.action.DATA_STATE"/>
        <action android:name="android.intent.action.DATE_CHANGED"/>
        <action android:name="android.server.checkin.FOTA_CANCEL"/>
        <action android:name="android.intent.action.MEDIABUTTON"/>
        <action android:name="android.intent.action.MEDIA_MOUNTED"/>
        <action android:name="android.intent.action.MEDIA_SCANNER_STARTED"/>
        <action android:name="android.intent.action.MEDIA_SCANNER_FINISHED"/>
        <action android:name="android.intent.action.TIME_SET"/>
        <action android:name="android.intent.action.TIME_TICK"/>
        <action android:name="android.intent.action.UMS_CONNECTED"/>
        <action android:name="android.intent.action.WALLPAPER_CHANGED"/>
        <action android:name="android.intent.action.PACKAGE_ADDED"/>
        <action android:name="android.intent.action.PACKAGE_REMOVED"/>
        <action android:name="android.intent.action.PHONE_STATE"/>
        <action android:name="android.intent.action.SCREEN_OFF"/>
        <action android:name="android.intent.action.SCREEN_ON"/>
        <action android:name="android.intent.action.SERVICE_STATE"/>
        <action android:name="android.intent.action.SIG_STR"/>
        <action android:name="android.intent.category.ALTERNATIVE"/>
        <action android:name="android.intent.action.SETTINGS"/>
        <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
        <action android:name="android.net.wifi.WIFI_STATE_CHANGED"/>
        <action android:name="android.net.wifi.STATE_CHANGE"/>
        <action android:name="android.intent.action.REBOOT"/>
        <action android:name="android.intent.action.USER_PRESENT"/>
        <category android:name="android.intent.category.HOME"/>
      </intent-filter>
</receiver>
  </application>
```

* MainActivity 里面就启动一个服务,到 MyService 这个服务里面看看

```
 复制代码 隐藏代码

public class MainActivity extends Activity {
    home.php?mod=space&uid=1892347  // android.app.Activity
    protected void onCreate(Bundle bundle0) {
        LogCatBroadcaster.start(this);
        super.onCreate(bundle0);
        this.startService(new Intent(this, MyService.class));
    }

    @Override  // android.app.Activity
    protected void onDestroy() {
        super.onDestroy();
    }
}
```

* MyService 的 onCreate 函数 执行了 L 方法，发现这个就是第一层的代码

```
 复制代码 隐藏代码

    @Override  // android.app.Service
    public void onCreate() {
        super.onCreate();
        this.fv = new FloatView(this.getApplicationContext());
        this.L();
    }
```

## 第一层分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJbRMLH9riaaSnUX2qtTvJhYiaTEv8WR26pO2F8FbP9pQNeDfb8aKicWccor1Tsbzg1Kc9jcltXQgEYg/640?wx_fmt=png)

* 先看初始化了哪些东西
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJbRMLH9riaaSnUX2qtTvJhYeicRLs8Sbibiaib7Qa1ibSLhyHAC3up3Bib3UtLhQibD0HzSUqVHNytVTJticg/640?wx_fmt=png)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJbRMLH9riaaSnUX2qtTvJhYjTnBODGncjlb8VUHGC3QoXAZJoiczM9hzYao1AYeGSuSLziaiaUGAwfUA/640?wx_fmt=png)
* 到点击事件分析,发现解锁算法用到了两个参数

```
 复制代码 隐藏代码

        @Override  // android.view.View$OnClickListener
        public void onClick(View view0) {
            if(MyService.this.lp.getText().toString().trim().length() == 0) {
                return;
            }

            // 解锁算法
            if(MyService.this.lp.getText().toString().equals("" + (MyService.this.ck / this.val$Admin ^ MyService.sb(Integer.parseInt(this.val$清))))) {
                MyService.this.fv.removeView();
                MyService.this.Z();
                return;
            }

            MyService.this.密码错误.setVisibility(0);
            MyService.this.密码错误.setText("密码错误联系半支烟QQxxxxxxxx解锁");
            Runnable runnable0 = MyService.this.runn;
            MyService.this.hand.postDelayed(runnable0, 2000L);
        }
```

* 使用 YukiHookAPI(Xposed) Hook 获取关键参数

```
 复制代码 隐藏代码

// 类名
 findClass("com.fock.lock.MyService\$100000012").hook {
                injectMember {
                    method {
                        // 方法名
                        name = "onClick"
                        // 参数
                        param(ViewClass)
                        // 返回值
                        returnType = UnitType
                    }
                    // 方法执行后
                    afterHook {
                        // 反射获取
                        val admin = instance.getParam<Int>("val\$Admin")
                        val 清 = instance.getParam<String>("val\$清")
                        打印结果
                        loggerE(msg = "admin: $admin\n清: $清")
                    }
                }

            }
```

* 还原最终密码运算

```
 复制代码 隐藏代码

 // Kotlin 写法
 private fun 第一层() {
        // 识别码
        val ck = 56983
        // 参数1
        val arg1 = 14
        // 参数2
        val arg2 = sb(7)
        // 识别码 除以 参数1 异或运算 参数2
        val pass = ck / arg1 xor arg2
        "第一层密码: $pass".logd()
    }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJbRMLH9riaaSnUX2qtTvJhYge1sccxvzIZ6MsSScoRDCoNe3QwMUBpqI94OzbYT3XMcTQ7udkKPxQ/640?wx_fmt=png)

---

## 第二层分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJbRMLH9riaaSnUX2qtTvJhY6mwceUb1ziavr752Hpcu4DWMiaveKMnIaVpmLJ3zGw4ib93FjpI4nST8Q/640?wx_fmt=png)

* 看看初始化了哪些

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJbRMLH9riaaSnUX2qtTvJhYusL5BdAkktKTvoNYNFYHxzyLdkYZZbSFFZUEHxFSOlriaZE1zIicxO4Q/640?wx_fmt=png)

* 直接就是一堆让人头大的运算

```
 复制代码 隐藏代码

        @Override  // android.view.View$OnClickListener
        public void onClick(View view0) {
            int v15;
            int[][] arr2_v = {new int[]{4, 6, 8, 10, 13, 16, 17, 18, 21, 23, 27, 29, 0x1F, 33, 41, 45, 52, 54, 56, 61, 67, 69, 71, 73, 74, 76, 78, 80, 82, 84, 85, 86}};
            int[][] arr2_v1 = new int[arr2_v[0].length][arr2_v.length];
            int v;
            for(v = 0; v < arr2_v.length; ++v) {
                int v1;
                for(v1 = 0; v1 < arr2_v[0].length; ++v1) {
                    arr2_v1[v1][v] = arr2_v[v][v1];
                }
            }

            int[][] arr2_v2 = {new int[]{14, 16, 18, 19, 23, 24, 28, 29, 0x1F, 35, 37, 39, 41, 43, 0x2F, 0x30, 49, 51, 53, 57, 59, 62, 0x40, 66, 69, 73, 76, 0x4F, 81, 83, 85, 87, 0x6F, 0x83, 0x9C}};
            int[][] arr2_v3 = new int[arr2_v2[0].length][arr2_v2.length];
            int v2;
            for(v2 = 0; v2 < arr2_v2.length; ++v2) {
                int v3;
                for(v3 = 0; v3 < arr2_v2[0].length; ++v3) {
                    arr2_v3[v3][v2] = arr2_v2[v2][v3];
                }
            }

            int v4;
            for(v4 = 0; v4 < arr2_v1.length; ++v4) {
                int v5 = MyService.this.b + arr2_v1[MyService.this.b][MyService.this.b];
                MyService.this...