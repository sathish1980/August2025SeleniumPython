class Listconcepts():

    name = "satshish"
    course = ["java","python","c#","testing","java1","java","java"]
    NeeshCourse=["AI","AgenticAI"]
    def getCourse(self):
        print(self.course)
        print(type(self.course))
        print(self.course[-1]) #direct index
        print(self.course[1])
        print(len(self.course))
        for eachvalue in self.course: #dynamic vale
            print(eachvalue)
        if "Azure" in self.course:
            print("exist")
        # update
        self.course[0]="JAVA"
        self.course[1:4]="Python","CSharp"
        print(self.course)
        #insert /Add
        self.course.insert(1,"Azure")
        print(self.course)
        self.course.append("AWS")
        self.course.append("powerbi")
        print(self.course)
        self.course.extend(self.NeeshCourse)
        print(self.course)

        #remove
        self.course.remove("java")
        print(self.course)
        self.course.pop(1)
        self.course.pop()
        print(self.course)
        #del self.course
        #self.course.clear()
        #print(self.course)
        #print(self.course.sort(reverse=True))
        
        #print(newList)



obj = Listconcepts()
obj.getCourse()