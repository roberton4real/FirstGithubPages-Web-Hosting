import os
import re

# Function to slugify titles into folder-friendly names
def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text

# Base directory (current working directory)
base_dir = os.getcwd()

# List of query titles from your HTML links
queries = [
    # SQL Databases
    "Failed RSV backups for SQL databases",
    "Restored SQL Databases",
    "SQL Backups with Protection Stopped",
    "SQL Databases Not Using LRS Backup",
    "SQL IaaS Backups without Protected Data Sources",
    "Soft-Deleted SQL Backups",
    # Storage Accounts
    "Non-V2 Storage Accounts",
    "Storage Accounts Not LRS",
    "Storage Accounts with Public Access",
    # Unused Resources
    "Empty Resource Groups",
    "Stale Disk Snapshots",
    "Test Resource Groups",
    "Unattached Disks",
    "Unattached NICs",
    "Unused Public IPs",
    # Virtual Machines
    "Azure VM Backups in a RSV that are Soft-Deleted",
    "Azure VM Backups in a RSV with Protection Stopped",
    "Azure VM Backups in a RSV with no Source VM",
    "Azure VMs Not Utilizing AHUB",
    "Azure VMs that are Deallocated",
    "Azure VMs that are Stopped (not Deallocated)",
    "Azure VMs without RSV Backups",
    "Failed RSV backups for VMs",
    "Linux VMs with AHUB enabled",
    "Recovery Services Vault MUA & Guard Compliance Dashboard",
    "Windows VMs without AHUB enabled"
]

# HTML template for each project page
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="../assets/css/styles.css">
</head>
<body>
    <main class="main">
        <section class="section">
            <h1>{title}</h1>
            <p>This is the project page for <strong>{title}</strong>. Customize this content as needed.</p>
            <a href="../index.html">← Back to Workbook</a>
        </section>
    </main>
</body>
</html>"""

# Create a folder and index.html for each query
for title in queries:
    folder_name = slugify(title)
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_template.format(title=title))

print("Folders and internal pages created for all queries: {}".format(len(queries)))
