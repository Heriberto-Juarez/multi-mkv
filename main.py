import os, random, string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    directory = input("Please enter the directory where MKV files are located.\n")
    isExist = os.path.exists(directory)

    outputFolder = './output'

    if not os.path.exists(outputFolder):
        os.mkdir(outputFolder)

    if isExist:
        print("The directory exists; Getting files...")
    else:
        print("Directory not found.")
        raise SystemExit

    print("Generating list of videos...")

    list_of_files = []

    videosList = os.path.join(outputFolder, './videos_list.txt')

    if os.path.exists(videosList):
        # Remove file before deleting.
        os.remove(videosList)

    with open(videosList, 'a') as f1:
        for root, dirs, files, in os.walk(directory):
            for file in files:
                f1.write("file '" + os.path.join(root, file) + "'\n")
                print("File found: " + file)

    outputName = ''
    while len(outputName) < 1:
        outputName = input("Write a title for your file.\n")
        outputName = os.path.join(outputFolder, outputName)

        print("Merging...")
        originalOutput = os.path.join(outputFolder, randomword(20))

        os.system(
            'ffmpeg  -loglevel info -f concat -safe 0  -i ' + videosList + ' -c copy   "' + originalOutput + '.mkv"')
        os.system('ffmpeg -i ' + originalOutput + '.mkv  -vcodec libx265 -crf 28 ' + outputName + '.mp4')

        if os.path.exists(originalOutput + '.mkv'):
            print("Deleting temporal mvk file.")
            os.remove(originalOutput + '.mkv')
        if os.path.exists(videosList):
            print("Deleting the list of videos.")
            os.remove(videosList)

        outputLocation = os.path.join(os.getcwd(), outputName + ".mp4")

        print("Completed! The output file is located at: " + outputLocation)
