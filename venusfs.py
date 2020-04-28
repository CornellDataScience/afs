from fuse import FUSE, FuseOSError, Operations
from filesystem import Filesystem
import venus
import os

class VenusFilesystem(Filesystem):
    def __init__(self, root, localfiles):
        self.root = root
        self.local = localfiles

    def open(self, path, flags=None):
        if path in self.local.key():
            #check whether the file is stored locally
            __file = os.open(self._full_path(self.get[path]),flags)
            print ("file in local cache")
            return __file
        else:
            # if not, make it a request message and run the request func
            file_name.type = "request"
            venus.request() #how do requests work
