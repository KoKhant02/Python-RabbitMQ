import pika

def send_message():
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='hello')

    # Send a message to the queue
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello RabbitMQ!')

    print(" [x] Sent 'Hello RabbitMQ!'")
    connection.close()

if __name__ == "__main__":
    send_message()
