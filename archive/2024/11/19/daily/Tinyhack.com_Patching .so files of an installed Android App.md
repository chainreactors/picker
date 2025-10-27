---
title: Patching .so files of an installed Android App
url: https://tinyhack.com/2024/11/18/patching-so-files-of-an-installed-android-app/
source: Tinyhack.com
date: 2024-11-19
fetch_date: 2025-10-06T19:20:59.909806
---

# Patching .so files of an installed Android App

[Skip to content](#content)

[Tinyhack.com](https://tinyhack.com/)

A hacker does for love what others would not do for money.

# Patching .so files of an installed Android App

If we installed an Android APK and we have a root access, we can modify the .so (native) filesof that app without altering the signature. This is true even if `extractNativeLibs` is set to false in `AndroidManifest.xml`. We can also [patch the AOT compiled file](https://github.com/giacomoferretti/odex-patcher) (ODEX/VDEX) without changing the package signature, but that’s another story, I am just going to focus on the native code.

[![](https://tinyhack.com/wp-content/uploads/2024/11/7zFM_LFk6Z5kaJr.png)](https://tinyhack.com/wp-content/uploads/2024/11/7zFM_LFk6Z5kaJr.png)

native libraries are stored uncompressed and page aligned

As a note: this is not a vulnerability, it requires root access. This method was discussed in [the Mystique exploit](https://dawnslab.jd.com/mystique-paper/CSW22-mystique.pdf) presentation (2022). I just want to show that this is useful for pentest purpose, with an extra tip of how to write binary patch in C.

## Background

I was doing a pentest on an Android app with a complex RASP. There are many challenges:

* If I unpack the APK file and repack it, it can detect the signature change
* If I use Frida, it can detect Frida in memory, even when I change the name using [fridare](https://github.com/suifei/fridare)
* It can detect Zygisk, so all injection methods that use Zygisk are detected
* It can detect hooks on any function, not just PLT. It seems that it is done by scanning the prologue of functions to see if it jumps to a location outside the binary; the app developer needs to call this check manually (this is quite an expensive operation), which is usually done before it performs some critical scenario.
* The RASP uses a native library, which is obfuscated

Given enough time, I am sure it is possible to trace and patch everything, but we are time-limited, and I was only asked to check a specific functionality.

When looking at that particular functionality, I can see that it is implemented natively in a non-obfuscated library. In this specific case, If I can patch the native code without altering the signature, I don’t need to deal with all the anti-frida, anti-hook, etc.

## Android Native Libs Installation

Before Android 6.0, all native libraries were extracted during installation. So, when an app is installed, the original APK file and the extracted libraries are stored on device, which takes quite a lot of extra space for the user.

Since Android 6, there has been a setting in `AndroidManifest.xml` called `extractNativeLibs`. If this is set to true, then the behavior is the same as the previous version. If this is set to `false`, the libraries are not extracted, but the libraries must be stored uncompressed and aligned to the page boundary inside the APK (using `zipalign`). With this setting set to `false`, the APK will be larger, but when installed, it will not take extra space for the extracted libraries.

Because the libraries are not compressed and are in a page-aligned position, Android can just `mmap` the libraries to memory. In [Android Gradle Plugin since 3.6.0 extractNativeLibs defaults to false](https://developer.android.com/build/releases/past-releases/agp-3-6-0-release-notes) (February 2020), this is the setting if we are dealing with recent apps.

We can see where the APK files of an Android application are installed using: `adb shell pm path com.example.package`. If we have a split APK, then the native libraries are stored in a separate APK, otherwise everything will be in one APK (base.apk).

The APK signature is checked during installation, but it is only checked again during boot. This makes sense: binary APKs can be really big (hundreds of megabytes), and reverifying this on every app startup will take time. Unlike iOS, which signs every executable binary (it also encrypts the binary if it is installed from the app store), Android doesn’t have something like that.

If `extractNativeLibs` is set to `true`, we can just overwrite the extracted .so files with our new files, and we are done. If `extractNativeLibs` is set to `false`, we can still put the library in directory which would have been used if `extractNativeLibs` is set to true.

For example, if the APK path is:

`/data/app/~~xa3ANgaSg-DH4SuFIlqKLg==/com.tinyhack.testnative-FFtQq51Ol3Dmg2qvpJAYRg==/base.apk`

Assuming we are using 64 bit Android, if we put our patched library in (we remove `base.apk` and replace it with `lib/arm64`:

`/data/app/~~xa3ANgaSg-DH4SuFIlqKLg==/com.tinyhack.testnative-FFtQq51Ol3Dmg2qvpJAYRg==/lib/arm64`

Then, this library will be loaded instead of the library with the same name inside the APK.

To prove this, I made a small app. This is the output when it was installed the first time.

[![](https://tinyhack.com/wp-content/uploads/2024/11/image.png)](https://tinyhack.com/wp-content/uploads/2024/11/image.png)

Pristine install

The JNI Code is very simple:

```
#include <jni.h>
#include <string>
#include <dlfcn.h>

extern "C" JNIEXPORT jstring JNICALL
Java_com_tinyhack_nativelib_NativeLib_stringFromJNI(
        JNIEnv* env,
        jobject /* this */) {
    std::string hello = "Hello from C++";
    return env->NewStringUTF(hello.c_str());
}

extern "C" JNIEXPORT jstring JNICALL
Java_com_tinyhack_nativelib_NativeLib_libLocation(
        JNIEnv* env,
        jobject /* this */) {
    //use dladdr to find the current library location
    Dl_info info;
    if (dladdr((void *)Java_com_tinyhack_nativelib_NativeLib_libLocation, &info)) {
        return env->NewStringUTF(info.dli_fname);
    }
    std::string hello = "Can't find library location";
    return env->NewStringUTF(hello.c_str());
}
```

To add the library:

`adb push libnativelib.so /data/local/tmp`

Then we copy it to the real destination (found using `pm path`):

`adb shell su -c cp /data/local/tmp/libnativelib.so /data/app/~~h8ArfmhA33K6xLYS0-KLSQ==/com.tinyhack.testnative-FKHrlxPDhIqH_YyxoglHzw==/lib/arm64`

And this is the output after I put in the patched native lib. Two things are different: I changed the message from “C++” to “CXX”, and the path is now different (it doesn’t list base.apk in the path).

[![](https://tinyhack.com/wp-content/uploads/2024/11/image-1.png)](https://tinyhack.com/wp-content/uploads/2024/11/image-1.png)

After I put in the patched libnativelib.so

This change will survive accross reboots, since it doesn’t touch the APK.

For anyone reading this in the future, this is valid as of Android 13

[![](https://tinyhack.com/wp-content/uploads/2024/11/image-2-461x1024.png)](https://tinyhack.com/wp-content/uploads/2024/11/image-2.png)

Device used for testing

## Patching files inside the APK

Another thing that we can do is to patch a library directly inside the APK. We can then overwrite the installed APK and the app will run fine, but after a reboot, the app will be uninstalled since the signature is invalid.

Overwriting the library must be done at the same offset. So we can’t just re-zip the files (the offsets will change), use a hex editor, or write a code that will patch the APK at a certain offset.

[![](https://tinyhack.com/wp-content/uploads/2024/11/HxD_m0rKRJuPKu.png)](https://tinyhack.com/wp-content/uploads/2024/11/HxD_m0rKRJuPKu.png)

Editing APK using HxD

Firt we push the APK to a writeable directory:

`adb push .\a.apk /data/local/tmp/`

Then copy it to the target as shown by `pm path com.example.packagename`

`adb shell su -c cp /data/local/tmp/a.apk /data/app/~~xa3ANgaSg-DH4SuFIlqKLg==/com.tinyhack.testnative-FFtQq51Ol3Dmg2qvpJAYRg==/base.apk`

And we can see the output: the path is still inside the base.apk, but the text has changed

[![](https://tinyhack.com/wp-content/uploads/2024/11/image-3.png)](https://tinyhack.com/wp-content/uploads/2024/11/image-3.png)

Path is inside base.apk

We can also patch any files that are not compressed (the c...