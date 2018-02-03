import React, { Component } from 'react'
import Search from  './components/Search'
import request from 'async-request'
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

  updateSearchTerm = (searchTerm) => {
    console.log(searchTerm)
    if (searchTerm.length === 0) {
        return null
    } else {
        this.getSearchData(searchTerm).then((data) => {
            this.setState({
                searched: true,
                loading: false,
                results: data
            })
        })
    }
}

getSearchData = async (searchTerm) => {
  let response
  try {
      response = await request('http://localhost:8080/search/',{
        method: 'GET',
        data: {
          terms: 'pizza', location: 'Irvine'
        }
      });
    //   var request = require("request");

    //   var options = { method: 'GET',
    //     url: 'http://localhost:8080/search/',
    //     qs: { terms: 'pizza', location: 'irvine' }
    //   };

    // request(options, function (error, response, body) {
    //   if (error) throw new Error(error);
    // });
  } catch (e) {
      console.log(e)
  }
  let data
  try {
      data = await response.json()
  } catch (e) {
      console.log(e)
  }
  return data
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