import os
import shutil

def deep_clean_git(root_path):
    print(f"🔍 Searching for hidden .git folders in: {root_path}")
    for root, dirs, files in os.walk(root_path):
        if '.git' in dirs:
            git_path = os.path.join(root, '.git')
            print(f"🧨 Removing embedded git: {git_path}")
            shutil.rmtree(git_path, ignore_errors=True)

if __name__ == "__main__":
    target_path = r"D:\Du_An_Mini\XiaoMi100T\src\modules\dubbing\TMF_Local_Engine"
    deep_clean_git(target_path)
    print("✅ Deep clean completed. You can now 'git add' this folder.")
