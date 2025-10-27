---
title: AWS Ransomware
url: https://dfir.ch/posts/aws_ransomware/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:07:59.467658
---

# AWS Ransomware

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# AWS Ransomware

21 Feb 2024

**Table of Contents**

* [Background](#background)
* [Reconnaissance](#reconnaissance)
* [Deletion of Buckets](#deletion-of-buckets)
* [You call it recovery - I call it scam](#you-call-it-recovery---i-call-it-scam)
* [Summary](#summary)

## Background

A customer contacted us reporting that an attacker had deleted several AWS S3 buckets (before allegedly downloading the data). Subsequently, the attacker left a ransom note (depicted below, sensitive information has been redacted). In this blog, we examine a recovery binary left behind by the attackers after deleting the buckets and show that the binary is nothing more than a red herring to increase the pressure on the victim.

```
!!! WARNING !!! !!! WARNING !!! !!! WARNING !!! !!! WARNING !!!

To recover your lost files and avoid leaking it:

Send us 0.2 Bitcoin (BTC) to our Bitcoin addresses
Price is not standard, depend on your data.

Contact us by email to confirm
restore@<redacted>.com

example:
1Krx5mJNqW8[...]
13o2MSsNNDP[...]

Linux
tar xzvf recoveryAKIAZ5ESTHWPHSNVAXZ7.tgz
chmod +x recovery
./recovery

You need to be authenticated into aws-cli with credentials to perform restore
run -> aws configure and authenticate if you are not already !
Once the recovery starts, you need to be sure your connection does not drop, your computer does not crash

Once you contact us we will explain how to avoid further attacks.

Contact us by email to confirm and attach file warning.txt
restore@<redacted>.com

AKIA S3 backup

Your files are downloaded and backed up on our servers. If we dont receive your payment in the next 5 days, we
will sell your files to the highest bidder or use them otherwise or permanently deleted. We also extract sensitive informations.
```

Another version of this ransom note, lacking the recovery component, has been uploaded to [VirusTotal](https://www.virustotal.com/gui/file/3f759783fc0e6ec98a6e5d7c87336a87e5281fd1029ee3f8c7f2bb75299d140b/detection). It was initially submitted on January 29, 2024, from France, matching roughly our timeline.

## Reconnaissance

We traced the initial actions of the attacker back to January 18, 2024, when they executed two standard reconnaissance commands against the AWS Simple Email Solution (SES) and Amazon Simple Storage Service (S3):

* *GetSendQuota*
* *ListBuckets*

[Invictus-IR](https://www.invictus-ir.com/) created [a CSV file](https://gist.github.com/invictus-ir/2e892e19aad49eafe449fae91b2ff25b#file-cloudtrail-csv) with interesting CloudTrail events from [another ransomware incident in the cloud](https://www.invictus-ir.com/news/ransomware-in-the-cloud). It is highly recommended that defenders and SOC members check their security monitoring for these event names, as these events could tell that an attacker has access to an AWS endpoint.

![Important CloudTrail event logs](/images/aws/cloud_trail.png "Important CloudTrail event logs")

Figure 1: Important CloudTrail event logs

## Deletion of Buckets

On February 5th 2024, the attacker utilized the command *DeleteBucket* to erase all buckets, leaving behind the previously mentioned ransom note. Before the deletion of the buckets, the following commands were recorded in the CloudTrail logs:

* *GetBucketVersioning* (see Figure 1 - versioning was not enabled)
* *GetBucketReplication*
* *GetBucketObjectLockConfiguration*
* *GetBucketLogging*
* *GetBucketRequestPayment*
* *GetAccelerateConfiguration*

## You call it recovery - I call it scam

Within the ransom note, the following three Linux commands are mentioned:

* tar xzvf recoveryBYESZ2ESTHWPWHDRAXZ7.tgz
* chmod +x recovery
* ./recovery

The attacker placed the archive (recoveryBYESZ2ESTHWPWHDRAXZ7.tgz) in the same folder as the ransom note, including a text file called *aws.txt*. The complete archive includes numerous unrelated folders containing Linux libraries, C source code files, Python files, etc., to boost the archive size and give the archive a more ‘serious’ touch.

Focusing only on the recovery part, we read the following statement inside the ransom note:

*You need to be authenticated into aws-cli with credentials to perform restore
run -> aws configure and authenticate if you are not already !
Once the recovery starts, you need to be sure your connection does not drop, your computer does not crash*

**Analysis of the binary**

The recovery binary (called simply *recovery*, see above) was initially [uploaded to VirusTotal](https://www.virustotal.com/gui/file/3440b4fc74f51d5104deb38924ec821f7f7b8ecd585667f84d4743dd305eb2ba/detection) on February 2nd, 2024. Upon launching the recovery binary, it prompts us for the AWS key. Subsequently, the binary informs us that it verifies the account information and prints details about it.

```
Welcome to AWS recovery
Please enter your AWS: malmoeb
Please enter your AWS key: malmoeb_key
Checking ...
Account Information:
    "UserId": "AIDAZ[...]",
    "Account": "6810[...]",
    "Arn": "arn:aws:iam::6810:user/<redacted>"
Creating folder: dfir
Total number of files: 240
Total size (GB): 5.00 GB
```

After entering the AWS key, the binary indicates it is checking something. However, based on the strace output (see my post about using [strace for Linux malware analysis](https://dfir.ch/posts/strace/)), the code sleeps for five seconds (the number 5 was passed on as an argument to the system call [clock\_nanosleep](https://man7.org/linux/man-pages/man2/clock_nanosleep.2.html)).

```
write(1, "Checking ...\n", 13)          = 13
clock_nanosleep(CLOCK_REALTIME, 0, {tv_sec=5, tv_nsec=0}, 0x7ffeb42cb290) = 0
```

Upon further examination of this behavior, we discover a call to the *sleepRandom()* function, directing the binary to sleep for a random duration. This aligns with the observed behavior in the strace output.

![Welcome to AWS recovery](/images/aws/checking.png "Welcome to AWS recovery")

Figure 2: Welcome to AWS recovery

The *sleepRandom()* function utilize the *sleep()* function under the hood:

![sleepRandom() function](/images/aws/sleepRandom.png "sleepRandom() function")

Figure 3: sleepRandom() function

The aforementioned account information was retrieved from the file *aws.txt*, which was included within the “recovery package” alongside the recovery binary. Below is a mockup version of the file:

```
$ cat aws.txt
Account Information:
{
    "UserId": "AIDAZ",
    "Account": "6810",
    "Arn": "arn:aws:iam::6810:user/malmoeb"
}

Buckets for the user with access key 2345:
2022-09-02 18:55:18 dfir

Folder Names:
dfir

Folder: dfir
Number of files: 240
Total size (GB): 5.00 GB

Total number of files: 240
```

Here is an excerpt from the strace output, showing the process of reading the aws.txt file ([openat()](https://linux.die.net/man/2/openat) followed by [read()](https://linux.die.net/man/3/read)):

```
openat(AT_FDCWD, "aws.txt", O_RDONLY)   = 3
fstat(3, {st_mode=S_IFREG|0664, st_size=355, ...}) = 0
read(3, "Account Information:\n{\n    \"User"..., 4096) = 355
clock_nanosleep(CLOCK_REALTIME, 0, {tv_sec=2, tv_nsec=0}, 0x7ffeb42cb290) = 0
write(1, "Account Information:\n", 21)  = 21
[...]
```

The binary generates a new directory ([mkdir](https://linux.die.net/man/2/mkdir)) and places randomly named files within it. The [openat()](https://linux.die.net/man/2/openat) syscall is used again, but this time, unlike above, the parameter *O\_CREAT* is passed to the function - *If pathname does not exist, create it as a regular file.*

```
mkdir("dfir", 0777)                     = 0
clock_nanosleep(CLOCK_REALTIME, 0, {tv_sec=0, tv_nsec=738335000}, NULL) = 0
chdir("dfir")                           = 0
openat(AT_FDCWD, "recoveryqbhcdarzow.bkp", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 4
close(4)                                = 0
openat(AT_FDCWD, "recoverykkyhiddqsc.bkp", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 4
close(4)                                = 0
[...