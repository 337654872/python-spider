import os

class DownloadFile4():

    def __init__(self, filePath):
        self.__filePath = filePath;

    def checkAndCreatePath(self):
        if not os.path.exists(self.__filePath):
            os.makedirs(self.__filePath)
            print('创建文件夹: %s' %self.__filePath)

    def downloadImage(self, Image):
        with open(self.__filePath,'wb') as f:
            f.write(Image)
            f.flush()
            f.close()

    def downloadContent(self, Content):
        with open(self.__filePath, 'w') as f:
            f.write(Content)
            f.flush()
            f.close()

    def getCurrentTime(self):
        pass