---
title: Cocos2d-x iOS游戏逆向分析实战
url: https://mp.weixin.qq.com/s/3UPlvNfctvuaee_et2W0LQ
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:13:12.146432
---

# Cocos2d-x iOS游戏逆向分析实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2IUOianAjUszB0ibPNdzxtm9CAib3iajBXMk7Ljc2e9BqGv65fBNTHpWrNiciaydBkZiaiaZR6z6uJL6oaHAjSrJUOpiaKLzd03lYfvmDM/0?wx_fmt=jpeg)

# Cocos2d-x iOS游戏逆向分析实战

Zedbully
Zedbully

看雪学苑

![]()

在小说阅读器中沉浸阅读

# 在移动游戏开发领域，Cocos2d-x 作为一款成熟的开源游戏引擎，被广泛应用于各类手游开发。然而，随着游戏安全需求的提升，对 Cocos2d-x 游戏的逆向分析也成为了安全研究人员和游戏开发者关注的重点。本文将深入剖析一个实际的 Cocos2d-x iOS 游戏逆向案例，分享完整的技术细节和实战经验。

#

**一、目标分析：好友赛游戏**

#

## 1.1 应用基本信息

* **应用名称：好友赛 (haoyousai)**
* **Bundle ID：**`com.oedere.lid23`
* **版本号：1.0 (Build 59)**
* **目标平台：iOS 15.0+**
* **CPU架构：arm64**
* **游戏类型：棋牌类游戏**

###

### 1.2 技术栈识别

通过静态分析和动态调试，我们识别出以下技术栈：

```
graph TD
A[Cocos2d-x游戏引擎] --> B[JavaScriptCore脚本引擎]
A --> C[OpenGL ES图形渲染]
B --> D[JSC字节码预编译]
B --> E[明文JS脚本]
    F[游戏逻辑] --> G[房间管理]
    F --> H[牌局处理]
    F --> I[用户交互]
```

### 1.3 应用结构分析

```
haoyousai.app/
├── haoyousai              # 主可执行文件 (15.9MB)
├── Frameworks/           # 依赖框架
├── script/              # 游戏脚本目录
├── src/                 # 源代码目录
├── res/                 # 资源文件
├── project.json         # Cocos项目配置
├── project.manifest     # 资源清单
└── main.js             # 入口JS文件
```

##

##

**二、逆向工具开发**

###

**cocos2dx\_frida\_toolkit.js**

### 2.1 工具架构设计

我们开发了一个全面的 Frida 逆向分析工具，整体架构如下：

```
// 工具架构示意图
class Cocos2dxFridaToolkit {
// 1. 基础模块
    - Helper Functions
    - Configuration Manager
    - Logger System

// 2. 检测模块
    - Cocos2dxDetector
    - ScriptEngineDetector

// 3. 分析模块
    - LuaScriptAnalyzer
    - JSScriptAnalyzer
    - CocosGameAnalyzer

// 4. 监控模块
    - InputOutputMonitor
    - PerformanceProfiler

// 5. 控制模块
    - ToolkitController
    - RPC Exports
}
```

### 2.2 关键技术实现

#### 2.2.1 脚本引擎检测

```
class Cocos2dxDetector {
// 检测Lua引擎
detectLuaEngine() {
const exports = ['luaL_loadbuffer', 'lua_pcall', 'lua_getglobal'];
return this.findExportsInMainModule(exports);
    }

// 检测JavaScriptCore
detectJavaScriptCore() {
const exports = ['JSEvaluateScript', 'JSObjectCallAsFunction'];
return this.findExportsInMainModule(exports);
    }

// 检测SpiderMonkey
detectSpiderMonkey() {
const exports = ['JS_EvaluateScript', 'JS_ExecuteScript'];
return this.findExportsInMainModule(exports);
    }

// 检测Cocos JS绑定
detectCocosBindings() {
const patterns = ['jsb_', 'cocos2d::', 'ScriptingCore::'];
return this.searchExportsByPattern(patterns);
    }
}
```

#### 2.2.2 脚本拦截与解密

**Lua脚本拦截**：

```
class LuaScriptAnalyzer {
    hookLuaFunctions() {
// Hook luaL_loadbuffer 拦截Lua脚本加载
        Interceptor.attach(Module.findExportByName(null, 'luaL_loadbuffer'), {
            onEnter: function(args) {
const buffer = args[1];  // 脚本缓冲区
const size = args[2];    // 脚本大小
const chunkname = args[3]; // 脚本名称

// 提取并保存脚本
this.scriptData = Memory.readByteArray(buffer, size);
this.scriptName = Memory.readUtf8String(chunkname);
            },
            onLeave: function(retval) {
if (this.scriptData) {
this.saveLuaScript(this.scriptName, this.scriptData);
                }
            }
        });
    }
}
```

**JavaScript脚本拦截**：

```
class JSScriptAnalyzer {
    hookJavaScriptCore() {
// Hook JSEvaluateScript 拦截JS执行
        Interceptor.attach(Module.findExportByName('JavaScriptCore', 'JSEvaluateScript'), {
            onEnter: function(args) {
const script = args[1];  // JS脚本字符串
const sourceURL = args[3]; // 源URL

// 读取脚本内容
const scriptStr = this.readJSString(script);
const urlStr = this.readJSString(sourceURL);

// 分析脚本内容
this.analyzeJSScript(scriptStr, urlStr);
            }
        });
    }

// 读取JS字符串的辅助函数
    readJSString(jsStringRef) {
const size = this.JSStringGetMaximumUTF8CStringSize(jsStringRef);
const buffer = Memory.alloc(size);
this.JSStringGetUTF8CString(jsStringRef, buffer, size);
return buffer.readUtf8String();
    }
}
```

