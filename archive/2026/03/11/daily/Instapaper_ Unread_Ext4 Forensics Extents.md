---
title: Ext4 Forensics Extents
url: https://digitalinvestigator.blogspot.com/2026/03/ext4-forensics-extents.html
source: Instapaper: Unread
date: 2026-03-11
fetch_date: 2026-03-12T04:09:00.568881
---

# Ext4 Forensics Extents

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Ext4 Forensics: Extents

Joseph Moronwi
March 11, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhB6eJcBB_nwetflk5lhHIM07bQoNHcBhYTaRqf4AvI45rrlsws3p5SdgqZ3qbsiEYlJgQH4wS-Wih5NKnAkWppJA-wMoS8NxnmGjRtMoZbX7YBIZRiccErkhz8ZYJCIKVCsdLIecWhkSQAJaDLSXNv8UMUfYLbFfr7obD01SFX6OTRf_akmfD8GRNFr9c/w653-h247/debugfs.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhB6eJcBB_nwetflk5lhHIM07bQoNHcBhYTaRqf4AvI45rrlsws3p5SdgqZ3qbsiEYlJgQH4wS-Wih5NKnAkWppJA-wMoS8NxnmGjRtMoZbX7YBIZRiccErkhz8ZYJCIKVCsdLIecWhkSQAJaDLSXNv8UMUfYLbFfr7obD01SFX6OTRf_akmfD8GRNFr9c/s613/debugfs.png)

Earlier versions of the extended file systems used a traditional Unix-style mapping where each file's inode pointed to individual data blocks via direct pointers and single/double/triple indirect blocks. This worked well for small-to-medium files on smaller disks but became very inefficient as hard drive capacities grew into hundreds of GB (and then TB) and large files (videos, VM images, and databases) became common. With indirect blocks, locating and accessing file data often requires traversing extra layers of indirection (single, double, or triple indirect pointers). Moreover, because the file system tracks every individual block separately—even when they are physically contiguous—the mapping structures grow very large, creating substantial metadata overhead and performance costs during operations like reads, writes, and lookups. This per-block tracking approach also makes it harder to keep allocations contiguous, leading to increased fragmentation on disk. The severity of that fragmentation largely depends on how intelligently the block allocator can place new blocks. For these very reasons, *extents* are used in ext4.

# Ext4 Extents

Extents address these issues by storing data in contiguous ranges of blocks with a single compact entry (start block + length), dramatically reducing metadata size, minimizing indirection, improving I/O efficiency, and naturally encouraging better contiguous allocation to limit fragmentation. An extent is a single descriptor that represents a range of contiguous physical blocks. Extents are similar to cluster runs in the NTFS file system—essentially, they specify an initial block address and the number of blocks that make up the extent. A file that is fragmented will have multiple extents, but ext4 tries very hard to keep files contiguous. Extents are more efficient at mapping data blocks of large contiguous files, as their structure generally consists of the address of the first physical data block, followed by a length. The Ext4 extent structure is shown in the figure below.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdP2uaHGT0EtUcKTosVbYD-MCLXpztO3ehLwdhlR47MPfkZ8BDduJNskT3MpoDwgMTQp9V9Rh1TSoB4Uss4d3_Yc6FoO7jCtyrN7R0zNFYuE6PwvDfnbcWpRImkvJvjT91d188AuFSfPAlx5KCp8HR8XMFGiYa2Ag2bELc8tSPF8zQXyHdiwOTzVLgQTg/w653-h515/3-Figure1-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdP2uaHGT0EtUcKTosVbYD-MCLXpztO3ehLwdhlR47MPfkZ8BDduJNskT3MpoDwgMTQp9V9Rh1TSoB4Uss4d3_Yc6FoO7jCtyrN7R0zNFYuE6PwvDfnbcWpRImkvJvjT91d188AuFSfPAlx5KCp8HR8XMFGiYa2Ag2bELc8tSPF8zQXyHdiwOTzVLgQTg/s496/3-Figure1-1.png) |
| Figure 1: Ext4 extent structure. Originally appeared in Mathur et al. (2007) |

