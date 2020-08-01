#Credit Card Generator
#Caution: This can be used for malicious purposes
#Im not liable for your actions
#Gotta Go Fast!!!! Enjoy My Code!!!!
#Also, thanks to my friend Cobra for helping me improve this code. Follow his GitHub: @FURRO404
#==========================================
import random
import datetime
#===========================================

#Lists And User Input

list1 = []
list2 = []

user_input = str(input("Type in a credit card you would like: Visa, MasterCard, Discover, or American Express: "))

times = int(input("How many credit cards do you want: "))

#==========================================

#if statement

if user_input == "Visa":
    for i in range(0,times):
        l = list1.clear()
        p = list2.clear()
        for i in range(0,16):
            n = random.randint(0,9)
            list1.append(n)
        for i in range(0,3):
            o = random.randint(0,9)
            list2.append(o)

        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2030, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)


        print("Your credit card number:", list1)

        print("Your cve:", list2)

        print("The expiration date:", random_date)
    
#==========================================

#elif statements
    
elif user_input == "MasterCard":
    for i in range(0,times):
        l = list1.clear()
        p = list2.clear()
        for i in range(0,16):
            n = random.randint(0,9)
            list1.append(n)
        for i in range(0,3):
            o = random.randint(0,9)
            list2.append(o)

        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2030, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        print("Your credit card number:", list1)

        print("Your cve:", list2)

        print("The expiration date:", random_date)


elif user_input == "Discover":
    for i in range(0,times):
        l = list1.clear()
        p = list2.clear()
        for i in range(0,16):
            n = random.randint(0,9)
            list1.append(n)
        for i in range(0,3):
            o = random.randint(0,9)
            list2.append(o)

        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2030, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

  
        print("Your credit card number:", list1)

        print("Your cve:", list2)

        print("The expiration date:", random_date)


elif user_input == "American Express":
    for i in range(0,times):
        l = list1.clear()
        p = list2.clear()
        for i in range(0,16):
            n = random.randint(0,9)
            list1.append(n)
        for i in range(0,3):
            o = random.randint(0,9)
            list2.append(o)

        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2030, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

  
        print("Your credit card number:", list1)

        print("Your cve:", list2)

        print("The expiration date:", random_date)
    
#============================================

#else statement
    
else:
    print("It seems like you misunderstood, please try again and read the instructions carefully!")
