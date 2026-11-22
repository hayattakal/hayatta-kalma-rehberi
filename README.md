# Hayatta Kalma Rehberi · Android paketi

Bu klasör, rehberin web sürümünü (index.html ve en/index.html) Capacitor ile Android uygulamasına çevirir. Rehberin bütün içeriği APK'nın içine gömülür, bu yüzden uygulama ilk açılıştan itibaren internetsiz çalışır.

- Paket adı: `com.drozayapps.hayattakal` (Play Store'a ilk yüklemeden sonra değiştirilemez)
- Hedef: Android 16 (API 36), en düşük Android 7 (API 24)
- İzinler: yalnızca konum (Pusula ve Konum aracı için, isteğe bağlı)
- Dil: telefon Türkçe ise Türkçe, değilse İngilizce sürüm açılır. Ayarlardaki dil bağlantısıyla değiştirilebilir ve seçim hatırlanır.

## Deneme APK'sı (bilgisayara bir şey kurmadan)

Bu proje GitHub'daki `android` dalına yüklendiğinde GitHub Actions otomatik olarak bir deneme APK'sı derler:
GitHub → hayatta-kalma-rehberi → Actions → "Android APK (deneme sürümü)" → son çalışma → Artifacts → `hayatta-kal-deneme-apk`.
Zip'i açıp APK'yı telefona atın ve kurun (telefon "bilinmeyen kaynak" izni isteyebilir).

## Bilgisayarda derleme (Android Studio ile)

1. Node.js 22 ve Android Studio'yu kurun.
2. Bu klasörde: `npm install`
3. İçeriği kopyalayın: `node hazirla.js ../01_Web_Uygulama` ve ardından `npx cap sync android`
4. `npx cap open android` ile Android Studio'da açın, Build → Generate Signed App Bundle ile Play Store'a yüklenecek `.aab` dosyasını üretin.

Rehber içeriği her güncellendiğinde 3. adımı tekrarlayın ve `android/app/build.gradle` içindeki `versionCode` sayısını bir artırın.

## Simgeler

`python ikonlar.py` uygulama simgelerini, açılış ekranını ve Play Store simgesini yeniden üretir.

## İmzalama anahtarı (önemli)

Play Store'a yüklemek için bir yükleme anahtarı (upload key) gerekir. Bu anahtar ve şifresi asla GitHub'a konmamalı, güvenli bir yerde yedeklenmelidir. Play App Signing açık olduğu için anahtar kaybolursa Google'dan sıfırlama istenebilir, ama bu süreç zaman alır.
