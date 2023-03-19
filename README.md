# m3u8-to-wpl CLI
A playlist converter from .wpl format to .m3u8, and from .m3u8 to .wpl, a passion project for personal use. Edit the code appropriately to suit your needs.

Main motivation for this project is that there is no open source coverter for wpl and m3u8. I use WMP for music streaming as the minilyrics plugin is the only good lyrics floater that I could find. HMU if you have found better alternatives.

## Demo
# .wpl to .m3u8
CLI command: python playlist_converter_2023.py --wpltom3u8 <playlist_path></br>
![wpltom3u8_command](https://user-images.githubusercontent.com/74093833/226176116-af7f9a30-100f-4c8c-91a1-90a798983322.JPG)

Left: Waltzes.wpl (original); Right: Waltzes.m3u8 (generated)</br>
![wpltom3u8](https://user-images.githubusercontent.com/74093833/226176125-54e6a7e8-86a8-4915-9189-d8751aa77d43.JPG)

# .m3u8 to .wpl
CLI command: python playlist_converter_2023.py --m3u8towpl <playlist_path></br>
![m3u8towpl_command](https://user-images.githubusercontent.com/74093833/226176249-9a259664-e84f-45e9-981e-aa8441b76b3f.JPG)

A folder is created with local music copied into.</br>
(IMPORTANT) Requires user to drag this folder into a new wmp playlist for wmp to create a wmp playlist.</br>
![m3u8towpl_created](https://user-images.githubusercontent.com/74093833/226176431-f0809b64-e7d0-41d5-80c4-3a4340c81e86.JPG)</br>
(IMPORTANT) Copy playlist generated <playlist_name>_original_path.txt</br>
![original_path](https://user-images.githubusercontent.com/74093833/226176478-be43b6a5-068c-40df-8062-54ac8ea035c4.JPG)</br>
Left: Karaoke_routine.m3u8 (original); Right: Karaoke_routine.wpl (generated and edited)</br>
(IMPORTANT) Replace wmp created playlist with generated playlist.</br>
![m3u8towpl](https://user-images.githubusercontent.com/74093833/226176524-c97b725e-bbcc-4e8a-9d9c-ccdc51b43695.JPG)
