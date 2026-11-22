# Uygulama simgesi, uyarlanabilir simge, açılış ekranı ve Play Store simgesini üretir.
# Kullanım: python ikonlar.py   (Pillow gerekir: pip install pillow)
from PIL import Image, ImageDraw
import os
BG=(20,23,26,255); OR=(242,163,58,255); WH=(233,236,239,255)
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'android','app','src','main','res')

def pusula(size, scale=1.0, bg=True, round_=False):
    """512 birimlik tasarımı size pikselde çizer. scale: desenin büyüklüğü."""
    S=4; N=size*S; im=Image.new('RGBA',(N,N),(0,0,0,0)); d=ImageDraw.Draw(im)
    if bg:
        if round_: d.ellipse([0,0,N-1,N-1],fill=BG)
        else: d.rectangle([0,0,N,N],fill=BG)
    k=N/512*scale; c=N/2
    P=lambda x,y:(c+(x-256)*k, c+(y-256)*k)
    ro,ri=180*k,154*k
    d.ellipse([c-ro,c-ro,c+ro,c+ro],fill=OR); d.ellipse([c-ri,c-ri,c+ri,c+ri],fill=BG if bg else (0,0,0,0))
    d.polygon([P(256,108),P(300,256),P(212,256)],fill=OR)
    d.polygon([P(212,256),P(300,256),P(256,404)],fill=WH)
    h=16*k; d.ellipse([c-h,c-h,c+h,c+h],fill=BG)
    return im.resize((size,size),Image.LANCZOS)

dens={'mdpi':1,'hdpi':1.5,'xhdpi':2,'xxhdpi':3,'xxxhdpi':4}
for n,f in dens.items():
    m=os.path.join(R,'mipmap-'+n)
    pusula(int(48*f)).save(os.path.join(m,'ic_launcher.png'))
    pusula(int(48*f),round_=True,scale=1.12).save(os.path.join(m,'ic_launcher_round.png'))
    # Uyarlanabilir simge ön yüzü: 108dp tuval, desen 66dp güvenli alanın içinde
    pusula(int(108*f),scale=0.62,bg=False).save(os.path.join(m,'ic_launcher_foreground.png'))

# Açılış ekranları: koyu zemin, ortada simge
def splash(w,h,path):
    im=Image.new('RGBA',(w,h),BG); s=int(min(w,h)*0.42)
    im.alpha_composite(pusula(s,bg=False),((w-s)//2,(h-s)//2)); im.convert('RGB').save(path)
for root,_,files in os.walk(R):
    for fn in files:
        if fn=='splash.png':
            p=os.path.join(root,fn); w,h=Image.open(p).size; splash(w,h,p)

out=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','04_Play_Store','gorseller')
os.makedirs(out,exist_ok=True)
pusula(512).save(os.path.join(out,'play-simge-512.png'))
print('simgeler hazır')
