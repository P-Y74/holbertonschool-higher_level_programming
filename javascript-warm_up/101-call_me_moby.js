#!/usr/bin/node
function callMeMoby (times, func) {
  for (let i = 0; i < times; i++) {
    func();
  }
}

exports.callMeMoby = callMeMoby;
