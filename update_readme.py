import os
import re
from datetime import datetime

# Configuration
REPO_ROOT = os.getcwd()
README_PATH = os.path.join(REPO_ROOT, "README.md")
SOLUTIONS_DIRS = [d for d in os.listdir(REPO_ROOT) if os.path.isdir(d) and not d.startswith(".")]

# XP Mapping
XP_MAP = {
    "Easy": 10,
    "Medium": 30,
    "Hard": 50
}

def extract_metadata(file_path):
    metadata = {
        "difficulty": "Unknown",
        "topic": "Unknown",
        "problem_link": "#",
        "problem_name": os.path.basename(file_path)
    }
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Simple regex to find metadata in comments
            diff_match = re.search(r"#\s*Difficulty:\s*(Easy|Medium|Hard)", content, re.I)
            topic_match = re.search(r"#\s*Topic:\s*(.*)", content, re.I)
            link_match = re.search(r"#\s*Problem:\s*(.*)", content, re.I)
            
            if diff_match:
                metadata["difficulty"] = diff_match.group(1).capitalize()
            if topic_match:
                metadata["topic"] = topic_match.group(1).strip()
            if link_match:
                metadata["problem_link"] = link_match.group(1).strip()
                
            # Try to get problem name from filename (e.g., 0001-Two-Sum.py -> Two Sum)
            name_match = re.match(r"\d+-(.*)\.py", os.path.basename(file_path))
            if name_match:
                metadata["problem_name"] = name_match.group(1).replace("-", " ")
                
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        
    return metadata

def generate_table_row(day, date, metadata, file_rel_path):
    diff_icon = "🟢" if metadata["difficulty"] == "Easy" else "🟡" if metadata["difficulty"] == "Medium" else "🔴" if metadata["difficulty"] == "Hard" else "⚪"
    xp = XP_MAP.get(metadata["difficulty"], 0)
    
    return f"| **{day}** | `{date}` | [{metadata['problem_name']}]({metadata['problem_link']}) | {diff_icon} | {metadata['topic']} | [`Solution`]({file_rel_path}) | ✅ | `+{xp}` |"

def update_readme():
    solutions = []
    
    # Walk through solution directories
    for root, dirs, files in os.walk(REPO_ROOT):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        
        for file in files:
            if file.endswith(".py") and file != "update_readme.py":
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, REPO_ROOT).replace("\\", "/")
                
                # Get file modification time for date (fallback to current date if needed)
                date = datetime.fromtimestamp(os.path.getmtime(full_path)).strftime("%Y-%m-%d")
                
                metadata = extract_metadata(full_path)
                solutions.append((date, metadata, rel_path))
                
    # Sort solutions by date
    solutions.sort(key=lambda x: x[0])
    
    total_xp = sum(XP_MAP.get(s[1]["difficulty"], 0) for s in solutions)
    
    # Generate table content
    table_rows = []
    for i, (date, metadata, rel_path) in enumerate(solutions, 1):
        table_rows.append(generate_table_row(i, date, metadata, rel_path))
        
    table_content = "\n".join(table_rows)
    
    # Read current README
    if not os.path.exists(README_PATH):
        print("README.md not found!")
        return
        
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()
        
    # Update XP section
    # Look for the XP table and replace it or just update the XP values if possible
    # For simplicity, we'll use markers in the README to inject content
    
    # 1. Update Daily Progress Log Table
    table_start_marker = "## 📅 Daily Problem Log (Recent)"
    table_header = "| Day | Date | Problem Card | Diff | Topic / Pattern | Code | Status | XP |"
    table_separator = "|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|"
    
    # Construct the new table section
    new_table_section = f"{table_start_marker}\n*(Detailed tracking of my daily solutions, categorized by their core pattern)*\n\n{table_header}\n{table_separator}\n{table_content}\n"
    
    # Replace the section between the marker and the next horizontal rule or header
    # We use a non-greedy match that stops at the next --- or ##
    pattern = rf"{re.escape(table_start_marker)}.*?(?=\n---|\n##|\Z)"
    updated_content = re.sub(pattern, new_table_section, readme_content, flags=re.DOTALL)
    
    # No need to manually update Level markers for now as they are static milestones
    
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)
        
    print(f"Successfully updated README.md with {len(solutions)} problems and {total_xp} total XP.")

if __name__ == "__main__":
    update_readme()
