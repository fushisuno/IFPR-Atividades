// index.tsx
import React, { useState } from 'react';
import { SafeAreaView, View, Text, Button, StyleSheet } from 'react-native';

const App = () => {
  const [visitorCount, setVisitorCount] = useState(0);

  const incrementCounter = () => {
    setVisitorCount(visitorCount + 1);
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.counterContainer}>
        <Text style={styles.title}>Contador de Visitantes</Text>
        <Text style={styles.count}>{visitorCount}</Text>
        <Button title="Adicionar Visitante" onPress={incrementCounter} />
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f0f0', // Fundo claro para melhor contraste
    justifyContent: 'center',
    alignItems: 'center',
  },
  counterContainer: {
    backgroundColor: '#ffffff', // Fundo branco para a área do contador
    padding: 20,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.2,
    shadowRadius: 2,
    elevation: 2,
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    fontWeight: 'bold',
  },
  count: {
    fontSize: 48,
    marginBottom: 20,
    color: '#333',
  },
});

export default App;
