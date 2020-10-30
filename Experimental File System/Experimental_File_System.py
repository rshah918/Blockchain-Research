import ipfshttpclient

class FileSystem:
    def __init__(self):
        '''
        filename_resolver: Nested hash table that maps filenames to its respective hash.
        reference_list: Hash table that keeps track of how many references each IFPS file has.
            -This is needed to only allow files to be deleted when its last reference is deleted
        client: Underlying IPFS node that performs block-level deduplication
        '''
        self.filename_resolver = {}
        self.reference_list = {}
        self.client = ipfshttpclient.connect()

    def saveFile(self,filename):
        '''Save a file to the IPFS filesystem, update file system global records'''
        res = self.client.add(filename)
        #map filename to file hash
        hash = res['Hash']
        self.filename_resolver[filename] = hash
        print("File " + filename + " added to the IPFS file system.\n")
        print("The file's hash is: ", hash)
        #increment reference count for that file hash
        if hash in reference_list:
            reference_list[hash] +=1
        else:
            reference_list[hash] = 1

    def readFile(self, filename):
        '''Read a file by resolving the filename and querying IPFS'''
        hash = self.filename_resolver[filename]
        file = self.client.cat(hash)
        print(file.decode("utf-8"))

    def moveFile(self):
        '''Move a file from one location to another'''
        pass

    def deleteFile(self):
        '''Delete a file'''
        pass


filename = input("Enter filename: ")
filesystem = FileSystem()
filesystem.saveFile(filename)
filesystem.readFile(filename)
