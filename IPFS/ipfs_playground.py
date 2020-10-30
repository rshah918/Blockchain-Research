'''
Goal:
    Transfer encrypted files across IPFS
    Be able to search the network for any file's metadata,
        -but only authorized users can see the contents of the file
        -Used encrypted ZIP files for this

    1: Create file called "encryptedfile.txt"
    2: CLI: "zip -er encryptedfile.zip encryptedfile.txt"
        -Create a password for the file
    3: CLI: "ipfs add encryptedfile.zip -w"
        -The -w wraps the file in a directory before uploading to IPFS
            -This allows you to preserve file hierarchy
            -Allows you to see metadeta for the file
        -Returns 2 hashes: First hash is for the file,
            second is for the top level directory.
    4: CLI: "ipfs cat <file hash>"
       -Use the first hash, which is the hash of the file, not the top level directory
       -Prints the raw bytes of the file to the terminal.
            -Basically just garbage
    5: CLI: "ipfs ls -v <directory hash>"
        -This displays metadata about all files in the directory
    6: CLI: "ipfs get <directory hash>"
        -This actually downloads the file from IPFS to your local file system
        -Creates a directory with the same name as the hash and stores it in there
    7: CLI: "cd <directory hash>"
        -Enter the newly made folder
    8: CLI: "unzip encryptedfile.zip"
        -enter password
'''
