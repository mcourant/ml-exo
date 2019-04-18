const p1 = {x : 0, y : 3}
const p2 = {x : 1, y : 5}
const p3 = {x : 2, y : 3}
const tetaInit = {x : 1, y : 1}

let LR = 1

let tetaModif = {}

function hteta(teta, x){
      return teta.x + teta.y * x
}

function htetacarre(teta, x){
      return hteta(teta, x) * hteta(teta,x)
}     

function resetTeta(teta, learningRate){      
      // console.log(learningRate);
      tetaModif = {x : teta.x - (learningRate/3) * ((hteta(teta,p1.x) - p1.y) + (hteta(teta, p2.x) - p2.y) + (hteta(teta, p3.x) - p3.y)), y : teta.y - (learningRate/3) * (((hteta(teta,p1.x) - p1.y) - p1.x) + ((hteta(teta, p2.x) - p2.y)-p2.x) + ((hteta(teta, p3.x) - p3.y)-p3.x))}
}

function cost(teta){
      return 1/2*3 * ((htetacarre(teta,p1.x) - p1.y) + (htetacarre(teta,p2.x) - p2.y) + (htetacarre(teta,p3.x) - p3.y))
}

function _(teta, learningRate, i = 0){
      if(i < 100){
            resetTeta(teta, learningRate)
            console.log('tetaModif:', tetaModif)
            learningRate = learningRate/2
            // console.log(learningRate);
            // console.log(cost(teta));
            i++
            _(tetaModif, learningRate, i)
      }
}5

_(tetaInit, LR)

