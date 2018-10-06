#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename date-stamps.

# TODO: Need to implement compression. Right now just adds to uncompressed zip file. look to zlib for help doing so
# TODO: Turn into full fledged program with many more features

import zipfile, os, datetime


 # filepath_YYYY-MM-SS
def dateStamp (filepathToStamp):
    dateStamp = str(datetime.date.today())
    dateStamp = filepathToStamp + '_' + dateStamp
    return dateStamp

 # filepath_YYYY-MM-SS_HHMMSS (HH, HHMM, HHMMSS possible)
def dateStampTime (filepathToStamp):
    dateStampTime = str(datetime.datetime.now())[:16] # Hours = 13, +Minutes = 16, +Seconds = 19
    dateStampTime = dateStampTime.replace(' ', '_').replace(':', '') # Tidy the name for Windows
    dateStampTime = filepathToStamp + '_' + dateStampTime
    return dateStampTime

# Safely creates a zip file at the given location. Allows for duplicate names
def createZipFolder(filepath):
    # Before creating .zip, check to see if it already exists
    if os.path.exists(filepath + '.zip'):
        # Name duplicates will follow a convention. Run through convention to find first available opening
        number = 2
        while True: # Loops until the break occurs
            modifiedFilepath = filepath + '_' + str(number)
            if not os.path.exists(modifiedFilepath + '.zip'):
                break
            number = number + 1
        # We now have a unique name. Create .zip
        zipPath = modifiedFilepath + '.zip'
    else:
        zipPath = filepath + '.zip'

    zipf = zipfile.ZipFile(zipPath, 'w', zipfile.ZIP_DEFLATED)
    return zipf

def zipFiles (filepath, zippath):
    lenDirPath = len(filepath)
    # Walk the entire folder tree and compress the files in each folder.
    for root, dirs, files in os.walk(filepath):
        # Add all the files in this folder to the ZIP file.
        for file in files:
            basePath = os.path.join(root, file)
            print (basePath)
            zippath.write(basePath, basePath[lenDirPath :]) # This removes the original filepath.

    zippath.close()

def backupToZip(filepath):
    # Backup the entire contents of "filepath" into a ZIP file.

    filepath = os.path.abspath(filepath) # Absolute version of pathname.

    # Choose one statement below. Comment out the Other
    # dateStamp will use the format YYYY-MM-SS
    # dateStampTime will use the format YYYY-MM-SS_HHMM (HH, HHMM, HHMMSS possible)

    # dateStampedFilepath = dateStamp(filepath)
    dateStampedFilepath = dateStampTime(filepath)

    backupZip = createZipFolder(dateStampedFilepath)
    zipFiles(filepath, backupZip)


if __name__ == '__main__':
    backupToZip('C:/Users/JMD/Pictures/FolderToBackup(2)');
