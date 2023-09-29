// HomeScreen.js
import React from 'react';
import { View, Button } from 'react-native';

const HomeScreen = ({ navigation }) => {
  return (
    <View>
      <Button
        title="lst old Chats"
        onPress={() => navigation.navigate('Chat')} // navageate to chat with other indv
      />
      <Button
        title="New Chat"
        onPress={() => navigation.navigate('Chat')}
      />
    </View>
  );
};

export default HomeScreen;
