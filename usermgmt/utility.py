import os
from emailtest import settings
from django.core.mail import EmailMessage
from emailtest.settings import EMAIL_HOST_USER
import zipfile
import requests

# to scrap files from urls
def _scrapfiles(urlslist):
    FileNames = []
    for url in urlslist:
        try:
            r = requests.get(url)
            file_name = os.path.join(settings.MEDIA_ROOT, url.split('.')[1] + ".html")
            with open(file_name, 'w+') as burn:
                burn.write(r.text)
                FileNames.append(file_name)
        except:
            import sys
            print str(sys.exc_info())
    return FileNames



# to zip files
def _zipfiles(FileNames):
    with zipfile.ZipFile(settings.MEDIA_ROOT + 'new.zip', 'w') as myzip:
        for f in FileNames:
            myzip.write(f)
        myzip.close()
    return  True

# to send mails to user
def _sendemail(to_email):
    try:
        msg = EmailMessage('Scrapped files ', 'Downloadable file', EMAIL_HOST_USER, [to_email])
        msg.content_subtype = "html"
        msg.attach_file(os.path.join(settings.MEDIA_ROOT,'new.zip'))
        msg.send()
        sucess=True
    except:
        sucess=False
        import sys
        print sys.exc_info()
    return sucess


