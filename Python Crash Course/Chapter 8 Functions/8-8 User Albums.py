def make_album(artist, album, tracks=""):
    if tracks:
        song = {'Artist': artist, 'Album': album, 'Number of tracks': tracks}
    else:
        song = {'Artist': artist, 'Album': album}


song = {}

while True:
    print("\nName the artist, album or number of tracks: ")
    print("(Press q to quit at any moment)")

    artist = input("Name of the artist: ")
    if artist == 'q':
        break
    song['Artist'] = artist

    album = input("Name of the Album: ")
    if album == 'q':
        break
    song['Album'] = album

    tracks = input("Number os tracks: ")
    if tracks == 'q':
        break
    song['Number of tracks'] = tracks
