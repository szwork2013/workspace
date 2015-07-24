/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 */
'use strict';

var React = require('react-native');
//var ReactTabs=require('react-tabs');
//var Tab=ReactTabs.Tab;
//var Tabs=ReactTabs.Tabs;
//var TabList=ReactTabs.TabList;
//var TabPanel=ReactTabs.TabPanel;

var {
  AppRegistry,
  StyleSheet,
  Text,
  View,
} = React;

var FavoriTopic = React.createClass({
  //handleSelect:function(index,last){
  //  console.log('Selected tab: '+index+', Last tab: '+last);
  //},
  render: function() {
    return (
      <View style={styles.container}>
        <Text style={styles.welcome}>
          Welcome to React Native!!!!!
        </Text>
        <Text style={styles.instructions}>
          To get started, edit index.ios.js
        </Text>
        <Text style={styles.instructions}>
          Press Cmd+R to reload,{'\n'}
          Cmd+D or shake for dev menu
        </Text>
      </View>
    //  <Tabs
    //    onSelect{this.handleSelected}
    //    selectedIndex={2}
    //      >
    );
  }
});

var styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});

AppRegistry.registerComponent('FavoriTopic', () => FavoriTopic);
