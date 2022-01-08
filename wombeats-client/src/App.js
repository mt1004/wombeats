import logo from './logo.svg';
import './App.css';
import * as React from 'react';
import ReactDOM from 'react-dom';
import SearchInputForm from './SearchInputForm.js';
import SearchResultTable from './SearchResultTable.js';
import axios from 'axios';
import API from "./utils/API";

class App extends React.Component {

  constructor(props) {
    super(props);

    let search = window.location.search;
    let params = new URLSearchParams(search);
    let artist = params.get('artist');
    let album = params.get('album');
    let track = params.get('track');
    let genre = params.get('genre');
    let year = params.get('year');
    let fromBpm = params.get('fromBpm');
    let toBpm = params.get('toBpm');

    this.state = {
      isLoading: true,

      artist: artist,
      album: album,
      track: track,
      year: year,
      genre: genre,
      fromBpm: fromBpm,
      toBpm: toBpm,

      results: [],
    };
  }

  on_field_change() {


  }

  render() {
        const { artist, album, track, year, genre, fromBpm, toBpm } = this.state;

        return (
            <div>
                <SearchInputForm
                    artist={artist}
                    album={album}
                    track={track}
                    year={year}
                    genre={genre}
                    from_bpm={fromBpm}
                    to_bpm={toBpm}
                />
                <SearchResultTable />
            </div>
        );
  }

  async componentDidMount() {

  }
}

export default App;