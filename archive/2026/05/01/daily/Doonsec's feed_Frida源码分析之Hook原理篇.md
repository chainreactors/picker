---
title: Frida源码分析之Hook原理篇
url: https://mp.weixin.qq.com/s/01jclmwrlxLDLCfHPFAN-g
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:56:04.120397
---

# Frida源码分析之Hook原理篇

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3L4wBGyy7cW4AHKyibaQuZriclRGW0ic4u1HIiaZJNn8q5aljpwIezia6NJEEr6mDJcs13Q6S4s1uneHgt4r0Wt0JCTJTJQd8WicLSE/0?wx_fmt=jpeg)

# Frida源码分析之Hook原理篇

gal2xy
gal2xy

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**Frida-gum简介**

Frida Gum 是一个底层代码插桩库，可在多个平台和架构上提供动态二进制插桩功能。它支持通过函数钩子（fun hooking`GumInterceptor`）、指令级跟踪（include-level tracing`GumStalker`）、内存访问监控（memory access monitoring`GumMemoryAccessMonitor`）和代码生成来运行时操作本地代码。该库支持 Darwin（macOS/iOS）、Linux、Windows、FreeBSD 和 QNX 平台上的 x86、x86\_64、ARM、ARM64 和 MIPS 架构。

**Hook函数的JS Bindings入口**

以Native层的Hook为例：

```
Interceptor.replace(addr, new NativeCallback(), retType, paramTypes)
Interceptor.attach(addr, {onEnter(args){}, onLeave(retval){}})
```

这些JS API在`bindings/gumjs/gumquickinterceptor.c`绑定了Native层函数。

`Interceptor.attach`绑定`gumjs_interceptor_attach`函数。

```
GUMJS_DEFINE_FUNCTION (gumjs_interceptor_attach)
{
  JSValue target_val = args->elements[0];
  JSValue cb_val = args->elements[1];
  JSValue data_val = args->elements[2];
  GumQuickInterceptor * self;
  gpointer target, cb_ptr;
  GumQuickInvocationListener * listener = NULL;
  gpointer listener_function_data;
  GumAttachReturn attach_ret;

self = gumjs_get_parent_module (core);

//...
// 解析 onEnter onLeave 并生成监听器
else
  {
    JSValue on_enter_js, on_leave_js;
    GumQuickCHook on_enter_c, on_leave_c;

if (!_gum_quick_args_parse (args, "pF*{onEnter?,onLeave?}", &target,
        &on_enter_js, &on_enter_c,
        &on_leave_js, &on_leave_c))
      goto propagate_exception;

if (!JS_IsNull (on_enter_js) || !JS_IsNull (on_leave_js))
    {
      GumQuickJSCallListener * l;

      l = g_object_new (GUM_QUICK_TYPE_JS_CALL_LISTENER, NULL);
      l->on_enter = JS_DupValue (ctx, on_enter_js);
      l->on_leave = JS_DupValue (ctx, on_leave_js);

      listener = GUM_QUICK_INVOCATION_LISTENER (l);
    }
else if (on_enter_c != NULL || on_leave_c != NULL)
    {
      GumQuickCCallListener * l;

      l = g_object_new (GUM_QUICK_TYPE_C_CALL_LISTENER, NULL);
      l->on_enter = on_enter_c;
      l->on_leave = on_leave_c;

      listener = GUM_QUICK_INVOCATION_LISTENER (l);
    }
//...
  }

//可选参数data解析...

  listener->parent = self;
// 调用	gum_interceptor_attach
  attach_ret = gum_interceptor_attach (self->interceptor, target,
GUM_INVOCATION_LISTENER (listener), listener_function_data,
      GUM_ATTACH_FLAGS_NONE);

if (attach_ret != GUM_ATTACH_OK)
    goto unable_to_attach;

  listener->wrapper = JS_NewObjectClass (ctx, self->invocation_listener_class);
JS_SetOpaque (listener->wrapper, listener);
JS_DefinePropertyValue (ctx, listener->wrapper,
GUM_QUICK_CORE_ATOM (core, resource),
JS_DupValue (ctx, cb_val),
0);

g_hash_table_add (self->invocation_listeners, listener);

return JS_DupValue (ctx, listener->wrapper);

//...
}
```

调用`gum_interceptor_attach`函数，传入的第四个参数（即flags）为`GUM_ATTACH_FLAGS_NONE = 0`。

而对于`Interceptor.replace`，其绑定的是`gumjs_interceptor_replace`，额外有另一个函数是`gumjs_interceptor_replace_fast`。它们都调用相同的方法`gum_interceptor_replace_with_type`，不同之处在于replace模式下传入的第二个参数为`GUM_INTERCEPTOR_TYPE_DEFAULT= 0`。

而replace fast模式下传入的第二个参数为`GUM_INTERCEPTOR_TYPE_FAST=1`。

```
// gum\guminterceptor.c
GumReplaceReturn
gum_interceptor_replace (GumInterceptor * self,
                         gpointer function_address,
                         gpointer replacement_function,
                         gpointer replacement_data,
                         gpointer * original_function)
{
return gum_interceptor_replace_with_type (self, GUM_INTERCEPTOR_TYPE_DEFAULT,
      function_address, replacement_function, replacement_data,
      original_function);
}

GumReplaceReturn
gum_interceptor_replace_fast (GumInterceptor * self,
                              gpointer function_address,
                              gpointer replacement_function,
                              gpointer * original_function)
{
return gum_interceptor_replace_with_type (self, GUM_INTERCEPTOR_TYPE_FAST,
      function_address, replacement_function, NULL,
      original_function);
}
```

