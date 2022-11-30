import pika
import sys
from pika.exchange_type import ExchangeType

#É recomendável abrir os outros programas simultaneamente.

#Através do terminal/prompt de comando, encontre o diretório do programa e digite:
 
#[ py .\NomeDoArquivo.py ]
#       ou
#[ python .\NomeDoArquivo.py]

#Conexão com o host em cloud.

url = f'amqps://gqrodjtl:bYuRxl-NwRFBXGJo3vstRGBbnUxlfoZk@jackal.rmq.cloudamqp.com/gqrodjtl'
parameters = pika.URLParameters(url)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#Metodo para criar uma exchange, mas caso já exista ele irá verificar se ela é da classe correta.

channel.exchange_declare(exchange='exchangeName', exchange_type=ExchangeType.fanout)

print('<=============== Matriz ==============> \n')

#Cria a mensagem.

for i in range(5):
    message = ' '.join(sys.argv[1:]) or input("Transmita mensagens para a rede: ")   
    #Publica a mensagem para o canal com os seguintes parametros.
    channel.basic_publish(exchange='exchangeName', routing_key='', body=message)
    print("\n Mensagem enviada: %r" % message)

#Encerra a conexão.

connection.close()

