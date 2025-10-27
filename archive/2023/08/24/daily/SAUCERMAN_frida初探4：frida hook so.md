---
title: frida初探4：frida hook so
url: https://saucer-man.com/information_security/1122.html
source: SAUCERMAN
date: 2023-08-24
fetch_date: 2025-10-04T12:00:41.328315
---

# frida初探4：frida hook so

* [Home](https://saucer-man.com/)
* [Archives](https://saucer-man.com/archives.html)
* [About](https://saucer-man.com/about.html)
* [Github](https://github.com/saucer-man)

Previous post
Next post
Back to top
Share post

* [1. 枚举module](#cl-1)
* [2. 枚举符号](#cl-2)
* [3. hook so](#cl-3)* [3.1 hook导出函数&symbols函数](#cl-4)
  * [3.2 hook 任意函数](#cl-5)
  * [3.3 获取指针参数返回值](#cl-6)
  * [3.4 inlineHook](#cl-7)
  * [3.5 修改函数参数和返回值](#cl-8)
  * [3.6 hook jni函数](#cl-9)
* [4. 打印堆栈](#cl-10)
* [5. 主动调用so函数](#cl-11)
* [6. 定位JNI函数](#cl-12)
* [7. JNItrace工具的使用](#cl-13)

# frida初探4：frida hook so

2023-08-24

6917

[信息安全](https://saucer-man.com/category/information_security/)

[frida](https://saucer-man.com/tag/frida/)

> 文章最后更新时间为：2023年08月24日 00:37:55

本篇文章主要记录frida hook so的常见用法，内容多参考自《frida 协议分析》

# 1. 枚举module

```
// 列举所有加载的module，也就是so
function listso() {
  Java.perform(function () {
    //枚举当前加载的模块
    var process_Obj_Module_Arr = Process.enumerateModules();
    for (var i = 0; i < process_Obj_Module_Arr.length; i++) {
      //包含"lib"字符串的
      if (process_Obj_Module_Arr[i].path.indexOf("lib") != -1) {
        console.log("模块名称:", process_Obj_Module_Arr[i].name);
        console.log("模块地址:", process_Obj_Module_Arr[i].base);
        console.log("大小:", process_Obj_Module_Arr[i].size);
        console.log("文件系统路径", process_Obj_Module_Arr[i].path);
      }
    }
  });
}

// 根据模块名加载module
var module = Process.findModuleByName("libxiaojianbang.so");
console.log(JSON.stringify(module));
//{"name":"libxiaojianbang.so","base":"0x7ad1ce6000","size":28672,"path":"/data/app/com.xiaojianbang.app-r_cD2g_EAJo-3V4FJEttXQ==/lib/arm64/libxiaojianbang.so"}
if(module != null){
    //do someting ...
}

// module的定义
declare class Module {
    name: string;            //模块名
    base: NativePointer;    //模块基址
    size: number;            //模块大小
    path: string;            //模块所在路径
    enumerateImports(): ModuleImportDetails[];    //枚举导入表
    enumerateExports(): ModuleExportDetails[];    //枚举导出表
    enumerateSymbols(): ModuleSymbolDetails[];    //枚举符号表
    findExportByName(exportName: string): NativePointer | null;    //获取导出函数地址
    getExportByName(exportName: string): NativePointer;        //获取导出函数地址
    static load(name: string): Module;                            //加载指定模块
    static findBaseAddress(name: string): NativePointer | null;        //获取模块基址
    static getBaseAddress(name: string): NativePointer;            //获取模块基址
    //获取导出函数地址
static findExportByName(moduleName: string | null, exportName: string): NativePointer | null;
//获取导出函数地址
    static getExportByName(moduleName: string | null, exportName: string): NativePointer;
}
```

# 2. 枚举符号

```
// 列举某个module的导入导出函数
function listsoinout(name) {
  Java.perform(function () {
    var imports = Module.enumerateImportsSync(name);

    var exports = Module.enumerateExportsSync(name);

    for (var i = 0; i < imports.length; i++) {
      console.log(imports[i].name + ": " + imports[i].address);
    }
    var exports = Module.enumerateExportsSync("libhello.so");
    console.log(JSON.stringify(exports[0]));
        //{"type":"function","name":"JNI_OnLoad","address":"0xc68995f1"}

    for (var i = 0; i < exports.length; i++) {
      console.log(exports[i].name + ": " + exports[i].address);
    }
  })
}

// 列举某个module的Symbol函数
function frida_Module() {
    Java.perform(function () {
        const hooks = Module.load('libc.so');
        var Symbol = hooks.enumerateSymbols();
        for(var i = 0; i < Symbol.length; i++) {
            console.log("isGlobal:",Symbol[i].isGlobal);
            console.log("type:",Symbol[i].type);
            console.log("section:",JSON.stringify(Symbol[i].section));
            console.log("name:",Symbol[i].name);
            console.log("address:",Symbol[i].address);
         }
    });
}

// 定位so中的函数
function findFuncInWitchSo(funcName) {
    var modules = Process.enumerateModules();
    for (let i = 0; i < modules.length; i++) {
        let module = modules[i];
        let _symbols = module.enumerateSymbols();
        for (let j = 0; j < _symbols.length; j++) {
            let _symbol = _symbols[i];
            if(_symbol.name == funcName){
                return module.name + " " + JSON.stringify(_symbol);
            }
        }
        let _exports = module.enumerateExports();
        for (let j = 0; j < _exports.length; j++) {
            let _export = _exports[j];
            if(_export.name == funcName){
                return module.name + " " + JSON.stringify(_export);
            }
        }
    }
    return null;
}
console.log(findFuncInWitchSo('strcat'));
//libc.so {"type":"function","name":"strcat","address":"0x7bc0e0322c"}
```

# 3. hook so

## 3.1 hook导出函数&symbols函数

```
function hook_native() {
  console.log("[*] Starting Hook Script.");
  var so_base_address = Module.findBaseAddress("libcyberpeace.so")
  console.log("so_base_address is: " + so_base_address)

  if (so_base_address) {
    var string_with_jni_addr = Module.findExportByName("libcyberpeace.so",
      "Java_com_testjava_jack_pingan2_cyberpeace_CheckString")
    console.log("string_with_jni_addr is: " + string_with_jni_addr)
    Interceptor.attach(string_with_jni_addr, {
      onEnter: function (args) {
        console.log("string_with_jni args: " + args[0], args[1], args[2])
        console.log(Java.vm.getEnv().getStringUtfChars(args[2], null).readCString())
      },
      onLeave: function (retval) {
        console.log("[*] 原始的So层函数返回值是:", retval)
        console.log(Java.vm.getEnv().getStringUtfChars(retval, null).readCString())
        var newRetval = Java.vm.getEnv().newStringUtf("new retval from hook_native");
        retval.replace(ptr(newRetval));
      }
    })
  } else {
    console.log("find so base address fail", so_base_address)
  }
}
```

onEnter是在原函数之前执行，然后执行原函数，最后执行onLeave函数中的代码。

onEnter接收的args，数组的前两个值是JNIENV和jclass/jobject，如果是静态方法则对应jclass，如果是实例方法则对应jobject，对于这类内存地址，可以通过console.log(hexdump(args[0])来打印内存，

或者也可以通过symbols符号来定位native方法地址：

```
function find_func_from_symbols() {
  var NewStringUTF_addr = null;
  var symbols = Process.findModuleByName("libart.so").enumerateSymbols();
  for (var i in symbols) {
      var symbol = symbols[i];
      if (symbol.name.indexOf("art") >= 0 &&
          symbol.name.indexOf("JNI") >= 0 &&
          symbol.name.indexOf("CheckJNI") < 0
      ){
          if (symbol.name.indexOf("NewStringUTF") >= 0) {
              console.log("find target symbols", symbol.name, "address is ", symbol.address);
              NewStringUTF_addr = symbol.address;
          }
      }
  }

  console.log("NewStringUTF_addr is ", NewStringUTF_addr);

  Interceptor.attach(NewStringUTF_addr, {
      onEnter: function (args) {
          console.log("args0",args[0])

      },
      onLeave: function (returnResult) {
          console.log("result: ", Java.cast(returnResult, Java.use("java.lang.String")));

      }
  })
}
```

## 3.2 hook 任意函数

在so文件中，只需要得到函数的内存地址，就可以完成任意函数的hook，函数的地址=so文件基址+函数相对于so的偏移地址

* 获取so文件基地址，可以通过findBaseAddress或者getBaseAddress来获取。

```
declare class Module {
......
    static findBaseAddress(name: string): NativePointer | null;
static getBaseAddress(name: string): NativePointer;
}
```

* 获取函数相对于so的偏移地址，可以在IDA的汇编界面上查看，这里的**偏移地址是函数定义部分的首地址，也就是.text段，不是在plt表的地址**

**需要注意的是，在32位so文件中的函数，需要在计算出的函数地址上+1，如果是64位则不需要**

下面是

```
function hook_native1() {
  console.log("[*] Starting Hook Script.");
  var so_base_address = Module.findBaseAddress("libcyberpeace.so")
  console.log("so_base_address is: " + so_base_address) // 32位需要加1，这里是64位

  if (so_base_address) {
    //要hook的函数在函数里面的偏移
    var n_addr_func_offset = 0x840;

    //加载到内存后 函数地址 = so地址 + 函数偏移
    var n_addr_func = so_base_address.add(n_addr_func_offset)

    var ptr_func = new NativePointer(n_addr_func);
    Interceptor.attach(ptr_func, {
      onEnter: function (args) {
        console.log("string_with_jni args: " + args[0], args[1], args[2])
        console.log(Java.vm.getEnv().getStringUtfChars(args[2], null).readCString())
      },
 ...