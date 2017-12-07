import json
from filters import all

def Select_data(twitterdata, info = False, f_htg = all, f_txt = all, f_rtc = all, f_ctr = all, f_plc = all, f_cre = all, f_unam = all, f_usna = all, f_udes = all, f_ucre = all, f_ufrc = all, f_ufoc = all, f_uloc = all, f_ulan = all, f_utzn = all, f_uutc = all):
    new_data = []
    tmp_record = []

    # Top row with information about the columns
    if info:
        return ["Hashtag", "Text", "Retweet count", "Country", "Place", "Created at", "U: Name", "U: Screen name", "U: Description", "U: Created at", "U: Friends count", "U: Followers count", "U: Location", "U: Language", "U: Time zone", "U: UTC Offset"]

    # Data
    for individual_message in twitterdata:
        tmp_record = []
        tmpdict = json.loads(individual_message)
        if (("entities" in tmpdict) and (len(tmpdict["entities"]["hashtags"]) > 0)) and (("text" in tmpdict["entities"]["hashtags"][0]) and isinstance(tmpdict["entities"]["hashtags"][0]["text"], str)):
            temp = tmpdict["entities"]["hashtags"][0]["text"].lower()
        else:
            temp = None
        if not f_htg(temp):
            continue
        tmp_record.append(temp)

        if ("text" in tmpdict):
            temp = tmpdict["text"]
        else:
            temp = None
        if not f_txt(temp):
            continue
        tmp_record.append(temp)
        if ("retweet_count" in tmpdict):
            temp = tmpdict["retweet_count"]
        else:
            temp = None
        if not f_rtc(temp):
            continue
        tmp_record.append(temp)
        try:
            temp = tmpdict["place"]["country"]
        except Exception:
            temp = None
        if not f_ctr(temp):
            continue
        tmp_record.append(temp)
        if (("place" in tmpdict) and (tmpdict["place"] != "null")):
            temp = tmpdict["place"]
        else:
            temp = None
        if not f_plc(temp):
            continue
        tmp_record.append(temp)
        if ("created_at" in tmpdict):
            temp = tmpdict["created_at"]
        else:
            temp = None
        if not f_cre(temp):
            continue
        tmp_record.append(temp)
        if ("user" in tmpdict and "name" in tmpdict["user"]):
            temp = tmpdict["user"]["name"]
        else:
            temp = None
        if not f_unam(temp):
            continue
        tmp_record.append(temp)
        if ("user" in tmpdict and "screen_name" in tmpdict["user"]):
            temp = tmpdict["user"]["screen_name"]
        else:
            temp = None
        if not f_usna(temp):
            continue
        tmp_record.append(temp)
        if ("user" in tmpdict and "description" in tmpdict["user"]):
            temp = tmpdict["user"]["description"]
        else:
            temp = None
        if not f_udes(temp):
            continue
        tmp_record.append(temp)
        if ("user" in tmpdict and "created_at" in tmpdict["user"]):
            temp = tmpdict["user"]["created_at"]
        else:
            temp = None
        if not f_ucre(temp):
            continue
        tmp_record.append(temp)
        if ("user" in tmpdict and "friends_count" in tmpdict["user"]):
            temp = tmpdict["user"]["friends_count"]
        else:
            temp = None
        if not f_ufrc(temp):
            continue
        tmp_record.append(temp)
        if ("user" in tmpdict and "followers_count" in tmpdict["user"]):
            temp = tmpdict["user"]["followers_count"]
        else:
            temp = None
        if not f_ufoc(temp):
            continue
        tmp_record.append(temp)
        if ("user" in tmpdict and "location" in tmpdict["user"]):
            temp = tmpdict["user"]["location"]
        else:
            temp = None
        if not f_uloc(temp):
            continue
        tmp_record.append(temp)
        if ("user" in tmpdict and "lang" in tmpdict["user"]):
            temp = tmpdict["user"]["lang"]
        else:
            temp = None
        if not f_ulan(temp):
            continue
        tmp_record.append(temp)
        if ("user" in tmpdict and "time_zone" in tmpdict["user"]):
            temp = tmpdict["user"]["time_zone"]
        else:
            temp = None
        if not f_utzn(temp):
            continue
        tmp_record.append(temp)
        if ("user" in tmpdict and "utc_offset" in tmpdict["user"]):
            temp = tmpdict["user"]["utc_offset"]
        else:
            temp = None
        if not f_uutc(temp):
            continue
        tmp_record.append(temp)

        new_data = new_data + [tmp_record]

    return new_data


def M_select_data(default_loc, start, end, f_htg = all, f_txt = all, f_rtc = all, f_ctr = all, f_plc = all, f_cre = all, f_unam = all, f_usna = all, f_udes = all, f_ucre = all, f_ufrc = all, f_ufoc = all, f_uloc = all, f_ulan = all, f_utzn = all, f_uutc = all):
    megastorage = []
    notimported = 0
    for i in range(start, end):
        if i < 10:
            filename = default_loc + "0" + str(i) + ".json"
        else:
            filename = default_loc + str(i) + ".json"
        try:
            selected_messages = open(filename).readlines()
            megastorage = megastorage + Select_data(selected_messages, False, f_htg, f_txt, f_rtc, f_ctr, f_plc, f_cre, f_unam, f_usna, f_udes, f_ucre, f_ufrc, f_ufoc, f_uloc, f_ulan, f_utzn, f_uutc)
        except IOError:
            print("File '" + filename + "' does not exist...")
            notimported = notimported + 1
    if notimported == 0:
        print("Directory " + default_loc + " imported (json-files " + str(start) + "-" + str(end) + ")")
    else:
        print("Directory " + default_loc + " imported (json-files " + str(start) + "-" + str(end) + ", except " + str(notimported) + " files)")
    return megastorage
