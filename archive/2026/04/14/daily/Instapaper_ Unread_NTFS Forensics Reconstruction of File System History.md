---
title: NTFS Forensics Reconstruction of File System History
url: https://digitalinvestigator.blogspot.com/2026/04/ntfs-forensics-reconstruction-of-file.html
source: Instapaper: Unread
date: 2026-04-14
fetch_date: 2026-04-15T04:44:11.310151
---

# NTFS Forensics Reconstruction of File System History

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Hard Disks and File System Forensics](https://digitalinvestigator.blogspot.com/search/label/Hard%20Disks%20and%20File%20System%20Forensics)

# NTFS Forensics: Reconstruction of File System Activity History

Joseph Moronwi
April 12, 2026
0

Forensic reconstruction of historical activity on a New Technology File System (NTFS) volume relies on the systematic analysis of specialized metadata structures and transactional journals to achieve high-fidelity timeline reconstruction of file and directory operations. This includes events such as creation, modification, access, attribute changes, renaming, movement, and deletion (including post-deletion artifacts). The cornerstone artifacts enabling this reconstruction are the Master File Table ($MFT), the Update Sequence Number Change Journal ($UsnJrnl), and the NTFS transactional $LogFile. Collectively known in the digital forensics community as the NTFS TriForce, these three components provide complementary layers of visibility. When correlated effectively, this triad enables investigators to construct detailed chronological narratives, detect anti-forensic techniques such as timestomping, recover evidence of deleted or relocated files, and reconstruct complex operational sequences that would otherwise remain obscured.

The Update Sequence Number (USN) Change Journal, commonly referred to as $UsnJrnl (or simply the Change Journal), serves as a persistent, high-fidelity audit mechanism within the NTFS file system. It systematically records a broad spectrum of file and directory operations—including creations, deletions, modifications, renames, attribute changes, security descriptor updates, and various reason-coded events—on a per-volume basis. Introduced with NTFS 3.0 in Windows 2000, the journal became enabled by default on system volumes starting with Windows Vista (and remains active in all subsequent Windows client and server editions). Beyond its native role in supporting Windows features such as Search Indexing, File Replication Service (FRS), and File History, the $UsnJrnl has emerged as a cornerstone artifact in modern digital forensics and incident response. It preserves chronological evidence of filesystem activity that often survives deletion, MFT record reuse, or basic timestomping attempts.

When analyzed in tandem with the NTFS $LogFile—which captures low-level transactional metadata operations (e.g., MFT record updates, index modifications, and atomic filesystem consistency changes)—the USN Journal provides a more comprehensive reconstruction of file-level events, including nuanced details about the sequence and nature of operations that might otherwise remain opaque.

Furthermore, the $UsnJrnl forms a foundational element of the well-established NTFS TriForce (sometimes extended to a “QuadLink” correlation incorporating the $MFT Mirror for integrity validation). This analytical triad—comprising the Master File Table (MFT) for current and residual metadata, the $LogFile for transactional depth, and the $UsnJrnl ($J alternate data stream) for high-level change logging—enables examiners to achieve granular reconstruction of system activity. Applications include:

* Timeline assembly across deleted or renamed files.
* Detection of anti-forensic techniques (e.g., timestomping via sequence number or timestamp discrepancies).
* Path reconstruction through parent MFT references
* Identification of ransomware staging, data exfiltration patterns, or lateral movement artifacts.

In advanced investigations, this TriForce approach significantly enhances the ability to uncover subtle filesystem behaviors and counter anti-forensic efforts, offering investigators a deeper, multi-layered understanding of what transpired on a Windows system.

## $MFT

In the NTFS file system, every file and directory is represented by one or more entries (commonly called file records) in the Master File Table (MFT). These records encapsulate comprehensive metadata, including filenames, timestamps, security descriptors, and—depending on size—resident data or pointers to non-resident content. Each MFT entry begins with a fixed-size file record header (typically 42 bytes on modern Windows systems), which starts with a signature ("FILE" for valid records or "BAAD" for corrupted ones). The header contains critical forensic fields, notably:

* The $LogFile Sequence Number (LSN) — an 8-byte value referencing the most recent transaction in the NTFS $LogFile that affected this MFT entry. This field supports filesystem recovery and enables correlation with low-level metadata changes.
* The sequence number (2 bytes) — a counter that increments each time the MFT record is (re)allocated. When a file is deleted, and its record is later reused for a new file, the sequence number is incremented. This mechanism allows differentiation between successive "generations" of the same MFT slot and helps validate file references during path reconstruction or deletion analysis.

Following the header is a sequence of attributes, each with its own header (containing type ID, length, resident/non-resident flag, etc.) and content. The two most ubiquitous attributes are:

* $STANDARD\_INFORMATION (0x10): Contains core metadata such as creation, modification, access, and MFT entry modification timestamps (MACE times), file attributes/flags, owner/security identifiers, and—on Windows 2000 and later—an 8-byte Update Sequence Number (USN) field. This USN serves as a direct reference to the most recent record in the $UsnJrnl ($J stream) associated with changes to this file or directory.
* $FILE\_NAME (0x30): Stores the filename (in Unicode) along with its set of timestamps and a parent file reference. The parent reference is a 64-bit value comprising the 48-bit MFT entry number of the parent directory and its 16-bit sequence number. This structure is essential for reconstructing full file paths, even for deleted entries, by recursively resolving parent references.

Additional attributes (e.g., $DATA, $ATTRIBUTE\_LIST for extension records, $OBJECT\_ID, $SECURITY\_DESCRIPTOR) may follow, depending on the file's characteristics. Hard-linked files will have multiple $FILE\_NAME attributes. Because the MFT maintains an entry for virtually every file and directory that has existed on the volume, extracting and parsing the entire $MFT file from a forensic image yields a near-complete inventory of filesystem activity. When combined with the $LogFile (for transactional depth) and the $UsnJrnl (for high-level change logging), analysts can achieve detailed timeline reconstruction, detect anti-forensic techniques (such as timestomping), and recover evidence of deleted or renamed files even after MFT record reuse.

## $LogFile

The NTFS $LogFile, located in Master File Table (MFT) record number 2, functions as the file system’s transactional journal. It records low-level metadata operations to guarantee volume consistency in the event of system crashes, power failures, or unexpected interruptions. In digital forensics and incident response, the $LogFile serves as a valuable “time machine,” preserving evidence of prior states of MFT entries, directory indices, and other metadata—eve...