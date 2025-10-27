---
title: CVE漏洞复现：Maglev中VisitFindNonDefaultConstructorOrConstruct的类型混淆
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458553429&idx=1&sn=d5674757eedccb83f6e0063db0a5205c&chksm=b18dbcdf86fa35c90d21a8db9c292c73f5adad26a9111751b5c4d2c718ea88c46623724de5d2&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-05-03
fetch_date: 2025-10-06T17:15:26.446131
---

# CVE漏洞复现：Maglev中VisitFindNonDefaultConstructorOrConstruct的类型混淆

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ey0Z2fLQtGQHrnic5NDLhqHh54JZvcEtuthKqnicgfXdAk32PC3v7dC0DMJhMrJWWicCxtTsqQ9JiceQ/0?wx_fmt=jpeg)

# CVE漏洞复现：Maglev中VisitFindNonDefaultConstructorOrConstruct的类型混淆

XiaozaYa

看雪学苑

```
一

前言
```

最近在学习`Maglev`相关知识，然后看了一些与其相关的`CVE`，感觉该漏洞比较容易复现，所以先打算复现一下，本文还是主要分析漏洞产生的原因，基础知识笔者会简单说一说，更多的还是需要读者自己去学习。

> 这里说一下为什么笔者不愿意在漏洞分析中写过多的前置知识，因为笔者认为读者都已经开始复现漏洞了，那么对基础知识应当是有一定的了解了，并且笔者的基础也比较差，所以不希望误人子弟，网上的资料很多，自己学学就 OK 啦。

#

```
二

环境搭建
```

```
git checkout 7f22404388ef0eb9383f189c1b0a85b5ea93b079
gclient sync -D
```

#

```
三

前置知识
```

**`new`关键字**：`new func()`效果为：

◆创建一个默认对象`this`，然后进行初始化`this.prop = val`

◆若`func`本身返回一个对象，则抛弃默认对象；否则返回默认对象

这里给一个示例代码：

```
class A {
        constructor() {
                this.x = 1;
        }
}

class B {
        constructor() {
                this.x = 1;
                return [1.1, 2.2];
        }
}

var a = new A();
var b = new B();
print(a); // [object Object]
print(b); // 1.1,2.2
```

**`new.target`**这里自行看资料（https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/new.target）。

**`Reflect.construct(target, argument, new_target)`**函数以`target`为构造函数创建对象，这里`new_target`提供原型，然后行为跟`new func()`类似。

上面的知识都比较简单，所以也不想细说了，如果读者不是很清楚的话，请自行查阅下相关资料吧，这里主要关注`JS`引擎层面的实现。

对于默认对象，其是通过`FastNewObject`函数创建的，其调用链如下：

```
TF_BUILTIN(FastNewObject, ConstructorBuiltinsAssembler)
TNode<JSObject> ConstructorBuiltinsAssembler::FastNewObject(
                                                TNode<Context> context,
                                                TNode<JSFunction> target,
                                                TNode<JSReceiver> new_target)
        ⇒ TNode<JSObject> ConstructorBuiltinsAssembler::FastNewObject(
                                                TNode<Context> context,
                                                TNode<JSFunction> target,
                                                TNode<JSReceiver> new_target,
                                                Label* call_runtime)
```

先来看看`TF_BUILTIN(FastNewObject, ConstructorBuiltinsAssembler)`：

```
TF_BUILTIN(FastNewObject, ConstructorBuiltinsAssembler) {
  auto context = Parameter<Context>(Descriptor::kContext);
  auto target = Parameter<JSFunction>(Descriptor::kTarget);
  auto new_target = Parameter<JSReceiver>(Descriptor::kNewTarget);

  Label call_runtime(this);
  // 先调用 FastNewObject
  TNode<JSObject> result = FastNewObject(context, target, new_target, &call_runtime);
  Return(result);

  BIND(&call_runtime);
  TailCallRuntime(Runtime::kNewObject, context, target, new_target);
}
```

该函数比较简单，其主要就是调用了`ConstructorBuiltinsAssembler::FastNewObject`函数：

