import os
import logging
from flask import Flask, request, jsonify
import requests

# ——— Configurar logging ———
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# ——— Leer credenciales de entorno ———
TELEGRAM_TOKEN   = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Verificar variables
if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
    raise Exception('❌ Debes definir TELEGRAM_TOKEN y TELEGRAM_CHAT_ID en las variables de entorno.')

# ——— Función para enviar mensajes ———
def enviar_telegram(texto: str):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': texto}
    try:
        resp = requests.post(url, data=payload)
        if not resp.ok:
            logging.error(f'Telegram error {resp.status_code}: {resp.text}')
    except Exception as e:
        logging.error(f'Error enviando Telegram: {e}')

# ——— Crear app Flask ———
app = Flask(__name__)

# ——— Mensaje al arrancar ———
enviar_telegram('🤖 Bot de notificaciones activo y a la escucha de señales.')

@app.route('/webhook-eth', methods=['POST'])
def webhook_eth():
    data = request.get_json(force=True)
    logging.info(f'Señal recibida (ETH): {data}')
    action = data.get('action', '').upper()
    if action in ('BUY', 'SELL'):
        enviar_telegram(f'📢 Señal ETH: {action}')
        return jsonify({'status': 'ok'}), 200
    else:
        return jsonify({'error': 'acción inválida'}), 400

@app.route('/webhook-pepe', methods=['POST'])
def webhook_pepe():
    data = request.get_json(force=True)
    logging.info(f'Señal recibida (PEPE): {data}')
    action = data.get('action', '').upper()
    if action in ('BUY', 'SELL'):
        enviar_telegram(f'📢 Señal PEPE: {action}')
        return jsonify({'status': 'ok'}), 200
    else:
        return jsonify({'error': 'acción inválida'}), 400

# Puedes añadir más endpoints del mismo modo para otras monedas...

if __name__ == '__main__':
    # Railway utilizará este comando para arrancar
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
