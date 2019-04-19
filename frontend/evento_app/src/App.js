import React, { Component } from 'react';
import PrimarySearchAppBar from './components/NavBar';
import CenteredGrid from './components/Grid';

class App extends Component {
  render() {
    return (
      <div>
        <PrimarySearchAppBar/>
        <CenteredGrid />
      </div>
    );
  }
}

export default App;
