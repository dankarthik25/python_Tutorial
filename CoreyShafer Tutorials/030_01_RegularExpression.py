# Allow to search for patten  regural expressions are in any langugages

import re


def showMatches(matches):
    for match in matches:
        print(match)        # list of all the matesch list


def matchPattern(pattern, text_to_serch):
    pattern = re.compile(pattern)
    # print(r'\tTAB') # >>> \tTab : treat esq seq as a char
    matches = pattern.finditer(text_to_serch)
    showMatches(matches)
    # return mathes


text_to_serch = """
coreym.com
097-241-7840
567-928-5461
Ha HaHa"""

# matchPattern(r'.', text_to_serch)   # matches all char [a-z,A-Z,0-9,special char ..except \n]
# matchPattern(r'coreym\.com', text_to_serch)  # \. search for .
# matchPattern(r'\d', text_to_serch)  # matchs digit:[0-9]
# matchPattern(r'\w', text_to_serch)  # matchs word:[a-z,A-Z,_]
# matchPattern(r'\W', text_to_serch)  # matchs except word means : ` ~,!,@,#,$,...\n,\t
# matchPattern(r'\s', text_to_serch)  # matchs: space,tab,newline

# # ANCHOR's
# # Word boundary
# matchPattern(r'\bHa', text_to_serch)  # matchs Ha with word boundary Ha(y) sampe Ha(y)Ha(n)
# matchPattern(r'\BHa', text_to_serch)  # matchs Ha with word Noboundary Ha(n) sampe Ha(n)Ha(y)
# # Begin and End of String
# matchPattern(r'^\n', text_to_serch)  # matchs begin of str
# matchPattern(r'HaHa$', text_to_serch)  # match end of string

# # Match the phone No
# matchPattern(r'\d\d\d', text_to_serch)  # matchs 097,241,784
# matchPattern(r'\d\d\d.\d\d\d.\d\d\d\d', text_to_serch)  # matchs

# # # # # # # #
# # Match Pattern in a file data.txt
# # # # # # # # #
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# with open('data.txt', 'r') as file1:
#     content = file1.read()
#     matches = pattern.finditer(content)
#     showMatches(matches)

##################
# Match a phone no
########################
# text_to_serch = """
# 097-241-7840
# 567-928-5461
# 097+241+7840
# 097.241.7840
# 800-241-7840
# 900-241-7840
# """
# # Charater Set :[] to match only - or . between no

# print('Using a Charater Set:')
# matchPattern(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d', text_to_serch)  # matchs
# print('match 800 or 900')
# matchPattern(r'[89]00[-.]\d\d\d[-.]\d\d\d\d', text_to_serch)  # matchs
# print('Digit between 1 and 7')
# matchPattern(r'[1-7]', text_to_serch)  # matchs

txt2ser = "123 Start a sentance and then bring adfa asdaf"
print('r[a-n]')
matchPattern(r'[a-n]', txt2ser)  # matchs

print('Search aeiou in a string')
matchPattern(r'[aeiou]', txt2ser)  # matchs

print("Search non vowels letters using character set not(^)")
matchPattern(r'[^aeiou]', txt2ser)  # matchs

txt2ser = """
mat
cat
pat
bat
rat
"""
print("match except bat")
matchPattern(r'[^b]at', txt2ser)  # matchs

# ######################
# Quantifies
###################

# | symbols | Function                          |
# |---------+-----------------------------------|
# | *       | 0 or more                         |
# | +       | 1 or more                         |
# | ?       | 0 or One                          |
# | {3}     | Exact Number                      |
# | {3,4}   | Range of Number{minimum, maximum} |

# matchPattern(r'\d{3}.\d{3}.\d{4}', txt2ser)  # matchs

txt2ser = """
Mr. Schafer
Mr smith
Ms Davis
Mrs. Robinson
Mr. Tharun
"""
# # Match stating with all Mr
matchPattern(r'Mr\.', txt2ser)  # matchs Shafer,Tharun but miss smith
matchPattern(r'Mr\.?', txt2ser)  # matchs Shafer,Tharun, smith
# # here '\.?' : means either "." may present or may not be present

matchPattern(r'(Mr|Ms|Mrs)\.?', txt2ser)
# r'(Mr|Ms|Mrs)\.?' # >>> 'Mr. ','Mr. ','Ms','Mr ','Mr. '
# here '\.?' : means either "." may present or may not be present

# r'(Mr|Ms|Mrs)\.?\s[A-Z]' # >>> 'Mr. ','Mr. ','Ms','Mr ','Mr. '
#  \s : space
#  [A-Z]: Uppercase chr
#  \w : (a-z,A-Z,0-9)

# ################
# # Using Groups : Matching (Mr, Ms, Mrs)
# ######################
#
# r'(Mr|Ms|Mrs)\.?\s[A-Z]\w+' # >>> 'Mr. Schafer', 'Mr Smith '
# r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*' # >>> 'Mr. Schafer ','Mr Smith', 'Mr. T '
matchPattern(r'(Mr|Ms|Mrs)\.?\s[A-Z]', txt2ser)


################
# Match emails
#############

email = """
CoreyMShafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""
matchPattern(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)', email)
print('regural Expression from online')
matchPattern(r'[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', email)

# 333
# Url
######################
urls = '''
https://www.google.com
https://corey.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(0), match.group(1), match.group(2), match.group(3))

subbed_urls = pattern.sub(r'\2\3', urls)  # group2,3
print(subbed_urls)

# finditer  return match obj withextra information including matching
###########################
#  Find all : just return the match obj as a list of strings
###########################

txt2ser = """
Mr. Schafer
Mr smith
Ms Davis
Mrs. Robinson
Mr. Tharun
"""
pattern = re.comple(r'(Mr|Ms|Mrs)\.?\s[A-Z]')

matches = pattern.findall(txt2ser)

for match in matches:
    print(match)


# 3
# MATCH : RETURN A 1ST MATCH at begging of string simillar to ^
##############################

sentence = 'Start a sentence and then bring it to  and end'
pattern = re.compile(r'Start')
matches = pattern.match(sentence)

# 3333
# find all
# 33333
pattern = re.compile(r'')
