from pydriller import RepositoryMining
import csv
import os

def main():
    methodLists = {}
    methodListsLongName ={}
    final = []
    repo = input("Please Enter Your Repository Address(URL or Local): ")
    try:
        for commit in RepositoryMining(repo,only_modifications_with_file_types=['.java']).traverse_commits():
            for mod in commit.modifications:
                for methods in mod.methods:
                    try:
                        netName = methods.name.split('::')[-1]
                        netLongName = methods.long_name.split('::')[-1]
                        # Check This Method is Added Before AND Modified Method Has More Parameters Than Previous One
                        if(methodLists.get(netName) and len(methodLists.get(netName)) < len(methods.parameters)):
                            final.append(
                                [
                                    commit.hash,
                                    mod.filename,
                                    methodListsLongName.get(netName),
                                    netLongName
                                ]
                            )
                            methodLists[netName] = methods.parameters
                            methodListsLongName[netName] = netLongName
                        else:
                            methodLists[netName] =  methods.parameters
                            methodListsLongName[netName] = netLongName
                    except:
                        pass
        if (len(final)):
            with open('Functions.csv', mode='w') as csv_file:
                employee_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                employee_writer.writerow(
                    ['Commit SHA', 'Java File', 'Old function signature', 'New function signature'])
                for item in final:
                    employee_writer.writerow(item)
                os.system('cls')
                print("\n\n*********************************************************\n*\t\t\t\t\t\t\t*\n*\t\tCSV FILE CREATED SUCCESSFULLY\t\t*\n*\t\t\t\t\t\t\t*\n*********************************************************\n\n")
        else:
            os.system('cls')
            print("\n No Result! Test Other Repositories\n")
    except:
        print("\nExecution Failed. Check your address and try again\n")


if __name__ == "__main__" : main()