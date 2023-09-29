from datetime import datetime
from simple_salesforce import Salesforce
import csv
import os
import json

if not os.environ.get("PRODUCTION"):
    from dotenv import load_dotenv
    load_dotenv()

#SALESFORCE_USERNAME = os.getenv('SALESFORCE_USERNAME');
#PASSWORD = os.getenv('PASSWORD');
#SECURITY_TOKEN = os.getenv('SECURITY_TOKEN');
#DOMAIN=os.getenv('DOMAIN');

SALESFORCE_USERNAME = os.getenv('SALESFORCE_USERNAME');
PASSWORD = os.getenv('PASSWORD');
SECURITY_TOKEN = os.getenv('SECURITY_TOKEN');
DOMAIN = os.getenv('DOMAIN');

def main():
    print('Please wait ...')
    #print(SALESFORCE_USERNAME)
    #print(PASSWORD)
    #print(SECURITY_TOKEN)
    #return SALESFORCE_USERNAME
    # Authentication settings details33
    sf = Salesforce(username=SALESFORCE_USERNAME,
                    password=PASSWORD,
                    security_token=SECURITY_TOKEN,
                    domain=DOMAIN)

    # Lead Column setting to be acquired
    columns = [
        "Id",
        "Email",
        "Company",
        "Address",
        "Phone",
        "FirstName",
        "LastName",
        "CreatedDate",
    ]
    sosl = 'SELECT {0[0]}, {0[1]}, {0[2]}, {0[3]}, {0[4]}, {0[5]}, {0[6]} , {0[7]} FROM Lead '.format(
        columns)
    lastName = input('Enter Last Name : ')
    leadStatus = input('Enter Status  : ')
    companyName = input('Enter Company Name  : ')
    #data = [{'LastName': 'Demo Call', 'Company': 'Test', 'Status': 'Open - Not Contacted'}]
    data = [{'LastName': lastName, 'Company': companyName, 'Status': leadStatus}]
    x = sf.bulk.Lead.insert(data, batch_size=10000, use_serial=True)
    print(x)
    # Data acquisition with SOSL Implementation
    data = sf.query_all(sosl)

    # Delete CSV file if it exists1
    output_csv = 'output.csv'
    if os.path.exists(output_csv):
        os.remove(output_csv)

    # Write to CSV file
    for k, v in data.items():
        if type(v) is list:
            with open(output_csv, 'w', newline="") as f:
                writer = csv.DictWriter(f, fieldnames=columns)
                writer.writeheader()
                for d in v:
                    data = json.loads(json.dumps(d))
                    del data['attributes']
                    d = datetime.strptime(
                        data['CreatedDate'], '%Y-%m-%dT%H:%M:%S.%f%z')
                    data['CreatedDate'] = d.strftime('%Y-%m-%d %H:%M:%S')
                    writer.writerow(data)


if __name__ == '__main__':
    main()


