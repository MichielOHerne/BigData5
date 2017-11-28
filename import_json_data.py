import json

def GetHashtags(twitterdata):
    hashtags = list()
    for individual_message in twitterdata:
        tmpdict = json.loads(individual_message)
        if (("entities" in tmpdict) and (len(tmpdict["entities"]["hashtags"]) > 0)):
            if (("text" in tmpdict["entities"]["hashtags"][0]) and isinstance(tmpdict["entities"]["hashtags"][0]["text"], str)):
                hashtags.append(tmpdict["entities"]["hashtags"][0]["text"].lower())
    return hashtags

def MergeHashtags(hashtags):
    unique_items = list()
    for item in hashtags:
        found_item = 0
        for i in range(len(unique_items)):
            if (unique_items[i][1] == item):
                unique_items[i][0] = unique_items[i][0] + 1
                found_item = 1
                break
        if (found_item == 0):
            unique_items.append([1, item])
    print(str(len(unique_items)) + " out of " + str(len(hashtags)) + " hashtags were unique")
    return unique_items

def RemoveUnimportant(elist, threshold):
    shorterui = list()
    numdel = 0
    for i in range(len(elist)):
        if elist[i][0] > threshold:
            shorterui.append([elist[i][0], elist[i][1]])
        else: numdel = numdel + 1
    print("Removed " + str(numdel) + " 'unimportant' hashtags")
    return shorterui

def SortDecByCol(list, col):
    return sorted(list, key=lambda list: -list[col])

def multiple_import(default_loc, numa, numb):
    megastorage = []
    for i in range(numa, numb):
        if i < 10:
            filename = default_loc + "0" + str(i) + ".json"
        else:
            filename = default_loc + str(i) + ".json"
        try:
            selected_messages = open(filename).readlines()
            megastorage = megastorage + GetHashtags(selected_messages)
        except IOError:
            print("File '" + filename + "' does not exist...")
    print("Directory " + default_loc + " imported (json-files " + str(numa) + "-" + str(numb) + ")")
    return megastorage



manyhastags = multiple_import("E:/20111231_20/", 0, 60)
manyhastags = manyhastags + multiple_import("E:/20111231_21/", 0, 60)
manyhastags = manyhastags + multiple_import("E:/20111231_22/", 0, 60)
manyhastags = manyhastags + multiple_import("E:/20111231_23/", 0, 60)

merged = MergeHashtags(manyhastags)
result = SortDecByCol(RemoveUnimportant(merged, 25), 0)

total_count = 0
for item in result:
    print("(" + str(item[0]) + ") \t" + item[1])
    total_count = total_count + item[0]
print("---\n(" + str(len(merged) - total_count) + ")\tother\n(" + str(len(merged)) + ")\ttotal unique\n(" + str(len(manyhastags)) + ")\ttotal")
