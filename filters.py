# Om te gebruiken:
# import filters as filter

def all(input):
    # Everything is excepted
    return True

def all_without_none(input):
    # Every item is excepted, as long as it is something
    if input is None:
        return False
    return True

def equal_to(input, sameas):
    # Only accept items that are the same as
    if input == sameas:
        return True
    return False

def larger_than(input, threshold):
    # Only accept integers greater than the threshold
    if isinstance(input, str):
        return True
    elif input is None:
        return False
    if input > threshold:
        return True
    return False

def in_between(input, min, max):
    # Only accept integers within the given limits
    if isinstance(input, str):
        return True
    elif input is None:
        return False
    if input > min and input < max:
        return True
    return False

def consists_of(input, included):
    # Only accept if the specified word is mentioned
    if isinstance(input, str):
        words =input.lower().split()
        if included.lower() in words:
            return True
    return False

def consists_of_or(input, included_list):
    # Same as consist_of, but now for a array of specified words, one of them should match
    for word in included_list:
        if isinstance(input, str):
            words =input.lower().split()
            if word.lower() in words:
                return True
    return False

def consists_of_and(input, included_list):
    # Same as consist_of, but now for a array of specified words, all of them must match
    counter = 0
    for word in included_list:
        if isinstance(input, str):
            words =input.lower().split()
            if word.lower() in words:
                counter = counter + 1
    if counter == len(included_list):
        return True
    else:
        return False
