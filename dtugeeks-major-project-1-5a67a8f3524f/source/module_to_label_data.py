__author__ = 'vikas'
import csv
import os

import ownModule

# src_name=input("Please enter the name of the source file you wish to lable")
src_name = "First1000.csv"
input_fp = open(ownModule.getProjectRoot() + "outputFiles" + os.path.sep + src_name, encoding="utf-8")
input_reader = csv.reader(input_fp, delimiter="|")
input_reader = [row for row in input_reader]
if not os.path.exists(ownModule.getProjectRoot() + "outputFiles" + os.path.sep + "labels_of_data.csv"):
    file_create = open(ownModule.getProjectRoot() + "outputFiles" + os.path.sep + "labels_of_data.csv", "w")
    file_create.close()
output_fp = open(ownModule.getProjectRoot() + "outputFiles" + os.path.sep + "labels_of_data.csv", "r")
output_reader = csv.reader(output_fp, delimiter=" ")
output_reader = [row for row in output_reader]
startpost = len(output_reader)
endpost = len(input_reader)
try:
    for i in range(startpost, endpost):
        print(input_reader[i])
        label = input("Please enter the label for the post")
        if label == "-2":
            break
        output_reader.append(label)
finally:
    output_handle = open(ownModule.getProjectRoot() + "outputFiles" + os.path.sep + "labels_of_data.csv", "w")
    writer = csv.writer(output_handle)
    writer.writerows(output_reader)
    output_handle.close()
