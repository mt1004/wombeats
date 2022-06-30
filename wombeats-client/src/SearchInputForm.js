import React, { useReducer } from "react";
import { Button, Icon, TextField, Paper, Typography, Box, Checkbox, FormControlLabel } from "@mui/material/";
import PropTypes from "prop-types";
import API from "./utils/API";

export function SearchInputForm(props) {

    const { artist, album, track, year, genre, fromBpm, toBpm, newMusicFriday } = props;

    return (
        <div>
            <Box
              component="form"
              noValidate
              autoComplete="off"
                style={{
                    display: "flex",
                    flexDirection: "row",
                    alignItems: "center",
                    justifyContent: "center",
                    width: "90%",
                    height: "90%",
                    padding: "10px",
                    margin: "10px",
                    backgroundColor: "lightblue",
                    borderRadius: "10px",
                    boxShadow: "0px 0px 10px 0px rgba(0,0,0,0.75)",
                    border: "1px solid #ccc",
                    flex: "1",
                }}
            >
                <form>
                    <TextField
                      id="standard-basic"
                      label="&nbsp;&nbsp;Artist"
                      name="artist"
                      defaultValue={artist}
                      variant="standard"
                      style={{
                          boxShadow: "0px 0px 10px 0px rgba(0,0,0,0.75)",
                          backgroundColor: "white",
                      }}
                    />
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <TextField
                      id="standard-basic"
                      label="&nbsp;&nbsp;Album"
                      name="album"
                      defaultValue={album}
                      variant="standard"
                      style={{
                          boxShadow: "0px 0px 10px 0px rgba(0,0,0,0.75)",
                          backgroundColor: "white",
                      }}
                    />
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <TextField
                      id="outlined-name"
                      label="&nbsp;&nbsp;Track"
                      name="track"
                      defaultValue={track}
                      variant="standard"
                      style={{
                          boxShadow: "0px 0px 10px 0px rgba(0,0,0,0.75)",
                          backgroundColor: "white",
                      }}
                    />
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <TextField
                      id="outlined-name"
                      label="&nbsp;&nbsp;Year"
                      name="year"
                      defaultValue={year}
                      variant="standard"
                      style={{
                          boxShadow: "0px 0px 10px 0px rgba(0,0,0,0.75)",
                          backgroundColor: "white",
                      }}
                    />
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <TextField
                      id="outlined-name"
                      label="&nbsp;&nbsp;Playlist"
                      name="genre"
                      defaultValue={genre}
                      variant="standard"
                      style={{
                          boxShadow: "0px 0px 10px 0px rgba(0,0,0,0.75)",
                          backgroundColor: "white",
                      }}
                    />
                    <br/><br/>
                    <TextField
                      id="outlined-name"
                      label="&nbsp;&nbsp;From BPM"
                      name="fromBpm"
                      defaultValue={fromBpm}
                      variant="standard"
                      style={{
                          boxShadow: "0px 0px 10px 0px rgba(0,0,0,0.75)",
                          backgroundColor: "white",
                      }}
                    />
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <TextField
                      id="outlined-name"
                      label="&nbsp;&nbsp;To BPM"
                      name="toBpm"
                      defaultValue={toBpm}
                      variant="standard"
                      style={{
                          boxShadow: "0px 0px 10px 0px rgba(0,0,0,0.75)",
                          backgroundColor: "white",
                      }}
                    />
                    <br/><br/>
                    &nbsp;&nbsp;
                    <FormControlLabel
                        control={<Checkbox defaultChecked={newMusicFriday} />}
                        label="New Music Friday"
                        name="newMusicFriday"
                    />
                    <br/><br/>
                    <Button
                        type="submit"
                        variant="contained"
                        style={{
                            backgroundColor: "white",
                        }}
                    >Search</Button>
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <Button
                        href="/"
                        variant="contained"
                        style={{
                            backgroundColor: "white",
                        }}
                    >Reset</Button>
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
  newMusicFriday: PropTypes.string,
};

export default SearchInputForm;