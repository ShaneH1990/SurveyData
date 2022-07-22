import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SURVEY_SHEET = GSPREAD_CLIENT.open('SurveyData(Responses)')
    

responses = SURVEY_SHEET.worksheet('Form Responses 1')

info = responses.get_all_values()

print(info)

data = input("\n Please enter which Gender results you would like: ")
if(data == "male"):
    print("results for males viewers:")
elif(data == "female"):
    print("results for female viewers:")

else:
    print("not a valid answer!")

group = input("\n Please enter which Age Group results you would like: ")
if(group == "15-25"):
    print("These are the following results for the 15-25 age group!:")
elif(group == "25-35"):
    print("These are the following results for the 25-35 age group!:")
elif(group == "35-45"):
    print("These are the following results for the 35-45 age group!:")
elif(group == "45-55"):
    print("These are the following results for the 45-55 age group!:")
elif(group =="55+"):
    print("These are the following results for the 55+ age group!:") 
else:
    print("invalid input! please type in a correct age group")




service = input("\n Please enter which Streaming Service results you would like: ")
if(service =="Netflix"):
    print("This is the percentage of people that uses Netflix:")
elif(service =="Disney+"):
    print("This is the percentage of people that uses Disney+:")
elif(service =="HBO Max"):
    print("This is the percentage of people that uses HBO Max:")
elif(service =="AppleTv"):
    print("This is the percentage of people that uses AppleTv:")
elif(service =="Hulu"):
    print("This is the percentage of people that uses Hulu:")
elif(service =="other"):
    print("This is the percentage of people that uses other streaming services:")
else:
    print("please type in a valid streaming service")




customer = input("\n would you like the 'library content' results or the 'original content' results: ")
if(customer =="library"):
    print("The library results are as follows:")
elif(customer == "original"):
    print("the original content results are as follows:")
else:
    print("invalid input! please type either 'library' or 'original'")




print(data)
