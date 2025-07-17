banner = f"""

████████ ██   ██ ███████ ██    ██  █████  ███    ██ 
   ██    ██   ██ ██       ██  ██  ██   ██ ████   ██ 
   ██    ███████ █████     ████   ███████ ██ ██  ██ 
  {"\33[94m"} ██    ██   ██ ██         ██    ██ {"\033[36m"}J{"\033[0m"}{"\33[94m"} ██ ██  ██ ██ 
   ██    ██   ██ ███████    ██    ██ {"\33[91m"}A{"\033[0m"}{"\33[94m"} ██ ██   ████ 
                                                    
 {"\033[0m"} 
   """ 
print(banner)
import os
def add_tag(path, tag, position="end"):
    if not os.path.isdir(path):
        print(f"Error: Folder not found at '{path}'")
        return
    print(f"Scanning folder: '{path}' for files to tag...")
    tagged_count = 0
    for filename in os.listdir(path):
        old_file_path = os.path.join(path, filename)
        name_part, extension_part = os.path.splitext(filename)
        if tag in name_part:
            print(f"Skipping '{filename}': Tag '{tag}' already present.")
            continue
        new_filename = ""
        if position == "start":
            new_filename = f"{tag}{name_part}{extension_part}"
        elif position == "end":
            new_filename = f"{name_part}{tag}{extension_part}"
        else:
            print(f"Invalid position specified: '{position}'. Please use 'start' or 'end'.")
            return
        new_file_path = os.path.join(path, new_filename)
        if os.path.exists(new_file_path) and old_file_path != new_file_path:
            base, ext = os.path.splitext(new_filename)
            i = 1
            while os.path.exists(os.path.join(path, f"{base}_{i}{ext}")):
                i += 1
            new_file_path = os.path.join(path, f"{base}_{i}{ext}")
            new_filename = os.path.basename(new_file_path) 
        try:
            os.rename(old_file_path, new_file_path)
            print(f"Tagged: '{filename}' -> '{new_filename}'")
            tagged_count += 1
        except OSError as e:
            print(f"Error tagging '{filename}': {e}")
    if tagged_count == 0:
        print(f"No files were tagged (either no files or tag already present).")
    else:
        print(f"Finished tagging {tagged_count} files in '{path}'.")
if __name__ == "__main__":
    fpath = input("path of folder  ex: c:/user/to/folder  : ")
    folder =  rf"{fpath}" 
    tag = input("The tag/string you want to add to the filenames : ")
    position = input(" add position : Where  the tag: start or end (default is end)  ")
    add_tag(folder, tag, position)
    print("\nScript execution finished.")
    print("Please check your folder to see the changes.")