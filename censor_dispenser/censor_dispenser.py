# These are the emails you will be censoring.
# The open() function is opening the text file that the emails are contained in and the .read() method
# is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# First task
# Write a function that can censor a specific word or phrase from a body of text, and then return the text.
# Mr. Cloudy has asked you to use the function to censor all instances of the phrase learning algorithms
# from the first email, email_one.
# Mr. Cloudy doesn't care how you censor it, he just wants it done.

# Second task
# Write a function that can censor not just a specific word or phrase from a body of text,
# but a whole list of words and phrases, and then return the text.
# Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two.
proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her", "herself"]
# Third task
# The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think.
# He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language
# and remove unnecessary instances of ‘negative words.’” Write a function that can censor any occurrence of a word
# from the “negative words” list after any “negative” word has occurred twice,
# as well as censoring everything from the list from the previous step as well and use it to censor email_three.
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]

# Fourth task
# This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you,
# “our company would be ruined! Censor it! Censor it all!”
# Write a function that censors not only all of the words from the negative_words and proprietary_terms lists,
# but also censor any words in email_four that come before AND after a term from those two lists.

# The fifth task
# Great job! The Board of Investors is none the wiser to what is going on in the lab and Mr. Cloudy is very happy.
# Take a moment to look over your functions, are they the best they can be? As a challenge, make sure they:
# Handle upper and lowercase letters.
# Handle punctuation.
# Censor words while preserving their length.


# write a function that would censor a list of words
# Here I need to figure out how to censor 's, -self, and so on

def censor_word(email, neg_word):
    censor_marks = ''
    for char in neg_word:
        if char in '.,!?;: \'\"#':
            censor_marks += char
        else:
            censor_marks += '#'
    special_character_lst = ['self', 's', 'ly']
    for special_char in special_character_lst:
        email = email.replace(' ' + neg_word + special_char, ' ' + censor_marks)
    email = email.replace(' ' + neg_word + ' ', ' ' + censor_marks + ' ')
    email = email.replace(' ' + neg_word.title() + ' ', ' ' + censor_marks + ' ')
    email = email.replace(' ' + neg_word, ' ' + censor_marks).replace(neg_word + ' ', censor_marks + ' ')
    email = email.replace(' ' + neg_word.title(), ' ' + censor_marks)
    email = email.replace(neg_word.title() + ' ', censor_marks + ' ')
    return email


# Write a function that would censor a list of words


def censor_list(email, lst_of_neg_words):
    for neg_word in lst_of_neg_words:
        email = censor_word(email, neg_word)
    return email

print(censor_list(email_two, proprietary_terms))
#y = censor_list(email_two, proprietary_terms)
#print(censor_list(y, x))
#print(censor_word(y, '######## #########s have'))

# write a function that would censor one word before and after a negative_word


def before_and_after(email, lst_of_neg_words):
    email = censor_list(email, lst_of_neg_words)
    split_email = email.split()
    new_censor_lst = []
    indices = range(len(split_email))
    for index in indices:
        if '#' in split_email[index]:
            try:
                new_censor_lst.append(split_email[index-1]+' '+split_email[index]+' '+split_email[index+1])
            except IndexError:
                new_censor_lst.append(split_email[index - 1]+' '+split_email[index])
            except IndexError:
                new_censor_lst.append(split_email[index]+' '+split_email[index + 1])
    email = censor_list(email, new_censor_lst)
    print(new_censor_lst)
    return email


# I can censor everything first, and then censor everything that comes before and after [REDACTED]!!!
# Everything works fine, just need to figure out that 's, -self problem

# print(before_and_after(email_two, proprietary_terms))
# print(email_two)
