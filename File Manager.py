import os 
import shutil 

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp   ],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Others': []
}

def get_file_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    for file_type, extensions in FILE_TYPES.items():
        if ext in extensions:
            return file_type
    return 'Others'

def organize_files(target_dir):
    if not os.path.exists(target_dir):
        print(f"Directory '{target_dir}' does not exist.")
        return

    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        if not os.path.isfile(item_path):
            continue
        file_type = get_file_type(item)
        dest_dir = os.path.join(target_dir, file_type)
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, item)
        if os.path.exists(dest_dir):
            print(f"Directory '{dest_dir}' already exists. Moving '{item}' to '{dest_dir}'")
            skipped += 1
            continue
        shutil.move(item_path, os.path.join(dest_dir, item))
        print(f"Moved '{item}' to '{dest_dir}'")
        moved += 1
        print(f"Organized {moved} files, skipped {skipped} files.")

if __name__ == "__main__":
    folder = input("\nEnter the path of the folder to organize:\n> ").strip()
    organize_folder(folder)