In ext4, each extent is represented using a 96-bit (12-byte) structure within the inode or extent tree. It contains a 32-bit logical block number (`ee_block`) which identifies the offset into the file on which the block run begins; a 16-bit length field, (`ee_len`) where the most significant bit is reserved for flagging uninitialized/preallocated extents; and a 48-bit physical block number (`ee_start_hi` + `ee_start_lo`) which indicates the file system block on which the extent begins. ee\_start\_hi denotes the high 16 bits of the physical block, while ee\_start\_lo denotes the low 32 bits of the physical block. If the most significant bit of ee\_len is set (ee\_len > 32768), it is uninitialized; the actual length is ee\_len - 32768. If the most significant bit is clear (ee\_len <= 32768), it is initialized. For initialized extents, the usable length is 15 bits, allowing a single extent to cover up to 2¹⁵ contiguous blocks—equivalent to approximately 128 MB with a 4 KB block size. Uninitialized extents allow space to be reserved without zeroing blocks immediately; when read, the virtual file system (VFS) returns zero-filled data to applications.

An inode can store up to four extents directly in its `i_block` area (which repurposes the old indirect block pointers from ext2/ext3). This setup suffices for smaller or mostly contiguous files. When a file becomes more fragmented or grows significantly, requiring more than four extents, ext4 builds an **extent tree** (often called an extent HTree) whose root is stored in the inode. This is a high-fanout, constant-depth tree similar to a B+ tree: The root resides in the inode and includes an extent header; intermediate (index) nodes contain pointers to child nodes; leaf nodes hold the actual extent descriptors, each pointing to a range of contiguous physical disk blocks. This tree organization enables efficient lookups and scalability for very large or highly fragmented files while keeping metadata compact and access fast. Ext4 tries to avoid fragments whenever possible; therefore, it is unusual to have many levels in the tree.

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZYdxxDZ7jHFdKv1Vux11YiG_CHpzB-ehn2kwpao4AQpOM7bcOvvgmXvDks2Zvj-wECGJ31pncIx8n_peMcdfOZuhUvBRIrGOhjgBlZwhJXOB5GeoEdy0Lon7et7Gz30f4321O2uMduXzIUairbYRLh_ZqdwI0ES5sZvf6fZvVfaO7A3JLU0En1Tc2kSU/w652-h587/3-Figure2-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZYdxxDZ7jHFdKv1Vux11YiG_CHpzB-ehn2kwpao4AQpOM7bcOvvgmXvDks2Zvj-wECGJ31pncIx8n_peMcdfOZuhUvBRIrGOhjgBlZwhJXOB5GeoEdy0Lon7et7Gz30f4321O2uMduXzIUairbYRLh_ZqdwI0ES5sZvf6fZvVfaO7A3JLU0En1Tc2kSU/s658/3-Figure2-1.png) |
| Figure 2: Ext4 extent tree structure. Originally appeared in Mathur et al. (2007). |

A comparison of the ext3 and ext4 inode structures reveals that ext4 places its extent data in the same 60-byte region (i\_block[EXT4\_N\_BLOCKS] at offset 0x28) previously occupied by ext3's block pointers. This 60-byte area begins with a **12-byte extent header** (ext4\_extent\_header). The header includes four 16-bit (2-byte) fields—`eh_magic` ( magic number 0xF30A); `eh_entries` (The number of entries following the extent header); `eh_max` (the maximum number of entries that might follow the extent header.); `eh_depth` (depth of the node)—followed by a 32-bit (4-byte) `eh_generation` (generation of the tree) field. The magic number is designed to differentiate between different extent implementations. As new features are added, the magic number can change to ensure backwards compatibility with older implementations. The eh\_depth field exactly determines this: (i) Depth > 0 → interior/index node → contains ext4\_extent\_idx entries pointing to child blocks; (...