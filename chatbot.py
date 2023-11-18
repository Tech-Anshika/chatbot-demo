#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tyagi
#
# Created:     17/11/2023
# Copyright:   (c) tyagi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses ---------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('I am eating now.', ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the chatbot
while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print('Bot: Goodbye!')
        break
    else:
        bot_response = get_response(user_input)
        print('Bot:', bot_response)
