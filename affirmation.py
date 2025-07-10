#  custom Affirmation generator for 2 person
name = input("enter your name: ")

if name.lower() == "david":
    print("OH! hello David")
elif name.lower() == "lily":
    print("OH! hey , good morning lily")
else:
    print("who are you ?")

if name.lower() == "david" or name.lower() == "lily":
    day = input("what is today? ")
    if day.lower() == "monday":
        print("Monday sucks right huhhh!!!")
    elif day.lower() == "tuesday":
        print("ohh its tuesday , hmmmmm!!!! ")
    elif day.lower() == "wednesday":
        print("yeah , third day of the week ")
    elif day.lower() == "thursday":
        print("almost there , hehehehhe")
    elif day.lower() == "friday":
        print("finally friday ohhhhh")
    elif day.lower() == "saturday":
        print("ohh its saturday , weekend id here")
    elif day.lower() == "sunday":
        print("ohh yeeeeaaahhh finally right heehheheh rest well buddy")
    else:
        print("did we have a new kinda day now a days 😏🤔 ")
    your_mood = input("how do you feel(selct:(sad/happy/okayokay/not sure)) ? ")
    if your_mood == "sad":
        print("OHHH !!!~~~ dear i am here only for you , you know ")
    elif your_mood == "happy":
        print("ohhh!! greatttt i hope you have a blast today ")
    elif your_mood == "okayokay":
        print("it definitely gonna be a good day ")
    elif your_mood == "not sure":
        print("don't worry ,, you will figure it out and i know you gonna rock today too heheeheh ")
    any_plan = input(" what are your plans for today(select:be happy/be productive/ just wanna survive/ hope for the best i guess / other ) ? ")
    if any_plan == "be happy":
        print(" that's a good plan , go for it my baby '")
    elif any_plan == "be productive":
        print("YEah!!! that's an amazing plan buddy")
    elif any_plan == "just wanna survive":
        print("hohhhhh!! you silly , 🤣🤣🤣🤣 but really you will do great")
    elif any_plan == "hope for the best i guess":
        print("yes yes , i will hope for you too but i know you don't need it ")
    elif any_plan == "other":
        print("whatever you are planning , i know it will be amazing ")
else:
    print("okay! do you best ")