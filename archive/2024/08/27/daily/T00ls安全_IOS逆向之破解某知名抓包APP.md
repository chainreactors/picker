---
title: IOS逆向之破解某知名抓包APP
url: https://mp.weixin.qq.com/s?__biz=Mzg3NzYzODU5NQ==&mid=2247484744&idx=1&sn=603ebccd02cb66b1a3b23d520b3e0b1d&chksm=cf1ea3e4f8692af2f2bf1dd45544d0d79dbe7810bf4cc580288e7ef2b0b6dbc518e3221cd5f4&scene=58&subscene=0#rd
source: T00ls安全
date: 2024-08-27
fetch_date: 2025-10-06T18:06:50.976441
---

# IOS逆向之破解某知名抓包APP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfWONQnDqWGBZ3FYu4mX3Jkg5jRn5TJkoceibeJdSAbA4VSibhZhXu5YTOA/0?wx_fmt=jpeg)

# IOS逆向之破解某知名抓包APP

原创

apibug

T00ls安全

# 0x00 前言

本文的测试目标是一个\*\*\*\*\*\*APP，可以使用hook或者代理的方式来获取高级功能，如解密HTTPS流量、重写HTTP请求以及重放等功能。本文主要提供一些思路以及介绍一下数据之间的转换。

---

# 0x01 分析

运行后发现高级功能都需要付费才可以，抓包发现请求和返回都加密了。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfW8KiaO0KcXqib3yPI43pg0icEl7zpLSqRQ8Q4WRNvoIWtGYbA2uaicgmG8Q/640?wx_fmt=png&from=appmsg)

使用`frida-ios-dump`将ipa文件dump出来，之后用ida打开，发现该程序是用到了OC和swift。而且http请求采用了`Alamofire`，它是一个用 Swift 编写的 HTTP 网络库。

该程序较小，猜测加密函数中有`encrypt`关键字，于是在函数中搜索`encrypt`。

当然也可以根据http请求的一些内容搜索进而去定位加密的算法，在这里就不演示了。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfWgVwqdNwDNIoGmuuQgbg7iaEg78FUAk1k7Uo3d1yeouqZIkQ1l49Gz0g/640?wx_fmt=png&from=appmsg)

可以看到有一些，可以使用`frida-trace`来追踪一下是调用了哪个方法。

```
frida-trace -U -f com.stormtech.sniffer -m "*[* *encrypt*]"
```

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfWtrXXBCyDyHdWeFHjj8Kb84G3vxYyAzCCjTMG6hJwcEy178eTfVKoVA/640?wx_fmt=png&from=appmsg)

经过进一步验证发现是调用了类`XMXXTEA`相关的加密函数。一般这样同个类存在多个加（解）密，大多数都是简单的调用复杂的。

从上图就可以看出来

```
encryptStringToBase64String:arg1 stringKey:arg2
```

调用了

```
encryptToBase64String:arg1 stringKey:arg2。
```

所以我们看

```
+[XMXXTEA encryptStringToBase64String:arg1 stringKey:arg2]
```

即可。

命令如下：

```
frida-trace -U -f com.stormtech.sniffer -m "+[XMXXTEA encryptStringToBase64String:stringKey:]"
```

执行后可以发现与抓包的内容一致。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfWXeVzmg4y6aVZDRezHuetPLWBYVicP3ic9OEDcicibeibAqMw7ep8YIg9EPQ/640?wx_fmt=png&from=appmsg)

接下来我们看一下是否有数据的解密，同样在ida中搜`decrypt`

根据上面的经验，猜测解密的是

```
+[XMXXTEA decryptBase64StringToString:stringKey:]
```

结果进行追踪后发现并没调用，这里解密采用的是

```
+[XMXXTEA decryptBase64String:stringKey:]
```

可以看到解密数据。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfWv3CK4QMvoueucDdOSjxeD7PpH2oXFkO5x9rCylsomPKUBXLJfFBXLQ/640?wx_fmt=png&from=appmsg)

返回的json中有几个关键的键值可以猜出其含义。

例如`isVip`应该是判断是否为会员，`expire_on`表示到期时间，`auth_quantity`是授权数量，`function_list`应该是拥有的功能，比如非会员用户只有一个抓包功能，如果要拥有解密HTTPS、重写等功能，则`function_list应该是[1,2,3]`。

