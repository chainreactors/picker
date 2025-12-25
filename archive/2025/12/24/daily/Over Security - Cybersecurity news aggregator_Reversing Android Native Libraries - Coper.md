---
title: Reversing Android Native Libraries - Coper
url: https://viuleeenz.github.io/posts/2025/12/reversing-android-native-libraries-coper/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-24
fetch_date: 2025-12-25T03:26:53.795680
---

# Reversing Android Native Libraries - Coper

[>
$ cd /home/Viuleeenz](../../../../)

* [About](../../../../about/)
* [Posts](../../../../posts/)
* [Whitepapers](../../../../whitepapers)

13 minutes

# [Reversing Android Native Libraries - Coper](https://Viuleeenz.github.io/posts/2025/12/reversing-android-native-libraries-coper/)

This blog post is part of a recent personal investigation into a malware loader known as **Coper**. Rather than providing a full, line-by-line dissection of the malware, the goal is to introduce a high-level approach to triaging an Android native library.

An increasing number of Android malware families now rely on native libraries to hide their payloads, making reverse engineering a little bit more challenging. Nowadays, having an understanding of what is happening on native libraries is a fundamental skill that needs to be mastered, since it also represents a pivotal point to start investigating other malware families and even architecture.

> 💡 *Through this blogpost, I try to make it as more understandable as possible, making reverse native libraries a little bit less disorienting. Because of that, I would like to make a soft introduction to native libraries, going against a real world example, covering something that goes over the mere basics, without losing the actual focus on learning new things along the way.*

Reference: `1e38419cea3379d8992d165f842f3fd78e9da32aa7f04bcb19e3bdf71d109e2f`

## From Java to Native Code Connection

To execute a function from a native library, the Java code must first declare a corresponding native method. When this Java-declared native method is invoked, the *paired* native function within the compiled library (ELF/.so) is executed.

In Java, a native method looks like a regular method declaration, with two key differences: it is marked with the `native` keyword, and it contains no implementation. This is because the method’s logic resides entirely in the compiled native library rather than in Java code.

![Figure 1: Loading Native Library](../../../../img/coper_notes/loading_native_library.png)

Figure 1: Loading Native Library

The bytecode in an Android application’s `.dex` file declares the native methods. Each of these declarations is paired with a corresponding subroutine in a shared native library. Before any native method can be invoked from Java, the application must load the shared library (`.so` file) using `System.loadLibrary` or `System.load`. When one of these loading methods is called, the `JNI_OnLoad()` function in the shared library (if present) is automatically executed.

> 💡 *If you start exploring the native library straight way, you will see that we do not have the On\_Load function. This could happen for many reasons. JNI\_Onload method usually runs immediately when the library is loaded, breaking this pattern could give some advantages to attackers that could use a dedicated method instead of relying on the builtin routine, having full control over the library running methods under specific conditions (e.g., after verifying device environment variables to detect root or emulation). Moreover in this way its also possible to bypass automation techniques that look for common and standard routines.*

In order to run a native method from Java, the native method must be ‘registered’, meaning that the JNI knows how to pair the Java method definition with the correct function in the native library. This can be done either by leveraging the **RegisterNatives JNI** (static *linking*) function or through `discovery` based on the **function names and function signatures matching** (dynamic *linking*) in both Java and the .so . For either method, a string of the Java method name is required for the JNI to know which native function to call.

In this example we are going to see the usage of function name and signature discovery. In order to pair the Java declared native method and the function in the native library the naming conventions need to meet specific requirements. A native method name needs to be concatenated with the following components:

* the prefix Java\_
* a mangled fully-qualified class name
* an underscore (“\_”) separator
* a mangled method name

![Figure 2: JNI function signature](../../../../img/coper_notes/jni_function_signature.png)

Figure 2: JNI function signature

Looking at the signature, it’s clear that something odd is still there. There are three int parameters that we have not identified in the Java call. What are they? Those parameters are part of the calling convention that actually hides a few things that our disassembler missed. If you look at JNI [documentations](https://developer.android.com/ndk/guides/jni-tips) its possible to rewrite parameters as follow:

```
void Java_com_morninghislbg_FxvheRBQy_odGLksAlj(
    JNIEnv *env,
    jobject this,
    jobject context
)
```

* `JNIEnv *env` represents a getaway to the entire Java world. If we need to call Java methods, classes, objects, access or instantiate strings, etc… **It could be basically seen as a pointer to a structure that contains JNI** [interface function pointers](https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/functions.html).
* `jobject this` is the Java object instance the methods belong to. This object allows the C function to access instance variables of the Java object itself, giving also a chance to call other methods on the same object
* `jobject context` is the actual parameter passed from Java

> 💡 *I know, all the information provided so far could be a little bit disorienting, however,* *before proceeding directly examining the native code, it’s important to get some preliminary information about JNI specification and functions and include them within your decompiler/disassemble tool, missing this step would literally make the reverse session a nightmare since your are not able to distinguish native methods and classes that will be used to follow the overall flow. You can import those files directly in [IDA](https://gist.github.com/Jinmo/048776db75067dcd6c57f1154e65b868) or [Ghidra](https://github.com/extremecoders-re/ghidra-jni).*

## Resolving Names and Creating Structure

Exploring the code through a disassembler and guided by the previous insight we could easily go directly to **Java\_com\_morninghislbg\_FxvheRBQy\_odGLksAlj** function. However, as soon as we open up the code, we are flooded by a quite long list of variables and some strings as well as a lot of *strange* code that appears to be called from an offset related to the first parameter.

![Figure 3: Unresolved JNI names](../../../../img/coper_notes/unresolved_jni_names.png)

Figure 3: Unresolved JNI names

To make the code more readable, its time to set parameters properly, according to the one identified in the previous section. In this case `a1` its the `JNIEnv *` , so we could expect properly resolved functions.

![Figure 4: JNIEnv type structure set](../../../../img/coper_notes/jnienv_typestruct_set.png)

Figure 4: JNIEnv type structure set

Resolving type and renaming the variables properly we could have a little bit more readable code, however, it’s far away from being explorable to reverse and understanding the general workflow. If we look at the beginning of this function we could easily spot a long sequence of **strcpy** with some interesting values like: ***com.morninghislbg:raw/urdvipkyjahgh** and **getResources**.* Those are quite interesting since we are seeing a potential resource and a method to retrieve that. Why? Moreover, we are also able to see some strings related to reflection techniques such as: ***dalvik/system/DexClassLoader**, **setAccessible** or even **Reflect/Field**.*

From here, its possible to make hypothesis and exploring few questions:

* What is that resource in the APK files?
  + Are those resources packed or encrypted? Does it contain code? Why is it used? Is there any relation between that and the DexClassLoader method?

From here there are a couple of options, resolving names for all variables (or...