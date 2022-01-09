import React, { useState, useEffect } from 'react';
import MaterialTable from 'material-table';

export default function SearchResultTable() {

  const [data, setData] = useState([])
  const columns = [
    { title: "ID", field: "id" },
    { title: "Username", field: "username" },
    { title: "Name", field: "name" },
    { title: "Email", field: "email" },
    { title: "Phone", field: "phone" },
    { title: "Web Link", field: 'website' },

]
useEffect(() => {
fetch("https://jsonplaceholder.typicode.com/users")
  .then(resp => resp.json())
  .then(resp => {
    setData(resp)
  })
}, [])
  return (
      <MaterialTable
        title="Employee Data"
        data={data}
        columns={columns}
      />
  );
}
