import sqlite3

con = sqlite3.connect("watch_later.db")
cur = con.cursor()

table_name = "watch_later"

cur.execute(f''' CREATE TABLE IF NOT EXISTS  {table_name}(
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL,
            duration TEXT NOT NULL)''')

def list_videos():
    cur.execute('''SELECT * FROM  watch_later''')
    print("\n" + '*' * 19 + " Watch later " + '*' * 19)
    for row in cur.fetchall():
        print(f"{row[0]}. {row[1]}, Duration: {row[2]}")
    print('*' * 51)

def add_video(name, duration):
    cur.execute(f'''INSERT INTO {table_name}(name, duration) 
                VALUES(?, ?)''', (name, duration))
    con.commit()

def update_video(index, new_name, new_duration):
    cur.execute(f'''UPDATE {table_name} SET name = ?, duration = ?
                WHERE id = ?''', (new_name, new_duration, index))
    con.commit()

def delete_video(index):
    cur.execute(f"DELETE FROM {table_name} WHERE id = ?", (index,))
    con.commit()

def main():
    print("** Youtube Watch Later Program **")
    while True:
        cur.execute(f"SELECT MAX(id) FROM {table_name}")
        last_row_id = cur.fetchone()[0]

        print("\n1. Print list of all videos")
        print("2. Add a new video")
        print("3. Update a videos's info")
        print("4. Delete a video from Watch Later")
        print("5. Exit Program")
        choice = input("Enter your choice (1-5): ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter name of the video: ")
                duration = input("Enter duration of the video: ")
                add_video(name, duration)
            case '3':
                list_videos()
                index = int(input("Enter the ID of the video you want to update: "))
                if 1<= index <= last_row_id:
                    new_name = input("Enter name of the video: ")
                    new_duration = input("Enter duration of the video: ")
                    update_video(index, new_name, new_duration)
                else:
                    print(f"No entry at index: {index}")
            case '4':
                list_videos()
                index = int(input("Enter the ID of the video you want to delete: "))
                if 1<= index <= last_row_id:
                    delete_video(index)
                else:
                    print(f"No entry at index: {index}")
            case '5':
                break
            case _:
                print("\nInvalid Input! Please enter numbers 1-5")

    con.close()


if __name__ == "__main__":
    main()