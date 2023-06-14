const express = require('express');
const app = express();
const bodyP = require('body-parser');
const compiler = require('compilex');
const options = { stats: true };
compiler.init(options);
app.use(bodyP.json());
app.use('/codemirror-5.65.9', express.static('E:/HocTap/Nam4/DoAn/demogpt/codemirror-5.65.9'));
app.get('/', function (req, res) {
    compiler.flush(function () {
        console.log('deleted');
    });
    res.sendFile('E:/HocTap/Nam4/DoAn/demogpt/index.html');
});
app.post('/compile', function (req, res) {
    let code = req.body.code;
    let input = req.body.input;
    let lang = req.body.lang;
    try {
        if (lang == 'Cpp') {
            if (!input) {
                let envData = { OS: 'windows', cmd: 'g++', options: { timeout: 10000 } }; // (uses g++ command to compile )
                compiler.compileCPP(envData, code, function (data) {
                    if (data.output) {
                        res.send(data);
                    } else {
                        res.send({ output: 'error' });
                    }
                });
            } else {
                let envData = { OS: 'windows', cmd: 'g++', options: { timeout: 10000 } }; // (uses g++ command to compile )
                compiler.compileCPPWithInput(envData, code, input, function (data) {
                    if (data.output) {
                        res.send(data);
                    } else {
                        res.send({ output: 'error' });
                    }
                });
            }
        } else if (lang == 'Java') {
            if (!input) {
                let envData = { OS: 'windows' };
                compiler.compileJava(envData, code, function (data) {
                    if (data.output) {
                        res.send(data);
                    } else {
                        res.send({ output: 'error' });
                    }
                });
            } else {
                //if windows
                let envData = { OS: 'windows' };
                //else
                compiler.compileJavaWithInput(envData, code, input, function (data) {
                    if (data.output) {
                        res.send(data);
                    } else {
                        res.send({ output: 'error' });
                    }
                });
            }
        } else if (lang == 'Python') {
            if (!input) {
                let envData = { OS: 'windows' };
                compiler.compilePython(envData, code, function (data) {
                    if (data.output) {
                        res.send(data);
                    } else {
                        let pattern = /File ".*", line /;
                        let error_data = data.error.split('\n');
                        let result = [];
                        for (let i = 0; i < error_data.length; i++) {
                            if (pattern.test(error_data[i])) {
                                result.push(error_data[i].replace(pattern, 'At line '));
                            } else {
                                result.push(error_data[i]);
                            }
                        }
                        res.send({ error: result.join('\n') });
                    }
                });
            } else {
                let envData = { OS: 'windows' };
                compiler.compilePythonWithInput(envData, code, input, function (data) {
                    if (data.output) {
                        res.send(data);
                    } else {
                        res.send({ output: 'error' });
                    }
                });
            }
        }
    } catch (e) {
        console.log('error');
    }
});

app.listen(8000);
