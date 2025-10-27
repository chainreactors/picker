---
title: Android 反序列化漏洞攻防史话
url: https://mp.weixin.qq.com/s?__biz=MzA3MzU1MDQwOA==&mid=2247484330&idx=1&sn=b725d8802e71d215baaf57bd8159648b&chksm=9f0c1c8da87b959bb6f98ddab396a6c9f5009a41efdb41d018d28aa7ab74a30508ce74f7394e&scene=58&subscene=0#rd
source: 有价值炮灰
date: 2023-02-19
fetch_date: 2025-10-04T07:30:21.363709
---

# Android 反序列化漏洞攻防史话

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3eicVGzibzClD8k0ayvYDcI54tlXOnd6sT8kZmEwfPtab3ia1tsGkia89mF7tz3TwbbSbxknYSPNqSkjuvuyeT270Q/0?wx_fmt=jpeg)

# Android 反序列化漏洞攻防史话

原创

evilpan

有价值炮灰

序列化和反序列化是指将内存数据结构转换为字节流，通过网络传输或者保存到磁盘，然后再将字节流恢复为内存对象的过程。在 Web 安全领域，出现过很多反序列化漏洞，比如 PHP 反序列化、Java 反序列化等。由于在反序列化的过程中触发了非预期的程序逻辑，从而被攻击者用精心构造的字节流触发并利用漏洞从而最终实现任意代码执行等目的。

Android 中除了传统的 Java 序列化机制，还有一个特殊的序列化方法，即 Parcel[1]。根据官方文档的介绍，Parcelable 和 Bundle 对象主要的作用是用于跨进程边界的数据传输(IPC/Binder)，但 Parcel 并不是一个通用的序列化方法，因此不建议开发者将 Parcel 数据保存到磁盘或者通过网络传输。

作为 IPC 传输的数据结构，Parcel 的设计初衷是轻量和高效，因此缺乏完善的安全校验。这就引发了历史上出现过多次的 Android 反序列化漏洞，本文就按照时间线对其进行简单的分析和梳理。

> 注: 本文中所展现的 AOSP 示例代码，如无特殊说明则都来自文章发表时的 master 分支。

# Parcel 101

在介绍漏洞之前，我们还是按照惯例先来了解下基础知识。对于有过 Android 开发或者逆向分析经验的同学应该对 Parcel 都不陌生，但通常也很少直接使用该类去序列化/反序列化数据然后进行 IPC 通信，而是通过 AIDL 等方法去自动生成模版，然后集成实现对应接口。

## AIDL

关于 AIDL 开发的示例可以参考 Android 进程间通信与逆向分析[2] 一文，简单来说，假设有以下 AIDL 文件:

```
package com.evilpan;

interface IFooService {
    parcelable Person {
        String name;
        int age;
        boolean gender;
    }
    String foo(int a, String b, in Person c);
}
```

那么生成的(Java)模版大致结构如下:

```
public interface IFooService extends android.os.IInterface {

    public java.lang.String foo(int a, java.lang.String b, com.evilpan.IFooService.Person c) throws android.os.RemoteException;
    public static class Person implements android.os.Parcelable { /* ... */ }

    public static abstract class Stub extends android.os.Binder implements com.evilpan.IFooService {
        @Override public boolean onTransact(int code, android.os.Parcel data, android.os.Parcel reply, int flags) throws android.os.RemoteException {
            data.enforceInterface(descriptor);
            // ...
            switch(code) {
                case TRANSACTION_foo {
                    int _arg0;
                    _arg0 = data.readInt();
                    java.lang.String _arg1;
                    _arg1 = data.readString();
                    com.evilpan.IFooService.Person _arg2;
                    _arg2 = _Parcel.readTypedObject(data, com.evilpan.IFooService.Person.CREATOR);
                    java.lang.String _result = this.foo(_arg0, _arg1, _arg2);
                    reply.writeNoException();
                    reply.writeString(_result);
                    break;
                }
            }
        }
    }

    private static class Proxy implements com.evilpan.IFooService {
        @Override public java.lang.String foo(int a, java.lang.String b, com.evilpan.IFooService.Person c) throws android.os.RemoteException
        {
            android.os.Parcel _data = android.os.Parcel.obtain();
            android.os.Parcel _reply = android.os.Parcel.obtain();
            java.lang.String _result;
            try {
            _data.writeInterfaceToken(DESCRIPTOR);
            _data.writeInt(a);
            _data.writeString(b);
            _Parcel.writeTypedObject(_data, c, 0);
            boolean _status = mRemote.transact(Stub.TRANSACTION_foo, _data, _reply, 0);
            _reply.readException();
            _result = _reply.readString();
            }
            finally {
            _reply.recycle();
            _data.recycle();
            }
            return _result;
        }
    }
    // ...
}
```

其中 `IFooService.Stub` 类是本地的 IPC 实现，即服务端代码通过继承至该类并实现其 `foo` 方法；而 `Proxy` 则是客户端的的辅助类，客户端可以通过调用 `Proxy.foo` 方法间接地调用服务端的对应代码。数据传输的过程通过 `transact` 方法实现，其底层是 Android 的 Binder IPC；而数据的封装过程则通过 Parcel 实现。

可以看到上面模版代码中客户端分别调用了 `writeInterfaceToken`、`writeInt`、`writeString` 和 `writeTypedObject` 来填充传输的 `_data`，而 Stub 类的 onTransact 中以同样的顺序分别调用了 `enforceInterface`、`readInt`、`readString`、`readTypedObject` 来获取 `_data` 中的数据。

## Parcelable

在上面的 AIDL 中，我们还定义了一个数据结构 Person，该结构同样会由 AIDL 生成对应的模版类:

