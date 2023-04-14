from urllib.parse import unquote
import re
from pathlib import Path
import os
import shutil
import argparse

def openfile(file_path):
    #return list
    open_file = open(file_path, encoding="utf8") #open target file
    return open_file.readlines() #list obj    

# a general detection fn, returns a dictionary of playlist
# name, count, list of songs
def extractPlaylist(file_path):
    playlist_dict = {"name":Path(file_path).stem}
    ls = openfile(file_path) #list obj
    playlist = []
    keyword = "Merge/" # m3u8towpl (CHANGE HERE)
    keyword2 = "<media src=\"" # wpltom3u8
    for line in ls:        
        if keyword in line: # m3u8towpl
            res = re.split(keyword, unquote(line))
            playlist.append((keyword + res[-1]).replace("/", "\\").strip())

        elif keyword2 in line: # wpltom3u8
            res = re.split(keyword2, line)
            res = res[-1][:-4].replace("\\", "/")
            res = re.split(keyword, res)
            try:
                res = res[1].split(sep='"')[0]
            except:
                continue
            #print(res)
            #print((keyword + res).strip())
            playlist.append((keyword + res).strip())            

    playlist_dict['playlist'] = playlist
    playlist_dict['count'] = len(playlist)
    return playlist_dict

def m3u8towpl(file_path, playlist_dict):
    # Make directory
    directory_dst = str(Path(file_path).parents[0]) + "\\" + playlist_dict['name']
    try:
        os.mkdir(directory_dst)
    except FileExistsError:
        print("Folder already exist!")

    root = "D:\\Music\\" # CHANGE HERE
    new_file = open(directory_dst + "_original_path.txt", "w", encoding='utf8')
    print("Copying...")
    for song in playlist_dict['playlist']:
        src = root + song
        new_file.write("<media src=\"" + src + '"/>' + "\n")
        dst = directory_dst + "\\" + os.path.basename(Path(song))
        
        shutil.copyfile(src, dst)
    new_file.close()
    print("Finished!")
    print("Next steps: Create new playlist in WMP, drag folder into new playlist")
    print("Next steps: Paste playlist from '<playlist_name>_original_path.txt' to the wmp playlist.")
    os.startfile(directory_dst)
    os.startfile(directory_dst + "\\" + os.path.basename(Path(song)))

def wpltom3u8(file_path, playlist_dict):
    # Create m3u8
    new_file = open(str(Path(file_path).parents[0]) + "\\" + Path(file_path).stem + ".m3u8", "w", encoding='utf8')
    new_file.write("#EXTM3U\n")
    for song in playlist_dict['playlist']:
        new_file.write("/storage/emulated/0/Music/" + song + "\n")   


# Main
parser = argparse.ArgumentParser(description='Covert Playlist')

parser.add_argument('--m3u8towpl', metavar='wpltom3u8', type=str, help='Enter File Path of m3u8 playlist')
parser.add_argument('--wpltom3u8', metavar='m3u8towpl', type=str, help='Enter File Path of WPL playlist')

args = parser.parse_args()

if args.m3u8towpl:
    # "D:\Music\Merge\Karaoke_routine.m3u8"
    file_path = args.m3u8towpl
    playlist_dict = extractPlaylist(file_path)
    m3u8towpl(file_path, playlist_dict)

elif args.wpltom3u8:
    # "C:\Users\dkfvkslghkd\Music\Playlists\Waltzes.wpl"
    file_path = args.wpltom3u8
    playlist_dict = extractPlaylist(file_path)
    wpltom3u8(file_path, playlist_dict)
