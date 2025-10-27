---
title: Using Guids to guide the ID of samples’ capabilities or unique (attributable) properties…
url: https://www.hexacorn.com/blog/2024/10/02/using-guids-to-guide-the-id-of-samples-capabilities-or-unique-attributable-properties/
source: Hexacorn
date: 2024-10-03
fetch_date: 2025-10-06T18:52:24.071358
---

# Using Guids to guide the ID of samples’ capabilities or unique (attributable) properties…

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2024/09/21/rundll32-goes-to-hell/)
[Next →](https://www.hexacorn.com/blog/2024/10/12/the-sweet16-the-oldbin-lolbin-called-setup16-exe/)

# Using Guids to guide the ID of samples’ capabilities or unique (attributable) properties…

Posted on [2024-10-02](https://www.hexacorn.com/blog/2024/10/02/using-guids-to-guide-the-id-of-samples-capabilities-or-unique-attributable-properties/ "11:08 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

A few days ago [Karsten](https://x.com/struppigel) asked me what tool did I use for GUID extraction. I [replied](https://x.com/Hexacorn/status/1838982521054257232) that it was my own old tool written waaaay before yara’s birth.

In this post I will elaborate on this bit a bit…

That old GUID extraction tool was written in perl – yeah, I know… … and… it was basically reading the content of the whole sample to memory, and then, within that content, it was searching for… known GUIDs…. It was badly written, superslow, but… at that time… superuseful!

Why?

Because my short GUID list was curated. My tool looked only for GUIDs associated with known adware/spyware + popular GUIDs associated with COM interfaces abused by malware at that time. So, it was very ‘focused’ as it was helping me to quickly ID samples belonging to 180Solutions, Zango, BetterInternet, Ezula, Bonzi, ClearSearch, VirtuMonde and many others, and… was also highlighting to me some potentially interesting features of triaged samples like them including references to COM interfaces operating on shortcut files (IShellLink) or generic (IPersistFile) methods for saving files…

A [GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) itself is a very interesting IOC on its own. In theory, it is supposed to act as a global, unique identifier. In practice, it is not only just an identifier, but also a capability determinant, amongst other things.

in my [old post](https://www.hexacorn.com/blog/2022/07/22/week-of-data-dumps-part-2-guids/) I dumped a lot of ‘GUID to <something>’ mappings that any data hoarder should find useful… For example, taking just that list, validating it (it actually had some bugs!), and converting it to a set of yara rules is a step we can take to kinda partially duplicate the features of my old perl tool.

The conversion process walks through all GUIDs from the input file and creates a small yara rule for each of these GUIDs, where each of them is converted to 3 strings:

* GUID string as an ASCII
* GUID string as a Wide string (UTF16)
* binary representation of the GUID

The resulting file looks like [this](https://hexacorn.com/d/guids.yar).

The rules written this way take care of any textual references to GUID present inside the sample (ASCII and Unicode/Wide), plus it recognizes the most popular way of storing GUIDS – the 16-bytes long binary form. That is, it will pick up known GUID references inside the resources, embedded IDL files, as well as any actual code/data strings and of course, the binary form of GUID that programmers (often unknowingly) introduce to their programs.

Now that we have this yara file, we can test it by applying it to f.ex. win11’s Notepad.exe:

```
yara guids.yar notepad.exe
```

The results are:

```
guid_IUnknown notepad.exe
guid_IMarshal notepad.exe
guid_IAsyncInfo notepad.exe
guid___FIAsyncOperationCompletedHandler_1_Windows__CSystem__CLaunchQuerySupportStatus notepad.exe
guid_IPropertyDescriptionList notepad.exe
guid___FIAsyncOperationCompletedHandler_1_Windows__CSecurity__CEnterpriseData__CFileProtectionInfo notepad.exe
guid___x_ABI_CWindows_CStorage_CIStorageItem notepad.exe
guid_IFileDialog notepad.exe
guid_IShellItem notepad.exe
guid___x_ABI_CWindows_CFoundation_CIUriRuntimeClassFactory notepad.exe
guid___FIEventHandler_1_Windows__CSecurity__CEnterpriseData__CProtectedContentRevokedEventArgs notepad.exe
guid___x_ABI_CWindows_CSecurity_CEnterpriseData_CIFileProtectionManagerStatics notepad.exe
guid___x_ABI_CWindows_CStorage_CIStorageFileStatics notepad.exe
guid___x_ABI_CWindows_CSystem_CILauncherStatics2 notepad.exe
guid_IAccPropServices notepad.exe
guid_IFileSaveDialog notepad.exe
guid_IAgileObject notepad.exe
guid_CAccPropServices notepad.exe
guid___x_ABI_CWindows_CSecurity_CEnterpriseData_CIProtectionPolicyManagerStatics2 notepad.exe
guid_FileSaveDialog notepad.exe
guid___x_ABI_CWindows_CSecurity_CEnterpriseData_CIProtectionPolicyManagerStatics notepad.exe
guid___FIEventHandler_1_IInspectable notepad.exe
guid___x_ABI_CWindows_CApplicationModel_CDataTransfer_CIClipboardStatics notepad.exe
guid_IFileOpenDialog notepad.exe
guid___x_ABI_CWindows_CApplicationModel_CDataTransfer_CIDataPackagePropertySetView3 notepad.exe
guid_FileOpenDialog notepad.exe
guid___FIAsyncOperationCompletedHandler_1_Windows__CStorage__CStorageFile notepad.exe
guid_IFileDialogCustomize notepad.exe
guid_LocalAppData notepad.exe
```

Even without a single second spent in a disassembler or decompiler we can already see what sort of GUIDs the Notepad.exe references. Some of them are related to COM functionality (f.ex. guid\_IFileSaveDialog), some are just GUIDs used as function arguments to functions (f.ex. guid\_LocalAppData).

Is it very useful?

I guess… it depends….

If you had a good adware/spyware GUID database back in 2005-2008 you could quickly identify a lot of adware/spyware samples w/o even looking at their code. It worked really nicely.

There are also existing plug-ins for disassembler/decompilers that try to recognize existing GUIDs inside the code/data and rename these data chunks that look like known GUIDs with appropriate names of classes/interfaces or associated artifacts (f.ex. [Known Folder IDs](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid)).

The GUID values are present inside the PDB / RSDS structure included inside some of the PE files – they link the .EXE file with the .PDB file. The Module Version ID (MVID) and TypeLib ID are both GUIDs that are present inside compiled .NET assemblies and can be extracted & collected. Their unique values can be used to link samples coming from the same Visual Studio instance, and/or build environment. Last, but not least – it was allegedly a GUID that linked the first iteration of Melissa virus to its author who eventually got arrested.

GUIDs are great artifacts and it’s wise to both collect all the extractable instances of it, and look for the presence of the known ones in the analyzed samples.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Batch Analysis](https://www.hexacorn.com/blog/category/batch-analysis/), [Clustering](https://www.hexacorn.com/blog/category/clustering/), [Malware Analysis](https://www.hexacorn.com/blog/category/malware-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/10/02/using-guids-to-guide-the-id-of-samples-capabilities-or-unique-attributable-properties/ "Permalink to Using Guids to guide the ID of samples’ capabilities or unique (attributable) properties…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")