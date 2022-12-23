import shutil
import os 


from_dir = "C:/Users/inno/Downloads"
to_dir = "C:/Users/inno/Documents/destination"

list_all_files = os.listdir(from_dir)
print(list_all_files)

for i in list_all_files:
    name,extension = os.path.splitext(i)
    if extension == '':
        continue
    if extension in [".txt",".pdf",".rtf"]:
        source_path = from_dir + "/" + i 
        destination_path = to_dir +  "/" + i 
        path3 = to_dir + '/' + i

if os.path.exists(from_dir):
    print("Moving ",from_dir , "......")
    shutil.move(source_path,path3)
else:
    os.makedirs(destination_path)
    print("Moving " , from_dir , "......")
    shutil.move(source_path,path3)





 