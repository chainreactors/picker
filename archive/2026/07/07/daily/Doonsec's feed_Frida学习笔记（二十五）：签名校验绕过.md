---
title: Frida学习笔记（二十五）：签名校验绕过
url: https://mp.weixin.qq.com/s/wt4ReiXl3JXsCNaB6RkUDQ
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:01:33.928817
---

# Frida学习笔记（二十五）：签名校验绕过

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fJBlDTU8pLHSeY87QPoCpb2vwFauhc9r2MzibxVzjLcd5Z5ZT00IREKN9aIDbVsLW8FmVVBkBHH48Vdco3SSS6QmnsXT2JkadsCkplclRowo/0?wx_fmt=jpeg)

# Frida学习笔记（二十五）：签名校验绕过

原创

泡泡以安
泡泡以安

泡泡以安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 你反编了一行代码，`apktool b` 回打、`apksigner sign` 换上自签 keystore、`adb install` —— 装上手机，闪一下没了。logcat 里除了一行 `Process died` 什么都没有。没崩、没栈、没异常，就是不让你运行。
>
> 这一章讲三件事：**为什么改一个字节 App 就无法运行**、**怎么把它改好**、**什么时候改不动**。

## 一、签名机制：为什么必须重签

### 1.1 一个字节改动，为什么就要重新签名

拿到一个 APK，用 `apktool d` 解开，改一行字符串，`apktool b` 打回来，装机——装不上：

```
adb install app_repack.apk
Performing Streamed Install
adb: failed to install app_repack.apk:
  Failure [INSTALL_PARSE_FAILED_NO_CERTIFICATES:
  Failed collecting certificates for /data/app/vmdl.../base.apk:
  Attempt to read a length of size 78 at offset 32]
```

因为你改坏了签名。APK 签名不是 "一个额外的文件挂在 APK 外面"，它是对 APK 内所有文件内容的密码学哈希 + RSA 签名。改了任何一个字节，哈希对不上，签名验证失败，`PackageManager` 拒绝安装。

Android 有三代签名方案叠在一起，新的兼容老的：

* **v1（JAR Signature）**：Android 起就有。原理是 Java 的 JAR 签名——`META-INF/MANIFEST.MF` 里逐个文件记 SHA-256,`META-INF/CERT.SF` 是 MANIFEST 的签名摘要，`META-INF/CERT.RSA` 是 CERT.SF 用私钥 RSA 签名后的 PKCS#7 结构。只保护 APK 内单个文件的完整性，不保护整体 zip 结构——所以早年的 Janus 漏洞 CVE-2017-13156 能在 APK 头前面塞一个 dex,v1 校验不到。
* **v2（APK Signature Scheme v2, Android 7.0+）**：把整个 APK 文件当成字节流 hash，签名结果放在 zip 中央目录之前的 **APK Signing Block** —— 一个专门的 chunk 结构，chunk ID `0x7109871A`。这是当前主流校验用的。
* **v3（Android 9.0+）**：v2 的扩展，支持签名密钥轮换 `SigningCertificateLineage` —— 上一版本用密钥 A 签，下一版本换密钥 B，可以做无缝过渡。chunk ID `0xF05368C0`。
* **v4（Android 11.0+）**：为增量安装设计 `adb install --incremental`，签名放在独立的 `.apk.idsig` 文件里。日常逆向基本不用碰。

`apksigner sign --ks my.keystore` 默认会同时打 v1 + v2 + v3，安装时任一版本能过就行。

关键点： v2/v3 的哈希覆盖整个 APK zip 结构 —— 你甚至不能修改 zip 里文件的顺序、不能改 zip 头里的时间戳。任何一个字节变了，v2 hash 就变，签名就废。

### 1.2 keystore 生成 + apksigner 用法

生成一个自签 keystore，一次的事：

```
keytool -genkeypair -v \
  -keystore my.keystore \
  -alias mykey \
  -keyalg RSA -keysize 2048 \
  -validity 10000 \
  -storepass 123456 -keypass 123456 \
  -dname "CN=Test, OU=Test, O=Test, L=Test, ST=Test, C=CN"
```

给一个 APK 重签：

```
# 用 build-tools 里的 apksigner —— 不是 jarsigner,jarsigner 只能签 v1
export PATH="$ANDROID_HOME/build-tools/34.0.0:$PATH"

apksigner sign \
  --ks my.keystore --ks-pass pass:123456 \
  --out app_signed.apk \
  app_repack.apk

apksigner verify --print-certs app_signed.apk
# Verifies
# Verified using v1 scheme (JAR signing): true
# Verified using v2 scheme (APK Signature Scheme v2): true
# Verified using v3 scheme (APK Signature Scheme v3): true
# Signer #1 certificate DN: CN=Test, OU=Test, O=Test, ...
```

