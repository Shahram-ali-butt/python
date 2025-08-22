import requests
import random

def get_quote():
    random_id = random.randint(0, 100)

    url = f"https://api.freeapi.app/api/v1/public/quotes/{random_id}"
    response = requests.get(url) 
    res = response.json()
    if res["success"] and "data" in res:
        quote = res["data"]
        author = quote["author"]
        content = quote["content"]
        return (author, content)
    else:
        raise Exception("Could not fetch data!")
    
def main():
    try:
        (author, content) = get_quote()
        print(f"Quote: {content}")
        print(f"Author: {author}")
    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    main()
