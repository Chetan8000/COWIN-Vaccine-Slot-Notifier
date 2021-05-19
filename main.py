import json
import os
import random
from datetime import datetime
from time import sleep

import requests

PIN_CODE = 424304

def get_appointment_sessions_data(pin_code):
    """
    pin_code: 6 digit pin code (424002)
    """
    today_date = datetime.today().strftime('%d-%m-%Y')
    browser_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
    }
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}'.format(
        pin_code,
        today_date
    )
    response = requests.get(
        url,
        headers=browser_header
    )
    json_data = json.loads(response.text)
    return json_data


def appointment_sessions(PIN_CODE):
    data = get_appointment_sessions_data(PIN_CODE)
    if data.get('centers'):
        for center in data.get('centers'):
            if center.get('sessions'):
                for session in center.get('sessions'):
                    if session.get('available_capacity') and session.get('available_capacity') > 0:
                        available_capacity = session.get('available_capacity')

                        print('************' * 10)
                        print('hey session available')
                        print(str(center['name']) + '  >>>  ' + ' availability = ' + str(available_capacity))
                        print('************' * 10)

                        duration = 1  # seconds
                        freq = 440  # Hz
                        try:
                            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                        except:
                            os.system("sudo apt install sox -y")
                        finally:
                            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                        break


if __name__ == "__main__":


    aval = True
    while aval != False:
        appointment_sessions(PIN_CODE)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("On Time =", current_time)
        sleep(random.uniform(10, 15))
