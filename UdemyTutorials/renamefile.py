
def getNamebypath(path):
    listOfFiles = os.listdir(path)
    for videoName in listOfFiles:
        # print(videoName)
        videoNames.append(videoName)
    return videoNames

def getNameinOrder(path):
    svideoNames = []
    with open(os.path.join(path,'list'), "r") as reader :
        for v in reader:
    #         # name2 = ''.join(''.join(v.split(' ')[8:]).split("-")[:-1]) + ".mp4"
    #         # print(v[:-3])
            n1 = v.split(' ')
            i = 0
            for word in n1:
                if (word == '') and (i <8):
                    del n1[i]
                i += 1
            n1 = n1[8:]
            name = ' '.join(n1)
            if ('.mp4' in name) and (len(name)>0):
                # if '\n' in name:
                # name.replace('.mp4\n','.mp4')
                n1 = name.split(".")
                n1 = n1[:-1]
                name = ''.join(n1) + ".mp4"
                # print(name)
                svideoNames.append(name)
    return svideoNames

def setRename(videoNames,svideoNames):
    videorename = []
    for videoName in videoNames:
        i = 1
        # print("Search for Match" + videoName)
        for svideoName in svideoNames:
            # print(svideoName)
            # print(videoName )
            if (videoName in svideoName):
                # print('Match as found')
                temp = [i, videoName,svideoName]
                videorename.append(temp)
            i = i + 1
    return videorename

import os
videoNames = []
path = '/home/jayradhe/DBMS_Theory'#"/home/jayradhe/sqLiteTutorial"
# path = '/home/jayradhe/sqllite' 
#path ='/home/jayradhe/cppnuts/TutorialForBegineers'

videoNames = getNamebypath(path)# 
# print(" GIVEN FILES IN FOLDER")
# print (getNamebypath(path))
svideoNames = getNameinOrder(path)# 
# print(" Name of files from list")
# print(getNameinOrder(path))
videorename = setRename(videoNames,svideoNames)
# print(videorename)

for v in videorename:
    # print(v)
    rename = f'{v[0]:03}_{v[1]}'.replace(' ','')
    print(v[2],'\t|| ',rename)
    os.rename(os.path.join(path,v[2]), os.path.join(path,rename))
