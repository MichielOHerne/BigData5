# Om te gebruiken:
# import filters as filter

def country(all_data, country_code):
    column = None
    new_data = []
    for i in range(len(all_data[0])):
        if all_data[0][i] == "Place":
            column = i
            break
    else:
        print("No \"Place\"")
    new_data.append(all_data[0])
    if column != None:
        for i in range(1, len(all_data)):
            if all_data[i][column]['country_code'] == country_code:
                new_data.append(all_data[i])
    return new_data

def followers(all_data, min_nof = 0, max_nof = 9999):
    column = None
    new_data = []
    for i in range(len(all_data[0])):
        if all_data[0][i] == "U: Followers count":
            column = i
            break
    else:
        print("No \"U: Followers count\"")
    new_data.append(all_data[0])
    if column != None:
        for i in range(1, len(all_data)):
            if (all_data[i][column] > min_nof - 1) and (all_data[i][column] < max_nof + 1):
                new_data.append(all_data[i])
    return new_data

def friends(all_data, min_nof = 0, max_nof = 9999):
    column = None
    new_data = []
    for i in range(len(all_data[0])):
        if all_data[0][i] == "U: Friends count":
            column = i
            break
    else:
        print("No \"U: Friends count\"")
    new_data.append(all_data[0])
    if column != None:
        for i in range(1, len(all_data)):
            if (all_data[i][column] > min_nof - 1) and (all_data[i][column] < max_nof + 1):
                new_data.append(all_data[i])
    return new_data
