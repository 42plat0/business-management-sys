
const url = "http://127.0.0.1:5000/auth/api/hey";

const res = await fetch(url);

const json = await res.json();

console.log(json);