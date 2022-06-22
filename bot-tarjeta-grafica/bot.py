import requests
import time

TARJETA1 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402&intl=nosplash"
TARJETA2 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440&intl=nosplash"
TARJETA3 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434&intl=nosplash"
CAMARA = "https://www.bestbuy.com/site/gopro-hero10-black-action-camera/6474501.p?skuId=6474501&intl=nosplash"

CLASE_HTML = "c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"

PRODUCTOS = [
  ("RTX 3060", TARJETA1),
  ("RTX 3080", TARJETA2),
  ("RTX 3090", TARJETA3),
  ("GO PRO", CAMARA),
  ("TELEVISION", "https://www.bestbuy.com/site/hisense-75-class-u9dg-series-dual-cell-4k-uled-android-tv/6457439.p?skuId=6457439&intl=nosplash")
]

HEADERS = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
  "Accept": "*/*"
}


def guardar(contenido: str, nombre: str = "res.html") -> None:
  with open(nombre, "w") as f:
    f.write(contenido)


def jalar_pagina(url: str) -> str:
  res = requests.get(url, headers=HEADERS)
  return res.text


def hay_en_existencia(html: str) -> bool:
  return CLASE_HTML in html


def main() -> None:
  for nombre, url in PRODUCTOS:
    html = jalar_pagina(url)
    if hay_en_existencia(html):
      print(f"CORRE! Hay {nombre} en existencia! Compralo ya: {url}")
    else:
      print(f"NO HAY {nombre} en existencia. :(")


if __name__ == "__main__":
  seconds = 60 * 5
  contador = 1
  while True:
    print(f"Corrida #{contador}...")
    main()
    time.sleep(seconds)
    contador += 1