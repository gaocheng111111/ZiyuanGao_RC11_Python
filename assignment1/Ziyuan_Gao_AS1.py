# Imports:
# use python --version to check what version of python your standard installation is
# if this is 2.x you will have to use pip3 install otherwise pip install
# pip install pillow
import csv
import requests
from PIL import Image
from io import BytesIO

# Define the ArtTate class, with all attributes that you find usefull
class ArtTate:
    def __init__(self, id,accession_number,artist,artistRole,artistId,title,dateText,medium,creditLine,year,acquisitionYear,dimensions,width,height,depth,units,inscription,thumbnailCopyright,thumbnailUrl,url):
            self.id = id
            self.accession_number = accession_number
            self.artist = artist
            self.artistRole = artistRole
            self.artistId = artistId
            self.title = title
            self.dateText = dateText
            self.medium = medium
            self.creditLine = creditLine
            self.year = year
            self.acquisitionYear = acquisitionYear
            self.dimensions = dimensions
            self.units = units
            self.inscription = inscription
            self.thumbnailCopyright = thumbnailCopyright
            self.thumbnailUrl = thumbnailUrl
            self.url = url
            self.width = width
            self.depth = depth
            self.height = height
            self.imagePath = ""
# Define a function that prints a description
    def describe(self):
        print("id:" + self.id, "accession_number:" + self.accession_number, "artist:" + self.artist, "artistRole:" + self.artistRole, "artistId:" + self.artistId, "title:" + self.title, "dateText:" + self.dateText, "medium:" + self.medium, "creditLine:" + self.creditLine, "year:" + self.year, "acquisitionYear:" + self.acquisitionYear, "dimensions:" + self.dimensions, "width:" + str(self.width), "height:" + str(self.height), "depth:" + str(self.depth), "units:" + self.units, "inscription:" + self.inscription, "thumbnailCopyright:" + self.thumbnailCopyright)

# implement the get image function that saves the image to the specified folder
    def getImageFile(self):
        if self.thumbnailUrl:
            response = requests.get(self.thumbnailUrl)
        try:
            im = Image.open(BytesIO(response.content))
        except OSError:
            return None
        path = "Artimages/" + self.artist + "_" + self.id + ".jpg"
        self.imagePath = path
        im.save(path, "JPEG")

# Read in the rows of the artwork_data.csv file into a list of ArtTate objects
artPieces = []
with open("collection/artwork_data.csv", encoding = 'utf-8-sig') as artFile:
    artReader = csv.DictReader(artFile)

    for row in artReader:
        id = row['id']
        accession_number = row['accession_number']
        artist = row['artist']
        artistRole = row['artistRole']
        artistId = row['artistId']
        title = row['title']
        dateText = row['dateText']
        medium = row['medium']
        creditLine = row['creditLine']
        year = row['year']
        acquisitionYear = row['acquisitionYear']
        dimensions = row['dimensions']
        width = row['width']
        height = row['height']
        depth = row['depth']
        units = row['units']
        inscription = row['inscription']
        thumbnailCopyright = row['thumbnailCopyright']
        thumbnailUrl = row['thumbnailUrl']
        url = row['url']
        if width or depth or height:
            artPiece = ArtTate(id, accession_number, artist, artistRole, artistId, title, dateText, medium, creditLine, year, acquisitionYear, dimensions, width, height, depth, units, inscription, thumbnailCopyright, thumbnailUrl, url)
            artPieces.append(artPiece)
            print(artist)

# write a loop that saves all artwork thumbnails of an artist to a specific folder
for art in artPieces:
    if "Woodman" in art.artist:
        art.getImageFile()
