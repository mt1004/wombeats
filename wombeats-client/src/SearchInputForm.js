import React, { useReducer } from "react";
import { Button, Icon, TextField, Paper, Typography, Box } from "@mui/material/";
import PropTypes from "prop-types";
import API from "./utils/API";

export function SearchInputForm(props) {

    const { artist, album, track, year, genre, fromBpm, toBpm } = props;

    const [formInput, setFormInput] = useReducer(
        (state, newState) => ({ ...state, ...newState }),
        {
          artist: artist,
          album: album,
          track: track,
          year: year,
          genre: genre,
          fromBpm: fromBpm,
          toBpm: toBpm,
        }
    );

    const handleInput = evt => {
        const name = evt.target.name;
        const newValue = evt.target.value;
        setFormInput({ [name]: newValue });
        console.log(formInput);
    };

    console.log(artist);

    return (
        <div>
            <Box
              component="form"
              sx={{
                '& > :not(style)': { m: 1, width: '25ch' },
              }}
              noValidate
              autoComplete="off"
            >
                <form>
                    <TextField
                      id="outlined-name"
                      label="Artist"
                      name="artist"
                      defaultValue={artist}
                      onChange={handleInput}
                    />
                    <TextField
                      id="outlined-name"
                      label="Album"
                      name="album"
                      defaultValue={album}
                      onChange={handleInput}
                    />
                    <TextField
                      id="outlined-name"
                      label="Track"
                      name="track"
                      defaultValue={track}
                      onChange={handleInput}
                    />
                    <TextField
                      id="outlined-name"
                      label="Year"
                      name="year"
                      defaultValue={year}
                      onChange={handleInput}
                    />
                    <TextField
                      id="outlined-name"
                      label="Genre"
                      name="genre"
                      defaultValue={genre}
                      onChange={handleInput}
                    />
                    <TextField
                      id="outlined-name"
                      label="From BPM"
                      name="fromBpm"
                      defaultValue={fromBpm}
                      onChange={handleInput}
                    />
                    <TextField
                      id="outlined-name"
                      label="To BPM"
                      name="toBpm"
                      defaultValue={toBpm}
                      onChange={handleInput}
                    />
                    <Button type="submit" variant="contained">Search</Button>
                </form>
            </Box>
        </div>
     );
}

SearchInputForm.propTypes = {
  artist: PropTypes.string,
  album: PropTypes.string,
  track: PropTypes.string,
  year: PropTypes.string,
  genre: PropTypes.string,
  fromBpm: PropTypes.number,
  toBpm: PropTypes.number,
};

export default SearchInputForm;