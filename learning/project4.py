# 将文件夹备份到一个ZIP文件中

import zipfile,os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file

    folder = os.path.abspath(folder) # convert to absolute path

    number = 1
    # while True:
    zipFileName = 'd:\\'+os.path.basename(folder) + '_' + str(number) + '.zip'
    # if not os.path.exists(zipFileName):
    #     break
    # number = number + 1

    #  Create the Zip file
    print('Create %s ...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Walk the entire folder tree and compress the files in each other
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the  current folder to the ZIP file
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))

    backupZip.close()

    print('Done.')

backupToZip('D:\\pythonTest2')