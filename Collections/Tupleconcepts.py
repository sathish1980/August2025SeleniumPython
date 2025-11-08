class Tupleconcepts():

    name = "satshish"
    course = ("java", "python", "c#", "testing", "java1", "java", "java")
    NeeshCourse = ("AI", "AgenticAI")

    def getCourse(self):
        print((self.course))
        print(type(self.course))
        # retrieve
        for eachvalue in self.course:
            print(eachvalue)
        print(self.course[1])
        print(len(self.course))

        #update
        #Delete
        #Create
        newList = list[self.course]
        print(newList)
        print(type(newList))
        newv = tuple[newList]
        print(self.course.count("java"))

obj = Tupleconcepts()
obj.getCourse()