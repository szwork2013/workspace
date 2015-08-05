/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 */
'use strict';

var React = require('react-native');
var {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  ScrollView,
  TouchableOpacity,
  Image,
  PanResponder,
} = React;

var rebound = require('rebound');
var precomputeStyle=require('precomputeStyle');
var clamp = require('clamp');


var deviceWidth=
  require('Dimensions').get('window').width;



var ReactPage=React.createClass({
  render(){
    return(
        <ScrollView>
          <Image source={{uri:"http://sc5.io/blog/wp-content/uploads/2014/06/react.png"}}
                 style={{flex:1,height:320}} resizeMode="cover"/>
          <Text>
            JUST THE UI Lots of people use React as the V in MVC. Since React makes no assumptions about the rest of your technology stack, it's easy to try it out on a small feature in an existing project. VIRTUAL DOM React abstracts away the DOM from you, giving a simpler programming model and better performance. React can also render on the server using Node, and it can power native apps using React Native. DATA FLOW React implements one-way reactive data flow which reduces boilerplate and is easier to reason about than traditional data binding.
          </Text>
        </ScrollView>
      )
  }
})

var FlowPage =React.createClass({
  render(){
    return(
        <ScrollView>
          <Image source={{uri:"http://www.adweek.com/socialtimes/files/2014/11/FlowLogo650.jpg"}}
                 style={{flex:1,height:320}} resizeMode="contain"/>
          <Image source={{uri:"http://www.adweek.com/socialtimes/files/2014/11/FlowLogo650.jpg"}}
                 style={{flex:1,height:320}} resizeMode="contain"/>
          <Image source={{uri:"http://www.adweek.com/socialtimes/files/2014/11/FlowLogo650.jpg"}}
                 style={{flex:1,height:320}} resizeMode="contain"/>
        </ScrollView>
    )
  }
})

var JestPage=React.createClass({
  render(){
    return(
        <ScrollView>
          <Image source={{uri:"http://facebook.github.io/jest/img/opengraph.png"}}
                 style={{flex:1,height:320}} resizeMode="cover"/>
          <Image source={{uri:"http://facebook.github.io/jest/img/opengraph.png"}}
                 style={{flex:1,height:320}} resizeMode="cover"/>
          <Image source={{uri:"http://facebook.github.io/jest/img/opengraph.png"}}
                 style={{flex:1,height:320}} resizeMode="cover"/>
        </ScrollView>
    )
  }

})

var ScrollableTabView=React.createClass({
  getInitialState(){
    return {offsetX:0,}
  },
  componentDidMound(){
    this._scrollSpring.setCurrentValue(0);
  },
  componentWillMount(){
    this.currentPage=0;

    //Initialize the spring that will drive animations
    this.springSystem=new rebound.SpringSystem();
    this._scrollSpring=this.springSystem.createSpring();
    springConfig.tension=rebound.OrigamiValueConverter.tensionFromOrigamiValue(25);
    springConfig.friction=rebound.OrigamiValueConverter.frictionFromOrigamiValue(8);
    this._scrollSpring.setOvershootClampingEnabled(false);

    this._scrollSpring.addListener({
      onSpringUpdate:()=>{
        if(!this.scrollView||!this.tabUnderline){return}

        var numberOfTabs=this.props.children.length;
        var currentValue=this._scrollSpring.getCurrentValue();
        var offsetX=deviceWidth*currentValue;

        this.scrollView.setNativeProps(precomputeStyle({
              transform:[{translateX:-1*offsetX}],
            }));
        this.tabUnderline.setNatibeProps(precomputeStyle({
          left:offsetX/numberOfTabs
        }));
      },
    });

    this._panResponder=PanResponder.create({
      //Claim responder if it's a horizontal pan
      onMoveShouldSetPanResponder:(e,gestureState)=>{
        if(Math.abs(gestureState.dx)>Math.abs(gestureState.dy)){
          return true;
        }
      },
      //Touch is released , scroll to the one that you're closest to
      onPanResponderRelease:(e,gestureState)=>{
        var relativeGestureDistance=gestureState.dx/deviceWidth,
            lastPageIndex=this.props.children.length-1,
            vx=gestureState.vx;
        if(this.currentPage!=lastPageIndex&&(relativeGestureDistance<-0.5||(relativeGestureDistance<0&&vx<=0.5))){
          this.currentPage=this.currentPage+1;
        }else if(this.currentPage !=0 &&(relativeGestureDistance>0.5||(relativeGestureDistance>0&&vx>=0.5))){
          this.currentPage=this.currentPage-1;
        }
        this._scrollSpring.setEndValue(this.currentPage);
      },

      //Dragging,move the view with the touch
      onPanResponderMove:(e,gestureState)=>{
        var dx=gestureState.dx;
        var lastPageIndex=this.props.children.length-1;

        if(this.currentPage==0&&dx>0){
          //Don't set the spring if we're on the first page and trying to move before it
        }else if(this.currentPage == lastPageIndex && dx<0){
          //Don't set the spring if we're already o the last page and trying to move to the next
        }else{
          //This is awkward bcause when we are scrolling we are offsetting the underlying view
          // to the left(-x)
          var offsetX=dx-(this.currentPage*deviceWidth);
          this._scrollSpring.setCurrentValue(-1*offsetX/deviceWidth);
        }
      },
    });
  },
  goToPage(pageNumber){
    this._scrollSpring.setEndValue(pageNumber);
    this.props.onChangeTab&&
        this.props.onChangeTab({i:pageNumber,ref:this.props.children[pageNumber]});
  },
  renderTabOption(name,page){
    return(
        <TouchableOpacity key={name} onPress={()=>this.goToPage(page)}>
          <View style={styles.tab}>
            <Text>{name}</Text>
          </View>
        </TouchableOpacity>
    );
  },
  render(){
    var numberOfTabs=this.props.children.length;
    var tabUnderlineStyle={
      position:'absolute',
      width:deviceWidth/numberOfTabs,
      height:4,backgroundColor:'blue',bottom:0,
    }
    var sceneContainerStyle={
      width:deviceWidth*this.props.children.length,
      flex:1,flexDirection:'row'
    }

    return(
        <View style={{flex:1}}>
          <View style={styles.tabs}>
            {this.props.children.map((child,i)=>this.renderTabOption(child.key,i))}
            <View style={tabUnderlineStyle}
                ref={view=>{this.tabUnderline=view;}}/>
          </View>
          <View style={sceneContainerStyle}{...this._panResponder.panHandlers}
              ref={view=>{this.scrollView=view;}}>
            {this.props.children}
          </View>
        </View>
    )
  }
});

var A = React.createClass({
  render(){
    return (
      <ScrollableTabView>
        <ReactPage key="React"/>
      </ScrollableTabView>
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

AppRegistry.registerComponent('A', () => A);
