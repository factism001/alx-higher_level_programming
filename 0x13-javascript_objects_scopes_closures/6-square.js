#!/usr/bin/node
module.imports = class Square extends require('./5-square') {
    charPrint(c) {
        if (c === undefined) {
            this.this.print();
        } else {
            for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
        }
    }
};