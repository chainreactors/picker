---
title: ART脱壳源码修改点
url: https://misakikata.github.io/2022/10/ART%E8%84%B1%E5%A3%B3%E6%BA%90%E7%A0%81%E4%BF%AE%E6%94%B9%E7%82%B9/
source: Misaki's Blog
date: 2022-10-22
fetch_date: 2025-10-03T20:33:36.376461
---

# ART脱壳源码修改点

[Misaki's Blog](/)

Toggle navigation

* [archives](/archives/)
* [about](/about/)

# ART脱壳源码修改点

**Friday, October 21st 2022, 2:46 pm**

在将 dex 文件编译为 oat 文件的过程中 , 只要出现了 DexFile 对象 , 就可以将该对象对应的 dex 文件导出

## 已知的脱壳点

**/art/runtime/dex\_file.cc#OpenMemory**
OpenMemory算是常见的脱壳点，在# frida-unpack中也是使用此脱壳点来导出dex对象。

```
std::unique_ptr<const DexFile> DexFile::OpenMemory(const uint8_t* base,
size_t size,
const std::string& location,
uint32_t location_checksum,
MemMap* mem_map,
const OatDexFile* oat_dex_file,
std::string* error_msg) {
CHECK_ALIGNED(base, 4);  // various dex file structures must be word aligned
std::unique_ptr<DexFile> dex_file(
     new DexFile(base, size, location, location_checksum, mem_map, oat_dex_file));
if (!dex_file->Init(error_msg)) {
    dex_file.reset();
  }
  return std::unique_ptr<const DexFile>(dex_file.release());
}
```

添加导出代码

```
#include <sys/types.h>  //添加额外的库
#include <sys/stat.h>
#include <fcntl.h>

int dexCount = 0;  //注意位置

  char output[100]={0};
  int pid = getpid();
  sprintf(output, "/sdcard/%d_%d_output.dex", pid, dexCount);
  dexCount++;
  int fd = open(output,O_CREAT|O_RDWR,666);
  if (fd > 0)
  {
  	write(fd, base, size);
  	close(fd);
  }
```

**DexFile::DexFile()**

在17年的DEF CON 25 黑客大会中，Avi Bashan 和 SlavaMakkaveev 提出的通过修改DexFile的构造函数DexFile::DexFile()，以及OpenAndReadMagic()函数来实现对加壳应用的内存中的dex的dump来脱壳技术

```
DexFile::DexFile(const uint8_t* base, size_t size,
                 const std::string& location,
                 uint32_t location_checksum,
                 MemMap* mem_map,
                 const OatDexFile* oat_dex_file)
    : begin_(base),
      size_(size),
      location_(location),
      location_checksum_(location_checksum),
      mem_map_(mem_map),
      header_(reinterpret_cast<const Header*>(base)),
      string_ids_(reinterpret_cast<const StringId*>(base + header_->string_ids_off_)),
      type_ids_(reinterpret_cast<const TypeId*>(base + header_->type_ids_off_)),
      field_ids_(reinterpret_cast<const FieldId*>(base + header_->field_ids_off_)),
      method_ids_(reinterpret_cast<const MethodId*>(base + header_->method_ids_off_)),
      proto_ids_(reinterpret_cast<const ProtoId*>(base + header_->proto_ids_off_)),
      class_defs_(reinterpret_cast<const ClassDef*>(base + header_->class_defs_off_)),
      find_class_def_misses_(0),
      class_def_index_(nullptr),
      oat_dex_file_(oat_dex_file) {
  CHECK(begin_ != nullptr) << GetLocation();
  CHECK_GT(size_, 0U) << GetLocation();
}
```

添加代码

```
+   //------------------------------------------------------------------
+   // DEX file unpacking
+   //------------------------------------------------------------------
+
+   // let's limit processing file list
+

LOG(WARNING) << "Dex File: Filename: "<< location;
if (location.find("/data/data/") != std::string::npos) {
    LOG(WARNING) << "Dex File: OAT file unpacking launched";
    std::ofstream dst(location + "__unpacked_oat", std::ios::binary);
    dst.write(reinterpret_cast<const char*>(base), size);
    dst.close();
} else {
    LOG(WARNING) << "Dex File: OAT file unpacking not launched";
}

+   //------------------------------------------------------------------
```

**OpenFile**
这个函数跟OpenMemory类似，同样是调用了OpenMemory的返回，也可以在这里直接导出dexfile.

```
std::unique_ptr<const DexFile> dex_file(OpenMemory(location, dex_header->checksum_, map.release(), error_msg));
  if (dex_file.get() == nullptr) {
    *error_msg = StringPrintf("Failed to open dex file '%s' from memory: %s", location, error_msg->c_str());
    return nullptr;
  }
```

**Execute**
这个函数是寒冰大佬公布的，dex2oat对类的初始化函数并没有进行编译，进入到interpreter.cc文件中的Execute函数，进而进入ART下的解释器解释执行。

```
#include <fcntl.h>
 static inline JValue Execute(Thread* self, const DexFile::CodeItem* code_item,
                            ShadowFrame& shadow_frame, JValue result_register) {
 char *dexfilepath=(char*)malloc(sizeof(char)*1000);
    if(dexfilepath!=nullptr)
    {
    ArtMethod* artmethod=shadow_frame.GetMethod();
    const DexFile* dex_file = artmethod->GetDexFile();
    const uint8_t* begin_=dex_file->Begin();  // Start of data.
    size_t size_=dex_file->Size();  // Length of data.
    int size_int_=(int)size_;
    int fcmdline =-1;
    char szCmdline[64]= {0};
    char szProcName[256] = {0};
    int procid = getpid();
    sprintf(szCmdline,"/proc/%d/cmdline", procid);
    fcmdline = open(szCmdline, O_RDONLY,0644);
    if(fcmdline >0)
    {
        read(fcmdline, szProcName,256);
        close(fcmdline);
    }

    if(szProcName[0])
    {
            memset(dexfilepath,0,1000);
            sprintf(dexfilepath,"/sdcard/%s_%d_dexfile.dex",szProcName,size_int_);
            int dexfilefp=open(dexfilepath,O_RDONLY,0666);
            if(dexfilefp>0){
                                close(dexfilefp);
                                dexfilefp=0;

                            }else{
                                        int fp=open(dexfilepath,O_CREAT|O_RDWR,666);
                                        if(fp>0)
                                        {
                                            write(fp,(void*)begin_,size_);
                                            fsync(fp);
                                            close(fp);
                                            }

                                }
    }

    if(dexfilepath!=nullptr)
    {
        free(dexfilepath);
        dexfilepath=nullptr;
    }
   }
//=======================
```

## 其他脱壳点

看了寒冰大佬的文章，按照寻找脱壳点的办法找到几个新的脱壳点，这里也来记录一下，利用的是dexcache来到出dexfile。曾经有过类似的调用，也有不少利用dexcache来查找和导出的办法，比如在Java层hook函数getDex。

**DexCache\_getDexNative**

```
namespace art {
static jobject DexCache_getDexNative(JNIEnv* env, jobject javaDexCache) {
  ScopedFastNativeObjectAccess soa(env);
  mirror::DexCache* dex_cache = soa.Decode<mirror::DexCache*>(javaDexCache);
  // Should only be called while holding the lock on the dex cache.
  DCHECK_EQ(dex_cache->GetLockOwnerThreadId(), soa.Self()->GetThreadId());
  const DexFile* dex_file = dex_cache->GetDexFile();
  // =======================新增
int fcmdline = -1;
char szCmdline[64] = { 0 };
char szProcName[256] = { 0 };
int procid = getpid();
sprintf(szCmdline, "/proc/%d/cmdline", procid);
fcmdline = open(szCmdline, O_RDONLY, 0644);
if (fcmdline > 0) {
    read(fcmdline, szProcName, 256);
    close(fcmdline);
}
char *dexfilepath = (char *) malloc(sizeof(char) * 2000);
const uint8_t *begin_ = dex_file->Begin();   //dex的起始和大小
size_t size_ = dex_file->Size();

memset(dexfilepath, 0, 2000);
int size_int_ = (int) size_;

memset(dexfilepath, 0, 2000);
sprintf(dexfilepath, "%s", "/sdcard/fiart");
mkdir(dexfilepath, 0777);

memset(dexfilepath, 0, 2000);
sprintf(dexfilepath, "/sdcard/fiart/%s",szProcName);  //创建保存的文件
mkdir(dexfilepath, 0777);

memset(dexfilepath, 0, 2000);
sprintf(dexfilepath,"/sdcard/fiart/%s/%d_dexfile.dex",szProcName, size_int_);
int dexfilefp = open(dexfilepath, O_RDONLY, 0666);
if (dexfilefp > 0) {
    close(dexfilefp);
    dexfilefp = 0;
} else {
    dexfilefp = open(dexfilepath, O_CREAT | O_RDWR,0666);
    if (dexfilefp > 0) {
        write(dexfilefp, (void *) begin_,size_);
        fsync(dexfilefp);
        close(dexfilefp);
	}
}
// ================================
  if (dex_file == nullptr) {
    return nullptr;
  }
```

**GetNameAsString**
按照如下新增代码，需要新增库。

```
mirror::String* ArtMethod::GetNameAsString(Thread* self) {
  CHECK(!IsProxyMethod());
  StackHandleScope<1> hs(self);
  Handle<mirror::DexCache> dex_cache(hs.NewHandle(GetDexCache()));
  auto* dex_file = dex_cache->GetDexFile();
  // ================================
    char *dexfilepath=(char*)malloc(sizeof(char)*1000);
    const uint8_t* begin_=dex_file->Begin();  // Start of data.
    size_t size_=dex_file->Size();  // Length of data.
    int size_int_=(int)size_;
    int fcmdline =-1;
    char szCmdline[64]= {0};
    char szProcName[256] = {0};
    int procid = getpid();
    sprintf(szCmdline,"/proc/%d/cmdline", procid);
    fcmdline = open(szCmdline, O_RDONLY,0644);
    if(fcmdline >0)
    {
        read(fc...