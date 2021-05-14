let bitsUtils = require('bits-utils');
const chalk = require('chalk');
const fs = require('fs');
let axios = require('axios');
let { loadWords, getCodes, encodeOneWord } = require('../lib/lib');

const kiwiUrl = 'http://localhost:3001';
const filename = '../lib/common-words.txt';
const words = loadWords(filename);
const codes = getCodes(words);

var stream = fs.createWriteStream("../orange/file.txt");

stream.once('open', function(fd){

function sendWord(word) {
  const binaryData = encodeOneWord(word, codes);
  console.log(
    `The binary code for ${chalk.blueBright(word)} is ${chalk.blueBright(
      bitsUtils.printBuffer(binaryData)
    )}`
  );

  console.log(
    `Sending ${chalk.blueBright(
      bitsUtils.printBuffer(binaryData)
    )} to ${chalk.greenBright('kiwi')}`
  );
  stream.write(bitsUtils.printBuffer(binaryData) + "\n");
	console.log(
		`${chalk.blueBright(
			bitsUtils.printBuffer(binaryData)
		)} saved to file`
	);
	
	
  axios
    .post(`${kiwiUrl}/compressed`, binaryData, {
      headers: {
        'Content-Type': 'text/html'
      }
    })
    .then(res => {
      console.log(
        `Response from ${chalk.greenBright('kiwi')}: "${res.data.status}"`
      );
    });
}

function sendText(text) {
  axios
    .post(`${kiwiUrl}/text`, text, {
      headers: {
        'Content-Type': 'text/html'
      }
    })
    .then(res => {
      console.log(
        `Response from ${chalk.greenBright('kiwi')}: "${res.data.status}"`
      );
    });
}

sendWord('give');
sendWord('this');
sendWord(' ');
sendWord('\r\n'); //https://stackoverflow.com/questions/1761051/difference-between-n-and-r
sendWord('because');
sendWord('have');
sendWord('first');
sendWord('well');
sendWord('way');
sendWord('us');
sendWord('any');

sendText('give');
sendText('this\r\nbecause');
sendText('first\r\nwell have\r\nway us any');

stream.end();
});

fs.readFile('../orange/file.txt', 'utf8', (err, data) => {
	if(err){
		console.error(err);
		return;
	}
	console.log(data);
})
