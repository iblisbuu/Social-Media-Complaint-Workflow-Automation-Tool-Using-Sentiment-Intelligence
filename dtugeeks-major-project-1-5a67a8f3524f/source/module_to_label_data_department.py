'''
Created on Jan 18, 2016

@author: svarshney
'''

import csv
import os

import ownModule

src_name = "First1000.csv"
input_fp = open(ownModule.getProjectRoot() + "outputFiles" + os.path.sep + src_name, encoding="utf-8")
input_reader = csv.reader(input_fp, delimiter="|")
input_reader = [row for row in input_reader]

if not os.path.exists(ownModule.getProjectRoot() + "outputFiles" + os.path.sep + "labels_of_data_department.csv"):
    file_create = open(ownModule.getProjectRoot() + "outputFiles" + os.path.sep + "labels_of_data_department.csv", "w")
    file_create.close()

output_fp = open(ownModule.getProjectRoot() + "outputFiles" + os.path.sep + "labels_of_data_department.csv", "r")
output_reader = csv.reader(output_fp, delimiter=" ")
output_reader = [row for row in output_reader]

startpost = len(output_reader)
endpost = len(input_reader)

# Departments List
departments = list()
departments.append("Accounts and Deposits")
departments.append("Loans")
departments.append("Cards")
departments.append("Insurance")
departments.append("Service")
departments.append("Miscellaneous")

try:
    for i in range(startpost, endpost):
        print(input_reader[i])
        print("Please enter the department for the post")
        print(" Departments are as follows : ")

        for i, department in enumerate(departments):
            print(" %s for Department : %s " % (i + 1, department))

        label = input()

        if label == "-2":
            break
        output_reader.append(label)
finally:
    output_handle = open(ownModule.getProjectRoot() + "outputFiles" + os.path.sep + "labels_of_data_department.csv",
                         "w")
    writer = csv.writer(output_handle)
    writer.writerows(output_reader)
    output_handle.close()
