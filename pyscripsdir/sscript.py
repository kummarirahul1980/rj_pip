from os import *
import shutil
import pathlib
lsdir = listdir(".")
print(lsdir)

listrj = listdir("rj/rj")
print("list rj")
print(listrj)
# for i in listrj:
#     if not pathlib.Path("rj/rj/"+i).is_dir():
#         rmdir("rj_home/"+i)
#         print("REmovied")

#     continue
#     mkdir(pathlib.Path("rj_home")/i)
#     continue
#     src = pathlib.Path("rj/rj")/i
#     if i == "rj" and not src.is_dir():
#         print("Not a dir")
#         continue

#     print("Is a dir, ", i)
#     shutil.copytree(src, "rj_"+i, dirs_exist_ok=True)

# listrjhome = listdir("rj_home")
# for i in listrjhome:
#     try:
#         path = pathlib.Path("rj_home/"+i)/"__init__.py"
#         path.touch(  exist_ok=True)
        
#         with __builtins__.open (path, "w") as file:
#             string = "from %s import *"%("rj_"+i)
#             file.write(string)
#     except NotADirectoryError:
#         print("Not a dir")
h