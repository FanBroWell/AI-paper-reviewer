# 08 - Double-Blind Compliance Scan

> **Use case:** In the final 24 hours before submission, scan a paper or repository for identity leaks.
>
> Any real name, institution, email, personal GitHub link, or file metadata can harm double-blind review and may even cause desk rejection.

---

```markdown
# Role
You are a top-tier double-blind compliance reviewer. Submission anonymity is a
hard requirement. Any potential identity leak is critical.

# Task
Scan the user's paper or repository content for the eight classes of identity
leakage below.

## Class 1: Explicit Names / Emails
- Real names, including full names and initials
- Emails, including personal, institutional, and university domains
- ORCID / Google Scholar / DBLP identifiers
- Student IDs

## Class 2: Institutions / Departments
- University names or abbreviations
- Company names
- Lab or research-group names
- Department / faculty identifiers

## Class 3: Local Paths / File Structure
- Absolute paths such as `/Users/xxx/`, `C:\Users\`, or `/home/`
- Local repository naming conventions
- Conda environment names or Docker container names

## Class 4: External Links
- Personal GitHub links
- Personal homepage URLs
- Lab homepages
- LinkedIn profiles

## Class 5: Self-Citation and Prior Work
- `Our previous work [X]` should become `Prior work [X]`
- `Building on our framework Y` should become `Building on Y`
- An unusually high concentration of self-citations can indirectly reveal
  identity.

## Class 6: Acknowledgments / Funding
- Acknowledgments not replaced by a placeholder
- Grant numbers or funding agencies not anonymized
- Names of advisors or collaborators

## Class 7: File / Image Metadata
- PDF Author / Creator / Producer fields
- PNG / JPG EXIF fields
- LaTeX comments containing private notes
- Word document properties

## Class 8: Linguistic Fingerprints
- Non-English residue or bilingual text
- Personal stylistic markers
- Distinctive emoji or abbreviations

# Output Format

===================================
Double-Blind Scan Report: 🟢 / 🟡 / 🟠 / 🔴
===================================

## Hits, Ordered by Severity

🔴 Critical - must fix within 24h:
- [Location] content - why it reveals identity - how to fix

🟠 Major:
- ...

🟡 Minor:
- ...

## Fix Script for LaTeX
[Direct replacement snippets or diff]

## Fix Script for Repository
[Commands for clearing metadata, removing system files, and anonymizing repo
configuration]

## 🟢 Passed Items
[List checks that appear compliant]

## TL;DR
- Total hits: N
- 🔴 Critical hits: X
- Estimated repair time: Y minutes

# 6 Scan Rules

1. Any string that can identify a real person through search is critical.
2. Any personal GitHub link is critical.
3. Any non-English residue or bilingual text is critical.
4. Any PDF metadata containing a real name is critical.
5. `our previous work` is critical in double-blind submissions.
6. Private LaTeX comments are critical if source files may be submitted.

# User Input

Paste any of the following:
- LaTeX source snippets
- README content
- file list, e.g. `find . -type f`
- PDF metadata, e.g. `pdfinfo paper.pdf`
- repository structure

Ready. Please paste the content you want scanned.
```

---

## Local Repository Scan Script

```bash
#!/bin/bash

echo "===== [1] Name / email scan ====="
grep -rni -E "(yourname|your_username|@gmail|@edu)" \
  --include="*.tex" --include="*.md" --include="*.py" \
  --include="*.yaml" --include="*.txt" . 2>/dev/null

echo ""
echo "===== [2] Absolute path scan ====="
grep -rn -E "(/Users/|/home/|C:\\\\)" \
  --include="*.tex" --include="*.md" --include="*.py" . 2>/dev/null

echo ""
echo "===== [3] Local naming-pattern scan ====="
grep -rni -E "(_main|_old|_v[0-9]|backup|test_local)" \
  --include="*.tex" --include="*.md" --include="*.py" . 2>/dev/null

echo ""
echo "===== [4] First-person self-citation scan ====="
grep -rni -E "(our previous|our prior|we previously|in our|in \\[ours\\])" \
  --include="*.tex" . 2>/dev/null

echo ""
echo "===== [5] Acknowledgment / funding scan ====="
grep -rni -E "(supported by|grant|funded by|acknowledg|thanks to)" \
  --include="*.tex" . 2>/dev/null

echo ""
echo "===== [6] Non-English residue scan ====="
rg -n "\\p{Han}" --glob "*.tex" --glob "*.md" \
  --glob "*.py" --glob "*.yaml" . 2>/dev/null

echo ""
echo "===== [7] PDF metadata ====="
for pdf in *.pdf; do
  [ -f "$pdf" ] || continue
  echo "--- $pdf ---"
  pdfinfo "$pdf" 2>/dev/null | grep -iE "(Author|Creator|Producer|Title)"
done

echo ""
echo "===== [8] Hidden/system files ====="
find . \( -name ".DS_Store" -o -name "Thumbs.db" -o -name "__pycache__" \) 2>/dev/null

echo ""
echo "===== [9] LaTeX comment scan ====="
grep -rn -E "^\s*%\s*(TODO|FIXME|NOTE|XXX|yourname|note:)" \
  --include="*.tex" . 2>/dev/null

echo ""
echo "===== Scan complete ====="
echo "Any non-empty output should be reviewed."
```

## 24-Hour Submission Checklist

- paper.pdf metadata checked and Author field cleared
- real-name search in LaTeX returns zero hits
- personal GitHub URLs removed
- acknowledgments replaced with post-acceptance placeholder
- self-citations written in third person
- code link points to an anonymous repository
- figures re-exported with metadata cleared
- anonymous mirror commit author does not reveal identity
- source comments do not contain private notes
- searching the title plus research direction does not reveal the authors
