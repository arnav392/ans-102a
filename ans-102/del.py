import os
import shutil
from_dir="C:/Users/Win-10/Downloads"
to_dir="C:/Users/Win-10/Desktop"
extension=''
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension=='':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=from_dir + '/' + file_name
        path2=to_dir + '/' + "Image_Files"
        path3=to_dir + '/' + "Image_Files" + '/' + file_name
        print("path1",path1)
        print("path3",path3)
   