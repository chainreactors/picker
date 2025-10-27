---
title: Unsafe Archive Unpacking: Labs and Semgrep Rules
url: https://blog.doyensec.com/2024/12/16/unsafe-unpacking.html
source: Over Security - Cybersecurity news aggregator
date: 2024-12-17
fetch_date: 2025-10-06T19:41:22.974875
---

# Unsafe Archive Unpacking: Labs and Semgrep Rules

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# Unsafe Archive Unpacking: Labs and Semgrep Rules

16 Dec 2024 - Posted by Michael Pastor

## Introduction

During my recent internship with Doyensec, I had the opportunity to research **decompression attacks** across different programming languages. As the use of archive file formats is widespread in software development, it is crucial for developers to understand the potential security risks involved in handling these files.

The objective of my research was to identify, analyze, and detect vulnerable implementations in several popular programming languages used for web and app development, including Python, Ruby, Swift, Java, PHP, and JavaScript. These languages have libraries for archive decompression that, when used improperly, may potentially lead to vulnerabilities.

To demonstrate the risk of unsafe unpacking, I created proof-of-concept (PoC) code with different vulnerable implementations for each method and each language. My work also focused on safe alternatives for each one of the vulnerable implementations. Additionally, I created a web application to upload and test whether the code used in a specific implementation is safe or not.

To efficiently search for vulnerabilities on larger codebases, I used a popular SAST (Static Application Security Testing) tool - [Semgrep](https://semgrep.dev/index.html). Specifically, I wrote a set of rules to automatically detect those vulnerable implementations which it will make it easier to identify vulnerabilities.

**Secure and insecure code, labs and Semgrep rules for all programming languages have been published on** <https://github.com/doyensec/Unsafe-Unpacking>.

## Understanding Archive Path Traversal

Extracting an archive (e.g., a ZIP file) usually involves reading all its contents and writing them to the specified extraction path. An archive path traversal aims to extract files to directories that are outside the intended extraction path.

This can occur when archive extraction is improperly handled, as archives may contain files with filenames referencing parent directories (e.g., using `../`). If not properly checked, these sequences may cause the extraction to occur outside the intended directory.

For example, consider a ZIP file with the following structure:

```
/malicious
    /foo.txt
    /foo.py
    /../imbad.txt
```

When unzipping the archive to `/home/output`, if the extraction method does not validate or sanitize the file paths, the contents may be written to the following locations:

```
/home/output/foo.txt
/home/output/foo.py
/home/imbad.txt
```

As a result, `imbad.txt` would be written outside the intended directory. If the vulnerable program runs with high privileges, this could also allow the attacker to overwrite sensitive files, such as `/etc/passwd` â where Unix-based systems store user account information.

## Proving the Concept: Code Examples

To demonstrate the vulnerability, I created several proof-of-concept examples in various programming languages. These code snippets showcase vulnerable implementations where the archive extraction is improperly handled.

### Python

The combination of the `ZipFile` library as reader and `shutil.copyfileobj()` as writer makes the programmer responsible for handling the extraction correctly.

The usage of `shutil.copyfileobj()` is straightforward: as the first argument, we pass the file descriptor of the file whose contents we want to extract, and as the second argument, we pass the file descriptor to the destination file. Since the method receives file descriptors instead of paths, it doesnât know if the path is out of the output directory, making the following implementation vulnerable.

```
def unzip(file_name, output):
    # bad
    with zipfile.ZipFile(file_name, 'r') as zf:
        for filename in zf.namelist():
            # Output
            output_path = os.path.join(output, filename)
            with zf.open(filename) as source:
                with open(output_path, 'wb') as destination:
                    shutil.copyfileobj(source, destination)

unzip1(./payloads/payload.zip", "./test_case")
```

If we run the previous code, weâll realize that instead of extracting the zip content (`poc.txt`) to the `test_case` folder, it will be extracted to the parent folder:

```
$ python3 zipfile_shutil.py

$ ls test_case
# No output, empty folder

$ ls
payloads  poc.txt  test_case  zipfile_shutil.py
```

### Ruby

```
Zip::File.open(file_name).extract(entry, file_path)
```

The `extract()` method in Rubyâs `zip` library is used to extract an entry from the archive to the `file_path` directory. This method is unsafe since it doesnât remove redundant dots and path separators. Itâs the callerâs responsibility to make sure that `file_path` is safe:

```
require 'zip'

def unzip1(file_name, file_path)
  # bad
  Zip::File.open(file_name) do |zip_file|
    zip_file.each do |entry|
      extraction_path = File.join(file_path, entry.name)
      FileUtils.mkdir_p(File.dirname(extraction_path))
      zip_file.extract(entry, extraction_path)
    end
  end
end

unzip1('./payloads/payload.zip', './test_case/')
```

```
$ ruby zip_unsafe.rb

$ ls test_case
# No output, empty folder

$ ls
payloads  poc.txt  test_case  zip_unsafe.rb
```

### PHP, Swift, JS and Java

All the other cases are documented in Doyensecâs [repository](https://github.com/doyensec/unsafe-Unpacking), along with the Semgrep rules and the labs.

## Unsafe Unpacking Labs

As part of the research, I developed a few web applications that allow users to test whether specific archive extraction implementations are vulnerable to decompression attacks.

![Class Pollution Gadgets](../../../public/images/unsafe-unpacking-lab-1.png)

* **RUN**: without uploading an archive, the application will extract one of the prebuilt malicious archives. If the user uploads an archive, that archive will be unpacked instead.
* **Clear TXT Files**: the application will remove all the extracted files from the previous archives.
* **Fetch Directory Contents**: the web application will show you both the `archive directory` (where files are supposed to be extracted) and the `current directory` (where files are NOT supposed to be extracted).

![Class Pollution Gadgets](../../../public/images/unsafe-unpacking-lab-2.png)

These web application labs are available for every language except Swift, for which a desktop application is provided instead.

## Developing Semgrep Rules for Vulnerability Detection

One of the most efficient ways to detect vulnerabilities in open-source projects is by using static application analysis tools. Semgrep is a fast, open-source, static analysis tool that searches code, finds bugs, and enforces secure guardrails and coding standards.

Semgrep works by scanning source code for specific syntax patterns. Since it supports various programming languages and makes it simple to write custom rules, it was ideal for my research purposes.

In the following example Iâm using the `Unsafe-Unpacking/Python/PoC/src` folder from the GitHub repository, which contains 5 unzipping vulnerabilities. You can run the Semgrep rule by using the following command:

```
semgrep scan --config=../../rules/zip_shutil_python.yaml

...

âââââââââââââââââââ
â 5 Code Findings â
âââââââââââââââââââ

    zipfile_shutil.py
   â¯â¯â± rules.unsafe_unpacking
          Un...