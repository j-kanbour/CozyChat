import React from 'react';
import { createStackNavigator } from 'react-navigation-stack';
import { createAppContainer } from 'react-navigation';
import ChatScreen from 'src/pages/ChatScreen';
import HomeScreen from 'src/pages/HomeScreen';

const AppNavigator = createStackNavigator(
  {
    Home: HomeScreen,
    Chat: ChatScreen,
  },
  {
    initialRouteName: 'Home',
  }
);

export default createAppContainer(AppNavigator);
