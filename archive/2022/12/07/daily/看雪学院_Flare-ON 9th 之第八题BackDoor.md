---
title: Flare-ON 9th 之第八题BackDoor
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458486646&idx=2&sn=249efd303327892dedf7e2e0c16593b7&chksm=b18eb7fc86f93eea8d89c736fca8a5b3269470353b2704ba26fde64b1550560dcb409ce103c4&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-12-07
fetch_date: 2025-10-04T00:41:18.727209
---

# Flare-ON 9th 之第八题BackDoor

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Htr4puZRiaaymZZuwvnGiavmLNbSSQbEU6q5pNy7ic4pq9O04bVPzd9onToGl80owicib6zribpicMzKDkQ/0?wx_fmt=jpeg)

# Flare-ON 9th 之第八题BackDoor

wmsuper

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fhic9PHGb6VnEyUEXLGpf45rnE7IMxwaZRUwMZpq5icecFTY4SXKvia5zlfUQo5yDriaqrYcM6gFUXBw/640?wx_fmt=jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：wmsuper

```
一

概述
```

今年由火眼举办的flare-on 9th CTF刚刚结束，接下来准备介绍令我印象比较深刻的第八题BackDoor的解题方法。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fhic9PHGb6VnEyUEXLGpf45jVRYic8RvBQtECDm7VywlULhJ9GMFBa5gibXCEQgcnGut8KJQS6ibG3BA/640?wx_fmt=png)

#

#

```
二

C#反混淆
```

##

## **混淆原理**

使用DnSpy打开exe，确定无疑的是该C#编写的程序肯定经过了混淆，不是已知的任何一种混淆壳，无法使用De4dot直接反混淆：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fhic9PHGb6VnEyUEXLGpf45XIIuMCdXQIC3jdUibz2NsqLLTrK5pnFKkBib25OicNnLdh8OrrlPwI5sQ/640?wx_fmt=png)

##

## **第一层混淆**

让我们简单先分析下混淆的原理，根据原理来完成去混淆，通过分析，有大部分函数是通过触发异常来完成解密方法体的调用的，如下所示：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fhic9PHGb6VnEyUEXLGpf45cjFxseIiciazJWIOA6relrUdVSbXuQp5XAMvRniavdicUP39RIWheeHJYA/640?wx_fmt=png)
flare\_71方法使用DynamicMethod根据传入的字节码数组来进行动态调用：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fhic9PHGb6VnEyUEXLGpf45QulXIwWgIUe605mWv9fyiaXz3xX6dVQyEJhKKWQw8M22rVn11o5J9xA/640?wx_fmt=png)
这类受保护的方法还有一个很明显的特征就是开头是两个NOP，而且调用了flare\_71，知道这些后就可以编写代码还原第一层混淆：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fhic9PHGb6VnEyUEXLGpf45KUFM24icFgv9dQ7noI87bXAWEltic98cauSC1V8MzbTKxrrB4w6Rks6w/640?wx_fmt=png)
代码如下所示，自动寻找符合特征的函数，调用目标exe里面的相关方法并修复exe。

```
private static void flareon_wrap_decrypt(IList<TypeDef> typeDefs) {      foreach (var typeDef in typeDefs)         foreach (var methodDef in typeDef.Methods)             if (methodDef.Module.Name == Assembly.ManifestModule.ScopeName && methodDef.HasBody &&                 methodDef.Body.Instructions.Count > 2 && methodDef.Body.Instructions[0].OpCode == OpCodes.Nop &&                 methodDef.Body.Instructions[1].OpCode == OpCodes.Nop)             {                 var is_wrap = false;                 var find_true_call = false;                 MethodDef true_call_MethodDef = null;                 var is_get_all_args = false;                 var args_token = new int[2];                 var Instructions = methodDef.Body.Instructions;                   for (var i = 0; i < Instructions.Count; i++)                 {                     if (!find_true_call && Instructions[i].OpCode == OpCodes.Call)                     {                          find_true_call = true;                         true_call_MethodDef = (MethodDef)Instructions[i].Operand;                     }                     if (Instructions[i].OpCode == OpCodes.Ldsfld && Instructions[i + 1].OpCode == OpCodes.Ldsfld)                     {                          args_token[0] = ((FieldDef)Instructions[i].Operand).MDToken.ToInt32();                         args_token[1] = ((FieldDef)Instructions[i + 1].Operand).MDToken.ToInt32();                         Console.WriteLine("---------------------");                         Console.WriteLine(Instructions[i].Operand.ToString());                          Console.WriteLine(Instructions[i + 1].Operand.ToString());                         Console.WriteLine("---------------------");                         is_get_all_args = true;                     }                     if (Instructions[i].OpCode == OpCodes.Call && Instructions[i].Operand.ToString().Contains("flare_71") && is_get_all_args)                     {                           is_wrap = true;                     }                  }                 if (is_wrap && find_true_call)                 {                     CurrentMethod = methodDef;                     var fieldInfo0 = Assembly.Modules.FirstOrDefault().ResolveField(args_token[0]);                     var fieldInfo1 = Assembly.Modules.FirstOrDefault().ResolveField(args_token[1]);                     var arg0 = (Dictionary<uint, int>)fieldInfo0.GetValue(null);                     var arg1 = (byte[])fieldInfo1.GetValue(null);                      Console.WriteLine(methodDef.FullName);                     var dm = flare.flare_71(Assembly.Modules.FirstOrDefault(), true_call_MethodDef.MDToken.ToInt32(), arg0, arg1);                      var methodBody = MethodBodyReader.CreateCilBody(AssemblyWriter.moduleDef, arg1, null, true_call_MethodDef.Parameters, 1, true_call_MethodDef.Body.MaxStack, (uint)(arg1.Length), true_call_MethodDef.Body.LocalVarSigTok, GenericParamContext.Create(true_call_MethodDef));                      true_call_MethodDef.FreeMethodBody();                     true_call_MethodDef.Body = methodBody;                     Console.WriteLine(true_call_MethodDef.Name);                    }              } }
```

