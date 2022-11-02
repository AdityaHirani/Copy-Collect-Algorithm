import os
import shutil

target = input("Enter the full path of the file: ")
fileName = input("Enter the name of the file again: ")
slice = slice(-4)
fileInformation = "FileInformation" + "(" + fileName[slice] + ")" + ".txt"
fileName = "(Copied)" + fileName

shutil.copy2(target, fileName)

fileSize = "File size: " + str(os.path.getsize(target)) + "\n"
lastModified = "Last modified: " + str(os.path.getmtime(target)) + "\n"
created = "Created on: " + str(os.path.getctime(target)) + "\n"

allStats = os.stat(target)

typeAndPermissions = "File type and permissions: " + str(allStats.st_mode) + "\n"
inodeNumber = "Inode number: " + str(allStats.st_ino) + "\n"
deviceId = "Device id: " + str(allStats.st_dev) + "\n"
ownerId = "File owner id: " + str(allStats.st_uid) + "\n"
groupId = "File group id: " + str(allStats.st_gid) + "\n"

def Gather(fileInformation, fileSize, lastModified, created, typeAndPermissions, inodeNumber, deviceId, ownerId, groupId):
    file = open(fileInformation, "w")
    file.write(fileSize)
    file.write(lastModified)
    file.write(created)
    file.write(typeAndPermissions)
    file.write(inodeNumber)
    file.write(deviceId)
    file.write(ownerId)
    file.write(groupId)
    file.close()
    
Gather(fileInformation, fileSize, lastModified, created, typeAndPermissions, inodeNumber, deviceId, ownerId, groupId)
