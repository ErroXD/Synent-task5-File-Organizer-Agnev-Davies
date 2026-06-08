# 🗂️ File Organizer

A Python script that automatically sorts files in any folder into clean sub-directories by file type — no setup, no dependencies, just Python.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Supported File Types](#supported-file-types)
- [How It Works](#how-it-works)
- [Example](#example)
- [Adding New Categories](#adding-new-categories)
- [Edge Cases Handled](#edge-cases-handled)

---

## Overview

Messy Downloads folder? Desktop full of random files? File Organizer scans any directory you point it at, detects each file's type by its extension, creates the right sub-folder automatically, and moves every file into its place — all in seconds.

---

## Features

- Sorts files into **7 categories**: Images, Videos, Docs, Audio, Archives, Code, Others
- **Auto-creates folders** — no need to make them yourself
- **Safe by default** — skips files that already exist at the destination instead of overwriting
- **Cross-platform** — works on Windows, macOS, and Linux
- **Zero dependencies** — uses only Python's built-in `os` and `shutil` modules
- Prints a clean summary showing how many files were moved or skipped

---

## Project Structure

```
file-organizer/
│
├── file_organizer.py   # Main script
└── README.md           # This file
```

---

## Requirements

- Python **3.6 or higher**
- No third-party packages needed

Check your Python version:

```bash
python --version
```

---

## How to Run

**1. Clone or download the script**

```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```

**2. Run the script**

```bash
python file_organizer.py
```

**3. Enter the folder path when prompted**

```
=========================================
       🗂  FILE ORGANIZER v1.0
=========================================

Enter the full path of the folder to organise:
> /home/yourname/Downloads
```

**Windows path example:**

```
> C:\Users\YourName\Downloads
```

---

## Supported File Types

| Folder    | Extensions                                              |
|-----------|---------------------------------------------------------|
| Images    | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` `.webp` `.ico` `.tiff` |
| Videos    | `.mp4` `.mov` `.avi` `.mkv` `.wmv` `.flv` `.webm` `.m4v` |
| Docs      | `.pdf` `.doc` `.docx` `.xls` `.xlsx` `.ppt` `.pptx` `.txt` `.csv` `.odt` |
| Audio     | `.mp3` `.wav` `.aac` `.flac` `.ogg` `.m4a` `.wma`      |
| Archives  | `.zip` `.rar` `.tar` `.gz` `.7z` `.bz2`                |
| Code      | `.py` `.js` `.html` `.css` `.java` `.cpp` `.c` `.ts` `.json` `.xml` `.sh` |
| Others    | Anything not matched above                              |

---

## How It Works

```
Your folder
│
├── photo.jpg        ──►  Images/photo.jpg
├── report.pdf       ──►  Docs/report.pdf
├── song.mp3         ──►  Audio/song.mp3
├── archive.zip      ──►  Archives/archive.zip
├── script.py        ──►  Code/script.py
└── mystery.xyz      ──►  Others/mystery.xyz
```

Internally, the script follows these steps:

1. **Validate** the folder path exists
2. **List** every item in the folder with `os.listdir()`
3. **Skip** sub-directories (only files are moved)
4. **Detect** the category by matching the file extension against `FILE_CATEGORIES`
5. **Create** the destination folder with `os.makedirs(exist_ok=True)` if it doesn't exist
6. **Check** the destination doesn't already have a file with the same name
7. **Move** the file with `shutil.move()`
8. **Print** a final summary

---

## Example

**Before:**

```
Downloads/
├── holiday.png
├── resume.pdf
├── project.zip
├── notes.txt
├── clip.mp4
└── setup.exe
```

**After running File Organizer:**

```
Downloads/
├── Images/
│   └── holiday.png
├── Docs/
│   ├── resume.pdf
│   └── notes.txt
├── Archives/
│   └── project.zip
├── Videos/
│   └── clip.mp4
└── Others/
    └── setup.exe
```

**Terminal output:**

```
📂 Organising: /home/yourname/Downloads
─────────────────────────────────────────────
  ✅  holiday.png                       →  Images/
  ✅  resume.pdf                        →  Docs/
  ✅  project.zip                       →  Archives/
  ✅  notes.txt                         →  Docs/
  ✅  clip.mp4                          →  Videos/
  ✅  setup.exe                         →  Others/

─────────────────────────────────────────────
  Done!  Moved: 6 file(s)   Skipped: 0 file(s)
─────────────────────────────────────────────
```

---

## Adding New Categories

Open `file_organizer.py` and find the `FILE_CATEGORIES` dictionary near the top. Add a new key with a list of extensions:

```python
FILE_CATEGORIES = {
    "Images":    [".jpg", ".jpeg", ".png", ...],
    "Videos":    [".mp4", ".mov", ...],
    # Add your new category here:
    "Fonts":     [".ttf", ".otf", ".woff", ".woff2"],
    ...
}
```

Save the file and re-run — the new folder will be created automatically the next time the script runs.

---

## Edge Cases Handled

| Situation | Behaviour |
|-----------|-----------|
| Path does not exist | Prints an error and exits safely |
| Destination file already exists | Skips the file and prints a warning |
| Item is a folder, not a file | Silently skipped (only files are moved) |
| Extension is uppercase (e.g. `.JPG`) | Normalised to lowercase before matching |
| File has no extension | Moved to `Others/` |

---

## Modules Used

| Module | Purpose |
|--------|---------|
| `os` | List directory contents, build paths, check existence, create folders |
| `shutil` | Move files safely (works across drives and partitions) |

Both are part of Python's standard library — nothing to install.

---

## License

This project is for educational purposes as part of the Synent Tech internship programme.
