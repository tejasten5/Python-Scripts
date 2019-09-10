def user_sitemap(request):
    import os    
    list_allfiles=[]
    dest_path = os.path.join(settings.BASE_DIR, "client")
    list_allfiles=os.listdir(dest_path)
    global_list=[]        
    files={}
    folders=[]
    global_files=[]
    for dir in list_allfiles: 
        f=os.path.join(dest_path,dir)       
        if(os.path.isfile(f)==True):
            files={"name":dir,"path":f}
            global_files.append(files)
        else:
            files=get_folder_list(dir,os.path.join(dest_path,dir))
            folders.append({dir: files})
        files = {"files": global_files,"folders":folders}
    global_list.append(files)
    
    return render(request,'sitemap.html',{'global_list':global_list},)
    



def get_folder_list(dir_name,folder_path):
    global_files=[]
    files = {}
    global_folder_files={}
    for dir in os.listdir(folder_path):
        global_folder = {}
        f=os.path.join(folder_path,dir)       
        if(os.path.isfile(f)==True):
            file1={"name":dir,"path":f}
            global_files.append(file1)
            file1={}
        else:
            files=get_folder_list(dir,os.path.join(folder_path,dir)) 
            if(len(files) > 0):
                global_folder.update({dir: files}) 
            
        if len(global_folder) > 0 :
            files={"files": global_files}
            global_folder_files.update(global_folder)
        else:
            files={"files": global_files}
    files.update(global_folder_files)
    return files    
