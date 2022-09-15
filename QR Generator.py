
import pyqrcode 
from pyqrcode import QRCode


img="https://www.youtube.com"
url =pyqrcode.create(img)

url.svg("youtube_home page.svg",scale=20)
