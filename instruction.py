import filters as f
import operations as operation
import create_selection as cs

received = [cs.Select_data([], info = True)]
received = received + cs.M_select_data("E:/20111231_20/", 0, 10,                    \
                        f_htg=(lambda x: f.all_without_none(x)),                    \
                        f_rtc=(lambda x: f.larger_than(x, 0)),                      \
                        f_txt=(lambda x: f.consists_of_and(x,["year", "new"])),     \
                        f_cre=(lambda x: f.consists_of(x,"sun")))
#received = received + cs.M_select_data("E:/20111231_21/", 0, 60)
#received = received + cs.M_select_data("E:/20111231_22/", 0, 60)
#received = received + cs.M_select_data("E:/20111231_23/", 0, 60)

filtered = operation.Merge(received, "Hashtag")
filtered = operation.RemoveUnimportant(filtered, 2, 1)
filtered = operation.SortDec(filtered, 1)

for item in received:
    print(item)

