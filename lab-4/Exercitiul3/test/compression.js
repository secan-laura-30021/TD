const lib = require('bits-utils');

const text = 'STELELE NU POT STRALUCI FARA ÎNTUNERIC';
 console.log(text.length);
const symbols = lib.countASCIISymbols(text);
const alphabet = lib.getAlphabet(symbols);
console.log(alphabet);
const codes = lib.getSymbolsBitCodes(alphabet, 4)
console.log(codes);

