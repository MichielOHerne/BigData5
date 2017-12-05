import json

def Select_data(twitterdata, selection = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], info = False):
    new_data = []
    tmp_record = []
    numofcolumns = 0
    for i in selection:
        if i:
            numofcolumns = numofcolumns + 1
    # Top row with information about the columns
    if info:
        if selection[0]:
            tmp_record.append("Hashtag")
        if selection[1]:
            tmp_record.append("Text")
        if selection[2]:
            tmp_record.append("Retweet count")
        if selection[3]:
            tmp_record.append("Country")
        if selection[4]:
            tmp_record.append("Place")
        if selection[5]:
            tmp_record.append("Created at")
        if selection[6]:
            tmp_record.append("U: Name")
        if selection[7]:
            tmp_record.append("U: Screen name")
        if selection[8]:
            tmp_record.append("U: Description")
        if selection[9]:
            tmp_record.append("U: Created at")
        if selection[10]:
            tmp_record.append("U: Friends count")
        if selection[11]:
            tmp_record.append("U: Followers count")
        if selection[12]:
            tmp_record.append("U: Location")
        if selection[13]:
            tmp_record.append("U: Language")
        if selection[14]:
            tmp_record.append("U: Time zone")
        if selection[15]:
            tmp_record.append("U: UTC Offset")
        return [tmp_record]

    # Data
    for individual_message in twitterdata:
        tmp_record = []
        tmpdict = json.loads(individual_message)
        if selection[0]:
            if (("entities" in tmpdict) and (len(tmpdict["entities"]["hashtags"]) > 0)) and (("text" in tmpdict["entities"]["hashtags"][0]) and isinstance(tmpdict["entities"]["hashtags"][0]["text"], str)):
                tmp_record.append(tmpdict["entities"]["hashtags"][0]["text"].lower())
            else:
                tmp_record.append(None)
        if selection[1]:
            if ("text" in tmpdict):
                tmp_record.append(tmpdict["text"])
            else:
                tmp_record.append(None)
        if selection[2]:
            if ("retweet_count" in tmpdict):
                tmp_record.append(tmpdict["retweet_count"])
            else:
                tmp_record.append(None)
        if selection[3]:
            try:
                tmp_record.append(tmpdict["place"]["country"])
            except Exception:
                tmp_record.append(None)
        if selection[4]:
            if (("place" in tmpdict) and (tmpdict["place"] != "null")):
                tmp_record.append(tmpdict["place"])
            else:
                tmp_record.append(None)
        if selection[5]:
            if ("created_at" in tmpdict):
                tmp_record.append(tmpdict["created_at"])
            else:
                tmp_record.append(None)
        if ("user" in tmpdict):
            if selection[6]:
                if ("name" in tmpdict["user"]):
                    tmp_record.append(tmpdict["user"]["name"])
                else:
                    tmp_record.append(None)
            if selection[7]:
                if ("screen_name" in tmpdict["user"]):
                    tmp_record.append(tmpdict["user"]["screen_name"])
                else:
                    tmp_record.append(None)
            if selection[8]:
                if ("description" in tmpdict["user"]):
                    tmp_record.append(tmpdict["user"]["description"])
                else:
                    tmp_record.append(None)
            if selection[9]:
                if ("created_at" in tmpdict["user"]):
                    tmp_record.append(tmpdict["user"]["created_at"])
                else:
                    tmp_record.append(None)
            if selection[10]:
                if ("friends_count" in tmpdict["user"]):
                    tmp_record.append(tmpdict["user"]["friends_count"])
                else:
                    tmp_record.append(None)
            if selection[11]:
                if ("followers_count" in tmpdict["user"]):
                    tmp_record.append(tmpdict["user"]["followers_count"])
                else:
                    tmp_record.append(None)
            if selection[12]:
                if ("location" in tmpdict["user"]):
                    tmp_record.append(tmpdict["user"]["location"])
                else:
                    tmp_record.append(None)
            if selection[13]:
                if ("lang" in tmpdict["user"]):
                    tmp_record.append(tmpdict["user"]["lang"])
                else:
                    tmp_record.append(None)
            if selection[14]:
                if ("time_zone" in tmpdict["user"]):
                    tmp_record.append(tmpdict["user"]["time_zone"])
                else:
                    tmp_record.append(None)
            if selection[15]:
                if ("utc_offset" in tmpdict["user"]):
                    tmp_record.append(tmpdict["user"]["utc_offset"])
                else:
                    tmp_record.append(None)

        # Append with None if no user data is available
        while (len(tmp_record) < numofcolumns):
            tmp_record.append(None)

        if not None in tmp_record:
            new_data = new_data + [tmp_record]

    return new_data


def M_select_data(default_loc, start, end, selection = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]):
    megastorage = []
    notimported = 0
    for i in range(start, end):
        if i < 10:
            filename = default_loc + "0" + str(i) + ".json"
        else:
            filename = default_loc + str(i) + ".json"
        try:
            selected_messages = open(filename).readlines()
            megastorage = megastorage + Select_data(selected_messages, selection, False)
        except IOError:
            print("File '" + filename + "' does not exist...")
            notimported = notimported + 1
    if notimported == 0:
        print("Directory " + default_loc + " imported (json-files " + str(start) + "-" + str(end) + ")")
    else:
        print("Directory " + default_loc + " imported (json-files " + str(start) + "-" + str(end) + ", except " + str(notimported) + ")")
    return megastorage
