import os
i=1


print("                                      RESUME GENERATOR      ")

while(i<2):
    os.system("tupt setaf")
    print("fill the below all feilds for a good resume ")
    os.system("tupt setaf 0")
    os.system("tupt setaf 2")
    print('''\n
                1.Contact Information
                2.Education Details
                3.Thechinal Skills
                4.Experience
                5.Extracurricular Activity 
                6.Personal Details
                7.Make My Resume
                8.View Resume 
                ''')
    os.system("tupt setaf 0")
    os.system("tupt setaf 1")
    ch=input("Enter Your Choice:-")
    os.system("tupt setaf 0")
    if int(ch)==1:
        os.system("tupt setaf 1")
        print("\n\n Please Give Some Contact Information of You ")
        os.system("tupt setaf 0")
        Name=input("Name:- ")
        Email=input("Email:- ")
        Phone=input("Moblie Number:-")
        
        
    elif int(ch)==2:
        os.system("tupt setaf 1")
        print("\n\nPlease Give  Education Qualification Information  ")
        os.system("tupt setaf 0")
        Graduation=input("graduation(B.Tech/M.Tech/Degree/MBA):-")
        Branch_Stream=input("stream[CS/IT/EEE/ME/enter degree branch]:-")
        College=input("Name of the educational institute:-")
        Graduation_Percentage=raw_input("Percentage:-")
        Passing_out_year =input("year of passing:-")
        intermmidiate=input("intermmidiate borad :-")
        intermmidiate_percantage=input("12th percentage\cpga:-")
        intermmidiate_POY=input("12th passing out year:-")
        Tenth =input("tenth borad:-")
        tenth_percantage=input("10th percentage\cpga:-")
        tenth_POY=input("10th passing out year:-")
    elif int(ch)==3:
        os.system("tupt setaf 1")
        print("\n\n About Your Techinical Skills   ")
        os.system("tupt setaf 0")
        software_language=input("Your Software Languages:-")
        applications=input("Your Computer Applications:-")
        Tech=input("Your Technologies:-")
        others=("Your Other Qualifitions:-")
    elif int(ch)==4:
        os.system("tupt setaf 1")
        print("\n\n Your Experience Details ")
        os.system("tupt setaf 0")
        Company=input("Company Name:-")
        Time=input("During the period:-")
        Onwhich=input("On Which Technology/language/Other:-")
    elif int(ch)==5:
        os.system("tupt setaf 1")
        print("\n\n Share Your Extracurricular Activity   ")
        os.system("tupt setaf 0")
        extra_activity=input(" What Is your Extacurricular Activitys:-")
    elif int(ch)==6:
        os.system("tupt setaf 1")
        print("\n\n Provide Your Personal Details  ")
        os.system("tupt setaf 0")
        name=input("Name:-")
        Addrres=input("Addrres:-")
        DOB=input("DOB-")
        Age=input("Age-")
        Gen=input("Gender:-")
        ms=input("Marital staus:-")
        Nationality=input("Nationality:-")
        Lng_know=input("Launguages Know:-")
    
    else:
        print("enter correct option")

input()
        
        
        
    
