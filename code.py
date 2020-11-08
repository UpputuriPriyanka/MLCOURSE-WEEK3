from flask import request
def festival_report(month):
    month=month.strip();
    l=["January","Feburary","March","April","May","June","July","August","September","October","November","December"]

    try:
        if (month=="January"):
            data="1-1-2020 : New year , 14-1-2020 : Lohri , 15-1-2020 : Sankranthi , 23-1-2020 : Subhash Chandra bose jayanthi , 26-1-2020 : Republic Day"
        elif (month=="Feburary"):
            data="21-2-2020 : Mahashivaratri"
        elif (month=="March"):
            data="9-3-2020 : Holika Dhan ,10-3-2020 : Holi , 25-3-2020 : Ugadhi&Gudi padwa , 26-3-2020 : cheti chand"
        elif (month=="Aril"):
            data="2-4-2020 : Ram Navami , 3-4-2020 : chaitra Navaratri parana , 8-4-2020 : Hanuman Jayanthi , 14-4-2020 : Ambedkar Jayanthi , 26-4-2020 : Akshaya Tritya"
        elif (month=="May"):
            data="1-5-2020 : May day"
        elif (month=="June"):
            data="23-6-2020 : jaganath Ratha Yatra"
        elif (month=="july"):
            data="5-7-2020 : Guru purinama  , 23-7-2020 : Hariyali Teej  , 25-7-2020 : Nag panchami"
        elif (month=="August"):
            data="3-8-2020 : Raksha Bandhan , 12-8-2020 : janmastami , 15-8-2020 : Independence day ,22-8-2020 : Ganesh chaturthi , 31-8-2020 : Onam"
        elif(month=="september"):
            data="1-9-2020:Anant Chaturdashi"
        elif(month=="October"):
            data="2-10-2020 : Gandhi Jyanathi , 17-10-2020: Sharad Navarathri , 24-10-2020 : Durga Puja Ashtami , 25-2-2020 : Dussehra"
        elif(month=="November"):
            data="4-11-2020 : karva Chath , 14-11-2020 : Diwali&Childrens day , 15-11-2020 : Govardhan puja , 16-11-2020 : Bhai dooj"
        elif(month=="December"):
            data="25-12-2020 : Merry chirstmas"
    except Exception as e:
        data="wrong"
    return data



def evaluate_expression(expr):
    try: 
        data=eval(expr)
    except Exception as e:
        data="wrong"
    return data

