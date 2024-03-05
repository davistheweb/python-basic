
def track_phone_number(phone_number):
    url=f"http://apilayer.net/api/validate? access_key={72e0256781323e3b663b544f92a12a5e}&number={+2347046387195}&country_code=&format=1"
    response = requests.get(url)
    data = response.json()

    if'valid' in data and data['valid']:
        print(f"Phone Number:{data['number']}")
        print(f"Country:{data['country_name']}")
        print(f"Location:{data['country_name']}")
        print(f"Carrier:{data['carrier']}")
        print(f"Line Type: {data['line_type']}")
    else:
        print("invalid phone number.")