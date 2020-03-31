"""
Problem:
Start with your program from Exercise 8-7. Write a while loop that allows users 
to enter an album’s artist and title. Once you have that information, call 
make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.
"""
def make_album(album_title, artist_name, num_of_track=''):
    """Return album detail"""
    detail = {
        'Album Title': album_title.title(),
        'Artist Name': artist_name.title()
    }
    return detail

while True:
    print("-- Press 'q' any time to quit --")
    album_name = input("Enter album name : ")
    if album_name == 'q':
        break
    artist_name = input("Enter artist name : ")
    if artist_name == 'q':
        break
    print(make_album(album_name, artist_name))