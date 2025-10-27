---
title: Java 代码解密：使用 Frida 还原 JVMTI Agent 加密保护的java类 & Linux 环境下的Frida 使用
url: https://rce.moe/2024/11/09/Java-Code-Decryption-Using-Frida-Restoring-JVMTI-Agent-Encrypted-Classes-Using-Frida-in-Linux/
source: 白帽酱の博客
date: 2024-11-10
fetch_date: 2025-10-06T19:15:16.902882
---

# Java 代码解密：使用 Frida 还原 JVMTI Agent 加密保护的java类 & Linux 环境下的Frida 使用

Toc

1. [从一个奇怪jar开始の奇妙分析](#%E4%BB%8E%E4%B8%80%E4%B8%AA%E5%A5%87%E6%80%AAjar%E5%BC%80%E5%A7%8B%E3%81%AE%E5%A5%87%E5%A6%99%E5%88%86%E6%9E%90)
   1. [从零开始の代码还原](#%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E3%81%AE%E4%BB%A3%E7%A0%81%E8%BF%98%E5%8E%9F)
      1. [SO分析](#SO%E5%88%86%E6%9E%90)
      2. [JVMTI](#JVMTI)
      3. [JVM](#JVM)
      4. [Frida](#Frida)
         1. [Linux平台下的远程 Frida HOOK](#Linux%E5%B9%B3%E5%8F%B0%E4%B8%8B%E7%9A%84%E8%BF%9C%E7%A8%8B-Frida-HOOK)
            1. [HOOK环境搭建](#HOOK%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA)
            2. [HOOK JVM](#HOOK-JVM)
            3. [HOOK dlopen](#HOOK-dlopen)
            4. [HOOK JVMTI](#HOOK-JVMTI)
   2. [结束](#%E7%BB%93%E6%9D%9F)
2. [参考](#%E5%8F%82%E8%80%83)

Toc

**0** results found
![](/images/logo.jpeg)

[首页](/)
[归档](/archives)
[分类](/categories)
[标签](/tags)
[友链](/friends)
[关于](/about)

白帽酱

白帽酱

[首页](/)
[归档](/archives)
[分类](/categories)
[标签](/tags)
[友链](/friends)
[关于](/about)

Java 代码解密：使用 Frida 还原 JVMTI Agent 加密保护的java类 & Linux 环境下的Frida 使用

2024/11/09

[web](/categories/web)

[WEB](/tags/WEB)
[Frida](/tags/Frida)

Java 代码解密：使用 Frida 还原 JVMTI Agent 加密保护的java类 & Linux 环境下的Frida 使用

> 2024/11/08 auth: 橙子酱 i@rce.moe

# 从一个奇怪jar开始の奇妙分析

在一次平常的代码审计中，我在尝试反编译一个 JAR 文件，发现大部分的CLASS反编译失败了，返回的结果一片空白

[![image-20241107174837584](https://cdn.nlark.com/yuque/0/2024/png/25577536/1731119534471-01498aa8-6985-45c2-928d-46364ddf9378.png)](https://cdn.nlark.com/yuque/0/2024/png/25577536/1731119534471-01498aa8-6985-45c2-928d-46364ddf9378.png)

这一定是被什么东西加密了，平常也经常遇到java agent的加密，先检查一下JVM启动参数

|  |
| --- |
| ``` /bin/java -- -Dsun.misc.URLClassPath.disableJarChecking=true -agentpath:./xxxagent.so ``` |

但是这次好像不太一样，agentpath 参数对应的不是JAR 而是一个so库，这里只能先试着逆着看看了

[![image-20241107180744294](https://cdn.nlark.com/yuque/0/2024/png/25577536/1731119534611-42856ce2-306a-430e-adb5-780d6c2f0871.png)](https://cdn.nlark.com/yuque/0/2024/png/25577536/1731119534611-42856ce2-306a-430e-adb5-780d6c2f0871.png)

## 从零开始の代码还原

### SO分析

接下来就开始使用ida分析这个so了

[![image-20241107180141745](https://cdn.nlark.com/yuque/0/2024/png/25577536/1731119534767-5c247ba3-5eaf-4c5c-b94e-d2ef763bf6f7.png)](https://cdn.nlark.com/yuque/0/2024/png/25577536/1731119534767-5c247ba3-5eaf-4c5c-b94e-d2ef763bf6f7.png)

这看起来不太妙

[![image-20241107180410546](https://cdn.nlark.com/yuque/0/2024/png/25577536/1731119534953-343a4b0d-8cf7-45a9-9709-48641b4bcf13.png)](https://cdn.nlark.com/yuque/0/2024/png/25577536/1731119534953-343a4b0d-8cf7-45a9-9709-48641b4bcf13.png)

IDA仅识别出了一部分函数，并且大多数函数体无法正确反编译。我不太擅长逆向，这里节约时间只能使用其他方法了。

### JVMTI

[![1731038300260](https://cdn.nlark.com/yuque/0/2024/jpeg/25577536/1731119535230-920069c7-7af1-499d-aec8-c9171101b16f.jpeg)](https://cdn.nlark.com/yuque/0/2024/jpeg/25577536/1731119535230-920069c7-7af1-499d-aec8-c9171101b16f.jpeg)

不同于常见的Java Agent ，目标项目使用了一种更底层的Agent类型 JVM Tool Interface (JVM TI) Agent。它是通过JVM导出的C++ API 对JVM 进行操作，来实现某些特定功能。

通过阅读JVMTI的相关文档发现 JVMTI Agent 可以通过注册 `ClassFileLoadHook` 来拦截 JVM 加载的类文件，从而实现在类加载时对其进行解密。

|  |
| --- |
| ``` //场景的伪代码示例 void JNICALL ClassFileLoadHook(jvmtiEnv *jvmti_env, JNIEnv *jni_env, jclass class_being_loaded,                                const char *name, jobject protection_domain, jint class_data_len,                                const unsigned char *class_data, jint *new_class_data_len,                                unsigned char **new_class_data) {     // 在这里可以插入解密代码, 它会加载class文件之前进行解密操作      std::cout << "Class file loaded: " << name << std::endl;      // 例如，解密后的字节码存放到new_class_data中     *new_class_data_len = class_data_len;  // 设置新的字节码长度     *new_class_data = const_cast<unsigned char *>(class_data);  // 这里假设没有改变数据      // 继续加载原始或解密后的class数据 } jvmtiEnv *jvmti = nullptr; JavaVM *jvm = nullptr; JNIEXPORT jint JNICALL Agent_OnLoad(JavaVM *vm, char *options, void *reserved) {     // 获取jvmti环境     jint res = vm->GetEnv(reinterpret_cast<void **>(&jvmti), JVMTI_VERSION);     if (res != JNI_OK || jvmti == nullptr) {         std::cerr << "Error: Unable to access JVMTI version." << std::endl;         return res;     }      // 注册ClassFileLoadHook回调     jvmtiEventCallbacks callbacks = {0};     callbacks.ClassFileLoadHook = &ClassFileLoadHook;      res = jvmti->SetEventCallbacks(&callbacks, sizeof(callbacks));     if (res != JVMTI_ERROR_NONE) {         std::cerr << "Error: Unable to set event callbacks." << std::endl;         return res;     }      // 启动ClassFileLoadHook事件     res = jvmti->SetEventNotificationMode(JVMTI_EVENT_CLASS_FILE_LOAD, JVMTI_ENABLE, nullptr);     if (res != JVMTI_ERROR_NONE) {         std::cerr << "Error: Unable to enable class file load event." << std::endl;         return res;     }      return JNI_OK; } ``` |

显然，我们只要 HOOK Agent中定义的 ClassFileLoadHook函数就可以拿到解密后的class字节码。

但是加壳后Agent 的解密函数难以定位，这里我们只能转到JVM的代码中分析了。

### JVM

目标使用了Open JDK，到官网就可以下到历史版本的源码（Oracle JDK 并没有提供JVM部分的源码）。

简单的搜索了下JVM的源码，通过API关键字定位到了一个函数`hotspot\src\share\vm\prims\jvmtiExport.cpp:post_to_env`。

|  |
| --- |
| ```   void post_to_env(JvmtiEnv* env, bool caching_needed) {     unsigned char *new_data = NULL;     jint new_len = 0;   /*......*/     JvmtiClassFileLoadEventMark jem(_thread, _h_name, _class_loader,                                     _h_protection_domain,                                     _h_class_being_redefined);     JvmtiJavaThreadEventTransition jet(_thread);     JNIEnv* jni_env =  (JvmtiEnv::get_phase() == JVMTI_PHASE_PRIMORDIAL)?                                                         NULL : jem.jni_env();     jvmtiEventClassFileLoadHook callback = env->callbacks()->ClassFileLoadHook;     if (callback != NULL) {       (*callback)(env->jvmti_external(), jni_env,                   jem.class_being_redefined(),                   jem.jloader(), jem.class_name(),                   jem.protection_domain(),                   _curr_len, _curr_data,                   &new_len, &new_data);     }     if (new_data != NULL) {       // this agent has modified class data.       if (caching_needed && *_cached_class_file_ptr == NULL) {         // data has been changed by the new retransformable agent         // and it hasn't already been cached, cache it         JvmtiCachedClassFileData *p;         p = (JvmtiCachedClassFileData *)os::malloc(           offset_of(JvmtiCachedClassFileData, data) + _curr_len, mtInternal);         if (p == NULL) {           vm_exit_out_of_memory(offset_of(JvmtiCachedClassFileData, data) + _curr_len,             OOM_MALLOC_ERROR,             "unable to allocate cached copy of original class bytes");         }         p->length = _curr_len;         memcpy(p->data, _curr_data, _curr_len);         *_cached_class_file_ptr = p;       }        if (_curr_data != *_data_ptr) {         // curr_data is previous agent modified class data.         // And this has been changed by the new agent so         // we can delete it now.         _curr_env->Deallocate(_curr_data);       }        // Class file data has changed by the current agent.       _curr_data = new_data;       _curr_len = new_len;       // Save the current agent env we need this to deallocate the       // memory allocated by this agent.       _curr_env = env;     }   }   /*......*/ }; ``` |

在JVM加载class字节码的时候，JVM会判断当前是否存在jvmtiEventClassFileLoadHook。如果存在就先执行hook，如果执行后字节码被修改则使用修改后的字节码。

一路跟随，我找到了这个函数，这个函数看起来非常适合HOOK，这里就决定使用它了。

|  |
| --- |
| ``` // this entry is for class file load hook on class load, redefine and retransform void JvmtiExport::post_class_file_load_hook(Symbol* h_name,                                             Handle class_loader,                                             Handle h_protection_domain,                                             unsigned char **data_ptr,                                             unsigned char **end_ptr,                                             JvmtiCachedClassFileData **cache_ptr) {   JvmtiClassFileLoadHookPoster poster(h_name, class_loader,                                       h_protection_domain,                                       data_ptr, end_ptr,                                 ...