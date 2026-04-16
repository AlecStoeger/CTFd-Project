# CS 4460 Final Project – CTF Server

## Overview

For this project, we developed a custom Capture The Flag (CTF) environment using CTFd. The goal was to create a series of cybersecurity challenges that simulate real-world scenarios across multiple domains including web security, digital forensics, and network analysis.

Our challenges are based on investigating digital evidence and uncovering hidden information, similar to real cybersecurity investigations.

---

## Challenge 1: Warmup

**Category:** Misc

**Description:**
A simple introductory challenge where the flag is directly provided to familiarize users with the CTF platform.

**Implementation:**
We created a basic text-based challenge with a visible flag.

**Solution:**
The flag is directly visible in the description:

```
flag{welcome_to_ctf}
```

---

## Challenge 2: Source Code Analysis

**Category:** Web

**Description:**
Players are given an HTML file and must inspect the source code to find hidden information.

**Implementation:**
We embedded the flag inside an HTML comment in the file:

```html
<!-- flag{view_source_to_find_me} -->
```

**Solution:**
Open the file and view source (Ctrl+U or Cmd+Option+U).
The flag is inside the comment.

---

## Challenge 3: Image Hidden Data

**Category:** Forensics

**Description:**
An image appears normal but contains hidden data.

**Implementation:**
We appended the flag to the end of the image file:

```bash
echo "flag{strings_can_find_hidden_data}" >> dr404.jpg
```

**Solution:**
Run:

```bash
strings dr404.jpg | grep flag
```

---

## Challenge 4: Network Breach (PCAP Analysis)

**Category:** Forensics / Network

**Description:**
Players analyze a packet capture file to find sensitive data.

**Implementation:**
We generated HTTP traffic containing the flag in a query string within the PCAP file.

**Solution:**

1. Open in Wireshark
2. Filter:

```
http
```

3. Follow HTTP stream
4. Locate flag:

```
flag{packets_tell_stories}
```

---

## Challenge 5: Email Metadata (OSINT)

**Category:** Forensics

**Description:**
Players analyze an intercepted email file to uncover hidden metadata.

**Implementation:**
We provided a `.eml` file with embedded metadata and clues.

**Solution:**
Use tools like:

```bash
exiftool intercepted.eml
```

Look for hidden fields or clues revealing the flag.

---

## Challenge 6: SQL Injection

**Category:** Web Exploitation

**Description:**
Players interact with a vulnerable web application and must bypass login authentication.

**Implementation:**
We created a Flask web application with an insecure SQL query:

```python
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
```

This allows SQL injection attacks.

**Solution:**
Enter:

```
' OR '1'='1
```

This bypasses authentication and reveals the flag.

---

## Challenges Faced

* Difficulty installing steganography tools on macOS
* Learning Docker for deployment
* Designing challenges that were solvable but still realistic

---

## Conclusion

This project provided hands-on experience with cybersecurity concepts including web vulnerabilities, network analysis, and digital forensics. By building and solving challenges, we gained a deeper understanding of how vulnerabilities are created and exploited in real-world systems.

---
