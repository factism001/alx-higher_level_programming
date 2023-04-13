#!/usr/bin/node
module.imports = class Square extends require('./4-rectangle') {
    constructor (size) {
        super(size, size);
    }
};