当然这些不是我的猜测了,因为我前年就借了正版账号。

尝试修改一下`isVip`的值为1，看是否有反应。首先看一下

```
+[XMXXTEA decryptBase64String:stringKey:]
```

解密返回值的类型是什么。

主要代码：

```
onLeave(log, retval, state) {
    var ret = ObjC.Object(retval);
    log(`ret type is -->`+ret.$className);
  }
```

执行后返回的结果：

```
ret type is -->NSConcreteData
```

返回值是`NSConcreteData`类型的，可以看作为是`NSData`。

修改返回值有两种方法，第一种是将`NSData`转化为`NSString`，然后利用字符串替换来修改，修改完毕后转化`NSData`并替换；

第二种是将`NSData`转化为可变数组`NSMutableDictionary`，然后修改键的值，最后再转化`NSData`并替换。

## 方法一：使用NSString替换

对应的主要OC代码如下：

```
 NSString *str =@"{\"uid\": \"b07b6ee3a93a44ae8d3cf80a3c6f47f5\", \"userID\": \"502456\", \"isVip\": 0, \"member_type\": 0, \"member_title\": \"\\u57fa\\u7840\\u7248\", \"expire_on\": \"\\u6682\\u672a\\u5f00\\u901aVIP\", \"auth_quantity\": 0, \"auth_mail\": null, \"is_primary\": 0, \"trail_status\": 0, \"function_list\": [1], \"timestamp\": 1666080682, \"ts\": 0}";
NSData* data =[str dataUsingEncoding:NSUTF8StringEncoding];//NSString转换为NSData
NSString*oldString =[[NSString alloc]initWithData:data encoding:NSUTF8StringEncoding];//NSData转换为NSString
NSString* newString =[str stringByReplacingOccurrencesOfString:@"\"isVip\": 0" withString:@"\"isVip\": 1"];//替换字符串
NSLog(@"旧字符串是:\n%@",oldString);
NSLog(@"新字符串是:\n%@",newString);
```

这里为了使用`NSData`数据，采用的是`NSString`转换而来的，当然也可以采用`byte`来生成。主要代码：

```
Byte byte[] = {0x7B,..., 0x7D};
NSData *byteData = [[NSData alloc] initWithBytes:byte length:sizeof(byte)/sizeof(Byte)];
```

OC代码执行的结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfWXvsQEKVneRWT3nNnzicbTE6D3TNfDaQyibCc7pNDpgfSXwNcFdHO6jVg/640?wx_fmt=png&from=appmsg)

可以成功替换，翻译成`frida`的js实现如下：

```
  onLeave(log, retval, state) {
    var ret = ObjC.Object(retval);
    var oldNSStr = ObjC.classes.NSString.alloc().initWithData_encoding_(ret, 4);//NSData转换为NSString
    log(`www.apibug.com旧-->`+ oldNSStr);
    var newNSStr = oldNSStr.stringByReplacingOccurrencesOfString_withString_('"isVip": 0','"isVip": 1');//替换字符串
    log(`www.apibug.com新-->`+ newNSStr);
    retval.replace(newNSStr.dataUsingEncoding_(4));//NSString转换为NSData，并替换返回值
  }
```

执行结果(同时查看我的账号界面可以看到PRO标志)：

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfWG4d8dibO3WywiavoxwU4j9UBqfYtL0EMBryxAZ2wuYMPttsAetFloVTg/640?wx_fmt=png&from=appmsg)

但是点击解密HTTPS流量、重写等功能还是跳转到会员开通界面，这是因为这些功能是从`function_list`中获取的，所以想要解锁功能还需修改这里。主要代码：

