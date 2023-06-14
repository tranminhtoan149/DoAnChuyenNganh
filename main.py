# import os
# import openai

# openai.api_key = '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'
# model_id = 'gpt-3.5-turbo'

# def response(conversation):
#   response = openai.Completion.create(
#     model=model_id,
#     message = user_input,
#     temperature=0,
#     max_tokens=100,
#     top_p=1,
#     frequency_penalty=0.0,
#     presence_penalty=0.0,
#   )
#   return response.choices

# while True:
#   user_input = input("User: ")
#   print(response(user_input)[0].text)
import openai

openai.api_key = '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'
model_id = 'gpt-3.5-turbo'

def chatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    # api_usage = response['usage']
    # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    # stop means complete
    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

conversation = []
# conversation.append({'role': 'system', 'content': 'How may I help you?'})
# conversation = chatGPT_conversation(conversation)
# print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

prompt = "At line 25, in <module> print(longest_increasing_subsequencse([10, 9, 2, 5, 3, 7, 101, 18])) NameError: name 'longest_increasing_subsequencse' is not defined. Làm thế nào để sửa lỗi này?"
conversation.append({'role': 'user', 'content': prompt})
conversation = chatGPT_conversation(conversation)
print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))