import redis

def subscribe_messages():
    # Conectar a Redis
    client = redis.StrictRedis(host='localhost', port=6379, db=0)
    
    pubsub = client.pubsub()
    channel = 'mi_canal'
    
    # Suscribirse al canal
    pubsub.subscribe(channel)
    print(f"Suscrito al canal: {channel}")

    try:
        # Escuchar mensajes
        for message in pubsub.listen():
            # Ignorar mensajes de tipo 'subscribe'
            if message['type'] == 'message':
                print(f"Recibido: {message['data'].decode('utf-8')}")
    except KeyboardInterrupt:
        print("Suscriptor terminado.")
    finally:
        pubsub.unsubscribe()
        pubsub.close()

if __name__ == '__main__':
    subscribe_messages()