```
public static class Person implements android.os.Parcelable
{
  public java.lang.String name;
  public int age = 0;
  public boolean gender = false;
  public static final android.os.Parcelable.Creator<Person> CREATOR = new android.os.Parcelable.Creator<Person>() {
    @Override
    public Person createFromParcel(android.os.Parcel _aidl_source) {
      Person _aidl_out = new Person();
      _aidl_out.readFromParcel(_aidl_source);
      return _aidl_out;
    }
    @Override
    public Person[] newArray(int _aidl_size) {
      return new Person[_aidl_size];
    }
  };
  @Override public final void writeToParcel(android.os.Parcel _aidl_parcel, int _aidl_flag)
  {
    int _aidl_start_pos = _aidl_parcel.dataPosition();
    _aidl_parcel.writeInt(0);
    _aidl_parcel.writeString(name);
    _aidl_parcel.writeInt(age);
    _aidl_parcel.writeInt(((gender)?(1):(0)));
    int _aidl_end_pos = _aidl_parcel.dataPosition();
    _aidl_parcel.setDataPosition(_aidl_start_pos);
    _aidl_parcel.writeInt(_aidl_end_pos - _aidl_start_pos);
    _aidl_parcel.setDataPosition(_aidl_end_pos);
  }
  public final void readFromParcel(android.os.Parcel _aidl_parcel)
  {
    int _aidl_start_pos = _aidl_parcel.dataPosition();
    int _aidl_parcelable_size = _aidl_parcel.readInt();
    try {
      if (_aidl_parcelable_size < 4) throw new android.os.BadParcelableException("Parcelable too small");;
      if (_aidl_parcel.dataPosition() - _aidl_start_pos >= _aidl_parcelable_size) return;
      name = _aidl_parcel.readString();
      if (_aidl_parcel.dataPosition() - _aidl_start_pos >= _aidl_parcelable_size) return;
      age = _aidl_parcel.readInt();
      if (_aidl_parcel.dataPosition() - _aidl_start_pos >= _aidl_parcelable_size) return;
      gender = (0!=_aidl_parcel.readInt());
    } finally {
      if (_aidl_start_pos > (Integer.MAX_VALUE - _aidl_parcelable_size)) {
        throw new android.os.BadParcelableException("Overflow in the size of parcelable");
      }
      _aidl_parcel.setDataPosition(_aidl_start_pos + _aidl_parcelable_size);
    }
  }
  @Override
  public int describeContents() {
    int _mask = 0;
    return _mask;
  }
}
```

其中关键的是 writeToParcel 和 `CREATOR.createFromParcel` 方法，分别填充了该自定义结构序列化和反序列化的实现，当然我们也可以自己继承 `Parcelable` 去实现自己的可序列化数据结构。

## 内存布局

从接口上看，Parcel 可以支持按照一定顺序写入和读取 int、long 等原子数据，也支持 String、IBinder、和 FileDescriptor 这些复杂的数据结构。为了理解后文介绍的漏洞，还需要了解在二进制层面这些数据的存储方式。

Parcel 的代码接口实现在 android/os/Parcel.java 中，但大部分方法最终都会调用到其中的 native 方法，其 JNI 定义在 frameworks/base/core/jni/android\_os\_Parcel.cpp 文件里，最终的实现则是在 frameworks/native/libs/binder/Parcel.cpp 中。

以 `Parcel.writeInt` 为例，其 Java 实现很简单，直接转到 native 方法:

```
private static native int nativeWriteInt(long nativePtr, int val);
public final void writeInt(int val) {
    int err = nativeWriteInt(mNativePtr, val);
    if (err != OK) {
        nativeSignalExceptionForError(err);
    }
}
```

C++ 中的 JNI 实现则是先将 nativePtr 转换为 Parcel 指针，而后直接调用 `writeInt32` 方法:

```
static int android_os_Parcel_writeInt(jlong nativePtr, jint val) {
    Parcel* parcel = reinterpret_cast<Parcel*>(nativePtr);
    return (parcel != NULL) ? parcel->writeInt32(val) : OK;
}
```

接下来就是最终实际的实现了:

```
status_t Parcel::writeInt32(int32_t val)
{
    return writeAligned(val);
}

template<class T>
status_t Parcel::writeAligned(T val) {
    static_assert(PAD_SIZE_UNSAFE(sizeof(T)) == sizeof(T));
    static_assert(std::is_trivially_copyable_v<T>);

    if ((mDataPos+sizeof(val)) <= mDataCapacity) {
restart_write:
        memcpy(mData + mDataPos, &val, sizeof(val));
        return finishWrite(sizeof(val));
    }

    status_t err = growData(sizeof(val));
    if (err == NO_ERROR) goto restart_write;
    return err;
}
```

`writeAligned` 是个模版函数，用于写入基础的 C++ 数据类型，即 int、float、double 等，也可以写入指针数据。实现也相对简单，这里面就涉及到了 Parcel 内部的几个重要数据结构:

* • mData: 序列化数据内存缓冲区的内存起始地址(指针)；
* • mDataPos: 序列化数据当前解析到的相对位置；
* • mDataCapacity: 缓冲区的总大小；

还有一个字段 mDataSize 表示当前序列化数据的大小，其实这个字段基本上和 mDataPos 的值是一致的，二者都在 finishWrite 函数中进行更新:

```
status_t Parcel::finishWrite(size_t len)
{
    if (len > INT32_MAX) {
        // don't accept size_t values which may have come from an
        // inadvertent conversion from a negative int.
        return BAD_VALUE;
    }

    //printf("Finish write of %d\n", len);
    mDataPo...