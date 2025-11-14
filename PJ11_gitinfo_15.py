import subprocess
from datetime import datetime

def get_git_commit_hash():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        return "Git commit не найден"

def get_git_commit_date():
    try:
        return subprocess.check_output(['git', 'log', '-1', '--format=%cd']).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        return "Дата коммита не найдена"

def save_build_info():
    commit_hash = get_git_commit_hash()
    commit_date = get_git_commit_date()
    build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("build_info.txt", "w", encoding="utf-8") as f:
        f.write(f"Commit hash: {commit_hash}\n")
        f.write(f"Commit date: {commit_date}\n")
        f.write(f"Build time: {build_time}\n")

    print("Файл build_info.txt обновлён.")

if __name__ == "__main__":
    save_build_info()
