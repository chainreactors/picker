---
title: NTFS Timestamps Forensic Investigation
url: https://digitalinvestigator.blogspot.com/2025/12/ntfs-timestamps-forensic-investigation.html
source: Instapaper: Unread
date: 2025-12-17
fetch_date: 2025-12-18T03:21:15.222834
---

# NTFS Timestamps Forensic Investigation

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# NTFS Timestamps Forensic Investigation

Joseph Moronwi
December 16, 2025
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgET0lYwKBaHjW0hpUz5XylOcKaM_hLg8tezhfJO26UBzOd6hMCar08ztIYQYrgH9sbA_0iN59ZwWQGyZhnZI2zdWPZ9GQp7IIHvMYVR-UNvtRUht_hUUB50wTqoD_M2GT0KG9Mahh8tfOagxhG1SW3zjMEmB1FOkJQwPFpVGqWWCAgUFwjIPzPhjEpwY8/w651-h256/luh.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgET0lYwKBaHjW0hpUz5XylOcKaM_hLg8tezhfJO26UBzOd6hMCar08ztIYQYrgH9sbA_0iN59ZwWQGyZhnZI2zdWPZ9GQp7IIHvMYVR-UNvtRUht_hUUB50wTqoD_M2GT0KG9Mahh8tfOagxhG1SW3zjMEmB1FOkJQwPFpVGqWWCAgUFwjIPzPhjEpwY8/s800/luh.png)

Among the various types of digital evidence, temporal footprints are especially valuable because they enable investigators to confirm the time of an intrusion and reconstruct the sequence of events surrounding an incident. In NTFS, two attributes within the Master File Table (MFT) store the MACB (also known as MACE) timestamps: the **$STANDARD\_INFORMATION ($SI)** attribute and the **$FILE\_NAME ($FN)** attribute.

All timestamps stored in the NTFS $STANDARD\_INFORMATION ($SI) and $FILE\_NAME ($FN) attributes are encoded as Windows FILETIME values. A FILETIME value represents the number of 100-nanosecond intervals elapsed since January 1, 1601, 12:00 A.M. (UTC). Because they are stored in UTC, these timestamps are not affected by local time zones or daylight saving time (DST). NTFS timestamps have a theoretical resolution of 100 nanoseconds. Both $SI and $FN provide four timestamp values commonly referred to as **MACB**, representing the following events:

* **Modified** – last modification of file content.
* **Accessed** – last access to file content.
* **Changed**—last modification of file metadata (i.e., changes to the MFT entry).
* **Birth**—file creation time (creation of the MFT entry).

The modification (M), access (A), and creation (B) timestamps of a file or directory are easily accessible through the Windows Explorer “Properties” dialog. These values are retrieved from the $STANDARD\_INFORMATION ($SI) attribute. The fourth timestamp—the metadata change time (C)—is not shown to users and is generally hidden at the GUI level.

The timestamps stored in the $FILE\_NAME ($FN) attribute are not directly visible to users and are not guaranteed to match those in $SI. When a file is created, all four timestamps in both $SI and $FN are initialized to the same values. However, while $SI timestamps may be updated by normal file operations (e.g., modifying content, accessing the file, or changing metadata), the timestamps in $FN are not directly updated by these actions. Instead, $FN timestamps are only refreshed when the $FN attribute itself changes, such as during file creation, copying, moving, renaming, or hard-link operations. In these cases, the operating system overwrites the existing $FN timestamps with the current values from $SI. Because Windows provides no API for directly modifying $FN timestamps, they are significantly more difficult to forge than the $SI timestamps presented to the user.

## The $STANDARD\_INFORMATION Attribute

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJx07eo_2WYjP45kHoB6GCS03zx3bRbdvvJjythAgjbOyJJMy8T0-kydqWApg_N8yewuyL-yQZ_vKyYTGs6EER33a925e9tv0z_zTynDiHOMpdw_6QhSfoBbmnERipgEEvBNJxPFE059ZV6mW66M-EzbuNONYsra_VjFJ8DBWFiIBEr8xuUQ_JCIpUw3U/w655-h206/SI-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJx07eo_2WYjP45kHoB6GCS03zx3bRbdvvJjythAgjbOyJJMy8T0-kydqWApg_N8yewuyL-yQZ_vKyYTGs6EER33a925e9tv0z_zTynDiHOMpdw_6QhSfoBbmnERipgEEvBNJxPFE059ZV6mW66M-EzbuNONYsra_VjFJ8DBWFiIBEr8xuUQ_JCIpUw3U/s742/SI-1.png) |
| Figure 1: The STANDARD\_INFORMATION attribute hex dump |

Following the MFT header for an MFT entry (in this case, MFT entry 24102) is the $STANDARD\_INFORMATION attribute. This attribute is always resident. The attribute ID for this attribute is 0x10 00 00 00. The first part of this
attribute follows a regular pattern known as the attribute header, which is 24 bytes long in this case.

The bytes at offsets 0x38-0x3B make up the four-byte identifier for this attribute. These
attribute IDs are defined in the $AttrDef metadata file.  Bytes 0x3C-0x3F define the length of this attribute. This conforms with the common practice of defining the length of an entry immediately following the identifier. The length shown here (endian reversed) is 0x00000060, which is 96
decimal. An inspection of Figure 1 above shows that 96 bytes from the beginning of this
attribute (offset 0x38), at byte offsets 0x98-0xA1, are the four values 0x30000000. These are a set of four bytes that should be another attribute ID. In this case, it is the ID for a
FileName Attribute, which is a valid entry, as we will see later.

At byte 0x40 is the resident/non-resident flag. This
is signified by 0x00 for a resident attribute and 0x01 for a non-resident attribute. The
flag refers to the body of the attribute itself. Other attributes will have similar
headers, in which each attribute will be defined as resident or non-resident. The next byte, at offset 0x41, indicates the length of the attribute name. In this case, the length is zero, since this attribute is not
allocated a name.

The bytes at offsets 0x42-0x43 indicate the offset
value to the start of the attribute content. These are not always used, as in this case, where
they are shown as 0x0000. The bytes at offset 0x44-0x45 are identified as a set
of flags that signify the following states: 0x0000 = normal, 0x0100 = compressed, 0x4000 = encrypted, and 0x8000 = sparse. It may well be the case that this field is included in the Attribute Header for use only with a $DATA Attribute.

The purpose of the bytes at offsets 0x46-0x47 is
unclear. Some sources suggest they are used as some form of attribute ID. Exploration of other MFTs suggests that these may be used for some purposes that
have not yet been sufficiently well identified by the writer. Part of
the field may be used as a flag to show malware-infected and malware-cleaned files.

The four bytes from offset 0x48-0x4B define
the length of the attribute content. In this case, the value is 0x00000048 (endian reversed), which is 72 bytes in
decimal. This attribute header is 24 bytes long, and the complete attribute, including
this header, is defined at bytes 0x3C-0x3F as 96 bytes. The value of the attribute content should therefore be 96 – 24 = 72, which is what is stored here.

The next two bytes, at offsets 0x4C-0x4D, indicate
the offset from the beginning of this attribute to the start of the attribute proper.
This is where the Standard Information attribute details start, after the header that is
currently being deconstructed. The value is 0x0018, which equals 24 decimal. Noting
from the figure above that the start offset for this attribute is 0x38, then the attribute content starts at offset 0x38 + 0x18 = 0x50.

Byte offset 0x4E is reported to be the
“indexed” flag, and byte offset 0x4F is reported to be padding to an 8-byte boundary.

### The $STANDARD\_INFORMATI...