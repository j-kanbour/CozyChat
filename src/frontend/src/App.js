import React from 'react';
import { createStackNavigator } from 'react-navigation-stack';
import { createAppContainer } from 'react-navigation';
import HomeScreen from 'src/pages/HomeScreen';
import SignInScreen from 'src/pages/SignUp';

const AppNavigator = createStackNavigator(
  {
    Sign: SignInScreen,
    Home: HomeScreen
  },
  {
    initialRouteName: 'Sign'
  }
);

export default createAppContainer(AppNavigator);
