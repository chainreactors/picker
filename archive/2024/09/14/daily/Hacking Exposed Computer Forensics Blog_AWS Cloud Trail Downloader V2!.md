---
title: AWS Cloud Trail Downloader V2!
url: https://www.hecfblog.com/2024/09/aws-cloud-trail-downloader-v2.html
source: Hacking Exposed Computer Forensics Blog
date: 2024-09-14
fetch_date: 2025-10-06T18:30:07.406026
---

# AWS Cloud Trail Downloader V2!

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)
Unlabelled
AWS Cloud Trail Downloader V2!

# AWS Cloud Trail Downloader V2!

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
September 12, 2024
•

•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYcPyab0cNomPnJqUbEohGO7jtweSoVM0UdDr5pJtUQsutFDTkRRbstpnXQ0gmEmvNUjatRI6VkP_DEt6es8WyKqQv_GG9hL6Xk1DR2o9tI0efqkOaZ3G9YQv53D1GO2YmP5aE2ehDg8arRVyZXTTuJc2379C5UkGk1m5QesJGKHzRTC-M_xhk2pj_QYQ/w640-h640/blogtitle.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYcPyab0cNomPnJqUbEohGO7jtweSoVM0UdDr5pJtUQsutFDTkRRbstpnXQ0gmEmvNUjatRI6VkP_DEt6es8WyKqQv_GG9hL6Xk1DR2o9tI0efqkOaZ3G9YQv53D1GO2YmP5aE2ehDg8arRVyZXTTuJc2379C5UkGk1m5QesJGKHzRTC-M_xhk2pj_QYQ/s1024/blogtitle.png)

Hello Reader,

      Time to dust the cobwebs off the blog! It's been a busy two years since I've joined Charles River Associates and I have so much to share. I'm restarting the blog with what I think is a pretty big update to the AWS Cloud Trail log download script I wrote for FOR509. I wrote the first one when a student asked if there was a script or a tool I could point to that would download Cloud Trail logs from the default AWS storage location. I spent the night solving the issue and then made multiple changes over that year making it more useful and stable, even using it myself many times!

Now for those not familiar with the issue this solves, let me explain. If you have an AWS account and you have not setup Cloud Trail (the default AWS audit log) to store logs in an S3 bucket then there is a default log storage location where AWS stores 90 days of audit events. However, you can't just access the default log storage like any other S3 bucket, instead you have to make calls into the Cloud Trail API to request them, 50 events at a time. Also important is that every region has its own bucket of logs.

So what the script originally did was use multiprocessing to launch a process per region to download the logs stored for it and then a curses interface to update the command line on how many events it has downloaded. However I knew there were more features I wanted to add. Here is a list of the new feature I've added.

**New Features**

1. **Output Directory:** You can now tell the script where to write out the logs and the resume tokens.Previously it would just write to the directory you ran the script from.
2. **Auto -Resume:** If for whatever reason the script failed ( the machine restarted,your hotel WiFi required a new session, etc...) if you run the script with the same output directory it will automatically resume from where it left off and not re-download any region already complete. It even keeps track of how many events were already downloaded so the counts stay accurate. In addition it will display up top that it has resumed and the total run time of the current execution.
3. **Windows/Linux/Mac Support**: The script now determines if you are running from Windows or not to use the appropriate libraries and calls so the script can run on any platform.
4. **Auto-removal of resume token**s: Once you have completely downloaded all the regions the program will delete the resume tokens and exit. This prevents any accidental resumes in the future.
5. **Support for AWS CLI profiles**: Previously the script required an API key to be passed into it. Now you can choose to either pass in a profile in your .aws/credentials file or a key in the command line arguments.
6. **Better cleanup on exit:** Previously if you tried to quit using the curses interface the python threads would hang. It now exits cleanly and kills all children.
7. **Better curses formatting**: When a region finishes its marked DONE in bold and clears all prior input there.
8. **Additional code commenting**: If you are attempting to read through the script for your own learning there are now additional code comments to explain whats going on.

Download the new script here: <https://raw.githubusercontent.com/dlcowen/sansfor509/main/AWS/Cloudtrail_downloadv2.py>

### Error Handling and Cleanup

The script also comes with improved error handling. For example, if a resume token file becomes corrupted or empty, the script won’t crash. Instead, it will handle these cases gracefully, ensuring the process continues uninterrupted.

Now, let’s walk through the system requirements, how to set up the environment, and how to execute the script.

### Requirements

To use the updated AWS CloudTrail Log Downloader, you’ll need the following:

* **Python 3.6+**: The script is written in Python, so having a working Python environment is required.
* **AWS CLI / Boto3**: You’ll need to install `boto3`, AWS’s SDK for Python, which the script uses to interact with AWS CloudTrail and manage sessions.
* **Curses Module**: The `curses` library provides the real-time interface. If you’re using Windows, you may need to install the `windows-curses` package.

To install the required dependencies on windows, run:

**pip install boto3 windows-curses**

For Linux/macOS, the curses library comes pre-installed, so you won’t need the windows-curses package.

**AWS Credentials**

To authenticate, the script will use your AWS credentials. These can be configured in one of two ways:

**AWS CLI credentials**

If you’ve configured AWS credentials using aws configure, the script will use these credentials automatically.

**Providing credentials directly via arguments**

You can pass your AWS Access Key, Secret Key, and Session Token directly when executing the script.

### How to Use the Script

Here’s a step-by-step guide on how to run the AWS CloudTrail Log Downloader.

**1. Clone the Repository or Save the Script**

First, clone the repository where the script is hosted or save the Python file to your local machine.

**2. Set Up Your AWS Environment**

Make sure your AWS environment is configured by running aws configure if you haven’t done so already. You can skip this step if you’re passing credentials directly through the script.

**3. Execute the Script**

You can run the script with the following command:

**python cloudtrail\_download.py --profile <profile name here> --output-directory /path/to/logs**

**Command-Line Arguments:**

**--access-key-id and --secret-key**: These are optional if your AWS credentials are configured in your environment.

**--profile**: Use this to specify the AWS CLI profile if you have multiple profiles.

**--output-directory**: Specify the directory where you want the CloudTrail logs to be saved.

If you prefer to pass AWS credentials directly, use:

**python cloudtrail\_download.py --access-key-id <YOUR\_AWS\_ACCESS\_KEY> --secret-key <YOUR\_AWS\_SECRET\_KEY> --output-directory /path/to/logs**

**4. Monitor the Progress**

Once the script is running, you’ll see a real-time UI with the progress of the log download for each AWS region. It will disp...