import os

base_dir = os.path.dirname(os.path.abspath(__file__))  # Use your current local folder

projects = {
    "Azure Policy Library": "azure-policy-library",
    "KQL Workbook Monitoring": "kql-workbook-monitoring",
    "SQL LRS Backup Migration": "sql-lrs-backup-migration",
    "Enable AHUB for VMs": "enable-ahub-vms",
    "Storage Account Owner Check": "storage-owner-check",
    "Change Backup Redundancy to LRS": "change-backup-lrs",
    "Terraform Automation": "terraform-automation",
    "CI/CD In Progress": "cicd-in-progress"
}

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
            <a href="../index.html">← Back to Portfolio</a>
        </section>
    </main>
</body>
</html>"""

for title, folder_name in projects.items():
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    with open(os.path.join(folder_path, "index.html"), "w") as f:
        f.write(html_template.format(title=title))
