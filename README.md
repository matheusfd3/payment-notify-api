# Payment Notify API

É uma API desenvolvida em Flask para gerenciar pagamentos PIX. A API permite a criação de pagamentos, geração de QR Codes, confirmação de pagamentos via webhook e comunicação em tempo real usando Socket.IO para atualizar a interface de usuário ao receber confirmações de pagamento.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python
- **Flask-SocketIO**: Comunicação em tempo real entre cliente e servidor
- **Flask-SQLAlchemy**: ORM para integração com banco de dados SQLite
- **SQLite**: Banco de dados relacional para armazenamento de dados de pagamentos
- **QRCode**: Geração de QR Codes para pagamentos

## Endpoints

### 1. Criar um pagamento PIX
- **Rota**: `/payments/pix`
- **Método**: `POST`
- **Descrição**: Cria um novo pagamento no sistema.
- **Armazenamento**: Os dados são salvos em um banco de dados SQLite.

### 2. Obter QR Code do pagamento
- **Rota**: `/payments/pix/qr_code/<file_name>`
- **Método**: `GET`
- **Descrição**: Retorna o arquivo `.png` do QR Code correspondente ao pagamento, onde `<file_name>` é o nome do arquivo de QR Code gerado.

### 3. Confirmar pagamento via Webhook
- **Rota**: `/payments/pix/confirm`
- **Método**: `POST`
- **Descrição**: Recebe a confirmação de pagamento via webhook enviado pelo banco. Atualiza o status do pagamento no sistema.

### 4. Visualizar status do pagamento
- **Rota**: `/payments/pix/<int:payment_id>`
- **Método**: `GET`
- **Descrição**: Retorna uma página HTML com o status do pagamento:
  - Se o pagamento não foi confirmado, carrega `payment.html`.
  - Se o pagamento foi confirmado, carrega `confirmed_payment.html`.
- **Observação**: Usa templates do Flask para renderizar as páginas HTML.

## Comunicação em Tempo Real

A aplicação utiliza **Socket.IO** para manter uma comunicação em tempo real entre o servidor e a página de pagamento.

- **Evento de Conexão**: Quando o cliente se conecta, a rota `@socketio.on("connect")` estabelece a comunicação com o servidor.
- **Confirmação de Pagamento**: Quando o banco confirma o pagamento via webhook, o servidor emite um evento Socket.IO para a página `payment.html`, que faz a atualização da interface para carregar `confirmed_payment.html`.

## Configuração do Ambiente

### Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/matheusfd3/payment-notify-api.git
   
   cd tasks-flask-crud
   ```
2. **Instale as dependências:**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Inicie o servidor:**
    ```bash
    python app.py
    ```