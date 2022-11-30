import pika
from pika.exchange_type import ExchangeType

#Função para receber a mensagem.

def on_message_received(ch, method, properties, body):
    print(f'Nova mensagem recebida: {body}')

#Conexão com o host em cloud.

url = f'amqps://gqrodjtl:bYuRxl-NwRFBXGJo3vstRGBbnUxlfoZk@jackal.rmq.cloudamqp.com/gqrodjtl'
parameters = pika.URLParameters(url)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#Metodo para criar uma exchange, mas caso já exista ele irá verificar se ela é da classe correta.

channel.exchange_declare(exchange='exchangeName', exchange_type=ExchangeType.fanout)

#Este método cria ou verifica uma fila.

queue = channel.queue_declare(queue='', exclusive=True)

#Vincula a fila a exchange nomeada.

channel.queue_bind(exchange='exchangeName', queue='')

#Consome e vincula as mensagens ao consumidor da função on_message_callback.

channel.basic_consume(queue='', auto_ack=True, on_message_callback=on_message_received)

print('<==== Filial - 01 ====>\n')
print('Aguardando mensagens...')

#Processa os eventos e despacha os timers e callbacks(do basic_consume) até que todos os consumidores sejam cancelados.

channel.start_consuming()