##

## **第二层混淆**

在解密出第一层混淆，很快又发现了第二层混淆， 通过方法体的token算出hash，然后通过hash索引PE文件中区段数据，经过RC4解密解密出方法体。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fhic9PHGb6VnEyUEXLGpf45qZzcLyVariaiaibUiciaHMicAsia8LnkfxCCicHRsCvIic9BfNucotyZiaFribwdw/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fhic9PHGb6VnEyUEXLGpf45BhAyMRvTLVZiafmvbD0lIJmHmpM4UlM45BqODEGa1rfgwHaic9cY1bibA/640?wx_fmt=png)
第二层混淆被保护的方法体的名称都是flared打头的：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fhic9PHGb6VnEyUEXLGpf45utzKXObSDR1Ojibs0Y57KQ1JzF3riafaZXlKBYib8gHznNDXpF8H48DRQ/640?wx_fmt=png)
接下来编写程序自动化找到这些函数，并调用RC4解密进行修复，代码如下所示：

```
private static void flareon_decrypt(IList<TypeDef> typeDefs){     foreach (var typeDef in typeDefs)        foreach (var methodDef in typeDef.Methods)            if (methodDef.Module.Name == Assembly.ManifestModule.ScopeName  &&                  methodDef.ToString().Contains("flared"))            {                Console.WriteLine(methodDef.Name);                var token = methodDef.MDToken.ToInt32();                var method = Assembly.Modules.FirstOrDefault()?.ResolveMethod(token);                var ILcode = method.GetMethodBody().GetILAsByteArray();                var hash_text = flare.flared_66(Assembly.Modules.FirstOrDefault(), token);                byte[] sec_data = GetSectionData(hash_text);                byte[] decrypted_IL_code = flare.rc4(new byte[] { 18, 120, 171, 223 }, sec_data);                var dm = flare.flared_67(Assembly.Modules.FirstOrDefault(), decrypted_IL_code, token);                Console.WriteLine(sec_data.Length);                 var methodBody = MethodBodyReader.CreateCilBody(AssemblyWriter.moduleDef, decrypted_IL_code, null, methodDef.Parameters, 1, methodDef.Body.MaxStack, (uint)(decrypted_IL_code.Length), methodDef.Body.LocalVarSigTok, GenericParamContext.Create(methodDef));                 if(methodDef.Body.HasExceptionHandlers)                {                    Console.WriteLine(methodDef.Name+": " +methodDef.Body.ExceptionHandlers.Count);                }                methodDef.FreeMethodBody();                methodDef.Body = methodBody;            } }
```

至此，程序反混淆完成，开始分析。

#

#

```
三

DNS隧道协议
```

在运行程序后，使用wireshark观察其网络活动，一开始我就注意到dns活动，猜测该后门和C&C交互使用DNS隧道进行通信：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fhic9PHGb6VnEyUEXLGpf45odmRtXGT6LLcRzwf8poyHibyhyHyxUs3jEkCeFTuoUfe8f1ElYUhGyQ/640?wx_fmt=png)
编写一个DNS server模拟C&C的响应包并对exe进行调试：

```
from dnslib import *from dnslib.server import *import sysimport time class TestResolver:    def __init__(self):        self.data=[]        op=[2, 10, 8, 19, 11, 1, 15, 13, 22, 16, 5, 12, 21, 3, 18, 17, 20, 14, 9, 7, 4]        for i in op:            op_str=str(i)            payload_len=len(op_str)            s=['43']            for k in range(payload_len):                s.append(str(ord(op_str[k])))            s=s+(4-len(s))*["0"]            pl='.'.join(s)            self.data+=(['192.0.0.%d'%(payload_len+1)]+[pl])         self.data=100*self.data        print(self.data)        self.pos=0     def resolve(self,request,handler):         reply = request.reply()        qname = request.q.qname        qtype = request.q.qtype         if "flare-on.com" in str(qname) and QTYPE[qtype]=='A':            answer = RR(rname=qname,ttl=60, rdata=A(s...