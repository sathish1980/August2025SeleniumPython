class Setconcepts():

    name = "satshish"
    course = {"java", "python", "c#", "testing", "java1", "java", "java","AI", "AgenticAI"}
    NeeshCourse = {"AI", "AgenticAI","python"}

    def getCourse(self):
        print((self.course))
        print(type(self.course))
        # retrieve
        for eachvalue in self.course:
            print(eachvalue)
        #print(self.course[1])
        print(len(self.course))

        #update -- not possible
        #remove
        #self.course[1]="Python"
        #self.course.pop()
        #self.course.remove("java1")

        print(self.course)

        """value = self.course.difference(self.NeeshCourse)
        print(value)
        self.course.difference_update(self.NeeshCourse)
        print(self.course)

        value = self.course.symmetric_difference(self.NeeshCourse)
        print(value)
        self.course.symmetric_difference_update(self.NeeshCourse)
        print(self.course)

        value = self.course.intersection(self.NeeshCourse)
        print(value)
        self.course.intersection_update(self.NeeshCourse)
        print(self.course)"""

        value = self.course.issubset(self.NeeshCourse)
        print(value)
        value1 = self.NeeshCourse.issubset(self.course)
        print(value1)
        value = self.course.issuperset(self.NeeshCourse)
        print(value)
        #self.course.intersection_update(self.NeeshCourse)
        #print(self.course)



obj = Setconcepts()
obj.getCourse()