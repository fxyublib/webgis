const dgram = require('dgram');
const server = dgram.createSocket('udp4');

// const local_ip = "192.168.0.xx";
const multicast_ip = "225.0.0.100"; // 这里必须是一个组播地址(D类IP地址)

server.on('close', () => {
    console.log('close socket');
});

server.on('listening', () => {
    console.log('listening...' );
    server.setBroadcast(true);
    server.setMulticastTTL(128);
    server.addMembership(multicast_ip);

    setInterval(() => {
        send_msg();
    }, 2000);
});

server.on('message', (msg, rinfo) => {
    console.log(`receive client message from ${rinfo.address}: ${rinfo.port}: ${msg}`);
});

server.bind(); // 随机绑定本机一个端口

function send_msg() {
    var date = new Date();
    console.log(date.toLocaleDateString() + " " + date.toLocaleTimeString() + ': send a message.');
    server.send('hi, i am server...', '8062', multicast_ip);
}