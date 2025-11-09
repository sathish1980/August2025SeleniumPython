class StringConcepts():

    name = " sathis'h' Kumar .R "
    (" "
     "athi"
     "'h' Kumar .R ")
    name1 = 'sathish Kumar .R'
    def string_concept(self):
        print(self.name)
        print(len(self.name))
        print(self.name[0])
        for eachvalue in self.name:
            print(eachvalue)
        if "kumar" in self.name:
            print("yes")
        print(self.name.__contains__("Kumar"))
        print(self.name=="sathis'h' Kumar .R")
        print(self.name.startswith("Sathi"))
        print(self.name.endswith(".R"))
        print(self.name.lower())
        print(self.name.upper())
        print(self.name.capitalize())
        print(self.name)
        print(self.name.strip())
        print(self.name.replace("'h'","h"))
        nameaftersplit = self.name.split("s")
        print(nameaftersplit)

        namenew ="sathish kumar R"
        print(len(namenew))
        #o/p : hsihtas
        count=1
        for eachvalue in range(0,len(namenew)):
            newvalue =len(namenew)-count
            #print(newvalue)
            print(namenew[newvalue])
            count=count+1
        namenew.title()
        newlist=list(namenew)
        print(newlist)
        print(newlist.count("a"))

       # print(namenew.__reversed__())




obj = StringConcepts()
obj.string_concept()