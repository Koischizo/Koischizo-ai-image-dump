# Written by ChatGPT because im lazy
import os

# Open the file in read mode
with open('./LICENSE', 'r') as f:
        # Read the contents of the file
        license = f.read()


# Open the file in write mode
with open('README.md', 'w') as f:
        # Write a string to the file
        f.write(f"# SchizoDev's AI image dump\nDo whatever you wanna do \n### License\n```{license}```\n## Images\n")


# Set the directory you want to read from
directory = './images/'

# Use a for loop to read all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.png'):  # Only read files with the .txt extension
            with open('README.md', 'a') as f:
                # Do something with the file
                f.write(f"![{filename}](./images/{filename})\n")
