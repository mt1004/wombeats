import logo from './logo.svg';
import './App.css';
import * as React from 'react';
import ReactDOM from 'react-dom';
import SearchInputForm from './SearchInputForm.js';
import SearchResultTable from './SearchResultTable.js';

function App() {
  return (
            <div>
                <SearchInputForm />
                <SearchResultTable />
            </div>
         );
}

export default App;