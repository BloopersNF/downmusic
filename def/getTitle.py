
# Get the titles of the video by the txt file
def getTitle(file):
    with open (file, 'r') as file:
        title = file.read()
    return title
