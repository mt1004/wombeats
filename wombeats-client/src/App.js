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
    let newMusicFriday = params.get('newMusicFriday');

    this.state = {
      isLoading: true,

      artist: artist,
      album: album,
      track: track,
      year: year,
      genre: genre,
      fromBpm: fromBpm,
      toBpm: toBpm,
      newMusicFriday: newMusicFriday,

      results: [],
    };
  }

  on_field_change() {


  }

  render() {
        const { artist, album, track, year, genre, fromBpm, toBpm, newMusicFriday } = this.state;

        return (
            <div>
                <SearchInputForm
                    artist={artist}
                    album={album}
                    track={track}
                    year={year}
                    genre={genre}
                    fromBpm={fromBpm}
                    toBpm={toBpm}
                    newMusicFriday={newMusicFriday}
                />
                <SearchResultTable
                    artist={artist}
                    album={album}
                    track={track}
                    year={year}
                    genre={genre}
                    fromBpm={fromBpm}
                    toBpm={toBpm}
                    newMusicFriday={newMusicFriday}
                />
            </div>
        );
  }

}

export default App;