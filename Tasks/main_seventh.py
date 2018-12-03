import re

########## FIRST TASK START ########################################
"""
a = re.compile('(?:[\d]{4}(-)?(0(([13578](-)?((0[1-9])|([12]\d)|(3[01])))|(2(-)?((0[1-9])|(1\d)|(2[0-8])))|([469](-)?((0[1-9])|([12]\d)|(30))))|(1(([02](-)?((0[1-9])|([12]\d)|(3[01])))|(1(-)?((0[1-9])|([12]\d)|(30)))))))')
# check if it's 30, 31 or 28 days in month. Only VISOCOSNIJ year can't be detected...... too TOUGH

print("TRUE" if a.fullmatch('20181129') else "FALSE")
print("TRUE" if a.fullmatch('20181131') else "FALSE")
"""
########## FIRST TASK END    #######################################


########## SECOND TASK START ########################################
"""

s = "Researchers for the Next Generation Simulation (NGSIM) program collected detailed vehicle trajectory data on southbound US 101 and Lankershim Boulevard in Los Angeles, CA, eastbound I-80 in Emeryville, CA and Peachtree Street in Atlanta, Georgia."

shift = ord('A') - ord('a')  # code of upper case letter

for x in range(ord('a'), ord('z')):
    pattern = '[' + chr(x) + chr(x + shift) + ']'
    if re.search(pattern, s):
        print(chr(x))

"""
########## SECOND TASK END    #######################################

########## THIRD TASK START #########################################
"""
s = "Researchers for the Next Generation Simulation (NGSIM) program collected detailed vehicle trajectory data on southbound US 101 and Lankershim Boulevard in Los Angeles, CA, eastbound I-80 in Emeryville, CA and Peachtree Street in Atlanta, Georgia."

pattern = re.compile('\w+')
list_of_words = pattern.findall(s)
print(len(list_of_words))
"""
########## THIRD TASK END    ########################################

########## FORTH TASK START #########################################
"""
s = "Apple, Banana, Cucumber, Drive, Ear, Five and Go."

pattern = re.compile("[a-zA-Z]+( |, |. |.|! |!|\? |\?|: | - )")
list_of_words = pattern.sub(lambda x: x[0][0].upper(), s)
print(list_of_words)
"""
########## FORTH TASK END    ########################################

########## FIFTH TASK START #########################################
""""""
print("Phone number: ")
pattern = re.compile("\+(?P<code>[1-9][\d]{0,2})(?P<number>[\d]{10,12})")
m = 0
while True:
    s = input()
    m = pattern.match(s)
    if m:
        break
    print("Invalid number")
    print("Try again!")
    print("Phone number: ")
print("Code: " + str(m['code']))
print("Number: " + str(m['number']))

########## FIFTH TASK END    ########################################
