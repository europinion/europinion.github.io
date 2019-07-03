// import { xml-js } from 'module'; // or './module'

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

function loadXMLDoc() {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
     // myFunction(this);
     console.log(this)
  };
  xmlhttp.open("GET", "./testdata.xml" , true);
  xmlhttp.send();
}

function myFunction(xml) {
	var convert = require('./lib/xml2json/xml2json.js');
	var options = {ignoreComment: true, alwaysChildren: true};
	var result = convert.xml2json(xml, options)
	console.log(result);
}

loadXMLDoc()