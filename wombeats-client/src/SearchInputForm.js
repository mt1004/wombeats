import React, { useReducer } from "react";
import { Button, Icon, TextField, Paper, Typography, Box } from "@mui/material/";
import PropTypes from "prop-types";
import API from "./utils/API";

export function SearchInputForm(props) {

    const { artist, album, track, year, genre, fromBpm, toBpm } = props;

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
                    />
                    <TextField
                      id="outlined-name"
                      label="Album"
                      name="album"
                      defaultValue={album}
                    />
                    <TextField
                      id="outlined-name"
                      label="Track"
                      name="track"
                      defaultValue={track}
                    />
                    <TextField
                      id="outlined-name"
                      label="Year"
                      name="year"
                      defaultValue={year}
                    />
                    <TextField
                      id="outlined-name"
                      label="Genre"
                      name="genre"
                      defaultValue={genre}
                    />
                    <TextField
                      id="outlined-name"
                      label="From BPM"
                      name="fromBpm"
                      defaultValue={fromBpm}
                    />
                    <TextField
                      id="outlined-name"
                      label="To BPM"
                      name="toBpm"
                      defaultValue={toBpm}
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
  year: PropTypes.number,
  genre: PropTypes.string,
  fromBpm: PropTypes.number,
  toBpm: PropTypes.number,
};

export default SearchInputForm;