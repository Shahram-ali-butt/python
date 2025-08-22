import requests

def get_response():
    url = "https://api.freeapi.app/api/v1/public/books"

    response = requests.get(url)
    res = response.json()
    if res["success"] and "data" in res:
        return res
    else:
        raise Exception("Could not fetch data!")

def getbooks():
    try:
        res = get_response()
        data = res["data"]
        books = data["data"]
        no_of_books = len(books)
        i = 0

        while i < no_of_books:
            title = books[i]["volumeInfo"]["title"]
            publisher = books[i]["volumeInfo"]["publisher"]
            preview_link = books[i]["volumeInfo"]["previewLink"]
            print(f"{i+1}. Title: {title}")
            print(f"Publisher: {publisher}")
            print(f"Preview Link: {preview_link}\n")
            i+=1

    except Exception as e:
        print(f"Could not fetch data! Error: {e}")

if __name__ == "__main__":
    getbooks()