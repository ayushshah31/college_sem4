var inputString = prompt("Enter string: ");

const ucFirst = (str) => {
    let str1 = str.slice(1);
    let startChar = str.charAt(0);
    startChar = startChar.toUpperCase();
    return (startChar + str1);
}

var str = ucFirst(inputString);
alert(str);