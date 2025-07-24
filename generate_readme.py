import os

HEADER = """# 🧠 LeetCode Solutions by Dirshaye

Auto-generated list of my LeetCode progress. Organized by folder.

---

"""

def get_problem_title(file_name):
    # Example: "238-product_except_self.py" -> "238. Product Except Self"
    base = os.path.splitext(file_name)[0]
    if '-' in base:
        parts = base.split('-', 1)
        number = parts[0]
        title = parts[1].replace('_', ' ').title()
        return f"{number}. {title}"
    else:
        return base.replace('_', ' ').title()

def generate_readme(base_path='.'):
    lines = [HEADER]

    for root, dirs, files in os.walk(base_path):
        if root == ".":
            continue

        folder_name = os.path.basename(root)
        lines.append(f"## 📂 {folder_name}\n")

        for f in sorted(files):
            if f.endswith(('.py', '.sql')):
                problem_title = get_problem_title(f)
                relative_path = os.path.join(root, f).replace(" ", "%20")
                link = f"[{problem_title}]({relative_path})"
                lines.append(f"- {link}")

        lines.append("")

    with open("README.md", "w", encoding='utf-8') as f:
        f.write("\n".join(lines))

    print("✅ README.md updated successfully.")

# Run the function
if __name__ == "__main__":
    generate_readme()
