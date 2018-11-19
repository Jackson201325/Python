def make_album(artist, album, tracks=""):
    if tracks:
        song = {'Artist': artist, 'Album': album, 'Number of tracks': tracks}
    else:
        song = {'Artist': artist, 'Album': album}
    print(song)


def __repr__(self):
    return song


a = make_album('Kendrik Lamar', 'Damn')
b = make_album('Mac Miller', 'Swimming', '15')
c = make_album('Eminem', 'Kamikaze')
