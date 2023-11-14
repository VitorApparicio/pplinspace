# spacemenu

## Função:
- Abre menu de opções retornando:
  - O número de pessoas no espaço conforme json disponibilizado em [People-In-Space](http://open-notify.org/Open-Notify-API/People-In-Space/).
  - A posição atual da ISS conforme json disponibilizado em [ISS-Position](http://api.open-notify.org/iss-now.json).

## Requerimentos:
  - python3.x
  - requirements.txt

## Uso:
```
  git clone https://github.com/VitorApparicio/spacemenu
  pip install -r requirements.txt
  python3.x spacemenu.py
```
  ## Retorno:
  - Sucesso - Type Int - Número de pessoas segundo o último json disponível no site.
  - Sucesso - Type String - Posição de Latitude e Longitude da ISS.
  - Falha - Retorno do menu.

