---
title: IOS逆向之某抓包APP
url: https://fuping.site/2022/10/21/IOS-Storm-Sniffer-Reverse/
source: 浮萍's Blog
date: 2022-10-22
fetch_date: 2025-10-03T20:36:05.449742
---

# IOS逆向之某抓包APP

[![logo](/favicon.png)](/)

* [主页](/)
* [所有文章](/archives/)
* [标签](/tags)
* [关于](/about)
* [RSS](/atom.xml)

# IOS逆向之某抓包APP

Oct 21, 2022[#IOS逆向](/categories/IOS%E9%80%86%E5%90%91/)

## 0x00 前言

本文的测试目标是一个抓包的APP，可以使用hook或者代理的方式来获取高级功能，如解密HTTPS流量、重写HTTP请求以及重放等功能。由于个人账户（没有付费成为苹果开发者账号）的限制，注入打包后，无法正常使用抓包功能，因此算是一篇半成品，不过本文主要提供一些思路以及介绍一下数据之间的转换。

## 0x01 分析

运行后发现高级功能都需要付费才可以，抓包发现请求和返回都加密了。

![img](1665733985358.png)

使用`frida-ios-dump`将ipa文件dump出来，之后用ida打开，发现该程序是用到了OC和swift。而且http请求采用了`Alamofire`，它是一个用 Swift 编写的 HTTP 网络库。

该程序较小，猜测加密函数中有`encrypt`关键字，于是在函数中搜索`encrypt`。

当然也可以根据http请求的一些内容搜索进而去定位加密的算法，在这里就不演示了。

![img](1665734067271.png)

可以看到有一些，可以使用`frida-trace`来追踪一下是调用了哪个方法。

|  |  |
| --- | --- |
| ``` 1 ``` | ``` frida-trace -U -f com.xxxx -m "*[* *encrypt*]" ``` |

使用该命令可以看到如下调用：

![img](1666079236052.png)

经过进一步验证发现是调用了类`XMXXTEA`相关的加密函数。一般这样同个类存在多个加（解）密，大多数都是简单的调用复杂的。从上图就可以看出来`encryptStringToBase64String:arg1 stringKey:arg2`调用了`encryptToBase64String:arg1 stringKey:arg2`。

所以我们看 `+[XMXXTEA encryptStringToBase64String:arg1 stringKey:arg2]`即可。

命令如下：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` frida-trace -U -f com.xxxx -m "+[XMXXTEA encryptStringToBase64String:stringKey:]" ``` |

执行后可以发现与抓包的内容一致。

![img](1666080138242.png)

接下来我们看一下是否有数据的解密，同样搜`decrypt`

![img](1666080460021.png)

根据上面的经验，猜测解密的是`+[XMXXTEA decryptBase64StringToString:stringKey:]`。结果进行追踪后发现并没调用，这里解密采用的是`+[XMXXTEA decryptBase64String:stringKey:]`。

可以看到解密数据。

![img](1666081155760.png)

不过解密结果不是字符串类型，我们用`CyberChef`的hex解码后是json数据。

![img](1666081298004.png)

返回的json中有几个关键的键值可以猜出其含义。例如`isVip`应该是判断是否为会员，`expire_on`表示到期时间，`auth_quantity`是授权数量，`function_list`应该是拥有的功能，比如非会员用户只有一个抓包功能，如果要拥有解密HTTPS、重写等功能，则`function_list`应该是[1,2,3]。当然这些只是猜测。

尝试修改一下`isVip`的值为1，看是否有反应。首先看一下`+[XMXXTEA decryptBase64String:stringKey:]`解密返回值的类型是什么。

主要代码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` onLeave(log, retval, state) {     var ret = ObjC.Object(retval);     log(`ret type is -->`+ret.$className);   } ``` |

执行后返回的结果：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ret type is -->NSConcreteData ``` |

返回值是`NSConcreteData`类型的，可以看作为是`NSData`。修改返回值有两种方法，第一种是将`NSData`转化为`NSString`，然后利用字符串替换来修改，修改完毕后转化`NSData`并替换；第二种是将`NSData`转化为可变数组`NSMutableDictionary`，然后修改键的值，最后再转化`NSData`并替换。

下面分别看一下两种方法的OC代码，以及翻译成frida的js实现的代码。

### 方法一：使用NSString替换

对应的主要OC代码如下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` NSString *str = @"{\"uid\": \"xxxxxxx\", \"userID\": \"xxxxx\", \"isVip\": 0, \"member_type\": 0, \"member_title\": \"\\u57fa\\u7840\\u7248\", \"expire_on\": \"\\u6682\\u672a\\u5f00\\u901aVIP\", \"auth_quantity\": 0, \"auth_mail\": null, \"is_primary\": 0, \"trail_status\": 0, \"function_list\": [1], \"timestamp\": 1666080682, \"ts\": 0}"; NSData * data = [str dataUsingEncoding:NSUTF8StringEncoding];//NSString转换为NSData NSString *oldString = [[NSString alloc]initWithData:data encoding:NSUTF8StringEncoding];//NSData转换为NSString NSString * newString = [str stringByReplacingOccurrencesOfString:@"\"isVip\": 0" withString:@"\"isVip\": 1"];//替换字符串 NSLog(@"oldString is:\n%@",oldString); NSLog(@"newString is:\n%@",newString); ``` |

这里为了使用NSData数据，采用的是NSString转换而来的，当然也可以采用byte来生成。主要代码：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` Byte byte[] = {0x7B,..., 0x7D}; NSData *byteData = [[NSData alloc] initWithBytes:byte length:sizeof(byte)/sizeof(Byte)]; ``` |

OC代码执行的结果如下：

![img](1666143640301.png)

可以成功替换，翻译成frida的js实现如下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` onLeave(log, retval, state) {   var ret = ObjC.Object(retval);   var oldNSStr = ObjC.classes.NSString.alloc().initWithData_encoding_(ret, 4);//NSData转换为NSString   log(`oldNSStr-->`+ oldNSStr);   var newNSStr = oldNSStr.stringByReplacingOccurrencesOfString_withString_('"isVip": 0','"isVip": 1');//替换字符串   log(`newNSStr-->`+ newNSStr);   retval.replace(newNSStr.dataUsingEncoding_(4));//NSString转换为NSData，并替换返回值 } ``` |

执行结果：

![img](1666100239409.png)

同时查看我的账号界面可以看到PRO标志。

![img](1666101158786.png)

但是点击解密HTTPS流量、重写等功能还是跳转到会员开通界面，这是因为这些功能是从`function_list`中获取的，所以想要解锁功能还需修改这里。主要代码：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` var newNSStr = oldNSStr.stringByReplacingOccurrencesOfString_withString_('"isVip": 0','"isVip": 1').stringByReplacingOccurrencesOfString_withString_('"is_vip": 0','"is_vip": 1').stringByReplacingOccurrencesOfString_withString_('"member_type": 0','"member_type": 1').stringByReplacingOccurrencesOfString_withString_('"auth_quantity": 0','"auth_quantity": 3').stringByReplacingOccurrencesOfString_withString_('"function_list": [1]','"function_list": [1,2,3,4,5]').stringByReplacingOccurrencesOfString_withString_('\\u6682\\u672a\\u5f00\\u901aVIP','2099-09-09 14:22'); log(`newNSStr-->`+ newNSStr); ``` |

再次执行

![img](1666100947797.png)

看到用户界面也成功变化了

![img](1666101229379.png)

高级功能也可以使用

![img](1666101255791.png)

例如重写功能，将请求的某度转到qq上

![img](1666101314198.png)

功能都是可以正常使用的。

### 方法二：使用NSMutableDictionary修改

对应的主要OC代码如下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` NSData * data = [str dataUsingEncoding:NSUTF8StringEncoding]; NSMutableDictionary * result = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingMutableContainers error:nil];//NSData转NSMutableDictionary [result setValue:[NSNumber numberWithInt:1] forKey:@"isVip"];//设置isVip为1 [result setValue:@"[1,2,3,4,5]" forKey:@"function_list"];//设置function_list [result setValue:@"2099-09-09 14:22" forKey:@"expire_on"];//设置expire_on NSLog(@"oldString is:%@",str); NSLog(@"After Change is:%@",result); ``` |

查看执行的结果

![img](1666141054823.png)

这里翻译成frida的js实现时，有一个问题，生成`NSMutableDictionary`时，由于需要传入`nil`，而frida中无法生成，导致这种方法不能使用。根据别人提出的方法`var nil=ObjC.Object(ptr("0x0"));`，测试代码如下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` var data = ObjC.classes.NSString.stringWithString_('{"aa":11,"bb":2}') ; var NSJSONSerialization = ObjC.classes.NSJSONSerialization; var nil=ObjC.Object(ptr("0x0")); NSJSONSerialization.JSONObjectWithData_options_error_(data,1,nil); ``` |

运行后直接崩溃，导致无法使用，因此在frida下，暂时放弃第二种方法。

分析的话到这里就结束了，但借助frida来获取高级版，不方便使用，而且无法在非越狱手机上使用，如果想在非越狱手机上使用的话，就需要使用一些插件来运行在非越狱手机上。

## 0x02 编写非越狱插件

编写插件采用了非越狱插件开发集成神器[MonkeyDev](https://github.com/AloneMonkey/MonkeyDev)，集成了theos+Tweaks+Reveal.framework +Cycript +class-dump+CaptainHook。

安装和卸载可以参考<https://github.com/AloneMonkey/MonkeyDev/wiki/%E5%AE%89%E8%A3%85>

安装完成后新建MonkeyApp，`File->New->Project->MonkeyApp`。

项目建立后将砸壳后的APP拖入到`TargetApp`目录下。

这里使用Logos进行Hook代码，HOOK 某个类里面的某个对象方法语法：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` %hook 类名 - (返回值)方法名:(id)arg1 .... { 		... } %end ``` |

根据上面的分析，这里我们需要对`XMXXTEA` 类的方法`decryptBase64String:stringKey:`进行HOOK，修改返回值，主要代码如下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` %hook XMXXTEA + (id) decryptBase64String:(NSString*) stringData stringKey:(NSString*) key{  	NSLog(@"Before : %@", %orig); 	NSData *data = %orig;//NSData     NSMutableDictionary *result = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingMutableContainers error:nil];//NSData转换NSMutableDictionary          [result setValue:[NSNumber numberWithInt:1] forKey:@"isVip"];     [result setValue:[NSNumber numberWithInt:1] forKey:@"member_type"];     [result setValue:[NSNumber numberWithInt:3] forKey:@"auth_quantity"];     [result setValue:@"[1,2,3,4,5]" forKey:@"function_list"];     [result setValue:@"2099-09-03 14:22" forKey:@"expire_on"];          NSData *data_result= [NSJSONSerialization dataWithJSONObject:result options:NSJSONWritingPrettyPrinted error:nil];     NSLog(@"After : %@", data_result);     return data_result; }  %end ``` |

其实和上面第二种方法中的OC代码一样，连接非越狱手机后使用⌘+R运行该项目。

首次在新设备上运行，需要设置-通用-描述文件与设备管理中信任证书，ios16以上需要开启开发者模式，隐私安全-开发者模式，而且需要重启。

运行后，高级版功能都可以打开，但是无法开启抓包功能。

因为开启抓包需要开通网络访问权限以及VPN的相关权限，由于账号没有付费成为苹果开发者账号，因此这些权限无法使用。

苹果开发者账号可用的权限：

![img](1666147369001.png)

非开发者账号可用的权限：

![img](1666147437744.png)

这里即使把权限添加上，也会编译不通过的。

![img](1666147780150.png)

这里就需要注册成开发者账号才可以继续进行，因此就放弃了。

## 0x03 总结

本文通过一款抓包APP借助于frida来获取高级权限，另外介绍了一下OC下NSData、NSString、NSMutableDictionary之间的数据转换，以及翻译成frida中js代码的实现。

其实...