### 2.3 性能优化与稳定性修复

在开发过程中，我们遇到了多个技术挑战并进行了优化：

#### 2.3.1 超时崩溃问题修复

**问题**：原始实现中遍历所有模块导出和ObjC类，导致Frida超时。

**解决方案**：

```
// 优化前：遍历所有模块
Process.enumerateModules().forEach(module => {
module.enumerateExports().forEach(export => {
// 处理每个导出
    });
});

// 优化后：只扫描主模块
const mainModule = Process.enumerateModules()[0];
mainModule.enumerateExports().forEach(export => {
// 只处理主模块导出
});

// 限制ObjC类遍历数量
const maxHooksPerCategory = CONFIG.maxHooksPerCategory || 50;
let hookCount = 0;
for (let className in ObjC.classes) {
if (hookCount >= maxHooksPerCategory) break;
// 处理ObjC类
    hookCount++;
}
```

#### 2.3.2 Hook稳定性修复

**问题**：尝试Hook数据符号地址导致崩溃。

**解决方案**：

```
function isExecutableAddress(address) {
const range = Process.findRangeByAddress(address);
return range && range.protection.includes('x');
}

function safeAttach(address, callbacks) {
if (!isExecutableAddress(address)) {
        logger.warn(`地址 ${address} 不可执行，跳过Hook`);
return null;
    }
return Interceptor.attach(address, callbacks);
}
```

#### 2.3.3 ObjC桥接修复

**问题**：直接传递JS字符串给ObjC方法导致类型不匹配。

**解决方案**：

```
function nsStr(jsString) {
// 使用NSString包装JS字符串
return ObjC.classes.NSString.stringWithUTF8String_(jsString);
}

function createDir(path) {
const fileManager = ObjC.classes.NSFileManager.defaultManager();
const nsPath = nsStr(path);
const errorPtr = Memory.alloc(Process.pointerSize);

// 正确传递参数
return fileManager.createDirectoryAtPath_withIntermediateDirectories_attributes_error_(
        nsPath,
1,  // YES
NULL,
        errorPtr
    );
}
```

##

**三、原生Tweak开发：CardRecorder**

###

### 3.1 设计思路

为了提供更稳定的游戏数据监控，我们开发了原生iOS Tweak，将关键功能从Frida脚本迁移到原生代码中。

### 3.2 核心实现

```
// CardRecorder.mm 核心代码分析

// 1. JavaScriptCore C-API Hook
__attribute__((constructor))
staticvoidCardRecorderInit(void) {
// 加载JavaScriptCore框架
void *jscHandle = dlopen("/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore", RTLD_NOW);

// 获取JSEvaluateScript函数指针
    JSEvaluateScript_t orig_JSEvaluateScript =
        (JSEvaluateScript_t)dlsym(jscHandle, "JSEvaluateScript");

// 使用MSHookFunction进行Hook
MSHookFunction(
        (void *)orig_JSEvaluateScript,
        (void *)hook_JSEvaluateScript,
        (void **)&orig_JSEvaluateScript
    );
}

// 2. Hook函数实现
static JSValueRef hook_JSEvaluateScript(
    JSContextRef ctx,
    JSStringRef script,
    JSObjectRef thisObject,
    JSStringRef sourceURL,
int startingLineNumber,
    JSValueRef *exception){
// 捕获JSContext
if (ctx && !g_jsCtx) {
        g_jsCtx = ctx;
NSLog(@"[CardRecorder] 捕获JSContext: %p", ctx);
    }

// 检测游戏脚本
if (!g_injected && script) {
size_t maxSize = JSStringGetMaximumUTF8CStringSize(script);
if (maxSize > 5000) {  // 只处理大型脚本
char *buffer = (char *)malloc(maxSize);
JSStringGetUTF8CString(script, buffer, maxSize);

// 检测关键词"setRoomData"
if (strstr(buffer, "setRoomData") != NULL) {
NSLog(@"[CardRecorder] 检测到游戏脚本，准备注入监控代码");
injectCardMonitor(ctx);
            }
free(buffer);
        }
    }

// 调用原始函数
return orig_JSEvaluateScript(ctx, script, thisObject, sourceURL, startingLineNumber, exception);
}

// 3. 监控代码注入
staticvoidinjectCardMonitor(JSContextRef ctx) {
constchar *monitorJS =
"(function(){"
"  if(window.__cardHookInstalled) return;"
"  window.__cardHookInstalled = true;"
"  setInterval(function(){"
"    try {"
"      if(!iGame || !iGame.Data || !iGame.Data.roomData) return;"
"      var selfSeat = iGame.Data.getSelfSeatNo ? iGame.Data.getSelfSeatNo() : 0;"
"      var players = iGame.Data.roomData.players;"
"      var result = {self_seat: selfSeat, my_hold: [], players: []};"
"      players.forEach(function(p){"
"        if(p.seat_no === selfSeat){"
"          result.my_hold = (p.hold || []).filter(c => c > 0);"
"        }"
"        result.players.push({"
"          seat: p.seat_no,"
"          out: p.out || [],"
"          kou: p.kou || []"
"        });"
"      });"
"      window.__cardData = JSON.stringify(result);"
"    } catch(e){}"
"  }, 1000);"
"})();";

// 在游戏JSContext中执行监控代码
    JSStringRef jsStr = JSStringCreateWithUTF8CString(monitorJS);
    JSValueRef exception = NULL;
JSEvaluateScript(ctx, jsStr, NULL, NULL, 0, &exception);
JSStringRelease(jsStr);
}
```

### 3.3 数据采集与存储

```
// 定时数据采集
static void startCardPolling(void) {
    dispatch_source_t timer = dispatch_source_create(
        DISPATCH_S...