age = input('Are you a cigarette addict older than 75 year old?yes or no :Y/N ')
if age.upper() == "Y":
    age_answer = True
else:
    age_answer = False
chronic = input('Do you have a severe chronic disease?yes or no :')
if chronic.upper() == "Y":
    chronic_answer = True
else:
    chronic_answer = False
immune = input('Is your immune system too weak?yes or no :')
if immune.upper() == "Y":
    immune_answer = True
else:
    immune_answer = False

risk = (age_answer or chronic_answer or immune_answer)

if risk == True:
    print('You are in risky group')
else:
    print('You are not in risky group')
