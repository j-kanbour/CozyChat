// HomeScreen.js
import React from 'react';
import { View, Button } from 'react-native';
import DynamicButtonList from 'src/components/dynamicbuttons';

const HomeScreen = ({ navigation }) => {
  return (
    <View>
      <DynamicButtonList />
      <Button
        title="New Chat"
        onPress={() => navigation.navigate('Chat')}
      />
    </View>
  );
};

export default HomeScreen;
