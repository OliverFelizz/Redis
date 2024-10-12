import redis


def publish_messages():
    # Conectar a Redis
    client = redis.StrictRedis(host='localhost', port=6379, db=0)
    
    channel = 'mi_canal'

    while True:
        message = input("Ingresa un mensaje para publicar (o 'salir' para terminar): ")
        if message.lower() == 'salir':
            break
        
        # Publicar el mensaje
        client.publish(channel, message)
        print(f"Publicado: {message}")

    print("Publicador terminado.")

if __name__ == '__main__':
    publish_messages()