```
TNode<JSObject> ConstructorBuiltinsAssembler::FastNewObject(
    TNode<Context> context, TNode<JSFunction> target,
    TNode<JSReceiver> new_target, Label* call_runtime) {
  // Verify that the new target is a JSFunction.
  Label end(this);
  // 检测 new_target 是否是 JSFunction
  TNode<JSFunction> new_target_func = HeapObjectToJSFunctionWithPrototypeSlot(new_target, call_runtime);
  // Fast path.
  // 快速路径
  // Load the initial map and verify that it's in fact a map.
  // 加载 new_target_func 的 initial_map or proto
  TNode<Object> initial_map_or_proto = LoadJSFunctionPrototypeOrInitialMap(new_target_func);
  // 如果 initial_map_or_proto 是 Smi，则调用 call_runtime 运行时函数（相当于慢速路径了）
  GotoIf(TaggedIsSmi(initial_map_or_proto), call_runtime);
  // 检查  initial_map_or_proto  是否是 Map
  GotoIf(DoesntHaveInstanceType(CAST(initial_map_or_proto), MAP_TYPE), call_runtime);
  // initial_map 是一个 Map
  TNode<Map> initial_map = CAST(initial_map_or_proto);

  // Fall back to runtime if the target differs from the new target's initial map constructor.
  // 加载 initial_map 的构造函数 new_target_constructor
  TNode<Object> new_target_constructor = LoadObjectField(initial_map, Map::kConstructorOrBackPointerOrNativeContextOffset);
  // 如果 target != new_target_constructor，则走慢速路径
  GotoIf(TaggedNotEqual(target, new_target_constructor), call_runtime);

  TVARIABLE(HeapObject, properties);
  Label instantiate_map(this), allocate_properties(this);
  GotoIf(IsDictionaryMap(initial_map), &allocate_properties);
  {
    // 分配 properties （非字典模式）
    properties = EmptyFixedArrayConstant();
    Goto(&instantiate_map);
  }
  // 字典模式
  BIND(&allocate_properties);
  {
    if (V8_ENABLE_SWISS_NAME_DICTIONARY_BOOL) {
      properties = AllocateSwissNameDictionary(SwissNameDictionary::kInitialCapacity);
    } else {
      properties = AllocateNameDictionary(NameDictionary::kInitialCapacity);
    }
    Goto(&instantiate_map);
  }

  BIND(&instantiate_map);
  // 最后根据 initial_map 创建 JSObject
  return AllocateJSObjectFromMap(initial_map, properties.value(), base::nullopt,
                                 AllocationFlag::kNone, kWithSlackTracking);
}
```

可以看到`ConstructorBuiltinsAssembler::FastNewObject`分为快速路径和慢速路径：

◆快速路径：直接根据new\_target的initial\_map进行默认对象的创建

* initial\_map的构造函数与target相同
* new\_target的initial\_map为一个有效map

◆慢速路径：调用Runtime::kNewObject运行时函数

这里的快速路径可能有点奇怪？因为这里`target`才是构造函数，所以默认对象的`map`再怎么说也不应该与`new_target`的`initial_map`相同，但这其实是一个优化，其会将`target`的`initial_map`和`new_target`的`prototype`缓存在`new_target`的`initial_map`域，这个后面再说。

然后可以看到走快速路径是存在两个条件的，不满足则会走慢速路径`Runtime::kNewObjec`：

```
RUNTIME_FUNCTION(Runtime_NewObject) {
  HandleScope scope(isolate);
  DCHECK_EQ(2, args.length());
  Handle<JSFunction> target = args.at<JSFunction>(0);
  Handle<JSReceiver> new_target = args.at<JSReceiver>(1);
  RETURN_RESULT_OR_FAILURE(
      isolate,
      JSObject::New(target, new_target, Handle<AllocationSite>::null()));
}
```

可以看到其直接调用了`JSObject::New`函数：

```
MaybeHandle<JSObject> JSObject::New(Handle<JSFunction> constructor,
                                    Handle<JSReceiver> new_target,
                                    Handle<AllocationSite> site) {
  // 这里可以看下注释：其对 new / Reflect.construct 的 new.target 存在不同的要求
  // If called through new, new.target can be:
  // - a subclass of constructor,
  // - a proxy wrapper around constructor, or
  // - the constructor itself.
  // If called through Reflect.construct, it's guaranteed to be a constructor.
  Isolate* const isolate = constructor->GetIsolate();
  DCHECK(constructor->IsConstructor());
  DCHECK(new_target->IsConstructor());
  DCHECK(!constructor->has_initial_map() ||
         !InstanceTypeChecker::IsJSFunction(constructor->initial_map().instance_type()));

  Handle<Map> initial_map;
  //【1】
  ASSIGN_RETURN_ON_EXCEPTION(
      isolate, initial_map,
      JSFunction::GetDerivedMap(isolate, constructor, new_target), JSObject);

  constexpr int initial_capacity = V8_ENABLE_SWISS_NAME_DICTIONARY_BOOL
                                       ? SwissNameDictionary::kInitialCapacity
                                       : NameDictionary::kInitialCapacity;

  Handle<JSObject> result = isolate->factory()->NewFastOrSlowJSObjectFromMap(
      initial_map, initial_capacity, AllocationType::kYoung, site);

  return result;
}
```

在`【1】`处会调用`JSFunction::GetDerivedMap`函数，这里的`constructor`传入的是`target`：

```
MaybeHandle<Map> JSFunction::GetDerivedMap(Isolate* isolate,
                                           Handle<JSFunction> constructor,
                                           Handle<JSReceiver> new_target) {
  // 为 constructor 即 target 分配 initial_map
  EnsureHasInitialMap(constructor);

  Handle<Map> constructor_initial_map(constructor->initial_map(), isolate);
  // 如果 target == new_target，则直接返回
  if (*new_target == *constructor) return constructor_initial_map;

  Handle<Map> result_map;
  // Fast case, new.target is a subclass of constructor. The map is cacheable
  // (and may already have been cached). new.target.prototype is guaranteed to
  // be a JSReceiver.
  // 否则为 new_target 创建 initial_map
  if (new_target->IsJSFunction()) {
    Handle<JSFunction> function = Handle<JSFunction>::cast(new_target);
    if (FastInitializeDerivedMap(isolate, function, constructor, constructor_initial_map)) {
      return handle(function->initial_map(), isolate);
    }
...