import React, { useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput, Image, TouchableOpacity, useColorScheme } from 'react-native';
//ha a git LF ezik akk ez : git config --global core.autocrlf true
export default function App() {
  const [gepIpcime, gepIpcimBeallit] = useState('');
  const [elmentettgepIpcime, elmentettgepIpcimBeallit] = useState('');
  const [settingLathato, settingLegyenLathato] = useState('');

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
      <Button title={settingLathato ? "Bezárás" : "Új gép hozzáadása"} onPress={() => settingLegyenLathato(!settingLathato)} />
      {settingLathato && (
        <View style={{ marginTop: 20, width: "100%", alignItems: "center" }}>
          <Text>Add meg a PC IP címét:</Text>
          <TextInput
            style={styles.input}
            value={gepIpcime}
            onChangeText={gepIpcimBeallit}
            placeholder="192.168.x.x"
          />
          <Button title="IP mentése" onPress={gepIPelementese} />
        </View>
      )}
      {/* hatra pause resume eolre */}
      <View style={{ flexDirection: "row", justifyContent: "space-between", width: "80%", marginTop: 20 }}>
        <TouchableOpacity onPress={() => Utasito('hatra')}>
          <Image source={require('./assets/hatra.png')} style={{ width: 70, height: 70, top: 30 }} />
        </TouchableOpacity>

        <TouchableOpacity onPress={() => Utasito('pause')}>
         <Image source={require('./assets/rP.png')} style={{ width: 130, height: 130 }} />
        </TouchableOpacity>

        <TouchableOpacity onPress={() => Utasito('elore')}>
          <Image source={require('./assets/fwd.png')} style={{ width: 70, height: 70, top: 30 }} />
        </TouchableOpacity>
      </View>
      {/* mute hang le fel  */}
      <View style={{ flexDirection: "row", justifyContent: "space-between", width: "80%", marginTop: 30 }}>
        <TouchableOpacity onPress={() => Utasito('mute')}>
          <Image source={require('./assets/M.png')} style={{ width: 70, height: 70, left: -20 }} />
        </TouchableOpacity>
        <TouchableOpacity onPress={() => Utasito('hangle')}>
          <Image source={require('./assets/VOLD.png')} style={{ width: 100, height: 75 }} />
        </TouchableOpacity>
        <TouchableOpacity onPress={() => Utasito('hangfel')}>
          <Image source={require('./assets/VOLU.png')} style={{ width: 100, height: 75, left: 30 }} />
        </TouchableOpacity>
      </View>
      {/* pc controls */}
      <View style={{ marginTop: -300, marginLeft: -280 }}>
        <TouchableOpacity onPress={() => Utasito('leallit')}>
          <Image source={require('./assets/shutdown.png')} style = {{width: 70, height: 70}} resizeMode='contain' />
        </TouchableOpacity>
      </View>
      <View style={{ marginTop: 300, marginLeft: 0 }}>
        <TouchableOpacity onPress={() => Utasito('egerfel')}>
          <Image source={require('./assets/FEL.jpg')} style = {{width: 90, height: 90}} resizeMode='contain' />
        </TouchableOpacity>
      </View>
      <View style={{ marginTop: 10, marginLeft: -200 }}>
        <TouchableOpacity onPress={() => Utasito('egerbal')}>
          <Image source={require('./assets/B2.jpg')} style = {{width: 100, height: 100}} resizeMode='contain' />
        </TouchableOpacity>
      </View>
      <View style={{ marginTop: -100, marginLeft: 200 }}>
        <TouchableOpacity onPress={() => Utasito('egerjobb')}>
          <Image source={require('./assets/J.jpg')} style = {{width: 100, height: 100}} resizeMode='contain' />
        </TouchableOpacity>
      </View>
      <View style={{ marginTop: 0, marginLeft: 0 }}>
        <TouchableOpacity onPress={() => Utasito('egerle')}>
          <Image source={require('./assets/LE.jpg')} style = {{width: 100, height: 100}} resizeMode='contain' />
        </TouchableOpacity>
      </View>

      <View style={{ marginTop:-325, marginLeft: -235 }}>
        <TouchableOpacity onPress={() => Utasito('balclick')}>
          <Image source={require('./assets/LC.jpg')} style = {{width: 100, height: 100}} resizeMode='contain' />
        </TouchableOpacity>
      </View>
      <View style={{ marginTop: -100, marginLeft: 235 }}>
        <TouchableOpacity onPress={() => Utasito('jobbclick')}>
          <Image source={require('./assets/RC.jpg')} style = {{width: 100, height: 100}} resizeMode='contain' />
        </TouchableOpacity>
      </View>
      <View style={{ marginTop: 150, marginLeft: 240 }}>
        <TouchableOpacity onPress={() => Utasito('fel')}>
          <Image source={require('./assets/SU.jpg')} style = {{width: 150, height: 150}} resizeMode='contain' />
        </TouchableOpacity>
      </View>
      <View style={{ top: -150, left: -120}}>
        <TouchableOpacity onPress={() => Utasito('le')}>
          <Image source={require('./assets/SD.jpg')} style = {{width: 150, height: 150}} resizeMode='contain' />
        </TouchableOpacity>
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
