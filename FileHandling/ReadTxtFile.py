class readData():


    def readFile(self):

        filepath = "C:\\Users\\DELL\\PycharmProjects\\August2025SeleniumPython\\Input\\Fita.txt"
        file = open(filepath,"r")
        print(file.read(100))
        #print(file.readline())
        #print(file.readline())
        #print(file.readlines())
        #listvalue = file.readlines()
        #for eachvalue in listvalue:
            #print(eachvalue)
        file.close()

    def writeFile(self):

        filepath = "C:\\Users\\DELL\\PycharmProjects\\August2025SeleniumPython\\Input\\output.txt"
        file = open(filepath,"a")
        filepathr = "C:\\Users\\DELL\\PycharmProjects\\August2025SeleniumPython\\Input\\Fita.txt"
        readfile = open(filepathr, "r")
        readdata = readfile.readlines()
        print(readdata)
        """for eachvalue in readdata:
            if eachvalue.__contains__("sathish"):
                file.write(eachvalue)"""
        #print(file.read(100))
        #print(file.readline())
        #print(file.readline())
        file.write(str(readdata))
        print("done")
        file.close()

obj= readData()
obj.writeFile()