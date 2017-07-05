from bs4 import BeautifulSoup
import numpy as np
crisSoup = BeautifulSoup(open('Qp.html'),"html.parser")#,"lxml")
print (type(crisSoup))
ques_paper = crisSoup.select('.section-cntnr')
# chosen_option = crisSoup.select('.menu-tbl > tr:nth-of-type(2) > .bold', )
# for option in chosen_option:
#     print (option.getText())
chosen_option = crisSoup.select('.menu-tbl > .bold')
print(len(chosen_option))
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
option_no = [0 if option.getText() == " -- " else int(option.getText()) for option in chosen_option]
attempted_option_no = np.array(option_no)
print(attempted_option_no)
