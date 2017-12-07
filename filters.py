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

def contain_word(all_data, word):
    column = None
    new_data = []
    for i in range(len(all_data[0])):
        if all_data[0][i] == "Text":
            column = i
            break
    else:
        print("No \"Text\"")
    new_data.append(all_data[0])
    if column != None:
        for i in range(1, len(all_data)):
            if all_data[i][column] != None:
                words = all_data[i][column].lower().split()
                if word in words:
                    new_data.append(all_data[i])
    return new_data





# Nieuw:
def all(input):
    return True

def all_without_none(input):
    if input == None:
        return False
    return True

def equal_to(input, sameas):
    if input == sameas:
        return True
    return False

def larger_than(input, threshold):
    if isinstance(input, str):
        return True
    elif input == None:
        return False
    if input > threshold:
        return True
    return False

def in_between(input, min, max):
    if isinstance(input, str):
        return True
    elif input == None:
        return False
    if input > min and input < max:
        return True
    return False

def consists_of(input, included):
    if isinstance(input, str):
        words =input.lower().split()
        if included.lower() in words:
            return True
    return False
