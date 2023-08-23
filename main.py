from brain import Brain

#--------------main-----------------#
date = input("Playlist of Top 100 songs of date (YYYY-MM-DD):  ")

brain = Brain(date)
brain.create_playlist() #creates playlist
brain.add_songs() #adds song
