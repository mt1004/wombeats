import logo from './logo.svg';
import './App.css';
import * as React from 'react';
import ReactDOM from 'react-dom';
import SearchInputForm from './SearchInputForm.js';
import SearchResultTable from './SearchResultTable.js';
import axios from 'axios';

function App() {
  const submitHandler = (e) => {
        e.preventDefault();
        axios.post("http://localhost:8083/createmodule", state)
        .then( response => {
            console.log(response)
        })
        .catch( error => {
            console.log(error)
        })
        console.log(moduletype);
    }

  return (
            <div>
                <SearchInputForm onChange={handleChange}/>
                <SearchResultTable />
            </div>
         );
}

export default App;