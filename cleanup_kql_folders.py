import os
import shutil
import re

# Function to slugify titles into folder-friendly names (must match creation script)
def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text

# Base directory (where this script lives / project root)
base_dir = os.getcwd()

# Same categories dict used to create the folders
categories = {
    "sql-databases": [
        "Failed RSV backups for SQL databases",
        "Restored SQL Databases",
        "SQL Backups with Protection Stopped",
        "SQL Databases Not Using LRS Backup",
        "SQL IaaS Backups without Protected Data Sources",
        "Soft-Deleted SQL Backups"
    ],
    "storage-accounts": [
        "Non-V2 Storage Accounts",
        "Storage Accounts Not LRS",
        "Storage Accounts with Public Access"
    ],
    "unused-resources": [
        "Empty Resource Groups",
        "Stale Disk Snapshots",
        "Test Resource Groups",
        "Unattached Disks",
        "Unattached NICs",
        "Unused Public IPs"
    ],
    "virtual-machines": [
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
}

deleted_count = 0
removed_categories = 0

for category, titles in categories.items():
    category_path = os.path.join(base_dir, category)
    if not os.path.isdir(category_path):
        continue

    # Remove each query subfolder
    for title in titles:
        folder_name = slugify(title)
        folder_path = os.path.join(category_path, folder_name)
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            deleted_count += 1
            print(f"Deleted folder: {folder_path}")

    # If the category folder is now empty, remove it as well
    try:
        if not os.listdir(category_path):
            os.rmdir(category_path)
            removed_categories += 1
            print(f"Removed empty category folder: {category_path}")
    except OSError as e:
        print(f"Could not remove {category_path}: {e}")

print(f"\nDeleted {deleted_count} query folders.")
print(f"Removed {removed_categories} empty category folders.")
