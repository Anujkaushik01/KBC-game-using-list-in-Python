import random

# Questions
questions = ['Who is current PM of India? ', 
             'Who is current President of Russia?',
             'Who is current President of USA?',
             'Who is current PM of UK?']

# Answers
answers = questions[:]
answers[0] = 'Narendra Modi'
answers[1] = 'Vladimir Putin'
answers[2] = 'Joe Biden'
answers[3] = 'Rishi Sunak'

# Options
question_options = [['Narendra Modi', 'Manmohan Singh', 'Droupadi Murmu', 'Amit Shah'], 
                     ['Vladimir Zelensky', 'Stalin', 'Vladimir Putin', 'Sergey Lavrov'],
                     ['Donald Trump', 'Joe Biden', 'Obama', 'Anthony Blinken'], 
                     ['Liss Truss', 'Manmohan Singh', 'Emmanuel Macron', 'Rishi Sunak']]

score = 0

# Welcome screen to the game.
print('\n','Welcome to Kaun Banega Crorepati!'.center(56),'\n')

# Question number
q_no = 0

# Loops until all questions are asked.
while questions:
  # Generates a random number from 0,1,2,3
  random_index = random.randrange(0, len(questions))
  
  q_no += 1
  
  # Prints random question
  print(f'{q_no}. {questions[random_index]}')
  
  # Print its options
  if random_index == 0:
    print(f'A. {question_options[0][0]}')
    print(f'B. {question_options[0][1]}')
    print(f'C. {question_options[0][2]}')
    print(f'D. {question_options[0][3]}')
    user_options = question_options[0]
    answer = answers[0]
  elif random_index == 1:
    print(f'A. {question_options[1][0]}')
    print(f'B. {question_options[1][1]}')
    print(f'C. {question_options[1][2]}')
    print(f'D. {question_options[1][3]}')
    user_options = question_options[1]
    answer = answers[1]
  elif random_index == 2:
    print(f'A. {question_options[2][0]}')
    print(f'B. {question_options[2][1]}')
    print(f'C. {question_options[2][2]}')
    print(f'D. {question_options[2][3]}')
    user_options = question_options[2]
    answer = answers[2]
  elif random_index == 3:
    print(f'A. {question_options[3][0]}')
    print(f'B. {question_options[3][1]}')
    print(f'C. {question_options[3][2]}')
    print(f'D. {question_options[3][3]}')
    user_options = question_options[3]
    answer = answers[3]
    
  # Taking user input
  user_input = input('\nEnter your answer: ')
  
  # Handling error if user not input anything 
  # or if he input something else
  while True:
    if not user_input:
      print('Enter answer! ')
      user_input = input('Enter your answer: ')
    elif (user_input.lower() not in ['a', 'b', 'c', 'd'] 
          and user_input not in ['1', '2', '3', '4']):
      print('Enter valid answer from A, B, C, D or 1, 2, 3, 4')
      user_input = input('Enter your answer: ')
    else:
      break
  
  # Marks user input
  if user_input in ['A', 'a', '1']:
    user_answer = user_options[0]
  elif user_input in ['B', 'b', '2']:
    user_answer = user_options[1]
  elif user_input in ['C', 'c', '3']:
    user_answer = user_options[2]
  elif user_input in ['D', 'd', '4']:
    user_answer = user_options[3]
  
  # Checking if user input is correct
  if user_answer == answer:
    print('Correct Answer!\n')
    score +=1
  else:
    print('Wrong Answer!\n')
  
  # Removing the question, its options, and its answer from lists
  questions.remove(questions[random_index])
  question_options.remove(question_options[random_index])
  answers.remove(answers[random_index])


# Ending screen with final score
print('Thank you for playing Kaun Banega Crorepati!'.center(56), '\n')
print(f'Your score is {score} out of {q_no}.'.center(56))
