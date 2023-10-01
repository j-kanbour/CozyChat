import React, { useState } from 'react';
import { View, TextInput, Button, FlatList, Text, StyleSheet } from 'react-native';

const HomeScreen = ({ navigation }) => {
  const [text, setText] = useState('');
  const [messages, setMessages] = useState([]);
  const [displayedMessages, setDisplayedMessages] = useState([]);

  const handleTextChange = (newText) => {
    setText(newText);
  };

  const handleSend = () => {
    if (text.trim() !== '') {
      const newMessages = [...messages, text];
      setMessages(newMessages);
      setDisplayedMessages(newMessages.slice().reverse());

      // Clear the input field
      setText('');
    }
  };

  return (
    <View style={styles.container}>
      <FlatList
        data={displayedMessages}
        renderItem={({ item }) => (
          <View style={styles.messageContainer}>
            <Text style={styles.messageText}>{item}</Text>
          </View>
        )}
        keyExtractor={(item, index) => index.toString()}
        inverted={true} // Reverse the display order so newest messages are at the bottom
      />
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.textInput}
          placeholder="Enter text..."
          value={text}
          onChangeText={handleTextChange}
        />
        <Button
          title="Send"
          onPress={handleSend}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-start', // Align items at the top of the screen
    padding: 16, // Add padding if needed
  },
  inputContainer: {
    flexDirection: 'row', // Display input and button horizontally
    alignItems: 'center', // Align input and button vertically
  },
  textInput: {
    flex: 1, // Take up remaining space
    borderWidth: 1,
    borderColor: 'gray',
    padding: 8,
  },
  messageContainer: {
    alignSelf: 'flex-end', // Align messages to the right
    backgroundColor: '#EFEFEF', // Background color for messages
    padding: 8,
    borderRadius: 8,
    marginTop: 4, // Add spacing between messages
  },
  messageText: {
    textAlign: 'right', // Align text to the right
  },
});

export default HomeScreen;
