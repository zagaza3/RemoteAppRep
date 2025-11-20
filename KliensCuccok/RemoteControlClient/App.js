import React, { useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';

export default function App() {
  const [gepIpcime, gepIpcimBeallit] = useState('');
  const [elmentettgepIpcime, elmentettgepIpcimBeallit] = useState('');

  useEffect(() => {
    const betoltIP = async () => {
      try {
        const ip = await AsyncStorage.getItem('szerver_ip');
        if (ip) {
          gepIpcimBeallit(ip);
          elmentettgepIpcimBeallit(ip);
        }
      } catch (e) {
        console.error('Valami nem jo az elso ip setting useeffectben:', e);
      }
    };
    betoltIP();
  }, []);

  const gepIPelementese = async () => {
    try {
      await AsyncStorage.setItem('szerver_ip', gepIpcime);
      elmentettgepIpcimBeallit(gepIpcime);
      alert('PC elemntve');
    } catch (e) {
      console.error('Valami nem jo ott ahol a szerveript mentem le:', e);
    }
  };

    const Utasito = async (utasitas) => {
    if (!elmentettgepIpcime) {
      alert('Ments el egy PC-t először!');
      return;
    }
    try {
      const valasz = await fetch(`http://${elmentettgepIpcime}:8000/${utasitas}`);
      const text = await valasz.text();
      console.log('Szerver valasza:', text);
    } catch (error) {
      console.error('Nem lehetett utasitas kuldeni:', error);
    }
  };

  return (
    <View style={styles.container}>
      <Text>Add meg a PC IP címét:</Text>
      <TextInput
        style={styles.input}
        value={gepIpcime}
        onChangeText={gepIpcimBeallit}
        placeholder="192.168.x.x"
      />
      <Button title="Save IP" onPress={gepIPelementese} />

      <View style={{ marginTop: 30 }}>
        <Button
          title="| | >"
          onPress={() => Utasito('pause')} 
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-start',
    alignItems: 'center',
    padding: 20,
    marginTop: 50,
  },
  input: {
    height: 40,
    width: '80%',
    borderColor: 'gray',
    borderWidth: 1,
    marginVertical: 10,
    paddingHorizontal: 10,
  },
});
