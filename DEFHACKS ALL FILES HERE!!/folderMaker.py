#!/usr/bin/python
import os.path

def getData( fromFileName):
    dataFileObject = open( fromFileName, 'rU')  #connects to file
    oneString = dataFileObject.read()
    dataFileObject.close()                        #ends connection
   #Separate the lines using the newlines
    SubjectTeacherRoom = oneString.split('\n')
    #splits file string into 1 list element per school     
    return SubjectTeacherRoom
gottenData = (getData( 'teachers.csv'))


def getSubject( index):
    if index < 4:
        return "art"
    if index < 20:
        return "bio"
    if index < 29:
        return "chem"
    if index < 37:
        return "cs"
    if index < 60:
        return "english"
    if index < 63:
        return "health"
    if index < 80:
        return "lang"
    if index < 105:
        return "math"
    if index < 110:
        return "music"
    if index < 120:
        return "pe"
    if index < 130:
        return "physics"
    if index < 155:
        return "ss"
    if index < 162:
        return "tech"
    else:
        return "notATeacher"

def getTeachers(data):
    teachers = []
    counter = 0
    while counter < 162:
        thing = data[counter].split(',')
        teacherName = thing[1]
        teachers.append(teacherName)
        counter += 1
    return teachers

def writeInFile( file, teacherName ):
    timeCounter = 0
    minute = 0
    hour = 3
    while timeCounter < 10:
        if minute < 10:
            minuteStr = "0" + str(minute)
        else:
            minuteStr = str(minute)
        if hour < 10:
            hourStr = "0" + str(hour)
        else:
            hourStr = str(hour)
        timeSlot = hourStr + ":" + minuteStr
        file.write(timeSlot + ",false" + ",ParentName" + ",StudentName" + "\n")
        minute += 3
        if minute == 60:
            minute = 0
            hour += 1
        timeCounter += 1
    return file

def makeFiles( data):
    teacherIndex = 0
    while teacherIndex < 162:
        path = getSubject(teacherIndex)
        teacherName = getTeachers(gottenData)[teacherIndex]
        fileName = teacherName + ".csv"
        newFile = open(path + "/"  + fileName, "w")
        writeInFile(newFile, teacherName)
        newFile.close()
        teacherIndex += 1
    return

makeFiles(gottenData)




