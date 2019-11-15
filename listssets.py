# Session 3 day 3

file_lines = []
#Read data from the file
with open("newscores.txt","r") as my_file:
    for line in my_file:
        # remove the newline character
        line = line.strip()
        print("1: removed line")
        # split the line where the comma is into multiple
        # strings and store them into a list called temp
        temp = line.split(",")
        print("2. split the line")
        #If the first item in temp is "Dave", modify the
        # second item
        if temp[0] == "Connor":
            # put the number as a string otherwise we have to
            # cast it before we write it out to the file
            temp[1] = "82"
            # recreate the line with the new value
            line = temp[0] + "," + temp[1]
            print("created new line")
        #Add each line to the list of lines
        file_lines.append(line)

# Write the data back out to the file
with open("newscores.txt", "w") as updated_file:
    for line in file_lines:
        updated_file.write(line + "\n")
        print("updated")
    print("File updated!")

allyslist = [1,2,3,4,5]
print("Allys list:")
print(allyslist)
allyslist.append(9)
print("Allys list:")
print(allyslist)
allystuple = tuple(allyslist)

print("Allys tuple:")
print(allystuple)

