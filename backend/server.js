const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Sample API route
app.get('/api/health', (req, res) => {
    res.json({ status: 'OK', message: 'Server is running.' });
});

// Example of another route
app.post('/api/data', (req, res) => {
    const data = req.body;
    // process data
    res.status(201).json({ message: 'Data received', data });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});