`Verifies` 就是 "三代签名都对"。这时 `adb install` 能过。

### 1.3 但是——安装能过 ≠ App 就认

装上去只是 `PackageManager` 认了 "这个 APK 有合法签名"。至于签名主体是谁 —— 是原开发者的 keystore 还是你的自签 —— `PackageManager` 只关心 "同一个包名不能升级到不同签名"，不关心 "这个签名是谁"。

App 内部的业务代码才是关键。它会在启动的某个时刻问系统：

> "我现在装的这个包，签名 hash 是什么？"

然后跟自己代码里硬编码或者服务端下发的 "预期签名 hash" 对比。你的自签 hash 不在预期列表里，业务代码触发拒绝分支 —— 闪退、Toast、静默 crash、业务功能不可用……各种拒绝方式。

这就是签名校验绕过的核心难题：不是让 `apksigner verify` 过关，而是让业务代码相信当前签名是原版。

### 1.4 五档校验光谱

按业务代码检查签名的复杂度，把常见做法分成五档，越往下越难打：

| 档次 | 实现方式 | 典型代码 | 常见于 |
| --- | --- | --- | --- |
| 第 1 档 | Java 层直调 PackageManager | `getPackageInfo(pkg, GET_SIGNATURES).signatures[0]` | 导流工具、内容浏览、免登录 App —— 大厂裸奔产品也在这一档 |
| 第 2 档 | 反射 + 字符串常量加密 | `Class.forName(base64("android.content.pm..."))` | 用了第三方混淆 SDK 但**不做服务端签名 gate** 的普通商业 App |
| 第 3 档 | Native 层 JNI 校验 | JNI `env->GetObjectField` 拿 signatures，或直接 `pread` 读 signing block | 客户端把签名字节塞进业务请求、**服务端做 gate** —— 电商、音乐、社交等有账号 / 付费闭环的 App |
| 第 4 档 | Java + Native 双链路交叉 | Java 一遍、Native 一遍，两边比对 | 风控 / 合规要求高、本地 + 服务端双验 —— 大厂内容平台、直播打赏、部分金融理财类 |
| 第 5 档 | 加固壳内嵌校验 + 分层触发 | 加固 wrapper 里 `libnesec` / `libpoison` 分层 SGN check + 反调试 + 分批解密 | 核心资产敏感（版权 / 游戏经济 / 风控数据 / 合规数据）、有预算上完整加固 —— 覆盖网易易盾、360 加固、腾讯乐固、爱加密的客户群，跨行业都有 |

判断在哪一档，三步走完：

```
# 1. dex 里搜签名读取,第 1、2 档在这里
jadx -d out target.apk
grep -rE "GET_SIGNATURES|GET_SIGNING_CERTIFICATES|getPackageInfo" out/sources/ | head

# 2. native so 列表,第 3、4 档在这里
unzip -l target.apk | grep -oE 'lib/arm64-v8a/lib[^.]+\.so' | sort -u
# 关注：libsentry / libargus / libtoken / libsecure / lib*guard / lib*shield 这类命名

# 3. 加固特征,第 5 档在这里
unzip -l target.apk | grep -iE "libnesec|libpoison|libjiagu|libsecshell|libDexHelper|libtup|libtosprotection"
# 出现 libnesec/libpoison = 网易加固；libjiagu = 360；libsecshell = 腾讯乐固
# libtup = 通付盾；libtosprotection = 爱加密
```

### 1.5 五档在真实 App 里的印证

