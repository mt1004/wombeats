import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';

export default function SearchInputForm() {
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
                    <TextField
                      id="outlined-name"
                      label="Artist"
                      defaultValue=""
                    />
                    <TextField
                      id="outlined-name"
                      label="Album"
                      defaultValue=""
                    />
                    <TextField
                      id="outlined-name"
                      label="Track"
                      defaultValue=""
                    />
                    <TextField
                      id="outlined-name"
                      label="Year"
                      defaultValue=""
                    />
                    <TextField
                      id="outlined-name"
                      label="Genre"
                      defaultValue=""
                    />
                    <TextField
                      id="outlined-name"
                      label="From BPM"
                      defaultValue=""
                    />
                    <TextField
                      id="outlined-name"
                      label="To BPM"
                      defaultValue=""
                    />
                    <Button variant="contained">Search</Button>
                </Box>
            </div>
         );

}