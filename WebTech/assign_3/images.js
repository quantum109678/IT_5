var imgarr=[
	"https://qph.fs.quoracdn.net/main-qimg-5d82e669c003ae9151cadedc63263766",
	"https://qph.fs.quoracdn.net/main-qimg-8762fa7aa9790f1861b0b864cfb391f0-c",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT33z752pNF-eCIM9PzBqfMHC3rVLCWGhtkgSaA6bU_6fum5IjESg",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4d0-M8dgUN3TJR2C_El3FkR1UCWXAg9fUkIY_FC9UGIvW4n8l"

]
var glo_ind=0;
function renderImage(ind) {
	var place=document.getElementById("render");
	if(glo_ind==3 && ind==1){
		place.src=imgarr[0];
		glo_ind=0;
	}
	if(glo_ind==0 && ind==-1){
		place.src=imgarr[3];
		glo_ind=3;
	}
	else if(ind==1){
		place.src=imgarr[glo_ind+1];
		glo_ind++;
	}
	else if(ind==-1){
		place.src=imgarr[glo_ind-1];
		glo_ind--;
	}


}