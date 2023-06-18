from PIL import ImageGrab

# Ekranın tamamını yakalamak için
#mevcut ekranın ekran görüntüsünü alır

screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")
