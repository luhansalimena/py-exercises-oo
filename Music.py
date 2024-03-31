class Music:
    name = ''
    artist = ''
    duration = 0

    def __init__(self,name,artist,duration) -> None:
        self.name = name
        self.artist = artist
        self.duration = duration

musica1 = Music('Bohemian Rhapsody','Queen',355)

musica2 = Music('Imagine','John Lennon',183)

musica3 = Music('Shape of You','Ed Sheeran',234)
