import threading, zipfile, logging

class AsyncZip(threading.Thread):
    def __init__(self,infile,outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile,'w',zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt','myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()
print("Main program waited uaaaaaaawdwntil background was finished!")


logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found','server.conf')
logging.error("Error occured")
logging.critical('Critical error -- shutting down')