```
              var newNSStr = oldNSStr
.stringByReplacingOccurrencesOfString_withString_('"isVip": 0','"isVip": 1')
.stringByReplacingOccurrencesOfString_withString_('"is_vip": 0','"is_vip": 1')
.stringByReplacingOccurrencesOfString_withString_('"member_type": 0','"member_type": 3')
.stringByReplacingOccurrencesOfString_withString_('\\u57fa\\u7840\\u7248','无敌牛逼版')
.stringByReplacingOccurrencesOfString_withString_('"can_deauthorize": false','"can_deauthorize": true')
.stringByReplacingOccurrencesOfString_withString_('"auth_quantity": 0','"auth_quantity": 99')
.stringByReplacingOccurrencesOfString_withString_('"auth_mail": null','"auth_mail": "apibug6@gmail.com"')
.stringByReplacingOccurrencesOfString_withString_('"function_list": [1]','"function_list": [1,2,3,4,5]')
.stringByReplacingOccurrencesOfString_withString_('"function_list": "[1]"','"function_list": "[1,2,3,4,5]"')
.stringByReplacingOccurrencesOfString_withString_('"trail_status": 0','"trail_status": 1')
.stringByReplacingOccurrencesOfString_withString_('"ts": 0','"ts": 1')
.stringByReplacingOccurrencesOfString_withString_('\\u6682\\u672a\\u5f00\\u901aVIP','无敌破解永久有效');

log(`新--> ${newNSStr.toString()}`);

//将新NSString转换回NSData在替换返回值
          var newData = newNSStr.dataUsingEncoding_(4);
          retval.replace(newData);
} catch (e){
log(`Error: ${e.message}`);
      }
```

再次执行:

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfWVqibzYic04eSqnxQPLX6YhmE3pkk54icrNfU7xEslw2uG6tibhZV9aRNjA/640?wx_fmt=png&from=appmsg)

看到用户界面也成功变化了,高级功能也全部可以使用

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfWiaticNolGxTrJxicGMVwp43Yn3Hf2hljIicZGJsgTwhhJv9AL5oXaBaaxw/640?wx_fmt=png&from=appmsg)

## 方法二：使用NSMutableDictionary修改

对应的主要OC代码如下：

```
    NSData * data =[str dataUsingEncoding:NSUTF8StringEncoding];
NSMutableDictionary* result =[NSJSONSerializationJSONObjectWithData:data options:NSJSONReadingMutableContainers error:nil];//NSData转NSMutableDictionary
[result setValue:[NSNumber numberWithInt:1] forKey:@"isVip"];//设置isVip为1
[result setValue:@"apibug6@gmail.com" forKey:@"auth_mail"];//这个无所谓
[result setValue:@"[1,2,3,4,5]" forKey:@"function_list"];//设置function_list
[result setValue:@"2099-09-09 14:22" forKey:@"expire_on"];//设置expire_on
NSLog(@"旧:%@",str);
NSLog(@"改变之后:%@",result);
```

执行的结果

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nNnMr2cAvmpW1Yepz84icGfWIWtNYHrX1Dhv4c52R1PQ0DE3Pq5N6UBCKZYkEPQH2QxVTSKJPSq0pg/640?wx_fmt=png&from=appmsg)

这里翻译成`frida`的js实现时，有一个问题，生成`NSMutableDictionary`时，由于需要传入nil，而frida中无法生成，导致这种方法不能使用。

根据GPT给出的方法`var nil=ObjC.Object(ptr("0x0"));`，测试代码如下：

```
var data = ObjC.classes.NSString.stringWithString_('{"aa":11,"bb":2}') ;
var NSJSONSerialization = ObjC.classes.NSJSONSerialization;
var nil=ObjC.Object(ptr("0x0"));
NSJSONSerialization.JSONObjectWithData_options_error_(data,1,nil);
```

运行后直接崩溃，导致无法使用，因此在`frida`下，暂时放弃第二种方法。

分析的话到这里就结束了，但借助frida来获取高级版，不方便使用，而且无法在非越狱手机上使用，如果想在非越狱手机上使用的话，就需要编写插件来运行在非越狱手机上。

---

# 0x02 编写非越狱插件

编写插件采用了非越狱插件开发集成神器`MonkeyDev`，已经在论坛内发布过了,不会安装直接搜索`MonkeyDev`即可,MonkeyDev集成了theos+Tweaks+Reveal.framework +Cycript +class-dump+CaptainHook。

安装完成后新建`MonkeyApp`

`File->New->Project->MonkeyApp`

项目建立后将砸壳后的APP拖入到`TargetApp`目录下。

这里使用Logos进行`Hook`代码，`HOOK` 某个类里面的某个对象方法语法：

```
%hook 类名
- (返回值)方法名:(id)arg1 ....
{
       ...
}
%end
```

根据上面的分析，这里我们需要对`XMXXTEA`类的方法`decryptBase64String:stringKey:`进行HOOK，修改返回值，完整代码如下：

```
%hook XMXXTEA
+(...