import shutil,os,glob,ssl,smtplib,sys

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


#Method to remove any old files from the meme folder 
#replaces with a fresh batch of memes
#with this implementation source dir is the ripme folder and dest being img folder
def moveMeme(sourceDir, destDir): 
    # files = glob.glob(folder to remove)
    files = glob.glob('folder/*')
    for f in files : 
        os.remove(f)
        # movees the memes from the sourcedir to the img folder
    files2 = os.listdir(sourceDir)
    for y in files2:
        shutil.move(sourceDir+y,destDir)

def sendMeme(psWd):
    # some variables for ease of use
    me = "rsenstudios@gmail.com"
    you = ['rishsen2000@gmail.com', 'rsenstudios@gmail.com']
    password = psWd# best not to save password on file for security purposes
    msg = MIMEMultipart()
    msg['Subject'] = 'Memes(Version 2.1)'
    msg['From'] = me    
    msg['To'] = ", ".join(you)

    path = "folder/"
    pngfiles = glob.glob( os.path.join(path, "*.png") )
    # gets all .png extensions files ready to send 
    for file in pngfiles:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
        fp = open(file, 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
 
    # Send the email via our own SMTP server.

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(me, password)
        server.sendmail(
            me, you, msg.as_string()
     )
    



moveMeme('img/','folder/')
psWd = sys.argv[1]
sendMeme(psWd)