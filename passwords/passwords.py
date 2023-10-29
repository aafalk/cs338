# passwords.py by Alex Falk 10/28/2023
# This program is for the CS338 assignment 'Brute-Force Password Cracking'
# https://cs.carleton.edu/faculty/jondich/courses/cs338_f23/assignments/12-passwords.html

import hashlib
import binascii

# Load words.txt into an array
# Code given by Jeff Ondich
words = [line.strip().lower() for line in open('words.txt')]

# UNCOMMENT TO RUN CODE
#+++++++++++++++++++++++++++++++++++++ START CODE FOR PART 1 +++++++++++++++++++++++++++++++++++++#

# # Load Username and hashed passwords into an array
# userAndHash = [line.strip().lower().split(':')[0:2] for line in open('passwords1.txt')]

# # Dictionary of 'words' with hash as key and the unhashed equivalent as value
# wordHashDict = {}
# for word in words:  
#     wordHashDict[binascii.hexlify(hashlib.sha256(word.encode('utf-8')).digest()).decode('utf-8')] = word

# # Check dictionary to find passwords
# f = open("cracked1.txt", "w")
# for item in userAndHash:
#     password = wordHashDict.get(item[1])
#     if password != None:
#         f.write(item[0] + ":" + password + "\n")

#+++++++++++++++++++++++++++++++++++++ END CODE FOR PART 1 +++++++++++++++++++++++++++++++++++++#
 
#+++++++++++++++++++++++++++++++++++++ START CODE FOR PART 2 +++++++++++++++++++++++++++++++++++++#

# # Load Username and hashed passwords into an array
# userAndHash = [line.strip().lower().split(':')[0:2] for line in open('passwords2.txt')]

# # Dictionary of 'userAndHash' with hashes as keys and usernames as values
# # The one downside to this approach (and the reason I couldn't use it for part 1) is that
# # duplicate passwords are not seen in the output. However, because the passwords are more unique
# # in part 2, there will be fewer duplicate passwords
# userHashDict = {}
# for item in userAndHash:
#     userHashDict[item[1]] = item[0]

# # Check hashes to find passwords
# f = open("cracked2.txt", "w")

# # Check dictionary to find passwords
# for firstWord in words:
#     for secondWord in words:
#         twoWords = firstWord + secondWord
#         userValue = userHashDict.get(binascii.hexlify(hashlib.sha256(twoWords.encode('utf-8')).digest()).decode('utf-8'))
#         if userValue != None:
#             f.write(userValue + ":" + twoWords + "\n")

#+++++++++++++++++++++++++++++++++++++ END CODE FOR PART 2 +++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++++++++ START CODE FOR PART 3 +++++++++++++++++++++++++++++++++++++#

# # Load Username and hashed passwords into an array
# userAndHash = [line.strip().lower().split(':')[0:2] for line in open('passwords3.txt')]

# # Create dictionary of username and salted hash
# # Create list of salts
# userHashDict = {}
# saltList = []
# for item in userAndHash:
#     userHashDict[item[1]] = item[0]
#     saltList.append(item[1].split('$')[2])

# # Find passwords
# f = open("cracked3.txt", "w")
# for salt in saltList:
#     for word in words:
#         saltedWord = salt + word
#         comparableHash = "$5$" + salt + "$" + binascii.hexlify(hashlib.sha256(saltedWord.encode('utf-8')).digest()).decode('utf-8')
#         userValue = userHashDict.get(comparableHash)
#         if userValue != None:
#             f.write(userValue + ":" + word + "\n")

#+++++++++++++++++++++++++++++++++++++ END CODE FOR PART 3 +++++++++++++++++++++++++++++++++++++#