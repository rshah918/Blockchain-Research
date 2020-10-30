import ipfshttpclient

class FileSystem:
    def __init__(self):
        '''
        filename_resolver: Nested hash table that maps filenames to its respective file hash.
        reference_list: Hash table that keeps track of how many references each file has.
            -This is needed to only allow files to be deleted when its last reference is deleted
        client: Underlying IPFS node that performs storage and block-level deduplication
        '''
        self.filename_resolver = {}
        self.reference_list = {}
        self.client = ipfshttpclient.connect()

    def resolveFileName(self, filename):
        '''Query global records to get the hash of a file from its filename'''
        filename_resolver = self.filename_resolver
        if filename not in filename_resolver:
            print("File does not exist!")
            exit(1)
        file_hash = filename_resolver[filename]
        return file_hash

    def saveFile(self,filename):
        '''Save a file to the IPFS filesystem, update file system global records'''
        reference_list = self.reference_list
        filename_resolver = self.filename_resolver
        #if file already exists, delete it's old hash from the global records
        if filename in filename_resolver:
            self.deleteFile(filename)
        #save the file
        res = self.client.add(filename)
        #map filename to file hash
        hash = res['Hash']
        filename_resolver[filename] = hash

        print("File " + filename + " added to the IPFS file system.\n")
        print("The file's hash is: ", self.resolveFileName(filename))
        #increment reference count for that file hash
        if self.resolveFileName(filename) in reference_list:
            reference_list[hash] += 1
        else:
            reference_list[hash] = 1
        print("Filename Resolver: ", filename_resolver)
        print("Reference List: ", reference_list)
    def readFile(self, filename):
        '''Read a file by resolving the filename and querying IPFS'''
        hash = self.filename_resolver[filename]
        file = self.client.cat(hash)
        print(file.decode("utf-8"))

    def moveFile(self):
        '''Move a file from one location to another'''
        pass

    def deleteFile(self, filename):
        '''
        Delete a file from the file system.
            -Updates global records to reflect file deletion, perform true deletion
                when reference count hits 0
        TODO: IPFS deletion!!!
        '''
        filename_resolver = self.filename_resolver
        reference_list = self.reference_list
        #decrement the number of references to the files hash
        if filename in filename_resolver:
            hash = self.resolveFileName(filename)
            reference_list[hash] -= 1
            #if number of references is 0, then delete the file from the filesystem
            if reference_list[hash] == 0:
                del reference_list[hash]
                #TODO: Delete file from IPFS node!!
        #delete filename->hash record
        if filename in filename_resolver:
            del filename_resolver[filename]




filename = input("Enter filename: ")
filesystem = FileSystem()
filesystem.saveFile('test.txt')
filesystem.saveFile('test2.txt')

#filesystem.readFile(filename)
