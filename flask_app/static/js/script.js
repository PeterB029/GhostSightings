var beliefs = [0, 0]
var spans = [
    document.querySelector('#believer'),
    document.querySelector('#skeptic')
]


function react_post(id){
    beliefs[id]++
    spans[id].innerHTML = beliefs[id]
}

// function react_post(id){
//     let believe = document.getElementById(id)
//     believe.innerText++
// }