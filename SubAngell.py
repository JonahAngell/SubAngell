SUBTRACK = "This is the sentence I will use as a test"
BANLIST = {"sentence":"phrase", "test":"practice"}

subtitle_track = SUBTRACK.split()
subtrack = '' 
x = - 1

for word in subtitle_track:
    x += 1
    if BANLIST(word):
        subtrack = subtrack + BANLIST(word) + ' '
    else
        subtrack = subtrack + word

print(subtrack)
