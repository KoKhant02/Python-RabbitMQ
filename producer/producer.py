import pika

# Setup connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='hello')

print("Producer is running. Type your message and press Enter (Ctrl+C to stop):")

try:
    while True:
        # Wait for user input
        message = input("Enter message: ")
        
        # Send message to the queue
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=message)
        
        # Print the log for sent message
        print(f"Successfully Sent Message '{message}' to queue.")
        
except KeyboardInterrupt:
    print("\nProducer stopped.")
finally:
    # Close the connection when Ctrl+C is pressed
    connection.close()
