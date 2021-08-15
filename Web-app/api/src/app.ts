import express from 'express';
//import bodyParser from 'body-parser';
import mongoose from 'mongoose';
import config from 'config';
import cors from 'cors';
import appMiddleware from './middleware';

const port:number = config.get("port");
//const host:string = config.get("host");

const app = express();

// CORS middleware
app.use(cors());

// Body-parser middleware
app.use(express.urlencoded({extended: true}))
app.use(express.json())

app.listen(port, () => {
    console.log(`listening on port ${port}`);
});

// User resource
app.post('/user', (req:express.Request, res:express.Response) => {
    console.log(req.body);
    res.send({
        'status':'success',
        'message':`added ${req.body.username} to the database`
    });
});

app.get('/user', (req:express.Request, res:express.Response) => {
    console.log(`received GET request -> Resource: User, Request: ${req.body} `);
    res.send({
        'status':'success',
        'message':`added ${req.body.username} to the database`
    });
});

// tests / healthchecks
app.get('/test1', appMiddleware.test1)

app.get('/test2/:id/:name', (req:express.Request, res:express.Response) => {
    console.log(`received GET request (test2/${req.params.id}/${req.params.name})`);
    res.send({
        'userId':req.params.id,
        'username':req.params.name,
        'email':'mailtojack@testmail.com',
        'tracking':[
            ['TSLA', 6],
            ['MSFT', 4],
            ['AAPL', 0],
            ['PLTR', 2],
        ]
    });
})