import os
from dotenv import load_dotenv

def DaneLogowania(file,login, password):
    print(file)
    try:
        #load_dotenv(str(sys.argv[1])) #odpalamy pik .env
        load_dotenv(str(file))
        _login = login#str(sys.argv[2])
        _password = password#str(sys.argv[3])
        LOGIN = os.getenv(_login)
        PASSWORD = os.getenv(_password)
    except Exception as e:
        print(str(e))
    else:
        if LOGIN is None or PASSWORD is None:
            print("Podane argumenty są nie prawidłowe.")
            print(LOGIN)
            print(PASSWORD)
        else:
            print(LOGIN)
            print(PASSWORD)
            return {LOGIN, PASSWORD}
