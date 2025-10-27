---
title: Frida 逆向一个 APP
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458586874&idx=1&sn=3bdc2f37290cd64b6fe65a45db267db7&chksm=b18c3e7086fbb76650050dc25930565ba870f58de685add83cd8dc9a04310233026c85bd1234&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-15
fetch_date: 2025-10-06T19:37:54.440322
---

# Frida 逆向一个 APP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHrjb2UUVHwD9aCzon0cAwSLWvGXGcot7b9J9GvFeKAsxqPUFZBXop0w/0?wx_fmt=jpeg)

# Frida 逆向一个 APP

mb\_vcrwlkem

看雪学苑

# 最近收到了一个APP让我研究一下登录，已经研究完成，下面则是我的整体思路。

```
为了安全考虑这个app我就不说是那个了 我就说整体的思路
仅供交流学习 严谨非法使用
```

## 开始进行抓包：

```
手机使用代理连接charles
之后开始点击app登录 进行抓包
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHP7SicPPWicwJlv6Kj5U1EqrPMA7QRgvucJ7ClJcLJD01mFJVIjLG46TA/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHWznIcYzhHQohrVxuJHMlbaNqHj74bLgvk9ZIva5cSBCibFaoApU77iaQ/640?wx_fmt=png&from=appmsg)

**下面则是我抓到的包：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHicpTic1rPAYUp9nS4ia4tFic0Z54NOzONxib8kwPawXSUmeNKpYPicgUicFAA/640?wx_fmt=png&from=appmsg)

```

```

```
抓包之后j进行改包也就是去掉form中的随机一个参数进行请求发送 这一步的目的就是去除掉没用的参数这样的话就可以在逆向的时候减少工作量 下面我告诉大家如何改包
```

```

```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHU9gngchZjL6pys6HVXCWPKrHTibGuV5ibfjrjVIPSsW6TILvNwGrTlFw/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHzRjx5oLesQhn7ZNHmIEex69I4FE91WHqIgN29vMicMd3uWvVE8EHXMg/640?wx_fmt=png&from=appmsg)

```
按照上面的步骤进行改包 然后发送请求看是否能够成功 如果不能成功的话这个参数是不能去除的
```

## 将app进行反编译

```
这里我用的是jadx
反编译成功之后 如下 注意看箭头标记的位置 如果包很多并没有乱码或者包少初步可以判断是没有加固
如果初步判断没有进行加壳那么就可以进行搜索

这里有两个搜索方案
    搜索url 也就是发请求的那个 login.ashx
    搜索关键字 也就是form中的  而我搜索的是关键字
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHgC1nDRfZDqrplJSCSib8Vb7XTjgYrCXoZSic65icy4f7RAiafxk5dXuibkg/640?wx_fmt=png&from=appmsg)

我 搜索到了第一个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHVefj7QUAqDMYjCfAlw9rr6ct40KKL1uG7tEA0S5KL7pUicibbn4BEg7A/640?wx_fmt=png&from=appmsg)

```
看起来是个常量
按照开发的逻辑来说常量是一个经常使用并且不变的 那么就是他了 咱们翻翻这一页的代码
很遗憾 并不是 继续看下一个 也就上面图中的最后一个
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHyK4VlR4U6e3ZuGoMUDicNvcTO35icHsZpTdgwqq5wpuOLY9h5fBqF9hA/640?wx_fmt=png&from=appmsg)

```
最后一个让我找到了可能是 因为有好多我发现的参数 也就是请求的参数里面看起来都有
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHkKR6RlIibz2n4m1xfQNdJOLze0lQarGedhMqITDL4sbvdhJicWhLadWQ/640?wx_fmt=png&from=appmsg)

## 既然找到了 那么就一个个进行破解

```
首先是
KEY_APP_ID
    这个是个常量的Key 值话也是个常量 那么好 第一个参数已经破解完成
channelid
    这个key 并不是个常量 这时候可以用frida进行调用
```

## 开始用frida

```
先进行注入检测 也就是随便一个函数看看是否有检测
很幸运 这个app并没有任何检测
```

## 开始接下来的一步开始进行破译

```
上面说到了 channelid这个值
    getChannelId 是这个函数产生的 那么我就开始用frida检测这个值看看他的参数是什么
```

```
import frida
import sys

rdev = frida.get_remote_device()
pid = rdev.spawn(["xxxx"])
session = rdev.attach(pid)
scr = """
Java.perform(function(){
    var AppUtils = Java.use("xxxx.util.AppUtils")
    AppUtils.getChannelId.implementation = function(c){
    var res = this.getChannelId(c)
    console.log(res,"getChannelId")
    return res
    }
})
"""

script = session.create_script(scr)

def on_message(message, data):
    print(message, data)

script.on("message", on_message)
script.load()
rdev.resume(pid)
sys.stdin.read()
```

```
我的经验是多hook几次看看是否是同一个值 如果是的话那么就直接用就好了
这里我多试了几次值是一样的 那么我就可以直接用了

好 接下来就开始破译下一个
    KEY_APP_VERSION
    这个看起来是个版本号
按照上面的代码 继续使用getCannelId这个hook脚本继续开始hook  还是建议多hook几次
好 我发现还是一样的 那么好！那还是继续用

接下来就是下一个参数
      udid
 这个get_uuid 还是用上面的代码进行hook(记得改函数和包 xxx 哪里)
 这个参数 我还是按照习惯多来了几次 发现每次都是不一样的 好那么深入进行探究！
```

