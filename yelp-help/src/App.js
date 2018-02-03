import React, { Component } from 'react';
import Search from  './components/Search'
// import {BrowserRouter as Router, Route} from 'react-router-dom'
import './App.css';

class App extends Component {
  constructor() {
      super()

      this.state = {
        searched: false,
        results: [],
        loading: false
      }
  }

  render() {
    return (
      <div>
        <Search 
          updateSearchTerm={this.updateSearchTerm} />
      </div>
    );
  }
}

export default App;