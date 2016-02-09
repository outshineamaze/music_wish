
$(document).ready(function(){


  var playlist = [{
      title:"遇到你的时候",
      artist:"",
      mp3:"http://7q5cas.com1.z0.glb.clouddn.com/遇到你的时候所有的星星都落到我头上-思璇.mp3",
    
      poster: "http://7q5cas.com1.z0.glb.clouddn.com/bg2.jpg-min"
    },{
      title:"亲爱的路人",
      artist:"",
      mp3:"http://7q5cas.com1.z0.glb.clouddn.com/亲爱的路人-思璇.mp3",
   
      poster: "http://7q5cas.com1.z0.glb.clouddn.com/beijing.jpg-min"
    },{
      title:"阴天",
      mp3:  "http://7q5cas.com1.z0.glb.clouddn.com/阴天-思璇.mp3",
      poster: "http://7q5cas.com1.z0.glb.clouddn.com/bg.jpg-min"
  }];
  
  var cssSelector = {
    jPlayer: "#jquery_jplayer",
    cssSelectorAncestor: ".music-player"
  };
  
  var options = {
    swfPath: "http://cdnjs.cloudflare.com/ajax/libs/jplayer/2.6.4/jquery.jplayer/Jplayer.swf",
    supplied: "ogv, m4v, oga, mp3"
	
  };
  
  var myPlaylist = new jPlayerPlaylist(cssSelector, playlist, options);
 
  
});