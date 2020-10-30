'''
IPFS vs BitTorrent:
    1: Both are decentralized file systems:
        -Data is divided into blocks, these blocks are stored across all peers
            in the network, as opposed to a central server.
BitTorrent:
    2: Old BitTorrent requires a "tracker" for each file
        -A tracker keeps track of all peers that own a chunk of that file
        - To download a file on BitTorrent:
            1: Find the torrent discriptor file from the normal internet
                -This file contains a list of trackers for that file
            2: Connect to one single tracker in that list
            3: The tracker contains a list of all peers that have peices of the file you're trying to download
            4: Download all peices of the target file from that list of peers
                -Rarest peices are downloaded first
        - Aleviated with the introduction of the Distributed Hash Table
IPFS:
    3: Pure Content Addressing:
        -Global distributed hash table
        -Download a file just from its Hash
    4: De-duplication of blocks
        -If a peer has 2 extremely similar files, then only one instance of the
        overlapping sections + the differing section will be saved.
        -One of the main advantages of IPFS over BitTorrent
        -Only if the similarities are on the 256KiB block boundries

'''
