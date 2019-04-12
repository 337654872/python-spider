from MyClass.ChromeOptions import ChromeOptions
from MyClass.DownloadFile import DownloadFile4

driverpaths = "D:\ProgramData\Anaconda3\Scripts\chromedriver.exe"
chromepaths = "C:\\Users\\yanfa\\AppData\\Local\Google\\Chrome\\Application\\chrome.exe"

down = DownloadFile4()
chrom =  ChromeOptions(chromepaths,driverpaths)

