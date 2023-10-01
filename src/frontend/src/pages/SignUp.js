// SignInScreen.js
import React, { useState } from 'react';
import { View, TextInput, Button, StyleSheet} from 'react-native';
import axios from 'axios';

const SignInScreen = ({ navigation }) => {
  const [name, setName_in] = useState('');
  const [identifier, setPass_in] = useState('');

  const [name_2, setName_up] = useState('');
  const [identifier_2, setPass_up] = useState('');
  const [identifier_3, pubkey_up] = useState('');

  const handleNewSignUp = async () => {
    try {
        const response = await axios.post("C:/Users/r2jk3/Desktop/chat/CozyChat/src/backend/src/user.py", {
          username: name, // Send the username and password as JSON data
          password: identifier,
        });
  
        if (response.status === 200) {
          // Authentication successful
          navigation.navigate('Home'); // Navigate to the main app screen
        } else {
          // Handle authentication failure
          console.log('Authentication failed');
        }
      } catch (error) {
        // Handle network or server errors
        console.error('Error:', error);
      }
  };

  const handleSignIn = async () => {
    try {
      const response = await axios.post('C:/Users/r2jk3/Desktop/chat/CozyChat/src/backend/src/user.py', {
        username: name, // Send the username and password as JSON data
        password: identifier,
      });

      if (response.status === 200) {
        // Authentication successful
        navigation.navigate('Main'); // Navigate to the main app screen
      } else {
        // Handle authentication failure
        console.log('Authentication failed');
      }
    } catch (error) {
      // Handle network or server errors
      console.error('Error:', error);
    }
  };

  return (
    <View style={styles.container}>
        <TextInput
        style={styles.input}
        placeholder="Name"
        value={name}
        onChangeText={setName_in}
        />
        <TextInput
        style={styles.input}
        placeholder="Password"
        value={identifier}
        onChangeText={setPass_in}
        />
        <Button
        style={marginBottom=20}
        title="Sign In"
        onPress={handleNewSignUp}
        />

        <View style={styles.separator1} />
        <View style={styles.separator} />

        <TextInput
        style={styles.input}
        placeholder="Name"
        value={name_2}
        onChangeText={setName_up}
        />
        <TextInput
        style={styles.input}
        placeholder="Password"
        value={identifier_2}
        onChangeText={setPass_up}
        />
        <TextInput
        style={styles.input}
        placeholder="Public Key"
        value={identifier_3}
        onChangeText={pubkey_up}
        />
        <Button
        title="Sign Up"
        onPress={handleSignIn}
        />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  input: {
    width: '80%',
    marginBottom: 20,
    padding: 10,
    borderWidth: 1,
    borderColor: 'gray',
    borderRadius: 10,
  },
  button: {
    marginbottom: 20,
  },
  separator1: {
    width: '0%',
    marginBottom: 20,
  },
  separator: {
    height: 1,
    width: '80%',
    backgroundColor: 'gray',
    marginBottom: 20,
  },
});


export default SignInScreen;
