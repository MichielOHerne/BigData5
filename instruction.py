import filters as f
import operations as operation
import create_selection as cs

dumpfolder = "E:/dump/"
received = [cs.Select_data([], info = True)]
received = received + cs.M_select_data("E:/20111231_20/", 0, 60,                    \
                        f_htg=(lambda x: f.all_without_none(x)),                    \
                        f_txt=(lambda x: f.consists_of_and(x,["year", "new"])))
#received = received + cs.M_select_data("E:/20111231_21/", 0, 60)
#received = received + cs.M_select_data("E:/20111231_22/", 0, 60)
#received = received + cs.M_select_data("E:/20111231_23/", 0, 60)

filtered = operation.Merge_ext(received, "Hashtag")
filtered = operation.RemoveUnimportant(filtered, 4, 1)
filtered = operation.SortDec(filtered, 1)

input("\tThe program will create " + str(len(filtered) - 1) + " files. \n\tAll files from the folder " + str(dumpfolder) + " will be DELETED.\n\tPress 'Enter' to continue... ")  # Ask user

operation.clear_dump(dumpfolder)  # Delete all the contents from the dump-folder
print("Old dump data deleted")

#print(filtered[0])
for i in range(1, len(filtered)):
    #print(filtered[i][0], filtered[i][1])
    output = open(dumpfolder+filtered[i][0]+".txt", "a")
    for j in range(0, len(filtered[i][2])):
        #print("\t", filtered[i][2][j][1])
        output.write(operation.clean_str(filtered[i][2][j][1], True))
        output.write("\n")
    output.close()
    print("File " + filtered[i][0] + ".txt created")
print("Finished")
