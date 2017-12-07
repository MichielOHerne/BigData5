import filters as f
import create_selection as cs

received = [cs.Select_data([], info = True)]
received = received + cs.M_select_data("E:/20111231_20/", 0, 16,        \
                        f_htg=(lambda x: f.all_without_none(x)),        \
                        f_rtc=(lambda x: f.larger_than(x, 0)),          \
                        f_txt=(lambda x: f.consists_of(x,"year")),      \
                        f_cre=(lambda x: f.consists_of(x,"sun")))
#received = received + cs.M_select_data("E:/20111231_21/", 0, 60)
#received = received + cs.M_select_data("E:/20111231_22/", 0, 60)
#received = received + cs.M_select_data("E:/20111231_23/", 0, 60)

for item in received:
    print(item)

