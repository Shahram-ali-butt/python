import json
file_name = 'watch_later.txt'

def get_videos():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []            

def save_video(video):
    with open(file_name, 'w') as file:
        json.dump(video, file)

def list_videos(videos):
    print("\n" + '*' * 19 + " Watch later " + '*' * 19)
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video["name"]}, Duration: {video["duration"]}")
    print('*' * 51)

def add_video(videos):
    name = input("Enter the name of the video: ")
    duration = input("Enter the duration of the video: ")
    videos.append({'name': name, 'duration': duration})
    save_video(videos)

def update_video(videos):
    list_videos(videos)
    index = int(input("Enter the index of the video you want to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter new name: ")
        duration = (input("Enter duration: "))
        videos[index - 1] = {"name": name, "duration": duration}
        save_video(videos)
    else:
        print(f"No video exists at index: {index}")

def delete_video(videos):
    list_videos(videos)
    index = int(input("Enter the index of the video you want to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_video(videos)
    else:
        print(f"No video exists at index: {index}")

def main():
    videos = get_videos()
    print("** Youtube Watch Later Program **")
    while True:
        print("\n1. Print list of all videos")
        print("2. Add a new video")
        print("3. Update a videos's info")
        print("4. Delete a video from Watch Later")
        print("5. Exit Program")
        choice = input("Enter your choice (1-5): ")

        match choice:
            case '1':
                list_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("\nInvalid Input! Please enter numbers 1-5")

if __name__ == "__main__":
    main()