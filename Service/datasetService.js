var express = require("express");
var app = express();
const request = require('request');
const cheerio = require('cheerio');
var fs = require('fs');
var json = {};

const writeStreme = fs.createWriteStream('dataset.json');
writeStreme.write("{}");
const jsonName = 'dataset.json';


app.get('/liste', liste);
function liste(reg, res) {
    fs.readFile(jsonName, 'utf8', function (err, data) {
        console.log(data);
        res.end(data);
    });
};

app.get('/vericek', vericek);
function vericek(reg, res) {
    var url = reg.query.url;
    request(url, (errorr, responsee, htmll) => {
        if (!errorr && responsee.statusCode == 200) {
            const $ = cheerio.load(htmll);
            $('.review-item').each((a, b) => {
                const commint = $(b).find('.review-text').text().replace(/,/g, '').replace(/\/s/g, '').replace('/\n/g', ' ').replace(/[\r\n]+/g, ' ').trim();
                const star = $(b).find('.ratings').children().attr("style").replace('width: ', '').replace('%', '');
                var newdata = {}
                newdata.commint = commint;
                if (star == 100 || star == 80) {
                    newdata.star = "1";
                }
                else if (star == 20 || star == 40) {
                    newdata.star = "0";
                }

                if (newdata.star == '0' || newdata.star == '1') {
                    json[i] = newdata;
                    i++;
                }
            });
            fs.writeFile(jsonName, JSON.stringify(json), function (err) {
                console.log("bir hata oluştu");
            });
            console.log(JSON.stringify(json));
            res.end("Veri çekme işlemi tamam");
        };
    });
};

var server = app.listen(8000, function () {
    console.log('sunucu çalışıyor');
});