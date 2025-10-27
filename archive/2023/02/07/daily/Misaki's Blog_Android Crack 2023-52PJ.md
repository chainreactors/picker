---
title: Android Crack 2023-52PJ
url: https://misakikata.github.io/2023/02/Android-Crack-2023-52PJ/
source: Misaki's Blog
date: 2023-02-07
fetch_date: 2025-10-04T05:48:40.669611
---

# Android Crack 2023-52PJ

[Misaki's Blog](/)

Toggle navigation

* [archives](/archives/)
* [about](/about/)

# Android Crack 2023-52PJ

**Monday, February 6th 2023, 12:31 pm**

## Android Crack 2023

### 【2023春节】解题领红包之三

APK：<https://down.52pojie.cn/nUvaFj.7z>|zYchSGxanOOx

用jadx反编译出来，其中关键是onCreate中的decrypt

```
public static final void m19onCreate$lambda0(MainActivity mainActivity, TextView textView, View view) {
        Intrinsics.checkNotNullParameter(mainActivity, "this$0");
        Intrinsics.checkNotNullParameter(textView, "$key");
        MainActivity mainActivity2 = mainActivity;
        mainActivity.jntm(mainActivity2);
        textView.setText(String.valueOf(mainActivity.num));
        if (mainActivity.check() == 999) {
            Toast.makeText(mainActivity2, "快去论坛领CB吧!", 1).show();
            textView.setText(mainActivity.decrypt("hnci}|jwfclkczkppkcpmwckng•", 2));
        }
    }
​
```

上面有两个部分，其中一是check结果为999，另一个就是解密那个字符串，check这个不需要传入参数，上面设定了get/set，这里直接修改判断即可。

```
public final int check() {
        int i = this.num + 1;
        this.num = i;
        return i;
    }
```

修改`if-ne`为`if-eq`

```
00000036  invoke-virtual      MainActivity->check()I, p0
0000003C  move-result         v0
0000003E  const/16            v1, 999
00000042  if-ne               v0, v1,
```

第二部分decrypt，这里

```
public final String decrypt(String str, int i) {
        Intrinsics.checkNotNullParameter(str, "encryptTxt");
        char[] charArray = str.toCharArray();
        Intrinsics.checkNotNullExpressionValue(charArray, "this as java.lang.String).toCharArray()");
        StringBuilder sb = new StringBuilder();
        for (char c : charArray) {
            sb.append((char) (c - i));
        }
        String sb2 = sb.toString();
        Intrinsics.checkNotNullExpressionValue(sb2, "with(StringBuilder()) {\n…     toString()\n        }");
        return sb2;
    }
```

写个python脚本复原

```
#coding:utf-8
​
​
list_s = []
def decrypt(str1, int2):
    for i in str1:
        list_s.append(chr(ord(i) - int2))
    return list_s
​
print("".join(decrypt("hnci}|jwfclkczkppkcpmwckng•", 2)))
```

当然，如果习惯用jeb打开的话就会发现，这个decrypt已经给我们复原好了。

![image-20230131175642195](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/02/06/12-30-52-a105145c7b57bd46b0a8c3a1e10ebac9-image-20230131175642195-dbded3.png)

### 【2023春节】解题领红包之四

APK：<https://down.52pojie.cn/JfCdrX.7z> | 5dPxREzsOa89

这个题需要知道自己的UID，反编译后可以看到主要的判断逻辑在onCreate

```
public static final void m19onCreate$lambda0(MainActivity mainActivity, View view) {
        Intrinsics.checkNotNullParameter(mainActivity, "this$0");
        A a = A.INSTANCE;
        EditText editText = mainActivity.edit_uid;
        EditText editText2 = null;
        if (editText == null) {
            Intrinsics.throwUninitializedPropertyAccessException("edit_uid");
            editText = null;
        }
        String obj = StringsKt.trim((CharSequence) editText.getText().toString()).toString();
        EditText editText3 = mainActivity.edit_flag;
        if (editText3 == null) {
            Intrinsics.throwUninitializedPropertyAccessException("edit_flag");
        } else {
            editText2 = editText3;
        }
        if (a.B(obj, StringsKt.trim((CharSequence) editText2.getText().toString()).toString())) {
            Toast.makeText(mainActivity, "恭喜你，flag正确!", 1).show();
        } else {
            Toast.makeText(mainActivity, "flag错误哦，再想想！", 1).show();
        }
    }
​
```

这里，我们可以得到两个信息，第一个参数是UID，第二个参数是flag，参数传入A类下的B函数中。

```
public final boolean B(String str, String str2) {
        Intrinsics.checkNotNullParameter(str, "str");
        Intrinsics.checkNotNullParameter(str2, "str2");
        if ((str.length() == 0 && str2.length() == 0) || !StringsKt.startsWith$default(str2, "flag{", false, 2, (Object) null) || !StringsKt.endsWith$default(str2, "}", false, 2, (Object) null)) {
            return false;
        }
        String substring = str2.substring(5, str2.length() - 1);
        Intrinsics.checkNotNullExpressionValue(substring, "this as java.lang.String…ing(startIndex, endIndex)");
        C c = C.INSTANCE;
        MD5Utils mD5Utils = MD5Utils.INSTANCE;
        Base64Utils base64Utils = Base64Utils.INSTANCE;
        String encode = B.encode(str + "Wuaipojie2023");
        Intrinsics.checkNotNullExpressionValue(encode, "encode(str3)");
        byte[] bytes = encode.getBytes(Charsets.UTF_8);
        Intrinsics.checkNotNullExpressionValue(bytes, "this as java.lang.String).getBytes(charset)");
        return Intrinsics.areEqual(substring, c.cipher(mD5Utils.MD5(base64Utils.encodeToString(bytes)), 5));
    }
```

上面的函数先对flag进行截取，去掉flag{}，只留中间的字符串。然后使用B类下的encode进行处理UID，处理后再进行md5操作，然后跟输入进行比较，相同则代表输入正确，也就是我们需要获取的值。

```
public static String encode(String str) {
        int length = str.length();
        char[] cArr = new char[length];
        int i = length - 1;
        while (i >= 0) {
            int i2 = i - 1;
            cArr[i] = (char) (str.charAt(i) ^ '5');
            if (i2 < 0) {
                break;
            }
            i = i2 - 1;
            cArr[i2] = (char) (str.charAt(i2) ^ '2');
        }
        return new String(cArr);
    }
```

这个算法稍微比上面的麻烦一点，本来打算用添加log或者frida来做，发现手机的终端都不能安装，干脆直接把算法实现一遍，需要修改下面的UID为自己的UID。Base64Utils和MD5Utils也可以自己使用编码加密来替代算法。

```
import org.apache.commons.io.Charsets;
​
public class checkme {
    public static String encode(String arg4) {
        int v0 = arg4.length();
        char[] v1 = new char[v0];
        int v0_1 = v0 - 1;
        while(v0_1 >= 0) {
            int v2 = v0_1 - 1;
            v1[v0_1] = (char)(arg4.charAt(v0_1) ^ 53);
            if(v2 < 0) {
                break;
            }
​
            v0_1 = v2 - 1;
            v1[v2] = (char)(arg4.charAt(v2) ^ 50);
        }
​
        return new String(v1);
    }
​
    public static void main(String[] args) {
        String v6 = encode(UID+"Wuaipojie2023");
        byte[] v6_1 = v6.getBytes(Charsets.UTF_8);
        String v6_2 = Base64Utils.INSTANCE.encodeToString(v6_1);
        String v6_3 = MD5Utils.INSTANCE.MD5(v6_2);
        System.out.println(C.INSTANCE.cipher(v6_3, 5));
    }
​
}
```

最后算出来的值就是，再加上前后的flag{}。

```
flag{i4jkj66h8j7i4j7hi6ihf4h02hi062i4}
```

### 【2023春节】解题领红包之六

APK：<https://down.52pojie.cn/cuKcNU.7z> | my4OyfjP5HG2

反编译APK，发现是一个native层的解题，继续看下面的流程，需要把音量调到100-101之间，应该是需要让这个v2不等于0，既可把flag写入到本地的图片上

```
private final void Check_Volume(double arg6) {
        TextView v0 = this.automedia;
        if(v0 == null) {
            Intrinsics.throwUninitializedPropertyAccessException("automedia");
            v0 = null;
        }
​
        v0.setText(((CharSequence)("当前分贝:" + arg6)));
        int v2 = 0;
        if(Double.compare(84.0, arg6) <= 0 && arg6 <= 99.0) {
            this.xigou(((Context)this));
            return;
        }
​
        if(100.0 <= arg6 && arg6 <= 101.0) {
            v2 = 1;
        }
​
        if(v2 != 0) {
            Toast.makeText(((Context)this), "快去找flag吧", 1).show();
            this.write_img();
        }
    }
```

其中的write\_img函数为

```
private final void write_img() {
        Closeable v2;
        InputStream v1_1;
        InputStream v0 = this.getAssets().open("aes.png");
        Intrinsics.checkNotNullExpressionValue(v0, "assets.open(\"aes.png\")");
        File v3 = new File(this.getPrivateDirectory(), "aes.png");
        Closeable v0_1 = (Closeable)v0;
        try {
            v1_1 = (InputStream)v0_1;
            v2 = (Closeable)new FileOutputStream(v3);
        }
        catch(Throwable v1) {
            throw v1;
        }
​
        try {
            ByteStreamsKt.copyTo$default(v1_1, ((OutputStream)(((FileOutputStream)v2))), 0, 2, null);
            goto label_27;
        }
        catch(Throwable v1_2) {
        }
​
        try {
            throw v1_2;
        }
        catch(Throwable v3_1) {
        }
​
        try {
            CloseableKt.closeFinally(v2, v1_2);
            throw v3_1;
        label_27:
            CloseableKt.closeFinally(v2, null);
            goto label_34;
        }
        cat...