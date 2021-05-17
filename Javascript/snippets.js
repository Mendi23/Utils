await new Promise(r => setTimeout(r, 3000)); // sleep(3000)
window.open('https://keep.google.com/u/0/','_self',''); // open url

function logger(target, name, descriptor) { // logger decorator (for nodejs)
    let fn = descriptor.value;
    let newFn  = function() {
      console.log('starting %s', name);
      fn.apply(target, arguments);
      console.log('ending %s', name);
    };
    descriptor.value = newFn;
    return descriptor;
}

function* func_to_iter(func, stop=null) {
  while ((i = func()) !== stop) {
    yield i;
  }
}

function pick(obj, props) {
  var picked = {};
  props.forEach(prop => {picked[prop] = obj[prop]});
  return picked;
}
