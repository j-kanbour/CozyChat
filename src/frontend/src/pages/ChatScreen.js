// ChatScreen.js
import React, { useState } from 'react';
import { View, TextInput, Button, Text, ScrollView } from 'react-native';

const ChatScreen = () => {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([]);

  const sendMessage = () => {
    if (message.trim() !== '') {
      setMessages([...messages, message]);
      setMessage('');
    }
  };

  return (
    <View>
      <ScrollView>
        {messages.map((msg, index) => (
          <Text key={index}>{msg}</Text>
        ))}
      </ScrollView>
      <TextInput
        value={message}
        onChangeText={(text) => setMessage(text)}
        placeholder="Type your message..."
      />
      <Button title="Send" onPress={sendMessage} />
    </View>
  );
};

export default ChatScreen;
