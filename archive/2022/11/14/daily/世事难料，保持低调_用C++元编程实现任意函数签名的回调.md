---
title: 用C++元编程实现任意函数签名的回调
url: https://blog.csdn.net/ariesjzj/article/details/127816351
source: 世事难料，保持低调
date: 2022-11-14
fetch_date: 2025-10-03T22:39:38.103984
---

# 用C++元编程实现任意函数签名的回调

# 用C++元编程实现任意函数签名的回调

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[ariesjzj](https://jinzhuojun.blog.csdn.net "ariesjzj")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2022-11-13 09:53:00 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.3k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
1

CC 4.0 BY-SA版权

文章标签：
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[元编程](https://so.csdn.net/so/search/s.do?q=%E5%85%83%E7%BC%96%E7%A8%8B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[回调函数](https://so.csdn.net/so/search/s.do?q=%E5%9B%9E%E8%B0%83%E5%87%BD%E6%95%B0&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[C++](https://so.csdn.net/so/search/s.do?q=C%2B%2B&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[函数注册](https://so.csdn.net/so/search/s.do?q=%E5%87%BD%E6%95%B0%E6%B3%A8%E5%86%8C&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2022-11-13 08:51:51 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/jinzhuojun/article/details/127816351>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756926.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

C++
专栏收录该内容](https://blog.csdn.net/ariesjzj/category_12100278.html "C++")

1 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文介绍了如何在C++中使用Variadic Templates和元编程技术实现类似Python中的任意函数签名回调注册。通过C++的OpRegistryImpl模板类和DispatchFnImpl模板，结合递归模板特化，能够在编译时为不同函数生成调用代码，实现对不同函数签名的回调函数的注册。这种技术在TFRT项目中被用于GPU和CPU操作的注册。

注册回调函数在`C++`中是十分常见的做法。如：

```
void (*func_ptr)(int, string);

void foo(int x, string s) {
    std::cout << __func__ << " " << x << " " << s << endl;
}

int main()
{
    func_ptr = foo;
    func_ptr(1, "hello");
    return 0;
}
```

但大多时候（像上面这个例子一样）需要显式给出回调函数的声明，因为编译需要这个信息来根据ABI生成函数调用代码。那么问题来了，如果我们想注册不同的任意函数签名的回调函数呢？

先来看下在Python中如何实现：

```
class Test:
    def __init__(self, func):
        self.callback = func

    def call_func(self, args):
        self.callback(*args)

def foo(x, y):
    print(f"foo {x} {y}")

test = Test(foo)
test.call_func((1, "hello"))
```

这里的`foo`是回调函数，在`Test`类的构造函数中传入并存于`callback`变量中。调用时将所有参数以tuple类型传入，然后调用回调函数时用星号进行unpacking。

Python是解释型语言，因此比较容易实现。但如果我们想在`C++`中实现呢？这就需要用到`C++`中Variadic Template特性（可参考《The C++ Programing Language》28.6）。它用到元编程（Meta-programming）。我们知道，meta-programming图灵完备，功能强大。这意味着很多事可以通过它放到编译时做，提高运行时效率，但是其缺点除了编译慢、code bloat外，还有就是难读。。。尤其是有些复杂的用法，看得那叫一个醱爽。关于variadic template的用法，最常用的例子可能就是`printf`了。代码可以参考https://en.cppreference.com/w/cpp/language/parameter\_pack，这里就不粘了。基本思想就是利用模板做编译时的递归。

回到主题问题上来，那如何基本它来实现任意函数签名的回调注册呢？在[TFRT](https://github.com/tensorflow/runtime)（TFRT是Google的项目，意在替换TensorFlow中的Runtime）中有这样的用法，下面走读下代码学习一下。先从简单的例子看它的用法。如`backends/gpu/lib/ops/test/test_ops.cc`中通过下面语句注册回调：

```
static llvm::Expected<DenseGpuTensor> GpuStreamSynchronize(
    GpuDispatchContext* dctx, const DenseGpuTensor& input,
    const TensorMetadata& result_md) {
  if (auto err = wrapper::StreamSynchronize(dctx->stream())) {
    return std::move(err);
  }
  return input.CopyRef();
}

registry->AddOp("tfrt_test.synchronize", TFRT_GPU_OP(GpuStreamSynchronize));

registry->AddOp("tfrt_test.create_dense_tensor",
                TFRT_GPU_OP(CreateDenseTensorOp), {"shape", "values"});
```

还有`test_cuda_kernels.cu.cc`中的下面语句：

```
static Expected<DenseGpuTensor> GpuAddOp(GpuDispatchContext* dctx,
                                         const DenseGpuTensor& tensor_a,
                                         const DenseGpuTensor& tensor_b,
                                         const OpAttrsRef& attrs,
                                         const TensorMetadata& result_md) {

registry->AddOp("tfrt_test.add", TFRT_GPU_OP(GpuAddOp));
```

它们的作用是将一个回调函数通过`AddOp`函数注册到注册表`Registry`中去。但问题是这些回调函数的函数签名是不一样的，这意味着我们没法简单地用一个固定类型的函数指针来存放与使用它们。这时meta-programming的作用就体现出来了，它可以在编译时为每种函数生成相应的glue code。

先来看看注册表类的实现。在文件`op_registry_impl.h`中定义了模板类`OpRegistryImpl`：

```
template <typename OpMetadataFnTy, typename DispatchFnTy, typename OpFlagsTy>
class OpRegistryImpl {
 public:
  struct OpEntry {
    OpMetadataFnTy metadata_fn = nullptr;
    DispatchFnTy dispatch_fn = nullptr;
    OpFlagsTy flags;
    string_view op_name;
    ...

  void AddOp(string_view op_name, DispatchFnTy dispatch_fn, OpFlagsTy flags,
             ArrayRef<string_view> attr_names) {
    assert(!op_name.empty() && "op names cannot be empty");
    auto& entry = op_mappings_[op_name];
    entry.dispatch_fn = dispatch_fn;
    entry.flags = flags;
    entry.attr_names.reserve(attr_names.size());
    for (auto name : attr_names) entry.attr_names.emplace_back(name);
    entry.op_name = op_mappings_.find(op_name)->first();
  }
```

CPU与GPU平台上对应的实现类`CpuOpRegistry::Impl`与`GpuOpRegistry::Impl`分别在文件`cpu_op_registry_impl.h`与`gpu_op_registry_impl.h`中：

```
// This is the pImpl implementation details for CpuOpRegistry.
struct CpuOpRegistry::Impl final
    : OpRegistryImpl<OpMetadataFn, CpuDispatchFn, CpuOpFlags> {};

using CpuOpEntry =
    OpRegistryImpl<OpMetadataFn, CpuDispatchFn, CpuOpFlags>::OpEntry;
}  // namespace tfrt
```

```
// This is the pImpl implementation details for GpuOpRegistry.
struct GpuOpRegistry::Impl final
    : OpRegistryImpl<OpMetadataFn, GpuDispatchFn, GpuOpFlags> {};

using GpuOpEntry =
    OpRegistryImpl<OpMetadataFn, GpuDispatchFn, GpuOpFlags>::OpEntry;
```

以CPU为例，`CpuOpRegistry`定义在`cpu_op_registry.h`中：

```
// This is the signature implemented by all CPU ops.  They take Tensor buffers
// inputs and allocate and return tensors for their results.  If the op has a
// metadata function, then the result of the function is passed in as
// result_mds, otherwise it is an empty list.
//
// If the kernel has a runtime failure, the chain should be set to the
// error value, and any invalid results should be set to errors as well.
using CpuDispatchFn = void (*)(const ExecutionContext& exec_ctx,
                               ArrayRef<AsyncValue*> inputs,
                               const OpAttrsRef& attrs,
                               ArrayRef<TensorMetadata> result_mds,
                               MutableArrayRef<RCReference<AsyncValue>> results,
                               AsyncValueRef<Chain>* chain);

...

// This represents a mapping from op names to the associated metadata functions
// (optional) and kernel dispatch functions.
class CpuOpRegistry {
    // Add an op with the specified dispatch function.  This style of dispatch
    // function does not require a metadata function.
    void AddOp(string_view op_name, CpuDispatchFn dispatch_fn, CpuOpFlags flags);
    ...
}
```

上面的`CpuDispatchFn` 是一个跳板函数，一会儿会提到。`CpuOpRegistry::AddOp`函数会调用对应实现类中的`AddOp`函数。对于GPU也是类似的，相关定义在`gpu_op_registry.h`中。

然后再来看看注册的回调函数。可以看到，这些函数都包了一个宏。以GPU为例，`TFRT_GPU_OP`定义在`gpu_op_utils.h`中：

```
#define TFRT_GPU_OP(...)                                             \
  ::tfrt::DispatchFnImpl<GpuDispatchContext, decltype(&__VA_ARGS__), \
                         &__VA_ARGS__>::Invoke
```

其中的模板类`DispatchFnImpl`定义在文件`include/tfrt/core_runtime/op_utils.h`中：

```
// This class is an implementation detail of TFRT_CPU_OP.
template <typename DeviceContext, typename F, F f>
struct DispatchFnImpl;

template <typename DeviceContext, typename Return, typename... Args,
          Return (*impl_fn)(Args...)>
struct DispatchFnImpl<DeviceContext, Return (*)(Args...), impl_fn> {
  // Only add DeviceContext* in the dispatch function if DeviceContext is not
  ...