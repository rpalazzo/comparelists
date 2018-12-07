#!/usr/bin/python

import argparse
 
def main():
    parser = argparse.ArgumentParser(description= \
      'Compare lists of elements in specified files.')
    parser.add_argument("file1", type=str, help= \
      "File containing first list of elements to compare")
    parser.add_argument("file2", type=str, help= \
      "File containing second list of elements to compare")
    parser.add_argument('-f', '--first', action='store_true', help= \
      "Display elements unique to first file")
    parser.add_argument('-s', '--second', action='store_true', help= \
      "Display elements unique to second file")
    parser.add_argument('-c', '--common', action='store_true', help= \
      "Display elements common to both files")
    parser.add_argument('-a','--all', action='store_true', help= \
      "Display unique elements for each file as well as common elements")
    parser.add_argument('-r','--report', action='store_true', help= \
      "Report statistics of unique and common elements")

    args = parser.parse_args()
    if (args.first or args.second or args.common or \
      args.all or args.report) == False:
        parser.error("Specify at least one switch argument")
 
    List1 = []
    List2 = []

    parseFile(args.file1, List1)
    parseFile(args.file2, List2)

    Unique1 = [i for i in List1 if i not in List2]
    Unique2 = [i for i in List2 if i not in List1]
    CommonWithDuplicates = [i for i in List1 + List2 \
      if i in List1 and i in List2]
    #Remove duplicates by converting to set and back to list
    Common = list(set(CommonWithDuplicates))
  
    if args.first or args.all:
        print("Unique in " + args.file1)
        for element in Unique1:
   	    print(element)
        print("")
 
    if args.second or args.all:
        print("Unique in " + args.file2)
        for element in Unique2:
	    print(element)
        print("")

    if args.common or args.all:
        print("Common to " + args.file1 + " and " + args.file2)
        for element in Common:
            print(element)
        print("")

    if args.report:
        LenUnique1 = len(Unique1)
        LenUnique2 = len(Unique2)
        LenList1 = len(List1)
        LenList2 = len(List2)
        LenCommon = len(Common) 

        if LenList1 == 0:
            print(args.file1 + " is empty")
        elif LenList2 == 0:
            print(args.file2 + " is empty")
        else:
            print(str(LenUnique1) + " of " + str(LenList1) + " (" + \
              percent(LenUnique1, LenList1) + ") are unique in " + args.file1)
            print(str(LenCommon) + " of " + str(LenList1) + " (" + \
              percent(LenCommon, LenList1) +  ") are common in " + args.file1) 
            print(str(LenUnique2) + " of " + str(LenList2) + " (" + \
              percent(LenUnique2, LenList2) + ") are unique in " + args.file2)
            print(str(LenCommon) + " of " + str(LenList2) + " (" + \
              percent(LenCommon, LenList2) +  ") are common in " + args.file2) 
            print("")

def parseFile(inputFile, List):
    try:
        with open(inputFile, "r") as f:
            for line in f.read().splitlines():
                List.append(line) 
    except:
        print("Error reading " + inputFile)
        exit()

 
def percent(part, whole):
   if whole == 0:
       return "UNDEFINED"
   else:
       float_result = float(part)/float(whole)
       percent_result =  "{:.1%}".format(float_result)
       return str(percent_result)

 
if __name__ == "__main__":
    main()
