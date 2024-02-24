import config
import email_functions

class Air_Quality:
    SO2 = config.data_aq['list'][0]['components']['so2']
    CO = config.data_aq['list'][0]['components']['co']
    NO = config.data_aq['list'][0]['components']['no']
    NO2 = config.data_aq['list'][0]['components']['no2']
    O3 = config.data_aq['list'][0]['components']['o3']
    PM2_5 = config.data_aq['list'][0]['components']['pm2_5']
    PM10 = config.data_aq['list'][0]['components']['pm10']
    NH3 = config.data_aq['list'][0]['components']['nh3']

    @classmethod
    def check_air(self, email):
        if (self.SO2 > 250 or self.NO2 > 150 or self.PM10 > 100 or self.PM2_5 > 50 or self.O3 > 140 or self.CO > 12400 ):
            email_functions.Send_Alert("Warning: Poor Air Quality", email)
            return "Warning: Air Quality"
        else:
            return "Air is safe"

def check_temp(email):
    if (config.data_temp - 273 > 38):
        email_functions.Send_Alert("Warning: Extreme Heat",email)
        return "Warning: Extreme Heat"
    elif (config.data_temp - 273 < 0):
        email_functions.Send_Alert("Warning: Extreme Cold",email)
        return "Warning: Extreme Cold"
    else:
        return "No Hazard Detected"

def check_wind(email):
    if (config.data_ws > 17):
        email_functions.Send_Alert("Warning: Violent Wind",email)
        return "Warning: Violent Wind"
    else:
        return "No Hazard Detected"

def check_rain(email):
    if(config.data_r['list'][7]['pop'] == 0):
       return "No Hazard Detected, no rain"
    elif (config.data_r['list'][8]['3h'] > 50):
        email_functions.Send_Alert("Warning: Flooding incoming in 5 days", email)
        return "Warning: Flooding incoming in 5 days"
    else:
        return "No Hazard Detected"
     

