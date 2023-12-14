# plex-file-renamer
# About
Python script for renaming media files according to Plex's naming conventions.
This script is useful when a Plex server does not automatically detect local media files and is unable to get content data for the files. Oftentimes renaming the file names and refreshing the library resolves this issue. This script is designed to make that process less tedious.
Guidelines I used for the file naming format: https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/

# Usage
This is an interactive program that does not take command-line arguments.
The user is first prompted for the directory path as well as the following data that Plex requires in its' file names: full name of the TV show, season number, release year, number for each episode.
The script is designed to work on any type of operating system, but was primarily tested on Linux Mint. Please create a new issue if there is a problem with this script running on your OS, or any other problem.
The only requirement to run this script is Python 3.


