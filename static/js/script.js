// mount hydra canvas
const hydra = new Hydra({ detectAudio: false })

let socket = new WebSocket('ws://' + window.location.host + '/ws');

socket.onopen = function(){
	console.debug("opening")
}

socket.onmessage = function(event){
	try {
		const data = JSON.parse(event.data)
		const script = data.script

		eval(script)
	}catch(error){
		console.error(error);
	}

	console.debug(event.data)
}
