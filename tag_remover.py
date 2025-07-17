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
def r_files(path, tag):
    if not os.path.isdir(path):
        print(f"Error: Folder not found at '{path}'")
        return
    print(f"Scanning folder: '{path}' for files to rename...")
    r_count = 0
    for i in os.listdir(path):
        if tag in i:
            old_file_path = os.path.join(path, i)
            new_i = i.replace(tag, "")
            new_i = new_i.strip()
            name_part, extension_part = os.path.splitext(new_i)
            if not extension_part and '.' in i:
                 _, original_ext = os.path.splitext(i)
                 if original_ext:
                     new_i = name_part + original_ext
                 else:
                     new_i = name_part
            new_file_path = os.path.join(path, new_i)
            if os.path.exists(new_file_path) and old_file_path != new_file_path:
                base, ext = os.path.splitext(new_i)
                i = 1
                while os.path.exists(f"{base}_{i}{ext}"):
                    i += 1
                new_file_path = os.path.join(path, f"{base}_{i}{ext}")
                new_i = os.path.basename(new_file_path)
            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: '{i}' -> '{new_i}'")
                r_count += 1
            except OSError as e:
                print(f"Error renaming '{i}': {e}")
        else:
            pass

    if r_count == 0:
        print(f"No files found containing '{tag}' in their names.")
    else:
        print(f"Finished renaming {r_count} files in '{path}'.")

if __name__ == "__main__":
    path = input("path of folder  ex: c:/user/to/folder  : ")
    path_folder = rf"{path}"
    tag_rm = input("tag or name u want to remove it   : ")
    r_files(path_folder, tag_rm)

    print("\nScript execution finished.")
    print("Please check your folder to see the changes.")