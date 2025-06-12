# Bot de Notificaciones Telegram

Este bot recibe señales vía webhook de TradingView y envía avisos a Telegram.

## Variables de entorno

- `TELEGRAM_TOKEN`  
- `TELEGRAM_CHAT_ID`

## Despliegue en Railway

1. Crear nuevo proyecto en Railway.
2. Conectar a tu repo GitHub.
3. En **Variables**, añade `TELEGRAM_TOKEN` y `TELEGRAM_CHAT_ID`.
4. En **Start Command**, pon:
