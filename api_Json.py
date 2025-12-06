import requests
import json

api_url = "https://jsonplaceholder.typicode.com/posts/1" 

try:
    # Make a GET request to the API
    response = requests.get(api_url)

    response.raise_for_status() 

    # Parse the JSON response into a Python dictionary
    data = response.json()

    print("Successfully fetched data from the API:")
    print(f"Type of data: {type(data)}")
    print("Fetched data:")
    print(json.dumps(data, indent=2))

    # Access specific elements of the data
    print(f"\nTitle of the post: {data['title']}")
    print(f"Body of the post: {data['body']}")

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
except KeyError as e:
    print(f"Key error accessing data: {e}")


#     Successfully fetched data from the API:
# Type of data: <class 'dict'>
# Fetched data:
# {
#   "userId": 1,
#   "id": 1,
#   "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#   "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
# }

# Title of the post: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Body of the post: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto

