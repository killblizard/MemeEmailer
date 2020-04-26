import shutil,os,glob,ssl,smtplib,sys

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


#Method to remove any old files from the meme folder
#replaces with a fresh batch of memes
#with this implementation source dir is the ripme folder and dest being img folder
def moveMeme(sourceDir, destDir):
    # files = glob.glob(folder to remove)
    os.system('find /home/kb/MEME/rips/reddit_sub_memes/ . -maxdepth 1 -type f |head -15| xargs mv -t "/home/kb/MEME/memesToSend"')

def sendMeme(psWd):
    # some variables for ease of use
    me = "rsenstudios@gmail.com"
    you = ['rishsen2000@gmail.com', 'rsenstudios@gmail.com']
    password = psWd# best not to save password on file for security purposes
    msg = MIMEMultipart()
    msg['Subject'] = 'Meme Sender Bot(Version 2.3)'
    msg['From'] = me
    msg['To'] = ", ".join(you)

    path = "memesToSend/"
    pngfiles = glob.glob( os.path.join(path, "*.png") )
    # gets all .png extensions files ready to send
    for file in pngfiles:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
        fp = open(file, 'rb')
        img = MIMEImage(fp.read(), _subtype="png")
        fp.close()
        msg.attach(img)

    # Send the email via our own SMTP server.

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(me, password)
        server.sendmail(
            me, you, msg.as_string()
     )



psWd = sys.argv[1]
sendMeme(psWd)
moveMeme('/home/kb/MEME/rips/reddit_sub_memes/','memesToSend/')
