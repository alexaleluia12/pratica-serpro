import http from 'node:https';

// vanilla query node 16

export default function httpQuery() {


    http.get('https://example.com/', (res) => {
        const {statusCode} = res;
        console.log('Request com status code ', statusCode);
        const data = [];

        res.on('data', block => data.push(block))
        res.on('end', () => {
            console.log('fin do request');
            console.log(Buffer.concat(data).toString())
        })
    }).on('error', (err) => {
        console.log('Erro');
        console.log({err})
    })

}