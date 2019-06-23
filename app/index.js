const express = require('express');
const app = express();
const PORT = 3200


app.get('/', function(req, res) {
    res.send('200');
})

app.listen(PORT, function () {
    console.log(`Server started on ${PORT}`);
})