尽管如此，`gum_interceptor_replace_with_type`跟`gum_interceptor_attach`的关键代码调用相同，因此以`gum_interceptor_attach`为例进行分析。

**gum\_interceptor\_attach**

```
GumAttachReturn
gum_interceptor_attach (GumInterceptor * self,
                        gpointer function_address,
                        GumInvocationListener * listener,
                        gpointer listener_function_data,
                        GumAttachFlags flags)
{
  GumAttachReturn result = GUM_ATTACH_OK;
  GumFunctionContext * function_ctx;
  GumInstrumentationError error;

  gum_interceptor_ignore_current_thread (self);
  GUM_INTERCEPTOR_LOCK (self);
// 开始hook事务
  gum_interceptor_transaction_begin (&self->current_transaction);
self->current_transaction.is_dirty = TRUE;
// 获取被hook函数的地址
  function_address = gum_interceptor_resolve (self, function_address);
// 生成跳板代码，第四个参数为false
  function_ctx = gum_interceptor_instrument (self, GUM_INTERCEPTOR_TYPE_DEFAULT,
      function_address, (flags & GUM_ATTACH_FLAGS_FORCE) != 0, &error);

if (function_ctx == NULL)
goto instrumentation_error;
// 重复hook
if (gum_function_context_has_listener (function_ctx, listener))
goto already_attached;
// 添加监听器(例如onEnter onLeave事件)
  gum_function_context_add_listener (function_ctx, listener,
      listener_function_data, (flags & GUM_ATTACH_FLAGS_UNIGNORABLE) != 0);

goto beach;

// labels ...
beach:
  {
// 结束hook事务，提交并处理hook事务
    gum_interceptor_transaction_end (&self->current_transaction);
    GUM_INTERCEPTOR_UNLOCK (self);
    gum_interceptor_unignore_current_thread (self);

return result;
  }
}
```

`gum_interceptor_attach`整个代码逻辑是通过事务的方式进行处理的。它首先调用`gum_interceptor_resolve()`函数以获取真实的函数入口地址。然后调用`gum_interceptor_instrument()`函数生成底层的跳板代码（相较于一级跳板），最后调用`gum_interceptor_transaction_end`提交Hook事务，里面会生成一级跳板。

## 获取真实函数入口地址

### gum\_interceptor\_resolve

```
static gpointer
gum_interceptor_resolve (GumInterceptor * self,
                         gpointer address)
{
// 进行指针认证，在支持指令认证的平台上调用ptrauth_strip进行认证，对于不支持的平台直接返回值
  address = gum_strip_code_pointer (address);
// 判断当前地址是否已经存入哈希表中
if (!gum_interceptor_has (self, address))
  {
// inline hook所修改的字节大小
const gsize max_redirect_size = 16;
    gpointer target;

    gum_ensure_code_readable (address, max_redirect_size);// 修改所在页为RWX权限

/* Avoid following grafted branches. */
//检查代码签名策略，如果需要代码签名，则直接返回地址
if (gum_process_get_code_signing_policy () == GUM_CODE_SIGNING_REQUIRED)// GUM_CODE_SIGNING_OPTIONAL
return address;
// 获取inline hook所涉及到的16字节中的相对跳转地址
    target = _gum_interceptor_backend_resolve_redirect (self->backend,
        address);
if (target != NULL)// 如果存在相对跳转地址，则进行递归，以获取最
return gum_interceptor_resolve (self, target);
  }

return address;
}
```

该函数功能主要是递归以穿透跳板代码，获取到真实的hook地址。具体来说，它通过`_gum_interceptor_backend_resolve_redirect`函数获取目标地址处的前16字节中的首个相对跳转指令，解析出跳转地址，如果存在相对跳转，则进一步递归调用`gum_interceptor_resolve`函数以获取无相对跳转指令的空间用于inline hook。

### gum\_ensure\_code\_readable

```
void
gum_ensure_code_readable (gconstpointer address,
                          gsize size){
/*
   * We will make this more generic once it's needed on other OSes.
   */
#ifdef HAVE_ANDROID
  gsize page_size;
  gconstpointer start_page, end_page, cur_page;

// 低于Android 10 直接返回
if (gum_android_get_api_level () < 29)
return;

  page_size = gum_query_page_size ();//获取系统页大小
  start_page = GSIZE_TO_POINTER (
GPOINTER_TO_SIZE (address) & ~(page_size - 1));
  end_page = GSIZE_TO_POINTER (
GPOINTER_TO_SIZE (address + size - 1) & ~(page_size - 1)) + page_size;

G_LOCK (gum_softened_code_pages);

if (gum_softened_code_pages == NULL)
    gum_softened_code_pages = g_hash_table_new (NULL, NULL);
// 添加起始页~结束页的地址到哈希表中
for (cur_page = start_page; cur_page != end_page; cur_page += page_size)
  {
if (!g_hash_table_contains (gum_softened_code_pages, cur_page))//是否已经加入到哈希表中
    {
if (gum_try_mprotect ((gpointer) cur_page, page_size, GUM_PAGE_RWX))//修改页权限为RWX
g_hash_table_add (gum_softened_code_pages, (gpointer) cur_page);//添加
    }
  }

G_UNLOCK (gum_softened_...