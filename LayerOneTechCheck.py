import difflib


def TechCheck(text1, text2):
    check = input("Are you sure you would like to proceed? y/n ")
    if check == 'y' or 'yes':
        for line in difflib.unified_diff(text1, text2):
            print(line)
    else:
        end


print("TESTING ONLY")
print("To use:"
      "This Python script should be contained within a folder with two items...\n The MOP configuration named 'MOP.txt'"
      "And the output of a 'show run' command in a txt file named 'showrun.txt'\n"
      "Executing this script from within the folder should yield the discrepencies")



TechCheck(open("MOP.txt").readlines(), open("showrun.txt").readlines())
