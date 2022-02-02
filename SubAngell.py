SUBTRACK = "This is the sentence I will use as a test. \n\nPlease do not touch"
BANLIST = {"sentence":"phrase", "test":"practice", "please":"por favor"}

subtitle_track = SUBTRACK.split("\n")
subtrack = ''

x = -1
for line in subtitle_track:
    x += 1
    subtitle_track[x] = subtitle_track[x].split()
    for word in subtitle_track[x]:
        if word.lower() in BANLIST:
            subtrack = subtrack + BANLIST[word] + ' '
        else:
            subtrack = subtrack + word + ' '
    subtrack = subtrack + '\n' 

print(subtrack)
