---
title: Deleted File Recovery in Ext4
url: https://digitalinvestigator.blogspot.com/2026/04/deleted-file-recovery-in-ext4.html
source: Instapaper: Unread
date: 2026-04-14
fetch_date: 2026-04-15T04:44:10.724222
---

# Deleted File Recovery in Ext4

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# Deleted File Recovery in Ext4

Joseph Moronwi
April 05, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaWWnQgFdhnzyWvvHuGH8OJl9bE5FCI_CqVg0atGM87ZvfZDxUnmQ1xxF__SgH_ZKQn6kxwermpBssNmmBNgm5jeFueFgTIfqDBozLBSxIKU52GHh68rqNCUjzcbm-t7mpgROPv0kx7WcW-0KnyW0MrTxYm7oiSwCJwb_5upI_gLRwf0Ncz_wbrFQe6XY/w655-h461/after1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaWWnQgFdhnzyWvvHuGH8OJl9bE5FCI_CqVg0atGM87ZvfZDxUnmQ1xxF__SgH_ZKQn6kxwermpBssNmmBNgm5jeFueFgTIfqDBozLBSxIKU52GHh68rqNCUjzcbm-t7mpgROPv0kx7WcW-0KnyW0MrTxYm7oiSwCJwb_5upI_gLRwf0Ncz_wbrFQe6XY/s643/after1.png)

The ext4 filesystem—the default choice for most modern Linux distributions—is a robust evolution of its predecessors, ext2 and ext3. While it brings significant improvements in performance, reliability, and scalability, one question continues to fascinate both system administrators and digital forensics enthusiasts: What actually occurs when you delete a file in ext4? When you hit the `rm` command, it feels instantaneous and final. Yet beneath the surface, the filesystem does not immediately erase your data. Instead, it performs a carefully coordinated sequence of metadata updates, block freeing, and journal transactions. Understanding this delicate process is key to mastering file recovery — and knowing exactly when (and how) your “deleted” files can still be rescued. In this article, we will dive deep into the internals of the ext4 filesystem to uncover exactly how file deletion works, why recovery is sometimes possible, and what techniques you can use to maximize your chances of successfully recovering deleted files.

# Ext4 File Deletion Process

When a file is deleted in ext4, the process begins with removing the directory entry that links the filename to its inode. This renders the file inaccessible by name/path. The inode's link count is then decremented, and once it reaches zero (with no open file descriptors), the inode is marked free in the inode bitmap. Crucially, the inode's extent tree (mapping to data blocks) is zeroed out (cleared), the file size and block count are zeroed, and the deletion time (`i_dtime`) is recorded—but the inode structure itself is not fully erased and remains reusable.

Simultaneously, the associated data blocks are marked free in the block bitmap and returned to the pool of available space. However, the actual data content in those blocks is left untouched. It will only be overwritten when the blocks are later reallocated to new files. This design—where metadata is updated, but raw data persists until reuse—is exactly why deleted file recovery is frequently possible on ext4, provided action is taken before the blocks are overwritten.

## Ext4 Journaling

One of ext4’s most important features is its **journaling** capability, which protects file system integrity by logging metadata changes before they are applied to the main structures. This mechanism also plays a supporting role in understanding (and sometimes assisting) deleted file recovery. When a file is deleted in ext4, the operation is wrapped in a journal transaction. The journal records the following key metadata updates to ensure atomicity and consistency in case of a crash or power failure:

* **Inode update** → The inode’s link count is decremented. When it reaches zero, the inode is marked free in the inode bitmap, its extent tree is cleared, the file size and block count are zeroed, and the deletion timestamp (`i_dtime`) is set. This inode update is journaled.
* **Directory entry modification** → The link between the filename and inode is removed from the parent directory (typically by adjusting record lengths (`rec_len`) in the directory block rather than zeroing the entry). This directory block change is also journaled.
* **Block bitmap update** → The data blocks previously allocated to the file are marked free in the block bitmap(s). The block bitmap changes are journaled, and revoke records or descriptor blocks may reference the affected blocks. But the journal does not typically log the list of every data block number being freed (especially for files using extents). It journals the bitmap block(s) and inode changes.

Importantly, the actual contents of the file’s data blocks are not written to the journal (in default metadata-journaling mode) and are not erased at deletion time. *Only in the much slower `data=journal` mode (full data + metadata journaling) would file contents also go through the journal—and even then, only for new writes, not retroactively for deletions*. They remain on disk until those blocks are reallocated and overwritten by new data. Each transaction is bounded by descriptor and commit records, tagged with sequence numbers to maintain proper ordering during replay. Once the changes are safely written to their final locations on disk, the transaction is **checkpointed**, allowing the journal space to be reused.

The data recorded in the ext4 journal during file deletion is critical to preserving file system integrity after a crash or power failure, but it does not typically include the actual file content. While the journal logs important metadata changes — such as inode updates, directory entry modifications, and block/inode bitmap adjustments — the raw data blocks of the deleted file remain untouched on the disk. This means that successful recovery of file content relies primarily on the fact that those blocks have not yet been reallocated and overwritten by new data, rather than on information stored in the journal itself.

In summary, the ext4 journal records critical changes to filesystem metadata and block allocation status during deletion. This information is essential for ensuring consistency and can sometimes assist recovery tools in locating old inodes or directory entries. However, it is important to note that the journal does not store the actual content of deleted files.

## The Role Of System Calls

File deletion in Linux is typically initiated by the `unlink()` or `unlinkat()` system calls. These calls instruct the kernel to remove the directory entry that associates the filename with its inode. The operation flows through the Virtual File System (VFS) layer, which provides a generic interface for file operations regardless of the underlying file system (in this case, ext4).

Changes made during deletion — such as updating the directory block, modifying the inode, and adjusting allocation bitmaps — are first applied in the kernel’s page cache (also known as the buffer cache). These dirty pages are not immediately flushed to disk; they may remain in memory for a short time before being written back. This caching layer introduces a small delay between the rm command and the actual disk updates.

It is worth distinguishing deletion from truncation (via the `truncate()` or `ftruncate()` syscalls). Truncation reduces or removes a file’s data content while leaving the directory entry and inode intact. Deletion, by contrast, removes the name-to-inode link and eventually frees the inode o...