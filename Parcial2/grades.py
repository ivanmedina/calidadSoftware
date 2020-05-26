class grades():

    def __init__(self):
        pass

    def readGrades(self,file):

        if file==None or len(file)==0:
            print("Error, file is none or empty")
            return 1


        grades_list=[]
        for line in file:
            if line!="\n":
                line=line.rstrip('\n')
                grades_list.append(line)
        return grades_list

    def getAverages(self,grades_list):
        averages=[]
        students=[]
        student=""
        average=0
        grades=[]
        count=0

        for stud in grades_list:
            if not stud in stud.split(' ')[0]:
                students.append(stud.split(' ')[0])

        for stud in students:
            for grade in grades_list:
                if grade.split(' ')[0]==stud:
                    average=average+int(grade.split(' ')[2])
                    count=count+1
            average=average/count
            count=0
            averages.append(average)
            average=0

        outputs=[]
        for i in range(0,len(students)):
            outputs.append(students[i]+" "+str(averages[i]))

        return outputs



if __name__ == '__main__':
    file=open("grades.txt","r")
    text=file.read()
    g=grades()
    f=g.readGrades(text)
    g.getAverages(f)
