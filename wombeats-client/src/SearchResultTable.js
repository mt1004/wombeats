import React, { useState, useEffect } from 'react';
import MaterialTable from 'material-table';
import { Link } from 'react-router-dom'

export default function SearchResultTable(props) {

    const { artist, album, track, year, genre, fromBpm, toBpm, newMusicFriday } = props;

    const [data, setData] = useState([])
    const columns = [
        { title: "Artist", field: "artist" },
        { title: "Album", field: "album" },
        { title: "Track", field: "track" },
        { title: "BPM", field: "bpm" },
        {
            title: "Spotify",
            field: "track_uri",
            render: rowData => <a href={rowData.track_uri}>Open in Spotify</a>
        },
        { title: "Release Date", field: "release_date" },
        {
            title: "Browser",
            field: "external_url",
            render: rowData => <a href={rowData.external_url}>Open in browser</a>
        }

    ]

    useEffect(() => {
    fetch("https://np-song-matcher-bpm.herokuapp.com/search?isLoading=true&artist=" + artist + "&album=" + album + "&track=" + track + "&year=" + year + "&genre=" + genre + "&fromBpm=" + fromBpm  + "&toBpm=" + toBpm + "&newMusicFriday=" + newMusicFriday)
        .then(resp => resp.json())
        .then(resp => {
        setData(resp)
        })
    }, [])
    return (
        <MaterialTable
            title="Song Data"
            data={data}
            columns={columns}
            options={{
                paging:true,
                pageSize:20,       // make initial page size
                emptyRowsWhenPaging: false,   // To avoid of having empty rows
                pageSizeOptions:[20, 50, 100],    // rows selection options
            }}
        />
    );
}
