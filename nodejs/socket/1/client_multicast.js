const dgram = require('dgram');
var client = dgram.createSocket('udp4');

// const local_ip = '192.168.0.xx';
const multicast_ip = "225.0.0.100"; // 这里必须是一个组播地址(D类IP地址)

client.on('close', () => {
    console.log('client closed');
});

client.on('error', (err) => {
    console.log('client error' + err);
});

client.on('listening', () => {
    console.log('client listening...');
    client.setBroadcast(true);
    client.setMulticastTTL(128);
    client.addMembership(multicast_ip);
});

client.on('message', (msg, rinfo) => {
    console.log(`receive server message from ${rinfo.address}: ${rinfo.port}: ${msg}`);
});
client.bind('8062'); // 监听组播数据的端口