def user_story_5(input_date3, input_date4): # A person cannot get married after their death date

    marriage_date = input_date3

    death_date = input_date4

    difference = death_date.year - marriage_date.year - ((marriage_date.month, marriage_date.day) > (death_date.month, death_date.day))

    if marriage_date != "NA" and marriage_date < datetime.datetime.today():
        if death_date != "NA" and death_date <= datetime.datetime.today():
            if difference < 0:
                print("Error: Marriage date should not occur after death date")
                return False
            else:
                return True
        else:
            print("Error: Death date not valid")
            return False
    else:
        print("Error: Marriage date not valid")
        return False
