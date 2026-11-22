// Web sürümünü (index.html, en/index.html ...) Android paketine kopyalar ve
// uygulama içinde çalışması için küçük düzeltmeler yapar.
// Kullanım: node hazirla.js [web klasörü]   (varsayılan: ../01_Web_Uygulama)
const fs = require('fs'), path = require('path');
const SRC = path.resolve(process.argv[2] || path.join(__dirname, '..', '01_Web_Uygulama'));
const OUT = path.join(__dirname, 'www');
fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(path.join(OUT, 'en'), { recursive: true });

const kopyala = f => fs.copyFileSync(path.join(SRC, f), path.join(OUT, f));
['icon.png', 'gizlilik.html', 'en/icon.png', 'en/privacy.html'].forEach(kopyala);

// Dil seçimi: ilk açılışta telefon Türkçe değilse İngilizce sürüm açılır,
// kullanıcı dil bağlantısına dokununca seçimi hatırlanır.
const dilTR = `<script>try{var d=localStorage.getItem("dil");if(d==="en"||(!d&&!/^tr/i.test(navigator.language||"")))location.replace("en/index.html")}catch(e){}</script>`;
const dilEN = `<script>try{if(localStorage.getItem("dil")==="tr")location.replace("../index.html")}catch(e){}</script>`;
const dilTik = `<script>document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest("a");if(!a)return;var h=a.getAttribute("href")||"";try{if(h==="en/index.html")localStorage.setItem("dil","en");if(h==="../index.html")localStorage.setItem("dil","tr")}catch(x){}},true)</script>`;

function duzelt(html, dilKodu) {
  let n = 0;
  const rep = (a, b) => { const k = html.split(a).length - 1; n += k; html = html.split(a).join(b); return k; };
  // Uygulama içinde servis çalışanına gerek yok (dosyalar zaten pakette).
  if (!rep('navigator.serviceWorker.register("sw.js").catch(()=>{});', '')) throw new Error('SW kaydı bulunamadı');
  // Klasör bağlantıları paket içinde index.html'e gitmeli.
  if (dilKodu === 'tr') rep('href="en/"', 'href="en/index.html"');
  else rep('href="../"', 'href="../index.html"');
  html = html.replace('<head>', '<head>' + (dilKodu === 'tr' ? dilTR : dilEN));
  html = html.replace('</body>', dilTik + '</body>');
  return { html, n };
}
for (const [f, k] of [['index.html', 'tr'], ['en/index.html', 'en']]) {
  const r = duzelt(fs.readFileSync(path.join(SRC, f), 'utf8'), k);
  fs.writeFileSync(path.join(OUT, f), r.html);
  console.log(f, 'hazır,', r.n, 'düzeltme');
}
