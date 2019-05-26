
function animate(call,args=undefined){
	args = Object.assign({duration:150,delay:0,frequecy:60,begin:undefined,complete:undefined},args)
	var t = 0.0;
	var interval = 1000.0/args.frequecy;
	var dt = 1.0/(args.duration/interval);
	// console.log(args.duration,args.delay);
	setTimeout(setInterval(call(t),interval),args.delay);
}

function printExamTime(header){
	request = new XMLHttpRequest();
	request.onreadystatechange = function() {
	  if(request.readyState === 4)
	    if(request.status === 200){
	      	time = +request.responseText;
	      	setInterval(function(){
				var horas = Math.floor((time % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
				var minutos = Math.floor((time % (1000 * 60 * 60)) / (1000 * 60));
				var segundos = Math.floor((time % (1000 * 60)) / 1000);
				header.innerHTML='<div class=timer>'+horas+':'+minutos+':'+segundos+'</div>';
				time-=1000;
			},1000);
			setTimeout(function(){
				location.href='/fimDeProva';
			},time);
	    }
	}
	
	request.open('Get', '/parametros/tempoDeProva');
	request.send();
}