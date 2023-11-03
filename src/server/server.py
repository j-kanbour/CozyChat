import asyncio
import websockets
from signal_protocol import SignalProtocolStore, SignalProtocolAddress, SessionCipher
from signal_protocol.store.signal_protocol_store import SignalStore, InMemorySignalProtocolStore
from signal_protocol.store.session_store import InMemorySessionStore

async def chat_server(websocket, path):
    # Generate identity key pair for the server
    server_identity_key_pair = SignalProtocolStore.generate_identity_key_pair()
    server_registration_id = 12345  # Replace with actual registration ID

    # Create a session store and session cipher for the server
    server_store = InMemorySignalProtocolStore(server_identity_key_pair, server_registration_id)
    server_session_store = InMemorySessionStore(server_store)
    server_session_cipher = SessionCipher(server_store, server_session_store)

    # Store the client WebSocket connection and associated cipher
    clients = {}

    try:
        async for message in websocket:
            # Decrypt the incoming message
            plaintext = server_session_cipher.decrypt_prekey_whisper_message(message)

            # Broadcast the decrypted message to all clients
            for client, client_cipher in clients.items():
                if client != websocket:
                    encrypted_message = client_cipher.encrypt(plaintext)
                    await client.send(encrypted_message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Remove the client from the dictionary when they disconnect
        del clients[websocket]

start_server = websockets.serve(chat_server, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
print('Chat server with Signal Protocol is running on port 8080')
asyncio.get_event_loop().run_forever()
