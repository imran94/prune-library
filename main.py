import os, sys, ntpath

def iterateFilesAndDelete(playlist, dirName):
    listOfFiles = os.listdir(dirName)
    print("Iterating through directory " + dirName)

    for entry in listOfFiles:
        path = os.path.join(dirName, entry)

        if os.path.isdir(path):
            # print(entry + " is directory")
            iterateFilesAndDelete(playlist, path)
        else:
            removeIfNotExists(playlist, path)

def removeIfNotExists(playlist, path):
    # print(track)
    track = ntpath.basename(path)
    isInPlaylist = False
    for name in playlist:
        if name == track:
            isInPlaylist = True

    if not isInPlaylist:
        print("Track " + track + " not in playlist. Deleting...")
        os.remove(path)

if __name__ == '__main__':
    playlistName = ""
    dirName = "."
    playlistName = sys.argv[1]
    dirName = sys.argv[2]

    os.chdir(dirName)

    playlistFile = open(playlistName, "r")
    playlist = list()
    for l in playlistFile:
        line = l.rstrip()
        if line:
            playlist.append(line)

    # print("Playlist: ")
    # print(playlist)
    iterateFilesAndDelete(playlist, dirName)
