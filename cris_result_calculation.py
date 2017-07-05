from bs4 import BeautifulSoup
import numpy as np
crisSoup = BeautifulSoup(open('Qp.html'),"html.parser")#,"lxml")
print (type(crisSoup))
ques_paper = crisSoup.select('.section-cntnr')
# chosen_option = crisSoup.select('.menu-tbl > tr:nth-of-type(2) > .bold', )
# for option in chosen_option:
#     print (option.getText())
chosen_options = crisSoup.select('.menu-tbl > .bold')
print("Total number of problems: %d"%len(chosen_options))
# option_number = []
# for option in chosen_option:
#     # if int(option.getText()) >= 0 or int(option.getText()) < len(chosen_option):
#     print(option.getText())
#     # else:
#     #     print("blank")
#     if option.getText() == " -- ":
#         option_number.append(0)
#     else:
#         option_number.append(int(option.getText()))
#
# print (len(option_number))
#Below is the equivalent of the code above
option_nos = [0 if option.getText() == " -- " else int(option.getText())\
              for option in chosen_options]
attempted_options = np.array(option_nos)
print ("This is the attempted option list:")
print(attempted_options)

real_options = crisSoup.select('.rightAns')
# print (len(real_options))
# for option in real_options:
#     print (int(option.getText().strip('. ')))
#Below is the equivalent of the code above
actual_options = np.array([int(option.getText().strip('. ')) for option in real_options])
print ("This is the actual option list:")
print (actual_options)

no_of_problems_not_attempted = sum(attempted_options == 0)
no_of_correct_problems = sum(attempted_options == actual_options)
no_of_incorrect_problems = len(actual_options) - no_of_correct_problems\
                           - no_of_problems_not_attempted
print ("Number of correct problems: %d"%no_of_correct_problems)
print ("Number of incorrect problems: %d"%no_of_incorrect_problems)
print ("Number of problems not attempted: %d"%no_of_problems_not_attempted)

marks_for_correct_problem = 4
marks_for_incorrect_problem = -1
score = no_of_correct_problems * marks_for_correct_problem\
        + no_of_incorrect_problems * marks_for_incorrect_problem
print ("Your score is: %d " %score)
