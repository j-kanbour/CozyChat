// SignInScreen.js
import React, { useState } from 'react';
import { View, TextInput, Button, StyleSheet} from 'react-native';

const SignInScreen = ({ navigation }) => {
  const [name, setName_in] = useState('');
  const [identifier, setPass_in] = useState('');

  const [name_2, setName_up] = useState('');
  const [identifier_2, setPass_up] = useState('');
  const [identifier_3, pubkey_up] = useState('');

  const handleSignIn = () => {
    // You can perform validation here and navigate to the main app screen if the input is valid.
    // For simplicity, let's just navigate to the main screen without validation.
    navigation.navigate('Home');
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
        onPress={handleSignIn}
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
