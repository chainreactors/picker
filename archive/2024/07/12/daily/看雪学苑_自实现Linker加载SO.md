---
title: 自实现Linker加载SO
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458563327&idx=1&sn=670709ec9ab327f3300d971f3b3f32ac&chksm=b18d827586fa0b63eb7802faea03fead3260d94526ef37bf91626f6cf77ee9389532a43d21eb&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-12
fetch_date: 2025-10-06T17:43:53.948885
---

# 自实现Linker加载SO

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HzZkN1cxicXAOOicPnzNtAEPcF9QiaStstrsXzLBaHCicI5cu0vxibiaichfEAWTzjdG9C62gbQBb98D6fw/0?wx_fmt=jpeg)

# 自实现Linker加载SO

ngiokweng

看雪学苑

```
一

前言
```

前一陣子在研究so加固，發現其中涉及自實現的Linker加載so的技術，而我對此知之什少，因此只好先來學習下Linker的加載流程。

本文參考AOSP源碼和r0ysue大佬的文章(https://bbs.kanxue.com/thread-269484.htm，不知為何文中給出的那個demo我一直跑不起來 )來實現一個簡單的自實現Linker Demo。

環境：`Pixel1XL`、`AOSP - Oreo - 8.1.0_r81`

```
二

Demo實現
```

Linker在加載so時大致可以分成五步：

1.讀取so文件：讀取ehdr( Elf header )、phdr( Program header )等信息。

2.載入so：預留一片內存空間，隨後將相關信息加載進去，最後修正so。

3.預鏈接：主要處理`.dynamic`節的內容。

4.正式鏈接：處理重定位的信息。

5.調用`.init`、`.init_array`

## `Read`

利用`open`+`mmap`來將待加載的so文件映射到內存空間，存放在`start_addr_`中。然後調用`Read`函數來獲取ehdr、phdr等信息。

```
int fd;
struct stat sb;
fd = open(path, O_RDONLY);
fstat(fd, &sb);
start_addr_ = static_cast<void **>(mmap(NULL, sb.st_size, PROT_READ | PROT_WRITE, MAP_PRIVATE, fd, 0));

// 1. 讀取so文件
if(!Read(path, fd, 0, sb.st_size)){
    LOGD("Read so failed");
    munmap(start_addr_, sb.st_size);
    close(fd);
}
```

`Read`函數實現如下，調用`ReadElfHeader`和`ReadProgramHeaders`來讀取ehdr和phdr。

AOSP源碼的`Read`中還會讀取Section Headers和Dynamic節，一開始我也有實現這部份的邏輯，但後來發現讀取後的信息根本沒有被用到，因此就把這部份給刪了。

```
bool MyLoader::Read(const char* name, int fd, off64_t file_offset, off64_t file_size) {
    bool res = false;

    name_ = name;
    fd_ = fd;
    file_offset_ = file_offset;
    file_size_ = file_size;

    if (ReadElfHeader() &&
        ReadProgramHeaders()) {
        res = true;
    }

    return res;
}
```

`ReadElfHeader`的實現如下，直接通過`memcpy`來賦值。

```
bool MyLoader::ReadElfHeader() {
    return memcpy(&(header_),start_addr_,sizeof(header_));
}
```

`ReadProgramHeaders`的實現直接copy源碼就可以，本質上還是內存映射的過程。

```
bool MyLoader::ReadProgramHeaders() {

    phdr_num_ = header_.e_phnum;

    size_t size = phdr_num_ * sizeof(ElfW(Phdr));

    void* data = Utils::getMapData(fd_, file_offset_, header_.e_phoff, size);
    if(data == nullptr) {
        LOGE("ProgramHeader mmap failed");
        return false;
    }
    phdr_table_ = static_cast<ElfW(Phdr)*>(data);

    return true;
}

void* Utils::getMapData(int fd, off64_t base_offset, size_t elf_offset, size_t size) {
    off64_t offset;
    safe_add(&offset, base_offset, elf_offset);

    off64_t page_min = page_start(offset);
    off64_t end_offset;

    safe_add(&end_offset, offset, size);
    safe_add(&end_offset, end_offset, page_offset(offset));

    size_t map_size = static_cast<size_t>(end_offset - page_min);

    uint8_t* map_start = static_cast<uint8_t*>(
            mmap64(nullptr, map_size, PROT_READ, MAP_PRIVATE, fd, page_min));

    if (map_start == MAP_FAILED) {
        return nullptr;
    }

    return map_start + page_offset(offset);

}
```

##

## `Load`

###

### 載入so基本信息

調用`Load`來載入so。

```
// 2. 載入so
if(!Load()) {
    LOGD("Load so failed");
    munmap(start_addr_, sb.st_size);
    close(fd);
}
```

`Load`的實現如下：

`ReserveAddressSpace`用於生成一片新的內存空間，之後的操作基本上都是在這片內存空間進行。`LoadSegments`、`FindPhdr`用於將待加載so的對應信息填充到此內存空間。

最後要修正so，將當前so修正為待加載的so，這部份放到後面來解析。

```
bool MyLoader::Load() {
    bool res = false;
    if (ReserveAddressSpace() &&
        LoadSegments() &&
        FindPhdr()) {

        LOGD("Load Done.........");
        res = true;
    }

    // 獲取當前so (加載器的so)
    si_ = Utils::get_soinfo("libnglinker.so");

    if(!si_) {
        LOGE("si_ return nullptr");
        return false;
    }
    LOGD("si_ -> base: %lx", si_->base);

    // 使si_可以被修改
    mprotect((void*) PAGE_START(reinterpret_cast<ElfW(Addr)>(si_)), 0x1000, PROT_READ | PROT_WRITE);

    // 修正so
    si_->base = load_start();
    si_->size = load_size();
//        si_->set_mapped_by_caller(elf_reader.is_mapped_by_caller());
    si_->load_bias = load_bias();
    si_->phnum = phdr_count();
    si_->phdr = loaded_phdr();

    return res;
}
```

`ReserveAddressSpace`的具體實現如下，先計算出`load_size_`後`mmap`一片內存，在我這個demo中`min_vaddr`是`0`，因此`load_start_ == load_bias_`，`load_bias_`代表的就是這片內存，而這片內存是用來存放待加載的so。

```
bool MyLoader::ReserveAddressSpace() {
    ElfW(Addr) min_vaddr;
    load_size_ = phdr_table_get_load_size(phdr_table_, phdr_num_, &min_vaddr);
    LOGD("load_size_: %x", load_size_);
    if (load_size_ == 0) {
        LOGE("\"%s\" has no loadable segments", name_.c_str());
        return false;
    }

    uint8_t* addr = reinterpret_cast<uint8_t*>(min_vaddr);

    void* start;

    // Assume position independent executable by default.
    void* mmap_hint = nullptr;

    start = mmap(mmap_hint, load_size_, PROT_NONE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

    load_start_ = start;
    load_bias_ = reinterpret_cast<uint8_t*>(start) - addr;

    return true;
}
```

`LoadSegments`的具體實現如下，遍歷Program Header Table將所有type為`PT_LOAD`的段加載進內存，源碼中是采用`mmap`來映射，但我嘗試後發現會有權限問題，因而采用`memcpy`的方案。

```
bool MyLoader::LoadSegments() {
    // 在這個函數中會往 ReserveAddressSpace
    // 裡mmap的那片內存填充數據

    for (size_t i = 0; i < phdr_num_; ++i) {
        const ElfW(Phdr)* phdr = &phdr_table_[i];

        if (phdr->p_type != PT_LOAD) {
            continue;
        }

        // Segment addresses in memory.
        ElfW(Addr) seg_start = phdr->p_vaddr + load_bias_;
        ElfW(Addr) seg_end   = seg_start + phdr->p_memsz;

        ElfW(Addr) seg_page_start = PAGE_START(seg_start);
        ElfW(Addr) seg_page_end   = PAGE_END(seg_end);

        ElfW(Addr) seg_file_end   = seg_start + phdr->p_filesz;

        // File offsets.
        ElfW(Addr) file_start = phdr->p_offset;
        ElfW(Addr) file_end   = file_start + phdr->p_filesz;

        ElfW(Addr) file_page_start = PAGE_START(file_start);
        ElfW(Addr) file_length = file_end - file_page_start;

        if (file_size_ <= 0) {
            LOGE("\"%s\" invalid file size: %", name_.c_str(), file_size_);
            return false;
        }

        if (file_end > static_cast<size_t>(file_size_)) {
            LOGE("invalid ELF file");
            return false;
        }

        if (file_length != 0) {
            // 按AOSP裡那樣用mmap會有問題, 因此改為直接 memcpy
            mprotect(reinterpret_cast<void *>(seg_page_start), seg_page_end - seg_page_start, PROT_WRITE);
            void* c = (char*)start_addr_ + file_page_start;
            void* res = memcpy(reinterpret_cast<void *>(seg_page_start), c, file_length);

            LOGD("[LoadSeg] %s  seg_page_start: %lx   c : %lx", strerror(errno), seg_page_start, c);

        }

        // if the segment is writable, and does not end on a page boundary,
        // zero-fill it until the page limit.
        if ((phdr->p_flags & PF_W) != 0 && PAGE_OFFSET(seg_file_end) > 0) {
            memset(reinterpret_cast<void*>(seg_file_end), 0, PAGE_SIZE - PAGE_OFFSET(seg_file_end));
        }

        seg_file_end = PAGE_END(seg_file_end);

        // seg_file_end is now the first page address after the file
        // content. If seg_end is larger, we need to zero anything
        // between them. This is done by using a private anonymous
        // map for all extra pages.

        if (seg_page_end > seg_file_end) {
            size_t zeromap_size = seg_page_end - seg_file_end;
            void* zeromap = mmap(reinterpret_cast<void*>(seg_file_end),
                                 zeromap_size,
                                 PFLAGS_TO_PROT(phdr->p_flags),
                                 MAP_FIXED|MAP_ANONYMOUS|MAP_PRIVATE,
                                 -1,
                                 0);
            if (zeromap == MAP_FAILED) {
                LOGE("couldn't zero fill \"%s\" gap: %s", name_.c_str(), strerror(errno));
                return false;
            }

            // 分配.bss節
            prctl(PR_SET_VMA, PR_SET_VMA_ANON_NAME, zeromap, zeromap_size, ".bss");
        }
    }

    return true;
}
```

`FindPhdr`的具體實現如下，簡單來說就是將Phdr信息填充進`load_bias_`那片內存。

```
bool MyLoader::FindPhdr() {

    const ElfW(Phdr)* phdr_limit = phdr_table_ + phdr_num_;

    // If there is a PT_PHDR, use it directly.
    for (const ElfW(Phdr)* phdr = phdr_table_; phdr < phdr_limit; ++phdr) {
        if (phdr->p_type == PT_PHDR...