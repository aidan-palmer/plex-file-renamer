# Script to rename media files according to Plex's naming conventions

import os


def get_dir():
    dir = input("Path to directory: ")

    if dir[-1] != "/" or dir[-1] != "\\":
        os_type = os.name
        if os_type == "nt":
            dir += "\\"
        else:
            dir += "/"

    return dir


def get_name():
    name = input("What is the full name of the show? ")
    return name


def get_season():
    season = input("What season is this show? (integer digits only): ")

    if int(season) < 10:
        season = "0" + season

    return season


def get_year():
    year = input("What year was the show released? ")
    return year


def rename(source, destination):
    try:
        os.rename(source, destination)
    except FileNotFoundError:
        print("ERROR: file not found.")


def main():
    folder = get_dir()
    name = get_name()
    season = get_season()
    year = get_year()

    for filename in os.listdir(folder):
        source = folder + filename
        extension = filename[-4:]

        print("\n" + filename + "\n")
        ep_num = input("What episode number is this?(Or enter q to skip this file) ")
        
        if ep_num == "q":
            continue

        if int(ep_num) < 10:
            ep_num = "0" + ep_num

        destination = f"{folder}{name} ({year}) - s{season}e{ep_num}{extension}"

        rename(source, destination)   

    print("\nFiles renamed successfully!\n")






if __name__ == '__main__':
    main()