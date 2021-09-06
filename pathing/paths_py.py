from pathlib import Path

# exists check
relative_path = Path("../pathing_test")
print(relative_path.exists())

relative_path_2 = Path("../pathing_test/dir1")
# rmdir function
if relative_path_2.exists(): pass
    # relative_path_2.rmdir() # uncomment this line later
# mkdir function
if not relative_path_2.exists():
    relative_path_2.mkdir()


pathx = Path("../pathing_test/dir1/a.py")
if not pathx.exists():
    pathx.touch()
# search
path = Path("../pathing_test/dir1")
print(path.glob("*")) # prints files recursively inside dir1
print(path.glob("*.*")) # prints files only inside dir1
for filex in path.glob("*.py"): # prints only files with py extension
    print(filex)
pathx.unlink()
