import os
i=1

print("                  ======================== ")
print("                   RESUME GENERATOR      ")
print("                  ======================== ")
print(       )    



while(i<2):
    
    print("fill the below all feilds for a good resume ")
    
    print('''\n
                1.Contact Information
                2.Education Details
                3.Thechinal Skills
                4.Experience
                5.Orgranation Details
                6.Personal Details
                7.Make My Resume
                8.View Resume 
                ''')
    
    
    ch=input("Enter Your Choice:-")
    
    if int(ch)==1:
        
        print("\n\n Please Give Some Contact Information of You ")
       
        Name=input("Name:- ")
        Email=input("Email:- ")
        Phone=input("Moblie Number:-")
        print("  ")

    elif int(ch)==2:
        
        print("\n\nPlease Give  Education Qualification Information  ")
        
        Graduation=input("graduation(B.Tech/M.Tech/Degree/MBA):-")
        Branch_Stream=input("stream[CS/IT/EEE/ME/enter degree branch]:-")
        College=input("Name of the educational institute:-")
        Graduation_Percentage=input("Percentage:-")
        Passing_out_year =input("year of passing:-")
        intermmidiate=input("intermmidiate borad :-")
        intermmidiate_percantage=input("12th percentage\cpga:-")
        intermmidiate_POY=input("12th passing out year:-")
        Tenth =input("tenth borad:-")
        tenth_percantage=input("10th percentage\cpga:-")
        tenth_POY=input("10th passing out year:-")
        print('  ')

    elif int(ch)==3:
        
        print("\n\n About Your Techinical Skills   ")
        
        software_language=input("Your Software Languages:-")
        applications=input("Your Computer Applications:-")
        Tech=input("Your Technologies:-")
        others=input("Your Other Qualifitions:-")
        print('  ')
    elif int(ch)==4:
        
        print("\n\n Your Experience Details ")
        
        Company=input("Company Name:-")
        Time=input("During the period:-")
        Onwhich=input("On Which Technology/language/Other:-")
        print('  ')
    elif int(ch)==5:
        
        print("\n\n Share Your Extracurricular Activity   ")
       
        extra_activity=input(" What Is your Extacurricular Activitys:-")
        print('  ')
    elif int(ch)==6:
        
        print("\n\n Provide Your Personal Details  ")
        
        name=input("Name:-")
        Addrres=input("Addrres:-")
        DOB=input("DOB-")
        Age=input("Age-")
        Gen=input("Gender:-")
        ms=input("Marital staus:-")
        Nationality=input("Nationality:-")
        Lng_knowin=input("Launguages Know:-")
        print('  ')
    
    else:
        print("enter correct option")

input()
        
        
        
    
