const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.send('Hello World, express.')
})

app.listen(3000);

console.log('Server running at http://127.0.0.1:3000/');