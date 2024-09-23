from sklearn import tree
import csv
x=[]
y=[]

input_file="/home/kian/Desktop/programming/trains/final_project/data_DB.csv"
with open(input_file,'r') as file:
    
    data=csv.reader(file)
    for item in data:

        x.append(item[0],int(item[1:3]))
        y.append(int(item[3]))
    
    clf=tree.DecisionTreeClassifier()
    clf=clf.fit(x,y)
    print('''
    Please enter the information in this way, otherwise the program will not work : 
    15,845-پژو 207-1402    ''')
    car_info=input("pease enter the car info :")
    car_info=car_info.strip().split('-')
    new_data=[car_info[0],car_info[1],car_info[2]]
    answer=clf.predict(new_data)
    print(answer[0])
