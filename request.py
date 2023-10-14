
import json
import requests


url = 'https://refactored-cod-r5r6g5x6wpvcr6g-8000.app.github.dev/prediction'

input_data_for_model = {
    'narrative' : "I contacted XXXX XXXX to inquire as to why a transaction was taking so long. The agent verified a my mailing address. Immediately I advised her my mailing address was my XXXX XXXX XXXX XXXX, FL XXXX. The address that the agent provided me was an address Transition had listed as my address recently. After researching the address it is a home worth almost {$1.00} XXXX. It is disturbing to me that this is listed on Transuion credit bureau as my address and I am dealing with an insurance company and they mailed correspondence to this address. I did not provide this address not do I know anyone that lives there."
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)
