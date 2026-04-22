import json
import os

PROJECT_ROOT = os.getcwd()

def write_files(data):
    for file in data["files"]:
        path = os.path.join(PROJECT_ROOT, file["path"])
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(file["content"])

        print(f"Written: {file['path']}")

if __name__ == "__main__":
    with open("architect_output.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    write_files(data)
    print("All files generated successfully.")
