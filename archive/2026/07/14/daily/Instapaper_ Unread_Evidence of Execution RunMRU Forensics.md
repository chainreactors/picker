---
title: Evidence of Execution RunMRU Forensics
url: https://digitalinvestigator.blogspot.com/2026/07/evidence-of-execution-runmru-forensics.html
source: Instapaper: Unread
date: 2026-07-14
fetch_date: 2026-07-15T04:49:53.452968
---

# Evidence of Execution RunMRU Forensics

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# Evidence of Execution: RunMRU Forensics

Joseph Moronwi
July 12, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxQgirh45ICj1pPOPxsW6-dWoWjCe1brK2EwA8C9jTBeFPo6EpWq30fW3uVSexYoB3ScXcObKmvbigNuCKnRS-gD3e8rOvrfHbZ8sNVX7rr_W4Ngjxa736WACcAdDilwnWRhYRmCcL-3B_68yfC-Szlhi7942rTccDJCxAIfinRyElObJllj_MnDPUsOQ/w658-h398/1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxQgirh45ICj1pPOPxsW6-dWoWjCe1brK2EwA8C9jTBeFPo6EpWq30fW3uVSexYoB3ScXcObKmvbigNuCKnRS-gD3e8rOvrfHbZ8sNVX7rr_W4Ngjxa736WACcAdDilwnWRhYRmCcL-3B_68yfC-Szlhi7942rTccDJCxAIfinRyElObJllj_MnDPUsOQ/s1023/1.jpg)

An enduring artifact originating in early Windows versions (pre-dating Windows XP) and persisting with minimal modification through contemporary releases (Windows 10/11) is the **Run dialog** (commonly invoked via Win + R). Originally integrated prominently within the classic Start Menu, its primary access vector has shifted toward the persistent keyboard shortcut, which remains the predominant method employed by users today.

This facility has consistently appealed to system administrators, power users, digital forensic examiners, and threat actors alike, enabling rapid, direct execution of applications, commands, and resources. Like numerous other Windows shell components, the Run dialog maintains a **Most Recently Used (MRU)** history of previously entered items. These entries are stored in the user-specific registry hive under the following key:

```
NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
```

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiY-9nN-QHSO81qVv__n14Xeu_gC3nIyHwXvHRNdesKzTy_bjdQ79a8VkAUb0eZdlszQ2Q5Hgi8GISwAy3CxQ245GoXZfbggd0uNldnWhsRqYJZRAp2p9Ifr8WtHgkMk5Awga9IP5eISvMPLw3HP1kHpOoxQj6GbYPshlS2ecAxW1wvCyLSuR18Eil1E8o/w654-h396/1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiY-9nN-QHSO81qVv__n14Xeu_gC3nIyHwXvHRNdesKzTy_bjdQ79a8VkAUb0eZdlszQ2Q5Hgi8GISwAy3CxQ245GoXZfbggd0uNldnWhsRqYJZRAp2p9Ifr8WtHgkMk5Awga9IP5eISvMPLw3HP1kHpOoxQj6GbYPshlS2ecAxW1wvCyLSuR18Eil1E8o/s1023/1.jpg)

The RunMRU key embodies a canonical string-based MRUList artifact, wherein discrete command executions are persisted as REG\_SZ values under single lowercase alphabetic identifiers (a–z), accommodating a maximum of 26 entries. The value data (as opposed to the value name) encapsulates the raw command string suffixed by the delimiter \1 (e.g., notepad.exe\1). A dedicated MRUList REG\_SZ value maintains the recency ordering as a contiguous string of these alphabetic designators, with the leftmost character representing the most recently utilized entry (position 0 in the MRU sequence). The LastWrite timestamp of the RunMRU key itself serves as a high-fidelity temporal anchor, directly correlating with the execution time of the foremost entry in the MRUList. Notably, only successfully resolved commands are recorded; failed executions are omitted. Re-execution of a prior command updates its position within the MRUList and refreshes the key’s LastWrite timestamp without allocating a new alphabetic slot, while new entries beyond the 26-slot capacity overwrite the least recently used value. This structure affords digital investigators a precise, user-specific chronology of Run dialog activity within the NTUSER.dat hive.

Retention of this artifact is subject to user-specific Start menu personalization settings. Disabling the privacy setting “Let Windows improve Start and search results by tracking app launches” directly suppresses the population of Run dialog history. The history is stored in plaintext and is limited to approximately 26 entries before older items are overwritten.

**RunMRU** constitutes one of the most elementary and transparent forensic artifacts encountered during Windows registry analysis. At a high level, its operational mechanics are as follows:

* **Command Ingestion and Storage**: The key is updated upon each successful execution of a command via the Run dialog. Individual commands are mapped to single-letter value names (a through z).

  + Novel commands are allocated a unique alphabetic value.
  + Re-execution of an existing command reassigns it to its prior letter and elevates it to the foremost position in the recency order.
  + Upon saturation of all 26 lettered values, subsequent commands overwrite the least recently utilized entry in a classic FIFO (first-in, first-out) manner.
* **Ordering Mechanism**: The MRUList value maintains the precise sequence of execution as a concatenated string, wherein the leftmost (index-0) position denotes the most recent entry.
* **Temporal Correlation**: The most recent command (position 0 within the MRU ordering) is intrinsically linked to the **LastWrite timestamp** of the RunMRU key, affording examiners a precise temporal marker for the final command invocation through this interface.

Solely valid and successfully processed commands are persisted; invalid inputs (such as references to non-existent files or malformed syntax) are generally excluded from recording.

## Invocation Methods for the Run Dialog

The Run dialog is implemented via an exported function within shell32.dll and can be instantiated through multiple vectors, all of which ultimately invoke the same underlying API. The principal methods include:

1. **Direct Keyboard Invocation**: Win + R
2. **Start Menu Integration**: Search for “Run” within the Windows Start Menu.
3. **Task Manager Utility**: Navigate to *File → Run new task* in Task Manager.
4. **Shell Protocol URI**: Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}
5. **Direct DLL Invocation**: rundll32.exe shell32.dll,#61
6. **Programmatic Access**: Invocation through Shell.FileRun() or the IShellDispatch.FileRun() interface.

Regardless of the invocation method used, all pathways converge on the same underlying shell32.dll functionality and use the same RunMRU registry key to populate the command history dropdown (provided the actions occur under the same user context).

### **Additional Technical Details**

* Methods #4 and #5 can be executed directly from the Run dialog or Explorer’s search bar. When launched from a command prompt or script, prefixing with explorer.exe may be required for the shell protocol variant.
* Method #5 executes the Run dialog by directly calling the exported ordinal 61 within shell32.dll.

This uniformity in backend behavior ensures consistent forensic artifacts across invocation techniques, with all activity traceable to the same RunMRU structure.

## Run Dialog Interaction with the RunMRU Artifact

Upon instantiation of the Run dialog, the process queries the MRUList value within the RunMRU key associated with the security context of the current user. Once retrieved, the dialog enumerates the referenced lettered values (a–z) to reconstruct the command history in the correct recency order for display. When a command is executed via the Run dialog, the following updates occur atomically:

* The new (or re-executed) command is written to an appropriate lettered value.
* The MRUList string is rewritten to reflect t...