```
 public static String getUDID(Context context) {
        return SecurityUtil.encode3Des(context, getIMEI(context) + HiAnalyticsConstant.REPORT_VAL_SEPARATOR + System.nanoTime() + HiAnalyticsConstant.REPORT_VAL_SEPARATOR + SPUtils.getDeviceId());
    }
```

```
这个是代码我发现了有时间生成 那确实每次都会不一样
好 接下来继续深层次研究除了时间的每个参数
getIMEI  多hook 几次看看是不是值是一样的
REPORT_VAL_SEPARATOR  这个是个常量
getDeviceId	 多hook 几次看看是不是值是一样的

根据验证 上面的值每次都是一样的! 好 接下来那么就继续下一步 用python进行组装
```

```
def make_uuid(
        imei,
        report_val_separator,
        nano_time,
        getDeviceId,
):
    make_str = imei + report_val_separator + str(nano_time) + report_val_separator + getDeviceId
    return make_str

uuid = make_uuid(
    imei="xxxx",
    report_val_separator="xxxx",
    nano_time=time.time_ns(),
    getDeviceId="xxxx",
)
```

```
很好那么看起来
context, getIMEI(context) + HiAnalyticsConstant.REPORT_VAL_SEPARATOR + System.nanoTime() + HiAnalyticsConstant.REPORT_VAL_SEPARATOR + SPUtils.getDeviceId()

encode3Des 这个第二个参数已经破译好了

这次开始破译 encode3Des
```

```
  public static String encode3Des(Context context, String str) {
        String desKey = AHAPIHelper.getDesKey(context);
        byte[] bArr = null;
        if (TextUtils.isEmpty(desKey)) {
            return null;
        }
        try {
            SecretKey generateSecret = SecretKeyFactory.getInstance("desede").generateSecret(new DESedeKeySpec(desKey.getBytes()));
            Cipher instance = Cipher.getInstance("desede/CBC/PKCS5Padding");
            instance.init(1, generateSecret, new IvParameterSpec(iv.getBytes()));
            bArr = instance.doFinal(str.getBytes("UTF-8"));
        } catch (Exception unused) {
        }
        return encode(bArr).toString();
    }
```

```
这段代码看起来就是个加密  3DES（Triple DES）加密，也称为 DESede
那么好 代码里面也没什么难的地方  那么就改成Python吧
```

```
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import base64

def encode_3des(des_key, data, iv):
    if len(des_key) != 24:
        raise ValueError("The DES key must be 24 bytes long for 3DES.")

    # 确保密钥长度为 24 字节
    des_key = des_key.encode('utf-8')[:24]

    cipher = DES3.new(des_key, DES3.MODE_CBC, iv.encode('utf-8'))

    # 对输入数据进行 padding
    padded_data = pad(data.encode('utf-8'), DES3.block_size)

    # 加密数据
    encrypted_data = cipher.encrypt(padded_data)

    # 返回加密后的数据，并进行 base64 编码
    return base64.b64encode(encrypted_data).decode('utf-8')

# 示例调用
des_key = "your_24_byte_key_here"
iv = "your_8_byte_iv_here"  # IV 长度为 8 字节
data = "The data to encrypt"
encoded_data = encode_3des(des_key, data, iv)
print(f"Encrypted data: {encoded_data}")
```

```
其中des_key需要拿到
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHWy81F2iawEuqGiaZCDCcsnjHhsGINsuhrDicqicOYiaOBNOEw4jgQtSOYvw/640?wx_fmt=png&from=appmsg)

```
看起来是个so文件
    按照我的经验来说继续hook这个 多hook几次看看值是不是一样的  经验看 很多都是死值 除了大型app
    很好 这个是个死值
    那俺么我就得到了 des_key
IV
    现在还差一IV  但是他这个IV是常量
    private static final String iv = "appapich";

很好很好 UUID 我已经完成
```

```
import frida
import sys

rdev = frida.get_remote_device()
pid = rdev.spawn(["xxxx"])
session = rdev.attach(pid)
scr = """
Java.perform(function(){
    var AppUtils = Java.use("xxxx.util.AppUtils")
    AppUtils.getChannelId.implementation = function(c){
    var res = this.getChannelId(c)
    console.log(res,"getChannelId")
    return res
    }
})
```

```
接下来看下一个参数
    userkey 这个在请求中并没有发现这个值 如果下面没有引用的话 那么就不管

checkNullParams(treeMap); 这个干了什么 去看看
private static void checkNullParams(Map<String, String> map) {
       for (String str : map.keySet()) {
           if (map.get(str) == null) {
               map.put(str, "");
           }
       }
   }
这段 Java 代码的目的是检查给定的 Map<String, String> 中的每个键值对，
如果某个值是 null，则将该值替换为空字符串 ""
接下来看这个代码
String signByType = SignManager.INSTANCE.signByType(i, treeMap);
还是进行hook下面的代码
```

```
public final String signByType(@SignType int i, TreeMap<String, String> paramMap) {
        Intrinsics.checkNotNullParameter(paramMap, "paramMap");
        StringBuilder sb = new StringBuilder();
        String str = KEY_V1;
        if (i != 0) {
            if (i == 1) {
                str = KEY_V2;
            } else if (i == 2) {
                str = KEY_SHARE;
            } else if (i == 3) {
                str = KEY_AUTOHOME;
            }
        }
        sb.append(str);
        for (String str2 : paramMap.keySet()) {
            sb.append(str2);
            sb.append(paramMap.get(str2));
        }
        sb.append(str);
        String encodeMD5 = SecurityUtil.encodeMD5(sb.toString());
        if (encodeMD5 != null) {
            Locale ROOT = Locale.ROOT;
            I...