![签名校验五档光谱](https://mmbiz.qpic.cn/sz_mmbiz_png/fJBlDTU8pLGc63j1QggywAEibriawZjZ8zJTqkxOHRvTiaPHBmt6PlzxyXxjWl4BMibbv580xbsYagJUD0ByZ6Ihl2vveaicwmOow5nAWb588mF0/640?from=appmsg)

签名校验五档光谱

理论最容易变成空谈。同一台 Pixel 5（Android 14, Magisk root），把五个真实 App 分别走一次 "最简重打包 → 装机 → 看在哪一档" 的流程：

| 档次 | 真实样本 | 版本 | 换签后现象 | 加载器/校验特征 |
| --- | --- | --- | --- | --- |
| 第 1 档 | 抖音极速版 `com.ss.android.ugc.aweme.lite` | 2024 | 直接可用，视频/直播/新人红包全部触发 | 无 native 校验 so |
| 第 1 档 | 小宇宙播客 `app.podcast.cosmos` | 2.63.0 | 直接可用，推荐流全部加载 | 无 native 校验 so |
| 第 3 档 | QQ 音乐 `com.tencent.qqmusic` | 13.8.1 | 首页显示 "糟糕发生错误了"，其它页面正常 | Java 层读签名字节参与请求，服务端拒服务 |
| 第 4 档 | 小红书 `com.xingin.xhs` | 8.69.0 | 启动 3 秒内 `Fatal signal 6 SIGABRT` 自杀 | `libsentry.so` bytehook 全 signal + native 直读 signing block |
| 第 5 档 | 网易云音乐 `com.netease.cloudmusic` | 9.2.80 | 500ms 内自杀，splash 都不出 | Nesec 加固 + Tinker + 多层联防 |

两条比档次数字更实用的分界线：

* **是否主动自杀**：第 1、3 档不自杀，要么直接可用要么服务端拒；第 4、5 档 `SIGABRT` / `System.exit` 让 App 死掉 —— 后者留给你调试的时间窗口极短，反馈周期从秒级恶化到每次崩溃从头再来。
* **签名读取的物理层**：全在 Java 层第 1、2 档的，`Signature` 对象替换就够；下沉到 native 第 3 档以上，Java hook 从原理上就绕不过 —— 比如小红书的 `libsentry.so` 直接 `pread` 读 APK signing block chunk `0xF05368C0`,Java 层任何 hook 都触及不到那条路径。

厂商规模不是决定因素。字节的极速版几乎裸奔、腾讯的 QQ 音乐比小红书弱一档、独立开发者的小宇宙完全不设防 —— **业务模式（签名是否参与商业闭环）** 才是决定档次的因素。

后面第二节讲第 1、2 档的 Java 层打法，第三节讲第 3、4、5 档的 native 层，四、五节是 QQ 音乐第 3 档和网易云音乐第 5 档的完整实战。

## 二、Java 层

Java 层是签名校验的第一站。所有的读签名操作最终都要经过 Android Framework 的 `PackageManager` API —— 无论业务代码用直调、反射、加密调用哪种姿势，最终都会 dispatch 到同一批系统方法。这一节把这批方法讲清楚，再讲怎么 hook。

### 2.1 Android 里读签名的完整 API 集

四条主要路径：

```
// 路径 1：传统 API,Android <= 8
PackageInfo pi = pm.getPackageInfo(pkg, PackageManager.GET_SIGNATURES);   // flag = 0x40
Signature[] sigs = pi.signatures;
byte[] bytes = sigs[0].toByteArray();      // → X.509 DER 编码,几百字节
int hash = sigs[0].hashCode();             // = Arrays.hashCode(mSignature)
String hex = sigs[0].toCharsString();      // → 大写 hex 字符串

// 路径 2：Android 9+ 引入的 SigningInfo, 推荐用法
PackageInfo pi = pm.getPackageInfo(pkg, PackageManager.GET_SIGNING_CERTIFICATES);  // flag = 0x08000000
SigningInfo si = pi.signingInfo;
Signature[] cur = si.getApkContentsSigners();          // 当前签名
Signature[] hist = si.getSigningCertificateHistory();  // 历史签名, v3 密钥轮换
boolean hasM = si.hasMultipleSigners();

// 路径 3：直接反射读 Signature 内部字段
Field f = Signature.class.getDeclaredField("mSignature");
f.setAccessible(true);
byte[] raw = (byte[]) f.get(sigs[0]);      // 底层字节数组

// 路径 4：算 hash 再对比, 这一步在业务代码里, 不是系统 API
MessageDigest md = MessageDigest.getInstance("SHA-256");
byte[] h = md.digest(bytes);
String hexHash = bytesToHex(h);            // 跟白名单里的 "abc..." 对比
```

`Signature` 对象的内部结构：

```
public class Signature {
    private final byte[] mSignature;      // 关键字段, 就是这个 byte[]
    private volatile int mHashCode;       // hashCode 缓存
    private volatile String mStringRef;   // toCharsString 缓存
    // ...
}
```

`mSignature` 是私有 final 字段，构造时确定，之后不可修改。`toByteArray()` 返回它的 `.clone()`；`hashCode()` 是 `Arrays.hashCode(mSignature)`；`toCharsString()` 是把 `mSignature` 转 hex。所有读法归根到底是读 `mSignature` 这个字段。

### 2.2 业务代码里的四种常见校验姿势

**姿势 A：直接算 hash 比对**

```
public class SignatureCheck {
    private static final String[] WHITELIST = {
        "d6e5dbbfa87f3d0e88bfe6ad1a5f9c22"    // MD5 of orig cert.der
    };

    public static boolean verify(Context ctx) throws Exception {
        PackageInfo pi = ctx.getPackageManager().getPackageInfo(
            ctx.getPackageName(), PackageManager.GET_SIGNATURES);
        byte[] bytes = pi.signatures[0].toByteArray();
        String md5 = md5Hex(bytes);
        for (String w : WHITELIST) if (w.eq...