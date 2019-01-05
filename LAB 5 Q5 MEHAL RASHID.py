def marksheet(name,fname,rno):
    subject_name=[]
    subject_marks=[]
    tot_marks=0
    for x in range(1,6):
        a=input("\nPlease Enter the Name of Subject"+str(x)+" :")
        b=int(input("Please Enter the Marks of Subject"+str(x)+":"))
        subject_name.append(a)
        subject_marks.append(b)

    for y in range(5):
        tot_marks += subject_marks[y]

    percentage = (tot_marks/500)*100
    if (percentage>=50) and (percentage<60):
        grade = 'D'
    elif (percentage>=60) and (percentage<70):
        grade = 'C'
    elif (percentage>=70) and (percentage<80):
        grade = 'B'
    elif (percentage>=80) and (percentage<90):
        grade = 'A'
    elif (percentage>=90) and (percentage<100):
        grade = 'A+'
    else:
        grade =  'Fail'
    print("\n\n")
    print(u"\u25A0"*38)
    print(u"\u25A0","Name         :{0:20}".format(name),u"\u25A0")
    print(u"\u25A0","Father's Name:{0:20}".format(fname),u"\u25A0")
    print(u"\u25A0","Roll Number  :{0:20}".format(rno),u"\u25A0")
    print(u"\u25A0"*38)
    
    a = [[0 for col in range(5)] for row in range(2)]

    for row in range(2):
        for col in range(5):
            if row==0:
                hmm=subject_name[col]
                a[row][col] = hmm
            if row==1:
                hmm=subject_marks[col]
                a[row][col] = hmm

    print(u"\u25A0"*70)
    for row in range(2):
        print("\n")
        for col in range(5):
            if row==0:
                print("|",'{:^10}'.format(a[row][col]),"|",end="")
            if row==1:
                print("|",'{:^10}'.format(a[row][col]),"|",end="")
    print("\n")
    print(u"\u25A0"*70)
    percentage = float("{0:.2f}".format(percentage))
    print(u"\u25A0"*38)            
    print(u"\u25A0","Total Marks  :{0:^20}".format(tot_marks),u"\u25A0")
    print(u"\u25A0","Percentage(%):{0:^20}".format(percentage),u"\u25A0")
    print(u"\u25A0","Grade        :{0:^20}".format(grade),u"\u25A0")
    print(u"\u25A0"*38)

name = input("Please Enter Your Name         :")
fname= input("Please Enter Your Father's Name:")
rno  = input("Please Enter Your Roll Number  :")
marksheet(name,fname,rno)
