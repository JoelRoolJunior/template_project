import os
from pathlib import Path

def main():
    delete_gitkeep()

def delete_gitkeep():
    paths = list(Path.cwd().rglob("*.gitkeep"))
    for path in paths:
        if os.path.exists(path):
            os.remove(path)

if __name__=='__main__':
    main()