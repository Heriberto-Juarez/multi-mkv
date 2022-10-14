import os

output_folder = './output'
input_file = input("Enter the name of the MP4 file \n")

output_file = os.path.join(output_folder, input_file + '-no-sound.mp4')

input_file_path = os.path.join('./output', input_file + '.mp4')
print("Removing sound... \n")

os.system("ffmpeg -i " + input_file_path + " -c copy -an " + output_file)

print("Sound removed.\n")
