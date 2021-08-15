import express from 'express';
import mongoose from 'mongoose';
import config from 'config';

const register = (req:express.Request, res:express.Response):void => {

}

const test1 = (req:express.Request, res:express.Response):void => {
    console.log(`received GET request (test1)`);
    res.send({
        'userId':'123',
        'username':'Jack',
        'email':'mailtojack@testmail.com',
        'tracking':[
            ['TSLA', 6],
            ['MSFT', 4],
            ['AAPL', 0],
            ['PLTR', 2],
        ]
    });
}

const test2 = (req:express.Request, res:express.Response):void => {
    res.send({
        'userId':'123',
        'username':'Jack',
        'email':'mailtojack@testmail.com',
        'tracking':[
            ['TSLA', 6],
            ['MSFT', 4],
            ['AAPL', 0],
            ['PLTR', 2],
        ]
    });
}

export default {register, test1, test2};