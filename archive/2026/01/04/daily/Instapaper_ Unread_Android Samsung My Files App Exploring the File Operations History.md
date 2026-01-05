---
title: Android Samsung My Files App Exploring the File Operations History
url: https://bebinary4n6.blogspot.com/2026/01/android-samsung-my-files-app-exploring.html
source: Instapaper: Unread
date: 2026-01-04
fetch_date: 2026-01-05T03:52:14.793146
---

# Android Samsung My Files App Exploring the File Operations History

# [Be-binary 4n6](https://bebinary4n6.blogspot.com/)

This is my blog about topics in the field of digital forensics.

## Sunday, January 4, 2026

### Android Samsung My Files App: Exploring the File Operations History

I’ve been exploring Samsung apps on Android, and I’d like to share some of my findings. Let’s start with the File Operations History maintained by the Samsung My Files app.

The My Files app keeps a database that logs actions performed on files and folders throughout the system. This database provides a detailed view of user and/or system activity, capturing events such as file creation, movement, copying, and deletion.

Android Version Tested:
Android 15

Test device:
Samsung Galaxy S23

Database Location:
`[...]/com.sec.android.app.myfiles/databases/OperationHistory.db`

The database can exist both system-wide and per user, for example:

* `/data/data/[...]` — system-wide
* `/data/user/0/[...]` — default user
* `/data/user/150/[...]` — secure folder

By analyzing this database, you can reconstruct file operations done on the system.

### The database structure

The most interesting tables in the database are:

1. operation\_history:

This table stores summary information about each file operation, including the date and time, type of operation, status, and the number of files or folders involved.

2. operation\_history\_data

This table contains the detailed information for each operation. It includes one entry per file or folder, specifying the file or folder name, as well as the source and destination paths for the operation.

#### Table operation\_history

* \_id - The primary key, iterating number to identify the operation
* mDate - Time and date in UTC when the operation was done. Not totally clear if it is the start or the end timestamp
* mOperationType - Type of Operation - human readable, e.g. MOVE, MOVE\_TO\_TRASH, RENAME, COPY, DELETE
* mItemCount - Number of Items the operation is done on. This is the aggregated number of folder and files
* mFolderCount - Number of folders the operation is done on
* mPageType - Location in the App from where the operation was triggered.
* mOperationResult - Result of the operation, not always filled with any data.

#### Table operation\_history\_data

* \_id - The primary key, iterating number to identify the file/folder used in operation
* operation\_id - The foreign key, with this we know which operation from the operation\_history is related to this line
* src\_path - Source path of the file or folder. Has different meanings for operation. E.g. CREATE\_FOLDER -> it is the folder where the new folder is created in
* src\_file\_id - Always identical with src\_path in my test data
* dst\_path - Destination path of the file or folder. E.g. the file that is created. Can be empty for operations - e.g. for DELETE or EMPTY\_TRASH
* dst\_file\_id - Always identical with the dst\_path in my test data
* file\_type - Decimal number - meaning currently not totally clear, seems to be based on some MIME type or extensions type things. Current test data shows the following mapping:

10 -  Image (JPEG)

11 - Image (JPG)

14 - Image (PNG)

19 - Image (WEBP)

53 - Image (HEIC)

100 - Audio (MP3)

102 - Audio (M4A)

107 - Audio (OPUS)

200 - Video (MP4)

311 - Document (CSV)

312 - Document (PDF)

315 - Document (DOCX)

330 - Document (TXT)

400 - Archive (APK)

410 - Archive (ZIP)

411 - Archive (RAR)

506 - (VCF)

526 - (TORRENT)

12289 - Folder

This leads me to that it is something like:

10 -99 = Images

1xx = Audio

2xx = Video

3xx = Documents

4xx = Archives

5xx = Others

12289 = Folder

### Getting and interpreting the data

1. Get an Operations Overview

```
SELECT
mDate [Operation Date],
_id [Operation ID],
mOperationType [Operation Type],
mItemCount [# of Files],
mFolderCount [# of Folder],
mPageType [Page Type],
mOperationResult [Result]
FROM operation_history;
```

2. Get list of all operations and the corresponding files / folders.

```
SELECT
oh.mdate [Operation Date],
ohd.operation_id [Operation ID],
ohd.src_path [Source Path],
ohd.src_file_id [Source File ID],
ohd.dst_path [Destination Path],
ohd.dst_file_id [Destination File ID],
oh.mOperationType [Operation Type],
oh.mItemCount [# of Files],
oh.mFolderCount [# of Folders],
oh.mPageType [Page Type],
oh.mOperationResult [Result],
oh.mMemoryFullCapacity [Storage Capacity Info]
FROM operation_history_data ohd
JOIN operation_history oh ON oh._id = ohd.operation_id
```

3. Are there any parsers out there?

I also looked into existing tools for parsing this data. Currently, ALEAPP includes a parser for the File Operations History, but it only supports Android versions below 13 and analyzes only the `operation_history` table.

After reviewing the code, I concluded that it would be possible to adapt the parser to support newer Android versions as well. I plan to do this in the future, but for now, I want to focus on my analysis of Samsung apps without interrupting the workflow by refactoring an existing parser.

### Meaning of the data / Conclusion

The entries in the File Operations History reflect the file operations performed by the Samsung My Files app. They provide a useful overview of what actions were taken on files and folders within the system.

The data is retained for a long period—in my test dataset, I was able to trace operations going back about one and a half years. I did not observe any triggers that would automatically delete entries from the database.

What the data don't show:

It is important to note that the database does not log individual files inside a folder when an operation is performed on the folder itself.

*Example:*

If I decide to move a folder to a new location, I select the folder in the UI and click “Move.” The File Operations History will store an entry for this folder and the move operation—but it will not create entries for each file inside the folder.

However, it may be possible to reconstruct some file-level operations by looking back at earlier entries. For example, if a file was created in that folder 30 minutes before the move and was not subsequently deleted based on entries in the database, you could infer that it was included in the move operation. But I would like to always double check this with additional data if possible in any way.

Additionally, the database only logs operations performed by Samsung apps, specifically the My Files app or calls to this app. Any operations done through third-party file managers will not appear in the File Operations History.

Future work:

I have stored my SQL queries for extracting data from the database in my GitHub repository for later use, such as building a parser:
<https://github.com/kalink0/useful_scripts/blob/master/sql/Android/Samsung%20Apps/sMyFiles.sql>

I also plan to create additional posts on Samsung apps, sharing my findings step by step.

on
[January 04, 2026](https://bebinary4n6.blogspot.com/2026/01/android-samsung-my-files-app-exploring.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=3962267980399809654&postID=2159919884182311109&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=3962267980399809654&postID=2159919884182311109&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=3962267980399809654&postID=2159919884182311109&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=3962267980399809654&postID=2159919884182311109&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=3962267980399809654&postID=2159919884182311109&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=3962267980399809654&postID=2159919884182311109&target=pinterest "Share to Pinterest")

Labels:
[android](https://bebinary4n6.blogspot.com/search/label/android),
[samsung](https://bebinary4n6.blogspot.com/search/label/...