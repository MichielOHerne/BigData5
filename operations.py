def Merge(all_data, by):
    column = None
    unique_items = list()
    for i in range(len(all_data[0])):
        if all_data[0][i] == by:
            column = i
            print("Merge by ", by, " in column ", str(column))
            break
    else:
        print("No column named " + by + " in the header of the data")

    unique_items.append([by, "Occurance"])

    for i in range(1, len(all_data)):
        found_item = False
        for j in range(1, len(unique_items)):
            if (unique_items[j][0] == all_data[i][column]):
                unique_items[j][1] = unique_items[j][1] + 1
                found_item = True
        if not found_item:
            unique_items.append([all_data[i][column], 1])

    return unique_items



def RemoveUnimportant(all_data, threshold, column):
    new_data = list()
    new_data.append(all_data[0])
    numdel = 0
    for i in range(1, len(all_data)):
        if all_data[i][column] > threshold - 1:
            new_data.append(all_data[i])
        else: numdel = numdel + 1
    print("Removed " + str(numdel) + " 'unimportant' rows")
    return new_data



def SortDec(data, col):
    new_data = []
    new_data.append(data[0])
    new_data.extend(sorted(data[1:], key=lambda data: -data[col]))
    return new_data
