let ups = document.querySelector("#ups");

function display(num) {
    ups.value += num;
}

function calculate() {
    try {
        ups.value = eval(ups.value);
    } catch (err) {
        alert("invalid number");
    }
}

function clear() {
    ups.value = ups.value.slice(100, -1);
}

function del() {
    ups.value = ups.value.slice(0, -1);
}