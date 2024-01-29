#!C:\Users\Tyupala\AppData\Local\Microsoft\WindowsApps\python3.11.exe
import os
import cgi
import subprocess
# Enable debugging
import cgitb
cgitb.enable()
process = 1

# Set the content type to HTML
print("Content-type: text/html\n")
# Retrieve form data
form = cgi.FieldStorage()
uploaded_file = form["file"]
file_name = uploaded_file.filename
action = form.getvalue('action')

# Save uploaded file temporarily
with open(f"{file_name}", "wb") as f:
    f.write(uploaded_file.file.read())
file_path = os.path.abspath(file_name)

print("<!DOCTYPE html>")
print("<html0>")
print("<head>")
print("<title>Shortcut CGI Script</title>")
print("</head>")
print("<body>")
print("<h2>Form Submission Result:</h2>")

print(f"<h1>file has been uploaded: {file_path}</h1>")
print(f"<h1>action: {action}</h1>")

#subprocess.run(["Source.exe", file_name, action])
subprocess.run(["Source.exe"])
#if action is "e":
#    os.remove(file_path)
print("</body>")
print("</html>")