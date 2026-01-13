import requests

# Paste your Raw URL here
url = "https://github.com/PavanNethminaDissanayake/Hello.py/blob/44398ae7ef3aeee00fafd37a6d3af5bd96aae317/Hello.py"

def fetch_file():
    try:
        # Sending a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (Status Code 200)
        if response.status_code == 200:
            print("--- File Fetched Successfully ---")
            print("Content of hello.py:\n")
            print(response.text)
        else:
            print(f"Failed to fetch file. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_file()
