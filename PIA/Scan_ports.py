import shodan
import logging	
import json

# Generate a config for the file error


# Request the necesary info to make the shodan api search in format list
ip_array = input("Please enter the public ip to be analyzed separated by"\
    " commas: \n> ")
ips = ip_array.split(',')

# The shodan api key to authenticate our search in the api
api_key = 'qYsYnBh8c6vx820iWeJc9VwzFMcIUU5l'
try:
    api = shodan.Shodan(api_key)
except shodan.APIError as error:
    print('>> Ocurrió un error con la API: \n%s' % error)
    logging.basicConfig(filename='ShodanAPIRequest.log',
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %H:%M:%S",
                        level=logging.ERROR)
    logging.error(f"Error: {error}")

# Save the response in a txt file to make reading easier
with open('API_Response.txt','w') as file:
    for ip in ips:
        try:
            response = api.host(ip)
            file.write(f"<< Open ports in IP : {ip} >>\n")
            for port in response['ports']:
                file.write(f"> {port} <\n")
            file.write("Scan complete, Have a nice day :D")
        
        except shodan.APIError as error:
            print('>> Ocurrió un error con la API: \n%s' % error)
            logging.basicConfig(filename='ShodanAPIRequest.log',
                                format="%(asctime)s %(message)s",
                                datefmt="%m/%d/%Y %H:%M:%S",
                                level=logging.ERROR)
            logging.error(f"Error: {error}")
            
        except Exception as error:
            print('>> Ocurrió un error: \n%s' % error)
            logging.basicConfig(filename='ShodanAPIRequest.log',
                                format="%(asctime)s %(message)s",
                                datefmt="%m/%d/%Y %H:%M:%S",
                                level=logging.ERROR)
            logging.error(f"Error: {error}")
            
        else:
            response = api.host(ip)
            full_response_file_name = 'Response.txt'
            with open(full_response_file_name, 'w') as file:
                data = json.dumps(response, indent=4)
                file.write(data)
                file.write('\n')
                file.write('-'*30)
                
            
        
