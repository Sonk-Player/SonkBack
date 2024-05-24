


def mapperSong(data):
    song = {
        "title"  : data["videoDetails"]["title"] ,
        "videoId" : data["videoDetails"]["videoId"],
        "chanelId" : data["videoDetails"]["channelId"],
        "author" : data["videoDetails"]["author"],
        "allowRatings": data["videoDetails"]["allowRatings"],
        "thumbnails" : data["videoDetails"]["thumbnail"]["thumbnails"],
        "durationSeconds": data["videoDetails"]["lengthSeconds"],
        "viewCount": data["videoDetails"]["viewCount"],
        }
        
    return song
        
        