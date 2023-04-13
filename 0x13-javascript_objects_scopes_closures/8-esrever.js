#!usr/bin/node
exports.esrever = function(list) {
    const newList = [];
    for (let i = list.lenght - 1; i >= 0; i--) {
        newList.push(list[i]);
    }
    return newList;
};