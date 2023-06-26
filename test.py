import subprocess

wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
data = wifi.decode('unicode_escape')
symbols = ['1', '2', '3', '4', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = ""
for d in data:
    if d.lower() in symbols or d == " ":
        text += d
print(text.strip())