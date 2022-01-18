# by Colten Haggard
import os

def main():
    # Tuples to hold file types I want to keep
    document_type = (".docx", ".html", ".htm", ".odf", ".ods", ".odt.", ".pdf", ".ppt", ".pptx", ".rtf", ".txt", ".xls", ".xlsx")
    image_type = (".bmp", ".dds", ".gif", ".jpeg", ".jpg", ".png", ".tiff", ".webp", ".xcf")
    video_type = (".mov", ".mp4", ".webm")
    music_type = (".mp3", ".wav")

    # Lists to hold paths to the folders I want those file types to go to
    usr = "Colten"
    doc_dir = "C:\\Users\\" + usr + "\\Documents\\"
    pic_dir = "C:\\Users\\" + usr + "\\Pictures\\"
    vid_dir = "C:\\Users\\" + usr + "\\Videos\\"
    music_dir = "C:\\Users\\" + usr + "\\Music\\"
    download_dir = "C:\\Users\\" + usr + "\\Downloads\\"

    # Test directories
    test_dl_dir = "C:\\VisualStudioCode\\Python Projects\\DownloadCleaner\\test_dl_dir\\"
    test_tgt_dir = "C:\\VisualStudioCode\\Python Projects\\DownloadCleaner\\test_tgt_dir\\"

    # A count of the various file types to keep plus a list for items to be removed
    doc_count = []
    pic_count = []
    vid_count = []
    music_count = []
    rem_count = []

    # Runs through every file in the download directory and checks what type it is and where it should go
    for entry in os.scandir(download_dir):
        # Checks if the directory is a document and also a file
        if entry.path.endswith(document_type) and entry.is_file():
            doc_count.append(entry.path)
            cur_dir = doc_dir
            entry_name = entry.name.split('.')

            # Using try except to catch the error caused by os.rename() when a file has the same name to add (n) to the end of the file that is being moved
            try:
                os.rename(entry.path, cur_dir + entry.name)
            except OSError:
                on = True
                count = 1

                while(on):
                    try:
                        os.rename(entry.path, cur_dir + entry_name[0] + "(" + str(count) + ")." + entry_name[1])
                    except OSError:
                        count += 1
                    else:
                        on = False
            print(entry.path + " was moved to " + cur_dir)
        # Checks if the directory is a picture and also a file
        elif entry.path.endswith(image_type) and entry.is_file():
            pic_count.append(entry.path)
            cur_dir = pic_dir
            entry_name = entry.name.split('.')

            # Using try except to catch the error caused by os.rename() when a file has the same name to add (n) to the end of the file that is being moved
            try:
                os.rename(entry.path, cur_dir + entry.name)
            except OSError:
                on = True
                count = 1

                while(on):
                    try:
                        os.rename(entry.path, cur_dir + entry_name[0] + "(" + str(count) + ")." + entry_name[1])
                    except OSError:
                        count += 1
                    else:
                        on = False
            print(entry.path + " was moved to " + cur_dir)
        # Checks if the directory is a video and also a file
        elif entry.path.endswith(video_type) and entry.is_file():
            vid_count.append(entry.path)
            cur_dir = vid_dir
            entry_name = entry.name.split('.')

            # Using try except to catch the error caused by os.rename() when a file has the same name to add (n) to the end of the file that is being moved
            try:
                os.rename(entry.path, cur_dir + entry.name)
            except OSError:
                on = True
                count = 1

                while(on):
                    try:
                        os.rename(entry.path, cur_dir + entry_name[0] + "(" + str(count) + ")." + entry_name[1])
                    except OSError:
                        count += 1
                    else:
                        on = False
            print(entry.path + " was moved to " + cur_dir)
        # Checks if the directory is music and also a file
        elif entry.path.endswith(music_type) and entry.is_file():
            music_count.append(entry.path)
            cur_dir = music_dir
            entry_name = entry.name.split('.')

            # Using try except to catch the error caused by os.rename() when a file has the same name to add (n) to the end of the file that is being moved
            try:
                os.rename(entry.path, cur_dir + entry.name)
            except OSError:
                on = True
                count = 1

                while(on):
                    try:
                        os.rename(entry.path, cur_dir + entry_name[0] + "(" + str(count) + ")." + entry_name[1])
                    except OSError:
                        count += 1
                    else:
                        on = False
            print(entry.path + " was moved to " + cur_dir)
        # Removes unwanted files
        else:
            # Checks if the directory is a file and removes the file if it is a file
            if entry.is_file():
                rem_count.append(entry.path)
                os.remove(entry.path)
                print(entry.path + "was removed.")
    
    print("\nDocuments\n")
    print(doc_count)
    print("\nPictures\n")
    print(pic_count)
    print("\nVideos\n")
    print(vid_count)
    print("\nMusic\n")
    print(music_count)
    print("\nTo be deleted\n")
    print(rem_count)


if __name__ == "__main__":
    main()
