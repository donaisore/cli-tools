import inquirer
import subprocess
res = subprocess.call('git branch')
print(res)

# questions = [inquirer.Checkbox(
#     'interests',
#     message="What are you interested in?",
#     choices=['Computers', 'Books', 'Science', 'Nature', 'Fantasy', 'History'],
# )]
# answers = inquirer.prompt(questions)  # returns a dict
# print(answers['interests']) 
