const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());


console.log('Restaurante')

app.post('/request_food', (req, res) => {    
    console.log("\n------- Se recibio una peticion -------")
    console.log(`Se esta recibiendo un pedido de: ${JSON.stringify(req.body.food)}`)    
    res.status(200).send({ "message": `Pedido de ${req.body.food} recibido` });

    console.log("--------- Finalizo la peticion ---------\n")
});


app.get('/ask_state', (req, res) => {    
    console.log("\n------- Se recibio una peticion -------")
    console.log(`Se esta solicitando el estado del pedido ${req.query.id}`)
    res.status(200).send({ "message": `La orden con el id ${req.query.id} esta siendo procesada` });
    console.log("--------- Finalizo la peticion ---------\n")
});

app.get('/notify_driver', (req, res) => {    
    console.log("\n------- Se enviara una peticion al repartidor -------")    
    console.log(`Se esta notificando que el pedido ${123456} esta listo`)
    axios.post('http://localhost:3200/notify_order', {
        id: '12345'        
      })
      .then(function (response) {
          console.log(`El repartidor respondio: ${response.data.message}`)
        res.status(200).send({ "message": `Orden 123456 notificada correctamente` });
      })
      .catch(function (error) {
        res.status(200).send({ "message": `Ocurrio un error al notificar la orden` });
      });    
    console.log("----------------- Finalizo la peticion ----------------\n")
});



app.listen(port, () => {
    console.log(`API Rest corriendo en http://localhost:${port}`);

});